"""Generate the corrected hyperlocal forecast -> forecast.json.

Fetches the current 10-day hourly forecast (Open-Meteo, source model from
model/model.json), applies the per-variable correction, and writes a single
JSON consumed by both the friends page and Home Assistant REST sensors.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
LAT, LON = 44.3205501, -71.7438537
UNITS = {"temperature_unit": "fahrenheit", "wind_speed_unit": "mph", "precipitation_unit": "inch"}

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
        booster_path = ROOT / "data" / params["booster_file"]
        if not booster_path.exists():
            print(f"WARN: {booster_path.name} not published to this repo - falling back to raw")
            return fc
        import lightgbm as lgb
        booster = lgb.Booster(model_file=str(booster_path))
        feats = params["features"]
        X = np.array([features_row(f, l, ts, c, feats) for f, l, ts, c in
                      zip(fc, lead_series, ts_index, cloud_series)])
        return pd.Series(booster.predict(X), index=fc.index)
    return fc


def main() -> None:
    model = json.loads((ROOT / "data" / "model.json").read_text())
    src = model.get("source_model", "best_match")

    r = requests.get("https://api.open-meteo.com/v1/forecast", params={
        "latitude": LAT, "longitude": LON, "hourly": ",".join(HOURLY),
        "daily": "weather_code,sunrise,sunset",
        "models": src, "forecast_days": 10, "timezone": "UTC", **UNITS}, timeout=60)
    r.raise_for_status()
    js = r.json()

    df = pd.DataFrame(js["hourly"])
    df["ts"] = pd.to_datetime(df.pop("time"), utc=True)
    df = df.set_index("ts")
    now = pd.Timestamp.now("UTC").floor("h")
    df = df[df.index >= now]
    lead = ((df.index - now) / pd.Timedelta("1D")).astype(int)
    cloud = df.get("cloud_cover", pd.Series(50, index=df.index))

    out_hourly = pd.DataFrame(index=df.index)
    bands = {}
    for fc_col, out_name in OUT_VARS.items():
        if fc_col not in df:
            continue
        actual_col = next((k for k, v in model["variables"].items()
                           if v["fc_col"] == fc_col), None)
        spec = model["variables"].get(actual_col, {"method": "raw"})
        out_hourly[out_name] = apply_correction(spec, df[fc_col], lead, df.index, cloud).round(1)
        out_hourly[f"{out_name}_raw"] = df[fc_col].round(1)
        b = spec.get("bands", {})
        if b:
            max_l = max(int(k) for k in b)
            lo = [b[str(min(int(l), max_l))][1] for l in lead]   # fc-actual p90 -> subtract
            hi = [b[str(min(int(l), max_l))][0] for l in lead]
            bands[out_name] = {"lo": (out_hourly[out_name] - np.array(lo)).round(1).tolist(),
                               "hi": (out_hourly[out_name] - np.array(hi)).round(1).tolist()}
    out_hourly["precip_in"] = df["precipitation"].round(3)
    out_hourly["precip_prob"] = df.get("precipitation_probability")
    out_hourly["cloud_pct"] = cloud
    out_hourly["wind_dir_deg"] = df.get("wind_direction_10m")
    out_hourly["weather_code"] = df.get("weather_code")

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
    ha_hourly = [{
        "datetime": t.isoformat(), "condition": ha_condition(h72["weather_code"].iloc[i]),
        "temperature": h72["temp_f"].iloc[i], "humidity": h72["humidity_pct"].iloc[i],
        "precipitation": float(h72["precip_in"].iloc[i] or 0),
        "precipitation_probability": None if pd.isna(h72["precip_prob"].iloc[i]) else int(h72["precip_prob"].iloc[i]),
        "wind_speed": h72["wind_mph"].iloc[i], "wind_gust_speed": h72["gust_mph"].iloc[i],
        "wind_bearing": None if pd.isna(h72["wind_dir_deg"].iloc[i]) else int(h72["wind_dir_deg"].iloc[i]),
    } for i, t in enumerate(h72.index)]
    ha_daily = [{
        "datetime": f"{d}T00:00:00-04:00", "condition": ha_condition(daily["weather_code"].iloc[i]),
        "temperature": daily["high_f"].iloc[i], "templow": daily["low_f"].iloc[i],
        "precipitation": daily["precip_in"].iloc[i],
        "precipitation_probability": None if pd.isna(daily["precip_prob_max"].iloc[i]) else int(daily["precip_prob_max"].iloc[i]),
        "wind_speed": daily["wind_max_mph"].iloc[i], "wind_gust_speed": daily["gust_max_mph"].iloc[i],
    } for i, d in enumerate(daily.index)]

    payload = {
        "generated_at": pd.Timestamp.now("UTC").isoformat(),
        "location": {"lat": LAT, "lon": LON, "name": "Bear Paw Trail, Littleton NH"},
        "source_model": src,
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
    (ROOT / "forecast.json").write_text(json.dumps(payload))
    print(f"forecast.json written: {len(h72)} hourly rows, {len(daily)} days, source={src}")
    print("methods:", payload["methods"])


if __name__ == "__main__":
    main()
