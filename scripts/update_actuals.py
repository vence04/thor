"""Append recent station actuals to data/actuals/ecowitt_hourly.parquet.

Two sources, tried in order:
1. Ecowitt.net cloud API v3 (works from GitHub Actions; needs ECOWITT_APP_KEY,
   ECOWITT_API_KEY, ECOWITT_MAC). Credentials come from the environment, or from
   1Password when running on Lloyd's PC, same as export_ha_stats.py.
2. Home Assistant long-term statistics (works on the home LAN; reuses export_ha_stats).

If neither source is available this now FAILS. It used to exit 0 with a warning so
the retrain could proceed on existing data - and that is precisely how the station
being dead went unnoticed from 2026-07-14 to 2026-09-12: nine consecutive green
retrains that ingested nothing at all. A silent no-op is worse than a red build.
"""
import os
import subprocess
import sys
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ACTUALS_PARQUET as PARQUET  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

ECOWITT_FIELDS = {
    ("outdoor", "temperature"): "temp_f",
    ("outdoor", "humidity"): "humidity_pct",
    ("outdoor", "dew_point"): "dewpoint_f",
    ("wind", "wind_speed"): "wind_mph",
    ("wind", "wind_gust"): "gust_mph",
    ("wind", "wind_direction"): "wind_dir_deg",
    ("solar_and_uvi", "solar"): "solar_wm2",
    ("solar_and_uvi", "uvi"): "uv_index",
    ("rainfall", "rain_rate"): "rain_rate_inh",
    ("rainfall", "daily"): "rain_daily_in",
    ("pressure", "relative"): "pressure_rel_inhg",
    ("pressure", "absolute"): "pressure_abs_inhg",
}


# env var -> field of the "Ecowitt API" item (API Credential) in claude-code-secrets.
# username/credential are the template's own fields; mac is a custom one.
OP_FIELDS = {"ECOWITT_APP_KEY": "username",     # Application Key
             "ECOWITT_API_KEY": "credential",   # API Key
             "ECOWITT_MAC": "mac"}              # custom field, the station MAC


def secret(name: str) -> str | None:
    """Environment first (GitHub Actions), then 1Password (Lloyd's PC)."""
    val = os.environ.get(name)
    if val:
        return val
    ref = f"op://claude-code-secrets/Ecowitt API/{OP_FIELDS[name]}"
    try:
        out = subprocess.run(["op", "read", ref], capture_output=True, text=True, timeout=30)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() or None


def from_ecowitt_cloud(start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame | None:
    app_key, api_key, mac = (secret(k) for k in
                             ("ECOWITT_APP_KEY", "ECOWITT_API_KEY", "ECOWITT_MAC"))
    missing = [k for k, v in zip(("ECOWITT_APP_KEY", "ECOWITT_API_KEY", "ECOWITT_MAC"),
                                 (app_key, api_key, mac)) if not v]
    if missing:
        print(f"ecowitt cloud unavailable: no value for {', '.join(missing)}")
        return None
    r = requests.get("https://api.ecowitt.net/api/v3/device/history", params={
        "application_key": app_key, "api_key": api_key, "mac": mac,
        "start_date": start.strftime("%Y-%m-%d %H:%M:%S"),
        "end_date": end.strftime("%Y-%m-%d %H:%M:%S"),
        "cycle_type": "30min", "temp_unitid": 1, "pressure_unitid": 4,
        "wind_speed_unitid": 9, "rainfall_unitid": 13,
        "call_back": "outdoor,wind,solar_and_uvi,rainfall,pressure"}, timeout=120)
    r.raise_for_status()
    js = r.json()
    if js.get("code") != 0:
        print(f"ecowitt cloud error: {js.get('msg')}")
        return None
    cols = {}
    for (grp, field), canon in ECOWITT_FIELDS.items():
        node = js.get("data", {}).get(grp, {}).get(field, {})
        lst = node.get("list", {})
        if lst:
            s = pd.Series({pd.to_datetime(int(k), unit="s", utc=True): float(v)
                           for k, v in lst.items()})
            cols[canon] = s
    if not cols:
        return None
    df = pd.DataFrame(cols)
    return df.resample("1h").mean()


def from_home_assistant() -> bool:
    """LAN-only path. Set HA_URL (e.g. http://<host>:8123) to enable it.

    Deliberately not defaulted to the home address: this file is published to the
    public thor repo, which runs the same retrain. A GitHub runner can never reach a
    LAN host anyway, so CI simply skips this.
    """
    base = os.environ.get("HA_URL", "").rstrip("/")
    exporter = ROOT / "scripts" / "export_ha_stats.py"
    if not base or not exporter.exists():
        return False
    try:
        requests.get(f"{base}/api/", timeout=3)
    except requests.exceptions.RequestException:
        return False
    subprocess.run([sys.executable, str(exporter)], check=True)
    return True


def main() -> None:
    existing = pd.read_parquet(PARQUET)
    last = existing.dropna(how="all").index.max()
    start = (last - pd.Timedelta(hours=2)).tz_convert("UTC")
    end = pd.Timestamp.now("UTC")

    new = from_ecowitt_cloud(start, end)
    if new is not None:
        merged = pd.concat([existing, new])
        merged = merged[~merged.index.duplicated(keep="last")].sort_index()
        merged.to_parquet(PARQUET)
        print(f"ecowitt cloud: appended {len(new)} hours; parquet now ends {merged.index.max()}")
        return
    if from_home_assistant():
        print("refreshed from Home Assistant long-term statistics")
        return

    # Two different situations, and conflating them is either noise or a silent failure.
    #
    #  - No credentials at all: the Ecowitt keys have not been set up yet. That is a
    #    known pending task, not a new outage, so warn and let the retrain continue
    #    rather than mailing a red build every Monday about something already known.
    #  - Credentials present but nothing came back: something IS broken - dead station,
    #    revoked key, API change. Fail, because this is the case that hid a dead sensor
    #    for two months behind nine green builds.
    configured = any(secret(k) for k in ("ECOWITT_APP_KEY", "ECOWITT_API_KEY"))
    if not configured:
        print("::warning::Ecowitt credentials are not configured, so no new observations "
              "were ingested. The offset model cannot improve until they are set. "
              f"Existing data ends at {last}.")
        return

    print("::error::Ecowitt credentials ARE configured but no observations could be "
          "fetched, and Home Assistant is not reachable from here. The station is "
          f"likely down. Existing data still ends at {last}.")
    sys.exit(1)


if __name__ == "__main__":
    main()
