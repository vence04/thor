"""Generate the corrected hyperlocal forecast -> forecast.json.

Fetches the current 10-day hourly forecast (Open-Meteo, source model from
model/model.json), applies the per-variable correction, and writes a single
JSON consumed by both the friends page and Home Assistant REST sensors.
"""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

import candidates as C  # noqa: E402
from fetch_archived_forecasts import MODELS as ALL_MODELS  # noqa: E402
from paths import ACTUALS_PARQUET, MODEL_DIR, MODEL_JSON, FORECAST_JSON as OUT_PATH  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LAT, LON = 44.3205501, -71.7438537
UNITS = {"temperature_unit": "fahrenheit", "wind_speed_unit": "mph", "precipitation_unit": "inch"}

# A correction that flattens the forecast is broken, not confident. On 2026-09-12 an
# lgbm model trained on a two-month window collapsed to a constant 58.7F for ten days
# because its doy feature could not extrapolate. Never publish that: if a corrected
# series varies far less than the raw one it came from, ship raw instead.
COLLAPSE_RATIO = 0.30

# A correction is a regression, so it can put a variable outside what it can physically
# be: on 2026-10-12 the wind correction produced -0.2 mph. Clamp to the possible range.
BOUNDS = {"wind_mph": (0, None), "gust_mph": (0, None), "humidity_pct": (0, 100)}
SPREAD_DAYS = 28

# Chance of precipitation is the share of the twelve models that forecast measurable
# rain in that hour - Ebert's "poor man's ensemble" (Mon. Wea. Rev., 2001). Tested
# 2026-10-18 on the day-0 archive against the station's gauge, last 30% held out (655
# hours, 78 wet): Brier 0.058, against 0.086 for the best single model read as yes/no,
# 0.110 for climatology, and 0.062 for a logistic regression over all twelve amounts,
# which overfits. Open-Meteo's own figure is published beside it as
# precip_prob_openmeteo so the two can be scored against each other from git history
# once a wet season has passed; it is one 27 km ensemble-cell number, the same whichever
# model is asked for, so it never varied with the bake-off anyway. best_match is left
# out because at this point it is byte-identical to gfs_seamless.
WET_IN = 0.01                 # the gauge's reporting step; the threshold the test used
ENSEMBLE = [m for m in ALL_MODELS if m != "best_match"]
MIN_MEMBERS = 4               # fewer than this with a value for the hour: use Open-Meteo's


def rain_chance(member_series: list, fallback: pd.Series | None) -> pd.Series:
    """Percent of models forecasting >= WET_IN in each hour; models with no value for
    an hour (shorter horizons) are left out of that hour's count, not counted as dry."""
    if not member_series:
        return fallback if fallback is not None else pd.Series(np.nan, index=[])
    vals = pd.concat(member_series, axis=1)
    wet = (vals >= WET_IN).where(vals.notna())
    frac = wet.mean(axis=1) * 100
    enough = vals.notna().sum(axis=1) >= MIN_MEMBERS
    if fallback is not None:
        frac = frac.where(enough, fallback)
    else:
        frac = frac.where(enough)
    return frac.round()


def station_spread(days: int = SPREAD_DAYS) -> dict:
    """How much each reading actually varies at the station, over the last few weeks.

    The collapse guard below compares a correction against this, not against the
    regional forecast's spread. At a sheltered site the station genuinely varies less
    than the model thinks - on 2026-10-12 station wind had sd 1.37 against the
    forecast's 2.16 - so judging the correction against the forecast discarded the best
    result this project has, wind measured 23-41% better than raw, for looking "too
    flat". A real collapse still fails: a flat line has sd near zero against either.
    """
    try:
        a = pd.read_parquet(ACTUALS_PARQUET)
    except Exception as exc:
        # Say so rather than degrading quietly: a missing pyarrow did exactly that on
        # 2026-10-12 and the guard went on rejecting the wind correction unnoticed.
        print(f"WARN: cannot read station history for the collapse guard ({exc}); "
              f"falling back to the forecast's own spread")
        return {}
    a = a[a.index >= a.index.max() - pd.Timedelta(days=days)]
    return {c: float(a[c].std()) for c in a.columns
            if a[c].notna().sum() >= 24 and pd.notna(a[c].std())}

HOURLY = ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "wind_speed_10m",
          "wind_gusts_10m", "wind_direction_10m", "precipitation", "precipitation_probability",
          "cloud_cover", "surface_pressure", "weather_code"]

# forecast col -> output name (corrected where a model exists)
OUT_VARS = {"temperature_2m": "temp_f", "relative_humidity_2m": "humidity_pct",
            "dew_point_2m": "dewpoint_f", "wind_speed_10m": "wind_mph",
            "wind_gusts_10m": "gust_mph", "surface_pressure": "pressure_hpa"}


def features_row(fc, lead_d, ts, cloud, feat_names):
    hour = ts.hour + ts.minute / 60
    doy = ts.dayofyear
    vals = {"fc": fc, "lead_d": lead_d,
            "sin_h": np.sin(2 * np.pi * hour / 24), "cos_h": np.cos(2 * np.pi * hour / 24),
            "sin_doy": np.sin(2 * np.pi * doy / 365), "cos_doy": np.cos(2 * np.pi * doy / 365),
            "cloud": cloud if cloud is not None else 50}
    return [vals[f] for f in feat_names]


def apply_correction(spec, fc_series, lead_series, ts_index, cloud_series):
    method, params = spec["method"], spec.get("params", {})
    fc = fc_series.astype(float)
    if method == "raw" or fc.isna().all():
        return fc
    if method == "bias":
        lead_bias = {int(k): v for k, v in params.get("bias_by_lead", {}).items()}
        hour_bias = {int(k): v for k, v in params.get("bias_by_hour", {}).items()}
        glob = params.get("bias_global", 0.0)
        max_lead = max(lead_bias) if lead_bias else 0
        corr = [lead_bias.get(min(int(l), max_lead), glob) + hour_bias.get(ts.hour, 0.0)
                for l, ts in zip(lead_series, ts_index)]
        return fc - np.array(corr)
    if method == "ridge":
        feats = params["features"]
        X = np.array([features_row(f, l, ts, c, feats) for f, l, ts, c in
                      zip(fc, lead_series, ts_index, cloud_series)])
        Xs = (X - np.array(params["scale_mean"])) / np.array(params["scale_std"])
        return pd.Series(Xs @ np.array(params["coef"]) + params["intercept"], index=fc.index)
    if method == "lgbm":
        booster_path = MODEL_DIR / params["booster_file"]
        if not booster_path.exists():
            print(f"WARN: {booster_path.name} is not present here - falling back to raw")
            return fc
        import lightgbm as lgb
        booster = lgb.Booster(model_file=str(booster_path))
        feats = params["features"]
        X = np.array([features_row(f, l, ts, c, feats) for f, l, ts, c in
                      zip(fc, lead_series, ts_index, cloud_series)])
        return pd.Series(booster.predict(X), index=fc.index)
    return fc


def main() -> None:
    model = json.loads(MODEL_JSON.read_text(encoding="utf-8"))
    src = model.get("source_model", "best_match")

    # Each variable comes from the model that forecasts it best at this site, as decided
    # by the weekly bake-off; anything without a verdict falls back to `src`. Asking for
    # several models in one call returns suffixed columns (temperature_2m_gem_seamless).
    per_var = {v: x.get("source_model", src) for v, x in model["variables"].items()}
    # a source may be a blend, so ask the API for every model any source draws on
    wanted = sorted({m for cand in {src, *per_var.values()} for m in C.members(cand)}
                    | set(ENSEMBLE))

    params = {"latitude": LAT, "longitude": LON, "hourly": ",".join(HOURLY),
              "daily": "weather_code,sunrise,sunset", "models": ",".join(wanted),
              "forecast_days": 10, "timezone": "UTC", **UNITS}
    # Open-Meteo returned a 503 on 2026-10-17 and this call had no retry, so the hourly
    # forecast simply failed. The archive fetcher already retries; this now matches it.
    js = None
    for attempt in range(4):
        try:
            r = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=60)
            if r.status_code == 200:
                js = r.json()
                break
            if r.status_code not in (429, 500, 502, 503, 504):
                r.raise_for_status()
            print(f"open-meteo returned {r.status_code}; retrying")
        except (requests.exceptions.RequestException, ValueError) as exc:
            print(f"open-meteo call failed ({type(exc).__name__}); retrying")
        time.sleep(10 * (attempt + 1))
    if js is None:
        raise RuntimeError("open-meteo did not return a usable forecast after 4 attempts")

    df = pd.DataFrame(js["hourly"])
    df["ts"] = pd.to_datetime(df.pop("time"), utc=True)
    df = df.set_index("ts")
    now = pd.Timestamp.now("UTC").floor("h")
    df = df[df.index >= now]
    lead = ((df.index - now) / pd.Timedelta("1D")).astype(int)
    def pick(var: str, cand: str) -> pd.Series | None:
        """The column for `var` from a candidate, averaging the members of a blend.

        Open-Meteo suffixes each column with the model name when several are asked
        for, and leaves it bare when only one is - hence the fallback.
        """
        cols = []
        for m in C.members(cand):
            for key in (f"{var}_{m}", var):
                if key in df and df[key].notna().any():
                    cols.append(df[key])
                    break
        if not cols:
            return None
        return cols[0] if len(cols) == 1 else pd.concat(cols, axis=1).mean(axis=1)

    cloud = pick("cloud_cover", C.members(src)[0])
    if cloud is None:
        cloud = pd.Series(50, index=df.index)

    spread = station_spread()
    out_hourly = pd.DataFrame(index=df.index)
    bands = {}
    for fc_col, out_name in OUT_VARS.items():
        actual_col = next((k for k, v in model["variables"].items()
                           if v["fc_col"] == fc_col), None)
        series = pick(fc_col, per_var.get(actual_col, src))
        if series is None:
            continue
        spec = model["variables"].get(actual_col, {"method": "raw"})
        corrected = apply_correction(spec, series, lead, df.index, cloud).round(1)
        raw_series = series.round(1)
        raw_sd, cor_sd = float(raw_series.std()), float(corrected.std())
        # prefer the station's own spread as the yardstick; fall back to the forecast's
        # where the station has no matching column (pressure is stored in inHg, not hPa)
        ref_sd = spread.get(actual_col, raw_sd)
        ref_name = "station" if actual_col in spread else "raw"
        if spec.get("method", "raw") != "raw" and ref_sd > 0 and cor_sd < COLLAPSE_RATIO * ref_sd:
            print(f"WARN: {out_name} correction collapsed (sd {cor_sd:.2f} vs {ref_name} "
                  f"{ref_sd:.2f}) - publishing raw for this variable")
            corrected = raw_series
            spec = {"method": "raw"}
            model["variables"][actual_col]["method"] = "raw"
        lo, hi = BOUNDS.get(out_name, (None, None))
        if lo is not None or hi is not None:
            corrected = corrected.clip(lower=lo, upper=hi)
        out_hourly[out_name] = corrected
        out_hourly[f"{out_name}_raw"] = raw_series
        b = spec.get("bands", {})
        if b:
            max_l = max(int(k) for k in b)
            lo = [b[str(min(int(l), max_l))][1] for l in lead]   # fc-actual p90 -> subtract
            hi = [b[str(min(int(l), max_l))][0] for l in lead]
            bands[out_name] = {"lo": (out_hourly[out_name] - np.array(lo)).round(1).tolist(),
                               "hi": (out_hourly[out_name] - np.array(hi)).round(1).tolist()}
    out_hourly["precip_in"] = pick("precipitation", src).round(3)
    om_prob = pick("precipitation_probability", src)
    members = [s for s in (pick("precipitation", m) for m in ENSEMBLE) if s is not None]
    if len(members) < MIN_MEMBERS:
        print(f"WARN: only {len(members)} models returned precipitation - "
              f"publishing Open-Meteo's probability")
    out_hourly["precip_prob"] = rain_chance(members, om_prob)
    out_hourly["precip_prob_openmeteo"] = om_prob
    out_hourly["cloud_pct"] = cloud
    out_hourly["wind_dir_deg"] = pick("wind_direction_10m", src)
    out_hourly["weather_code"] = pick("weather_code", src)

    # daily rollup from corrected hourlies (local time days)
    local = out_hourly.tz_convert("America/New_York")
    g = local.groupby(local.index.date)
    daily = pd.DataFrame({
        "high_f": g["temp_f"].max().round(0),
        "low_f": g["temp_f"].min().round(0),
        "high_raw_f": g["temp_f_raw"].max().round(0),
        "low_raw_f": g["temp_f_raw"].min().round(0),
        "precip_in": g["precip_in"].sum().round(2),
        "precip_prob_max": g["precip_prob"].max(),
        "wind_max_mph": g["wind_mph"].max().round(0),
        "gust_max_mph": g["gust_mph"].max().round(0),
        "weather_code": g["weather_code"].agg(lambda x: int(x.mode().iloc[0])),
    })
    daily.index = [str(d) for d in daily.index]

    def ha_condition(code):
        c = int(code) if pd.notna(code) else 0
        if c in (0, 1):
            return "sunny"
        if c == 2:
            return "partlycloudy"
        if c == 3:
            return "cloudy"
        if c in (45, 48):
            return "fog"
        if c in (66, 67):
            return "snowy-rainy"
        if c in (71, 73, 75, 77, 85, 86):
            return "snowy"
        if c >= 95:
            return "lightning-rainy"
        return "rainy"

    h72 = out_hourly.iloc[:72]
    # `epoch` exists so a reader can find the hour that is current NOW rather than
    # trusting entry 0. GitHub's scheduler drops most of the runs this repo asks for -
    # measured 2026-10-17, thirteen runs in forty-three hours, gaps up to five hours -
    # so the file is routinely hours old while still holding the right numbers for the
    # right hours. Comparing ISO strings would not work: these are UTC and Home
    # Assistant's now() is -04:00.
    ha_hourly = [{
        "datetime": t.isoformat(), "epoch": int(t.timestamp()),
        "condition": ha_condition(h72["weather_code"].iloc[i]),
        "temperature": h72["temp_f"].iloc[i], "humidity": h72["humidity_pct"].iloc[i],
        "precipitation": float(h72["precip_in"].iloc[i] or 0),
        "precipitation_probability": None if pd.isna(h72["precip_prob"].iloc[i]) else int(h72["precip_prob"].iloc[i]),
        "wind_speed": h72["wind_mph"].iloc[i], "wind_gust_speed": h72["gust_mph"].iloc[i],
        "wind_bearing": None if pd.isna(h72["wind_dir_deg"].iloc[i]) else int(h72["wind_dir_deg"].iloc[i]),
    } for i, t in enumerate(h72.index)]
    ha_daily = [{
        # midnight local, with whatever offset that date actually has: a hardcoded
        # -04:00 was right only until EDT ends on 2026-11-01.
        "datetime": pd.Timestamp(f"{d}T00:00:00").tz_localize("America/New_York").isoformat(),
        "condition": ha_condition(daily["weather_code"].iloc[i]),
        "temperature": daily["high_f"].iloc[i], "templow": daily["low_f"].iloc[i],
        "precipitation": daily["precip_in"].iloc[i],
        "precipitation_probability": None if pd.isna(daily["precip_prob_max"].iloc[i]) else int(daily["precip_prob_max"].iloc[i]),
        "wind_speed": daily["wind_max_mph"].iloc[i], "wind_gust_speed": daily["gust_max_mph"].iloc[i],
    } for i, d in enumerate(daily.index)]

    payload = {
        "generated_at": pd.Timestamp.now("UTC").isoformat(),
        "location": {"lat": LAT, "lon": LON, "name": "Bear Paw Trail, Littleton NH"},
        "source_model": src,
        "source_models": per_var,
        "precip_prob_models": len(members),
        "model_trained_at": model.get("trained_at"),
        "methods": {k: v["method"] for k, v in model["variables"].items()},
        "n_train": {k: v["n_train"] for k, v in model["variables"].items()},
        "hourly": {"ts": [t.isoformat() for t in h72.index],
                   **{c: h72[c].where(h72[c].notna(), None).tolist() for c in h72.columns}},
        "hourly_bands": {k: {kk: vv[:72] for kk, vv in v.items()} for k, v in bands.items()},
        "daily": {"date": list(daily.index),
                  **{c: daily[c].where(daily[c].notna(), None).tolist() for c in daily.columns}},
        "ha_hourly": ha_hourly,
        "ha_daily": ha_daily,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(payload), encoding="utf-8")
    print(f"{OUT_PATH} written: {len(h72)} hourly rows, {len(daily)} days, source={src}")
    print("methods:", payload["methods"])


if __name__ == "__main__":
    main()
