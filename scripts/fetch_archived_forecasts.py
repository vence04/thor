"""Fetch archived model forecasts for Bear Paw Lodge from Open-Meteo.

Two products:
1. Historical Forecast API -> day-0 (freshest-run) hourly series per model, for the
   source bake-off against station actuals.
2. Previous Runs API -> the same variables as forecast 1..7 days ahead, for
   lead-time-dependent bias modelling.

Free, keyless, non-commercial. Writes parquet to the forecast dir for this repo layout (see scripts/paths.py).
"""
import time
import sys
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import FORECAST_DIR  # noqa: E402

LAT, LON = 44.3205501, -71.7438537
START, END = "2025-08-18", None  # END defaults to today
OUT = FORECAST_DIR

HOURLY = [
    "temperature_2m", "relative_humidity_2m", "dew_point_2m",
    "wind_speed_10m", "wind_gusts_10m", "wind_direction_10m",
    "precipitation", "cloud_cover", "surface_pressure", "shortwave_radiation",
]
UNITS = {"temperature_unit": "fahrenheit", "wind_speed_unit": "mph", "precipitation_unit": "inch"}

# Every model Open-Meteo serves for this point, verified 2026-10-17 by asking the API
# for all of them and keeping the ones that came back with values; gfs_graphcast025 is
# the only one that returned nothing. Seven of these were missing until today, among
# them four of the six families Apple credits on its own WeatherKit attribution page
# (Met Office, Meteo-France, JMA, and DWD via icon). best_match is kept because it is
# what an app gets by default - and at this location it is byte-identical to
# gfs_seamless, checked against both the archive and the live API, so it is in the
# bake-off as the baseline everybody else is using, not as a candidate.
MODELS = ["best_match", "ecmwf_ifs025", "ecmwf_aifs025_single", "gfs_seamless",
          "gfs_hrrr", "ncep_nbm_conus", "icon_seamless", "gem_seamless",
          "ukmo_seamless", "meteofrance_seamless", "jma_seamless", "metno_seamless",
          "knmi_seamless"]

# The second location: the nearest public station with years of history, so models can
# be ranked over whole seasons rather than the three summer-and-autumn months the Bear
# Paw sensor has been outdoors. See fetch_public_obs.py for why, and for what this
# record may and may not decide.
REGIONAL_LAT, REGIONAL_LON = 44.3681, -71.5453          # KHIE, Whitefield NH
# The earliest date the whole roster is served at this point: ECMWF-AIFS starts in
# 2025-04, NBM in 2025-01, and everything else is older. Checked 2026-10-17 by probing
# 2022-01-01, 2023-01-01, 2024-01-01, 2024-07-01, 2025-01-01 and 2025-04-01. Starting
# where they ALL exist keeps the ranking a fair fight; an earlier start would score
# some models on winters the others never saw.
REGIONAL_START = "2025-04-01"

PREV_DAYS = 7
# Every model gets a previous-runs archive, not just four: a model without one cannot
# be chosen as a variable's source, and the bake-off's wind and pressure winner
# (gem_seamless) was being excluded for that reason alone. Verified 2026-10-12 that
# the previous-runs API serves gem_seamless, icon_seamless and gfs_hrrr.
PREV_MODELS = MODELS


def get(url: str, params: dict, retries: int = 4) -> dict:
    for i in range(retries):
        try:
            r = requests.get(url, params=params, timeout=180)
        except requests.exceptions.RequestException:
            time.sleep(10 * (i + 1))
            continue
        if r.status_code == 200:
            try:
                return r.json()
            except ValueError:
                # A 200 whose body is not JSON - a truncated reply or an HTML error page.
                # Transient: one killed the weekly retrain on 2026-10-12 while the API was
                # otherwise healthy. Retry rather than crashing the whole run.
                time.sleep(10 * (i + 1))
                continue
        if r.status_code in (429, 500, 502, 503):
            time.sleep(10 * (i + 1))
            continue
        raise RuntimeError(f"{r.status_code}: {r.text[:300]}")
    raise RuntimeError("retries exhausted")


def frame(js: dict) -> pd.DataFrame:
    df = pd.DataFrame(js["hourly"])
    df["ts"] = pd.to_datetime(df.pop("time"), utc=True)
    return df.set_index("ts")


def fetch_day0(lat: float = LAT, lon: float = LON, start: str = START,
               out: Path = OUT, tag: str = "day0") -> None:
    end = END or pd.Timestamp.now("UTC").strftime("%Y-%m-%d")
    out.mkdir(parents=True, exist_ok=True)
    for model in MODELS:
        js = get("https://historical-forecast-api.open-meteo.com/v1/forecast", {
            "latitude": lat, "longitude": lon, "start_date": start, "end_date": end,
            "hourly": ",".join(HOURLY), "models": model, "timezone": "UTC", **UNITS,
        })
        df = frame(js)
        if not df.notna().any().any():
            # a model with no coverage here: skip rather than write an empty frame the
            # bake-off would have to special-case
            print(f"{tag} {model}: no data at this point, skipped")
            continue
        df.to_parquet(out / f"{tag}_{model}.parquet")
        print(f"{tag} {model}: {len(df)} rows, {df.notna().sum().sum()} values")
        time.sleep(2)


def fetch_prev_runs() -> None:
    """Previous Runs API keeps ~90 days of history for _previous_dayN variables."""
    end = END or pd.Timestamp.now("UTC").strftime("%Y-%m-%d")
    start = (pd.Timestamp(end) - pd.Timedelta(days=90)).strftime("%Y-%m-%d")
    core = ["temperature_2m", "wind_speed_10m", "wind_gusts_10m", "precipitation",
            "relative_humidity_2m", "cloud_cover"]
    for model in PREV_MODELS:
        hourly = [f"{v}_previous_day{d}" for v in core for d in range(1, PREV_DAYS + 1)]
        js = get("https://previous-runs-api.open-meteo.com/v1/forecast", {
            "latitude": LAT, "longitude": LON, "start_date": start, "end_date": end,
            "hourly": ",".join(hourly), "models": model, "timezone": "UTC", **UNITS,
        })
        df = frame(js)
        long = []
        for v in core:
            for d in range(1, PREV_DAYS + 1):
                col = f"{v}_previous_day{d}"
                if col in df:
                    s = df[col].rename(v).to_frame()
                    s["lead_d"] = d
                    long.append(s.reset_index())
        out = (pd.concat(long).groupby(["ts", "lead_d"]).first().reset_index())
        out["model"] = model
        out.to_parquet(OUT / f"prevruns_{model}.parquet", index=False)
        print(f"prevruns {model}: {len(out)} rows")
        time.sleep(2)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    fetch_day0()
    fetch_prev_runs()
    # The regional archives are large, reproducible from the API, and only ever read by
    # the weekly bake-off that fetches them. They stay out of git (see .gitignore).
    fetch_day0(REGIONAL_LAT, REGIONAL_LON, REGIONAL_START, OUT / "regional", "regional")
