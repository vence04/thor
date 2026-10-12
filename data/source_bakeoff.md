# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Actuals: Ecowitt station hourly means, 2025-08-18 to 2026-10-12.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Day-0 skill by variable (lower MAE = better)

### dewpoint_f

| model          |    n |   mae |   bias |   rmse |
|:---------------|-----:|------:|-------:|-------:|
| ncep_nbm_conus | 1649 |  2.39 |   0.65 |   3.43 |
| icon_seamless  | 1649 |  2.61 |  -0.79 |   3.50 |
| gem_seamless   | 1649 |  2.74 |  -0.55 |   3.78 |
| ecmwf_ifs025   | 1649 |  2.76 |  -0.65 |   3.74 |
| gfs_hrrr       | 1649 |  3.00 |  -0.48 |   4.18 |
| best_match     | 1649 |  3.00 |  -0.48 |   4.18 |
| gfs_seamless   | 1649 |  3.00 |  -0.48 |   4.18 |

### gust_mph

| model          |    n |   mae |   bias |   rmse |
|:---------------|-----:|------:|-------:|-------:|
| ncep_nbm_conus | 1649 |  3.47 |   2.29 |   4.62 |
| gem_seamless   | 1649 |  3.83 |   1.77 |   5.52 |
| gfs_hrrr       | 1649 |  4.80 |   3.66 |   6.67 |
| best_match     | 1649 |  4.80 |   3.66 |   6.67 |
| gfs_seamless   | 1649 |  4.80 |   3.66 |   6.67 |
| icon_seamless  | 1649 |  5.52 |   5.10 |   7.45 |
| ecmwf_ifs025   | 1649 |  7.25 |   7.13 |   8.76 |

### humidity_pct

| model          |    n |   mae |   bias |   rmse |
|:---------------|-----:|------:|-------:|-------:|
| ecmwf_ifs025   | 1649 |  7.04 |   0.58 |   9.81 |
| best_match     | 1649 |  7.57 |   0.50 |   9.70 |
| gfs_hrrr       | 1649 |  7.57 |   0.50 |   9.70 |
| gfs_seamless   | 1649 |  7.57 |   0.50 |   9.70 |
| icon_seamless  | 1649 |  7.77 |   1.56 |  10.47 |
| gem_seamless   | 1649 |  7.93 |   0.08 |  11.13 |
| ncep_nbm_conus | 1649 |  8.66 |   5.11 |  10.97 |

### precip_in

| model          |    n |   mae |   bias |   rmse |
|:---------------|-----:|------:|-------:|-------:|
| best_match     | 2063 |  0.00 |  -0.00 |   0.04 |
| gfs_hrrr       | 2063 |  0.00 |  -0.00 |   0.04 |
| gfs_seamless   | 2063 |  0.00 |  -0.00 |   0.04 |
| icon_seamless  | 2063 |  0.01 |  -0.00 |   0.03 |
| gem_seamless   | 2063 |  0.01 |  -0.00 |   0.03 |
| ncep_nbm_conus | 2063 |  0.01 |  -0.00 |   0.02 |
| ecmwf_ifs025   | 2063 |  0.01 |   0.00 |   0.02 |

### pressure_abs_hpa

| model         |    n |   mae |   bias |   rmse |
|:--------------|-----:|------:|-------:|-------:|
| gem_seamless  | 9234 |  1.25 |  -0.26 |   2.64 |
| icon_seamless | 9234 |  1.32 |  -0.34 |   2.65 |
| ecmwf_ifs025  | 9234 |  1.40 |  -0.47 |   2.68 |
| best_match    | 9234 |  2.12 |  -1.27 |   3.13 |
| gfs_hrrr      | 9234 |  2.12 |  -1.27 |   3.13 |
| gfs_seamless  | 9234 |  2.12 |  -1.27 |   3.13 |

### temp_f

| model          |    n |   mae |   bias |   rmse |
|:---------------|-----:|------:|-------:|-------:|
| ecmwf_ifs025   | 1649 |  3.22 |  -0.64 |   4.52 |
| best_match     | 1649 |  3.45 |  -0.89 |   4.78 |
| gfs_hrrr       | 1649 |  3.45 |  -0.89 |   4.78 |
| gfs_seamless   | 1649 |  3.45 |  -0.89 |   4.78 |
| gem_seamless   | 1649 |  3.45 |  -0.21 |   4.93 |
| ncep_nbm_conus | 1649 |  3.69 |  -1.18 |   4.83 |
| icon_seamless  | 1649 |  3.82 |  -1.17 |   5.06 |

### wind_mph

| model          |    n |   mae |   bias |   rmse |
|:---------------|-----:|------:|-------:|-------:|
| gem_seamless   | 1649 |  2.43 |   2.30 |   2.93 |
| icon_seamless  | 1649 |  2.62 |   2.55 |   3.27 |
| ncep_nbm_conus | 1649 |  2.63 |   2.47 |   3.41 |
| best_match     | 1649 |  3.37 |   3.28 |   4.16 |
| gfs_seamless   | 1649 |  3.37 |   3.28 |   4.16 |
| gfs_hrrr       | 1649 |  3.37 |   3.28 |   4.16 |
| ecmwf_ifs025   | 1649 |  3.45 |   3.39 |   4.23 |

## MAE by lead time, days 1-7 (previous-runs)

### gust_mph

| model          |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match     | 6.79 |   3.64 |   3.71 |   3.98 |   4.33 |   4.73 |   4.68 |
| gem_seamless   | 4.26 |   4.13 |   4.25 |   4.11 |   4.25 |   4.53 |   5.05 |
| gfs_hrrr       | 6.79 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless   | 6.79 |   3.64 |   3.71 |   3.98 |   4.33 |   4.73 |   4.68 |
| icon_seamless  | 5.69 |   5.73 |   5.79 |   6.06 |   5.80 |   5.76 | nan    |
| ncep_nbm_conus | 3.49 |   3.59 |   3.64 |   3.68 |   3.66 |   3.69 |   3.70 |

### humidity_pct

| model          |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match     | 12.88 |  10.19 |  11.58 |  12.14 |  12.13 |  14.05 |  13.95 |
| ecmwf_ifs025   |  8.03 |   8.73 |   9.57 |   9.96 |  11.28 |  11.31 |  11.39 |
| gem_seamless   |  9.79 |  10.54 |  10.55 |  11.17 |  12.18 |  12.94 |  13.32 |
| gfs_hrrr       | 12.88 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless   | 12.88 |  10.19 |  11.58 |  12.14 |  12.13 |  14.05 |  13.95 |
| icon_seamless  |  8.53 |   8.66 |   9.12 |  10.30 |  11.25 |  11.80 | nan    |
| ncep_nbm_conus |  9.13 |   9.40 |   9.75 |  10.40 |  10.80 |  10.90 |  11.27 |

### temp_f

| model          |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match     | 3.55 |   4.67 |   4.80 |   5.14 |   5.26 |   5.78 |   5.81 |
| ecmwf_ifs025   | 3.37 |   3.52 |   3.65 |   4.02 |   4.10 |   4.47 |   4.47 |
| gem_seamless   | 3.71 |   4.45 |   4.07 |   4.54 |   4.67 |   4.81 |   5.27 |
| gfs_hrrr       | 3.55 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless   | 3.55 |   4.67 |   4.80 |   5.14 |   5.26 |   5.78 |   5.81 |
| icon_seamless  | 3.91 |   4.05 |   4.25 |   4.33 |   4.60 |   5.03 | nan    |
| ncep_nbm_conus | 3.88 |   4.01 |   4.00 |   4.06 |   4.23 |   4.29 |   4.33 |

### wind_mph

| model          |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match     | 4.60 |   2.73 |   2.54 |   2.63 |   2.62 |   2.61 |   2.42 |
| ecmwf_ifs025   | 3.56 |   3.62 |   3.40 |   3.50 |   3.62 |   3.17 |   3.09 |
| gem_seamless   | 2.57 |   2.17 |   1.87 |   1.82 |   1.87 |   1.78 |   1.89 |
| gfs_hrrr       | 4.60 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless   | 4.60 |   2.73 |   2.54 |   2.63 |   2.62 |   2.61 |   2.42 |
| icon_seamless  | 2.73 |   2.74 |   2.79 |   2.79 |   2.65 |   2.59 | nan    |
| ncep_nbm_conus | 2.65 |   2.63 |   2.57 |   2.49 |   2.23 |   2.11 |   1.98 |

## Seasonal day-0 MAE (temperature)

| model          |   fall |   summer |
|:---------------|-------:|---------:|
| best_match     |   2.76 |     3.84 |
| ecmwf_ifs025   |   2.36 |     3.70 |
| gem_seamless   |   2.69 |     3.89 |
| gfs_hrrr       |   2.76 |     3.84 |
| gfs_seamless   |   2.76 |     3.84 |
| icon_seamless  |   3.21 |     4.16 |
| ncep_nbm_conus |   2.88 |     4.14 |
