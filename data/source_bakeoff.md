# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Actuals: Ecowitt station hourly means, 2025-08-18 to 2026-07-14.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Day-0 skill by variable (lower MAE = better)

### pressure_abs_hpa

| model         |    n |   mae |   bias |   rmse |
|:--------------|-----:|------:|-------:|-------:|
| gem_seamless  | 7186 |  1.26 |  -0.02 |   2.71 |
| icon_seamless | 7186 |  1.33 |  -0.12 |   2.73 |
| ecmwf_ifs025  | 7186 |  1.43 |  -0.29 |   2.75 |
| best_match    | 7186 |  2.19 |  -1.12 |   3.20 |
| gfs_hrrr      | 7186 |  2.19 |  -1.12 |   3.20 |
| gfs_seamless  | 7186 |  2.19 |  -1.12 |   3.20 |

## MAE by lead time, days 1-7 (previous-runs)

_Not enough outdoor-era data yet — accumulates automatically via weekly retrain._

## Seasonal day-0 MAE (temperature)

| model   |
|---------|
