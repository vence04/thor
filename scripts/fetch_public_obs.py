"""Fetch public hourly observations from the nearest ASOS station.

The Bear Paw station went outdoors on 2026-07-13, so every model ranking we can make
from it covers summer and autumn and nothing else. A model that handles a July
afternoon well is not thereby a model that handles a January inversion well, and
ranking on three months is how you end up confidently using the wrong model all
winter. KHIE - Mount Washington Regional, Whitefield NH, 16 km east - has hourly
observations going back years, free and keyless, from the Iowa Environmental Mesonet
ASOS archive.

KHIE is not Bear Paw and is not meant to be. It answers a different question: which
MODELS handle this corner of the White Mountains, over whole seasons. The Ecowitt
still decides everything site-specific - the offsets, and the final choice between
models that the regional record cannot separate.

Writes data/obs_<station>.parquet (hourly means, our column names).
"""
import io
import sys
import time
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ACTUALS_DIR  # noqa: E402

# station, its coordinates, and how far it is from Bear Paw (44.3206, -71.7439)
STATION = "HIE"
STATION_NAME = "Mount Washington Regional, Whitefield NH"
STATION_LAT, STATION_LON = 44.3681, -71.5453
START_YEAR = 2024

IEM = "https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py"
# ASOS field -> our name. sknt and gust are knots; tmpf/dwpf already Fahrenheit.
FIELDS = {"tmpf": "temp_f", "dwpf": "dewpoint_f", "relh": "humidity_pct",
          "sknt": "wind_mph", "gust": "gust_mph", "mslp": "pressure_msl_hpa"}
KT_TO_MPH = 1.15078


def fetch_year(year: int) -> pd.DataFrame:
    params = {
        "station": STATION, "data": ",".join(FIELDS), "tz": "UTC",
        "year1": year, "month1": 1, "day1": 1,
        "year2": year + 1, "month2": 1, "day2": 1,
        "format": "onlycomma", "missing": "M", "trace": "0.0001",
        # report_type 3 is the routine hourly observation; 4 would add the specials
        # that cluster around squalls and would weight the record towards bad weather.
        "report_type": 3,
    }
    for attempt in range(4):
        try:
            r = requests.get(IEM, params=params, timeout=180)
            if r.status_code == 200 and r.text.count("\n") > 2:
                return pd.read_csv(io.StringIO(r.text), na_values=["M", ""])
            print(f"  {year}: HTTP {r.status_code}, {r.text.count(chr(10))} lines; retrying")
        except requests.exceptions.RequestException as exc:
            print(f"  {year}: {type(exc).__name__}; retrying")
        time.sleep(10 * (attempt + 1))
    raise RuntimeError(f"IEM did not return {STATION} data for {year}")


def main() -> None:
    now = pd.Timestamp.now("UTC")
    frames = []
    for year in range(START_YEAR, now.year + 1):
        df = fetch_year(year)
        print(f"  {year}: {len(df)} observations")
        frames.append(df)
        time.sleep(2)

    raw = pd.concat(frames, ignore_index=True)
    raw["ts"] = pd.to_datetime(raw.pop("valid"), utc=True, format="mixed")
    out = pd.DataFrame(index=raw.set_index("ts").index)
    for src, dst in FIELDS.items():
        if src in raw:
            out[dst] = pd.to_numeric(raw[src], errors="coerce").values
    for c in ("wind_mph", "gust_mph"):
        out[c] = out[c] * KT_TO_MPH
    # a calm hour reports no gust at all; that is a zero, not a missing reading
    out["gust_mph"] = out["gust_mph"].fillna(out["wind_mph"])

    hourly = out.resample("1h").mean()
    hourly = hourly.dropna(how="all")
    ACTUALS_DIR.mkdir(parents=True, exist_ok=True)
    path = ACTUALS_DIR / f"obs_{STATION.lower()}.parquet"
    hourly.to_parquet(path)
    span = f"{hourly.index.min():%Y-%m-%d} to {hourly.index.max():%Y-%m-%d}"
    by_season = hourly.groupby(hourly.index.month.map(
        {12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
         6: "summer", 7: "summer", 8: "summer", 9: "fall", 10: "fall", 11: "fall"}
    ))["temp_f"].count()
    print(f"{path.name}: {len(hourly)} hours, {span}")
    print("  hours by season:", by_season.to_dict())


if __name__ == "__main__":
    main()
