"""Where the data lives, in whichever repo this is running from.

The pipeline runs in two places:

  bearpaw-weather (private)  data/actuals/  data/forecasts/  model/  reports/
  thor            (public)   data/          data/            data/   data/

thor is flat because its data/ is the published feed - Home Assistant and the
Databricks pull both read fixed paths there, so the layout is a contract and is not
worth breaking. Resolving it here keeps one copy of every script instead of a fork
per repo, which is how predict.py already drifted once.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# bearpaw-weather has data/actuals/; thor does not.
FLAT = not (ROOT / "data" / "actuals").is_dir()

ACTUALS_DIR = ROOT / "data" if FLAT else ROOT / "data" / "actuals"
FORECAST_DIR = ROOT / "data" if FLAT else ROOT / "data" / "forecasts"
MODEL_DIR = ROOT / "data" if FLAT else ROOT / "model"
REPORTS_DIR = ROOT / "data" if FLAT else ROOT / "reports"

ACTUALS_PARQUET = ACTUALS_DIR / "ecowitt_hourly.parquet"
MODEL_JSON = MODEL_DIR / "model.json"

# The page is served from thor's repo root; the private repo keeps it under site/.
FORECAST_JSON = (ROOT / "site" / "forecast.json") if (ROOT / "site").is_dir() \
    else (ROOT / "forecast.json")


def ensure_dirs() -> None:
    for d in (ACTUALS_DIR, FORECAST_DIR, MODEL_DIR, REPORTS_DIR):
        d.mkdir(parents=True, exist_ok=True)
