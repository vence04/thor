"""Source bake-off: score each forecast model against Bear Paw station actuals.

Produces reports/source_bakeoff.md with MAE/bias per variable per model (day-0 skill,
11 months) and MAE by lead day 1-7 (previous-runs, 90 days).
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import (ACTUALS_DIR, ACTUALS_PARQUET, FORECAST_DIR, MODEL_DIR,
                   MODEL_JSON, REPORTS_DIR, ensure_dirs)  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FC = FORECAST_DIR
INHG_TO_HPA = 33.8639

# Before this the sensors sat indoors (discovered 2026-07-13: Jan "outdoor" temp ~70F,
# wind 0.0 for 4954h, no solar signal). Only pressure is valid earlier.
OUTDOOR_START = pd.Timestamp("2026-07-13T19:00:00Z")
FULL_HISTORY_VARS = {"pressure_abs_hpa"}

# actual column -> forecast column
VARMAP = {
    "temp_f": "temperature_2m",
    "humidity_pct": "relative_humidity_2m",
    "dewpoint_f": "dew_point_2m",
    "wind_mph": "wind_speed_10m",
    "gust_mph": "wind_gusts_10m",
    "pressure_abs_hpa": "surface_pressure",
    "precip_in": "precipitation",
}
SEASONS = {12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
           6: "summer", 7: "summer", 8: "summer", 9: "fall", 10: "fall", 11: "fall"}


def load_actuals() -> pd.DataFrame:
    a = pd.read_parquet(ACTUALS_PARQUET)
    a["pressure_abs_hpa"] = a["pressure_abs_inhg"] * INHG_TO_HPA
    # hourly precip from cumulative daily rain: increments within each local day
    daily = a["rain_daily_in"]
    inc = daily.diff()
    inc[inc < 0] = daily[inc < 0]  # day rollover: counter resets, new value IS the increment
    a["precip_in"] = inc
    return a


def score_day0(actuals: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows, srows = [], []
    for f in sorted(FC.glob("day0_*.parquet")):
        model = f.stem.replace("day0_", "")
        fc = pd.read_parquet(f)
        j = actuals.join(fc, how="inner", rsuffix="_fc")
        for av, fv in VARMAP.items():
            if av not in j or fv not in j:
                continue
            d = (j[fv] - j[av]).dropna()
            if av not in FULL_HISTORY_VARS:
                d = d[d.index >= OUTDOOR_START]
            if len(d) < 24:
                continue
            rows.append({"model": model, "variable": av, "n": len(d),
                         "mae": d.abs().mean(), "bias": d.mean(), "rmse": (d ** 2).mean() ** 0.5})
            for season, g in d.groupby(d.index.month.map(SEASONS)):
                srows.append({"model": model, "variable": av, "season": season,
                              "n": len(g), "mae": g.abs().mean(), "bias": g.mean()})
    return pd.DataFrame(rows), pd.DataFrame(srows)


def score_leads(actuals: pd.DataFrame) -> pd.DataFrame:
    rows = []
    lead_map = {"temp_f": "temperature_2m", "wind_mph": "wind_speed_10m",
                "gust_mph": "wind_gusts_10m", "humidity_pct": "relative_humidity_2m"}
    for f in sorted(FC.glob("prevruns_*.parquet")):
        model = f.stem.replace("prevruns_", "")
        fc = pd.read_parquet(f)
        for lead, g in fc.groupby("lead_d"):
            g = g.set_index("ts")
            j = actuals.join(g, how="inner", rsuffix="_fc")
            for av, fv in lead_map.items():
                d = (j[fv] - j[av]).dropna()
                if av not in FULL_HISTORY_VARS:
                    d = d[d.index >= OUTDOOR_START]
                if len(d) < 24:
                    continue
                rows.append({"model": model, "variable": av, "lead_d": lead,
                             "n": len(d), "mae": d.abs().mean(), "bias": d.mean()})
    return pd.DataFrame(rows)


def main() -> None:
    actuals = load_actuals()
    day0, seasonal = score_day0(actuals)
    leads = score_leads(actuals)

    out = ["# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)", "",
           f"Actuals: Ecowitt station hourly means, {actuals['temp_f'].dropna().index.min():%Y-%m-%d} to "
           f"{actuals['temp_f'].dropna().index.max():%Y-%m-%d}.",
           "Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).", ""]

    out.append("## Day-0 skill by variable (lower MAE = better)\n")
    if day0.empty:
        out.append("_Not enough outdoor-era data yet._\n")
    for var, g in (day0.groupby("variable") if not day0.empty else []):
        out.append(f"### {var}\n")
        out.append(g.sort_values("mae")[["model", "n", "mae", "bias", "rmse"]]
                   .to_markdown(index=False, floatfmt=".2f"))
        out.append("")

    out.append("## MAE by lead time, days 1-7 (previous-runs)\n")
    if leads.empty:
        out.append("_Not enough outdoor-era data yet — accumulates automatically via weekly retrain._\n")
    for var, g in (leads.groupby("variable") if not leads.empty else []):
        p = g.pivot_table(index="model", columns="lead_d", values="mae")
        out.append(f"### {var}\n")
        out.append(p.to_markdown(floatfmt=".2f"))
        out.append("")

    out.append("## Seasonal day-0 MAE (temperature)\n")
    st = seasonal[seasonal.variable == "temp_f"].pivot_table(index="model", columns="season", values="mae")
    out.append(st.to_markdown(floatfmt=".2f"))
    out.append("")

    (REPORTS_DIR).mkdir(exist_ok=True)
    (REPORTS_DIR / "source_bakeoff.md").write_text("\n".join(out))
    day0.to_csv(REPORTS_DIR / "day0_scores.csv", index=False)
    leads.to_csv(REPORTS_DIR / "lead_scores.csv", index=False)
    print("day-0 winners by variable:")
    print(day0.loc[day0.groupby("variable")["mae"].idxmin()][["variable", "model", "mae", "bias"]].to_string(index=False))


if __name__ == "__main__":
    main()
