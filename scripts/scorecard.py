"""Score the forecasts this repo actually published against what the station measured.

The retrain's cross-validation scores candidate models on history. This scores the
thing people actually read: every forecast.json committed here, compared hour by hour
with the station's readings, bespoke versus the raw regional forecast it started from.
On 2026-09-21 a one-off version of this check found the published temperature 7.6F too
warm on average while every backtest looked fine; running it every week makes that kind
of failure visible within days.

Reads forecast.json from git history, so the checkout needs full history
(fetch-depth: 0). Writes scorecard.json and scorecard.md to the reports directory.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ACTUALS_PARQUET, FORECAST_JSON, REPORTS_DIR, ROOT  # noqa: E402
from train import frozen_hours  # noqa: E402

VARS = {"temp_f": "Temperature (F)", "humidity_pct": "Humidity (%)",
        "dewpoint_f": "Dew point (F)", "wind_mph": "Wind (mph)", "gust_mph": "Gusts (mph)"}
WINDOWS_D = (7, 28)
LEADS = [(0, 6, "0-6h"), (6, 24, "6-24h"), (24, 48, "24-48h"), (48, 73, "48-72h")]

# Chance of precipitation is a probability, so it is scored with the Brier score - the
# mean squared gap between the published chance (0-1) and whether the gauge then
# recorded at least WET_IN in that hour - not with an average miss. 0 is perfect.
# "Climatology", always saying the window's own wet-hour rate, is the number a forecast
# has to beat to be worth publishing at all. Bespoke is the share of twelve models
# forecasting rain (predict.py, published since 2026-10-18); raw is Open-Meteo's own
# probability, published beside it for exactly this comparison. The gauge is a tipping
# bucket, so winter hours score snow as dry: read the wet_hours count before trusting a
# winter window.
WET_IN = 0.01
PROB_VARS = ("precip_prob", "precip_prob_openmeteo")


def published_forecasts(since: pd.Timestamp) -> list[dict]:
    rel = FORECAST_JSON.relative_to(ROOT).as_posix()
    shas = subprocess.run(["git", "-C", str(ROOT), "log", f"--since={since.isoformat()}",
                           "--format=%H", "--", rel],
                          capture_output=True, text=True, check=True).stdout.split()
    out = []
    for sha in shas:
        r = subprocess.run(["git", "-C", str(ROOT), "show", f"{sha}:{rel}"],
                           capture_output=True, text=True, encoding="utf-8")
        if r.returncode == 0:
            try:
                out.append(json.loads(r.stdout))
            except json.JSONDecodeError:
                pass
    return out


def pairs(forecasts: list[dict], actuals: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for f in forecasts:
        issued = pd.Timestamp(f["generated_at"])
        methods = f.get("methods", {})
        h = f.get("hourly", {})
        for i, ts in enumerate(h.get("ts", [])):
            t = pd.Timestamp(ts)
            lead = (t - issued).total_seconds() / 3600
            if lead < 0 or t not in actuals.index:
                continue
            for v in VARS:
                act = actuals.at[t, v] if v in actuals else np.nan
                bes, raw = (h.get(v) or [None])[i:i + 1], (h.get(v + "_raw") or [None])[i:i + 1]
                if pd.isna(act) or not bes or not raw or bes[0] is None or raw[0] is None:
                    continue
                rows.append((v, t, lead, float(act), float(bes[0]), float(raw[0]),
                             methods.get(v, "raw")))
    return pd.DataFrame(rows, columns=["var", "ts", "lead_h", "actual", "bespoke", "raw",
                                       "method"])


def station_wet(actuals: pd.DataFrame) -> pd.Series:
    """1 where the gauge recorded >= WET_IN in the hour, 0 where it recorded less, NaN
    where it reported nothing. Hourly amounts come from the cumulative daily counter,
    the same way bakeoff.load_actuals derives them."""
    if "rain_daily_in" not in actuals:
        return pd.Series(dtype=float)
    daily = actuals["rain_daily_in"]
    inc = daily.diff()
    inc[inc < 0] = daily[inc < 0]  # day rollover: the counter resets, the new value IS the increment
    return (inc >= WET_IN).astype(float).where(inc.notna())


def pairs_prob(forecasts: list[dict], wet: pd.Series) -> pd.DataFrame:
    rows = []
    for f in forecasts:
        issued = pd.Timestamp(f["generated_at"])
        h = f.get("hourly", {})
        bes_all, raw_all = h.get(PROB_VARS[0]), h.get(PROB_VARS[1])
        if not bes_all or not raw_all:
            continue  # published before both probabilities existed
        for i, ts in enumerate(h.get("ts", [])):
            t = pd.Timestamp(ts)
            lead = (t - issued).total_seconds() / 3600
            if lead < 0 or t not in wet.index or pd.isna(wet.at[t]):
                continue
            bes, raw = bes_all[i] if i < len(bes_all) else None, raw_all[i] if i < len(raw_all) else None
            if bes is None or raw is None:
                continue
            rows.append((t, lead, float(wet.at[t]), float(bes) / 100, float(raw) / 100))
    return pd.DataFrame(rows, columns=["ts", "lead_h", "wet", "bespoke", "raw"])


def summarise_prob(d: pd.DataFrame) -> dict:
    brier = lambda p: float(((p - d.wet) ** 2).mean())
    b, r = brier(d.bespoke), brier(d.raw)
    base = float(d.wet.mean())
    wet_hours = int(d[d.wet > 0].ts.nunique())
    # a dry window judges nothing: both scores are near zero and their ratio is noise
    return {"pairs": int(len(d)), "hours": int(d.ts.nunique()), "wet_hours": wet_hours,
            "bespoke_brier": round(b, 4), "raw_brier": round(r, 4),
            "climatology_brier": round(base * (1 - base), 4),
            "improvement_pct": round(100 * (1 - b / r), 1) if (r and wet_hours) else None}


def summarise(d: pd.DataFrame) -> dict:
    be, re = d.bespoke - d.actual, d.raw - d.actual
    b_mae, r_mae = float(be.abs().mean()), float(re.abs().mean())
    # which correction actually produced these forecasts, so the retrain's gate can tell
    # whether this result is evidence about the method it is considering
    shares = (d.method.value_counts(normalize=True).round(3).to_dict()
              if "method" in d else {})
    return {"pairs": int(len(d)), "hours": int(d.ts.nunique()),
            "published_methods": shares,
            "bespoke_mae": round(b_mae, 2), "raw_mae": round(r_mae, 2),
            "bespoke_bias": round(float(be.mean()), 2), "raw_bias": round(float(re.mean()), 2),
            "improvement_pct": round(100 * (1 - b_mae / r_mae), 1) if r_mae else None}


def main() -> None:
    now = pd.Timestamp.now("UTC")
    actuals = pd.read_parquet(ACTUALS_PARQUET)
    # a frozen sensor is not ground truth (see train.frozen_hours)
    for v in VARS:
        if v in actuals:
            actuals.loc[actuals.index.isin(frozen_hours(actuals, v)), v] = np.nan

    forecasts = published_forecasts(now - pd.Timedelta(days=max(WINDOWS_D) + 3))
    d = pairs(forecasts, actuals)
    dp = pairs_prob(forecasts, station_wet(actuals))
    card = {"generated_at": now.isoformat(), "forecasts_read": len(forecasts),
            "actuals_end": str(actuals.dropna(how="all").index.max()), "windows": {}}
    lines = ["# ThorCast scorecard", "",
             f"Every published forecast, compared hour by hour with the Bear Paw station. "
             f"Bespoke is what the page showed; raw is the regional model it started from. "
             f"Positive improvement means bespoke was closer. Updated {now:%Y-%m-%d %H:%M} UTC; "
             f"station data to {card['actuals_end'][:16]}.", ""]

    for days in WINDOWS_D:
        w = d[d.ts >= now - pd.Timedelta(days=days)]
        key = f"last_{days}_days"
        card["windows"][key] = {}
        lines += [f"## Last {days} days", ""]
        if w.empty:
            lines += ["_No overlapping forecasts and station readings yet._", ""]
            continue
        lines += ["| variable | hours | bespoke avg miss | raw avg miss | improvement | bespoke bias |",
                  "|---|---|---|---|---|---|"]
        for v, label in VARS.items():
            x = w[w["var"] == v]
            if x.empty:
                continue
            s = summarise(x)
            s["by_lead"] = {name: summarise(x[(x.lead_h >= lo) & (x.lead_h < hi)])
                            for lo, hi, name in LEADS if len(x[(x.lead_h >= lo) & (x.lead_h < hi)])}
            card["windows"][key][v] = s
            lines.append(f"| {label} | {s['hours']} | {s['bespoke_mae']} | {s['raw_mae']} | "
                         f"{s['improvement_pct']:+.0f}% | {s['bespoke_bias']:+.1f} |")
        lines.append("")
        wp = dp[dp.ts >= now - pd.Timedelta(days=days)]
        if not wp.empty:
            s = summarise_prob(wp)
            s["by_lead"] = {name: summarise_prob(wp[(wp.lead_h >= lo) & (wp.lead_h < hi)])
                            for lo, hi, name in LEADS if len(wp[(wp.lead_h >= lo) & (wp.lead_h < hi)])}
            card["windows"][key]["precip_prob"] = s
            lines += ["| rain chance (Brier, 0 = perfect) | hours | wet hours | bespoke | Open-Meteo | always-climatology | improvement |",
                      "|---|---|---|---|---|---|---|",
                      f"| Rain chance | {s['hours']} | {s['wet_hours']} | {s['bespoke_brier']} | "
                      f"{s['raw_brier']} | {s['climatology_brier']} | "
                      f"{s['improvement_pct']:+.0f}% |"
                      if s['improvement_pct'] is not None else
                      f"| Rain chance | {s['hours']} | {s['wet_hours']} | {s['bespoke_brier']} | "
                      f"{s['raw_brier']} | {s['climatology_brier']} | n/a |", ""]

    (REPORTS_DIR / "scorecard.json").write_text(json.dumps(card, indent=2), encoding="utf-8")
    (REPORTS_DIR / "scorecard.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
