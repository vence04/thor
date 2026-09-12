"""Fetch archived model forecasts for Bear Paw Lodge from Open-Meteo.

Two products:
1. Historical Forecast API -> day-0 (freshest-run) hourly series per model, for the
   source bake-off against station actuals.
2. Previous Runs API -> the same variables as forecast 1..7 days ahead, for
   lead-time-dependent bias modelling.

Free, keyless, non-commercial. Writes parquet to data/forecasts/.
"""
import time
import sys
from pathlib import Path

import pandas as pd
import requests

LAT, LON = 44.3205501, -71.7438537
START, END = "2025-08-18", None  # END defaults to today
OUT = Path(__file__).resolve().parents[1] / "data" / "forecasts"

HOURLY = [
    "temperature_2m", "relative_humidity_2m", "dew_point_2m",
    "wind_speed_10m", "wind_gusts_10m", "wind_direction_10m",
    "precipitation", "cloud_cover", "surface_pressure", "shortwave_radiation",
]
UNITS = {"temperature_unit": "fahrenheit", "wind_speed_unit": "mph", "precipitation_unit": "inch"}

MODELS = ["best_match", "ecmwf_ifs025", "gfs_seamless", "gfs_hrrr",
          "ncep_nbm_conus", "icon_seamless", "gem_seamless"]

PREV_DAYS = 7
PREV_MODELS = ["best_match", "ecmwf_ifs025", "gfs_seamless", "ncep_nbm_conus"]


def get(url: str, params: dict, retries: int = 4) -> dict:
    for i in range(retries):
        try:
            r = requests.get(url, params=params, timeout=180)
        except requests.exceptions.RequestException:
            time.sleep(10 * (i + 1))
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code in (429, 500, 502, 503):
            time.sleep(10 * (i + 1))
            continue
        raise RuntimeError(f"{r.status_code}: {r.text[:300]}")
    raise RuntimeError("retries exhausted")


def frame(js: dict) -> pd.DataFrame:
    df = pd.DataFrame(js["hourly"])
    df["ts"] = pd.to_datetime(df.pop("time"), utc=True)
    return df.set_index("ts")


def fetch_day0() -> None:
    end = END or pd.Timestamp.now("UTC").strftime("%Y-%m-%d")
    for model in MODELS:
        js = get("https://historical-forecast-api.open-meteo.com/v1/forecast", {
            "latitude": LAT, "longitude": LON, "start_date": START, "end_date": end,
            "hourly": ",".join(HOURLY), "models": model, "timezone": "UTC", **UNITS,
        })
        df = frame(js)
        df.to_parquet(OUT / f"day0_{model}.parquet")
        print(f"day0 {model}: {len(df)} rows, {df.notna().sum().sum()} values")
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
