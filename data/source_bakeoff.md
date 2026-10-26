# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-10-26.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Source in use, per variable

| variable | source |
|---|---|
| dewpoint_f | ncep_nbm_conus |
| gust_mph | blend of gem_seamless, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| humidity_pct | blend of gfs_hrrr, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| precip_in | best_match |
| pressure_abs_hpa | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |
| temp_f | ecmwf_ifs025 |
| wind_mph | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |

## Site skill, shortlisted candidates (lower MAE = better)

### dewpoint_f

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ncep_nbm_conus                                                                | 1913 |  2.30 |   0.65 |   0.98 | raw                |            1.77 |      574.00 |                   1.72 |
| knmi_seamless                                                                 | 1913 |  2.70 |  -0.31 |   0.97 | bias               |            1.94 |      574.00 |                   2.25 |
| ecmwf_ifs025                                                                  | 1913 |  2.73 |  -0.79 |   0.97 | bias               |            2.00 |      574.00 |                   2.34 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1913 |  2.11 |  -0.30 |   0.98 | ridge              |            2.14 |      574.00 |                   2.33 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  2.36 |  -0.15 |   0.98 | ridge              |            2.17 |      574.00 |                   2.42 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 1913 |  2.15 |  -0.01 |   0.98 | ridge              |            2.20 |      574.00 |                   2.36 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1913 |  2.16 |  -0.11 |   0.99 | ridge              |            2.24 |      574.00 |                   2.51 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 1913 |  2.01 |  -0.20 |   0.99 | ridge              |            2.26 |      574.00 |                   2.46 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  2.16 |  -0.27 |   0.98 | ridge              |            2.26 |      574.00 |                   2.40 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1913 |  2.35 |  -0.21 |   0.98 | ridge              |            2.27 |      574.00 |                   2.48 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  2.12 |  -0.25 |   0.99 | ridge              |            2.32 |      574.00 |                   2.49 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  2.12 |  -0.25 |   0.99 | ridge              |            2.32 |      574.00 |                   2.49 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  2.47 |   0.04 |   0.98 | ridge              |            2.33 |      574.00 |                   2.56 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1913 |  2.12 |  -0.27 |   0.99 | ridge              |            2.33 |      574.00 |                   2.61 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1913 |  2.59 |   0.21 |   0.97 | ridge              |            2.36 |      574.00 |                   2.65 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 1913 |  2.33 |  -0.24 |   0.98 | ridge              |            2.36 |      574.00 |                   2.57 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  2.18 |  -0.31 |   0.98 | ridge              |            2.41 |      574.00 |                   2.72 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                               | 1913 |  2.20 |  -0.08 |   0.98 | ridge              |            2.48 |      574.00 |                   2.71 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1913 |  2.17 |   0.04 |   0.98 | ridge              |            2.53 |      574.00 |                   2.81 |
| icon_seamless                                                                 | 1913 |  2.51 |  -0.87 |   0.98 | ridge              |            2.53 |      574.00 |                   2.90 |
| ecmwf_aifs025_single                                                          | 1913 |  2.56 |  -0.70 |   0.98 | ridge              |            2.67 |      574.00 |                   2.82 |
| best_match                                                                    | 1913 |  2.95 |  -0.68 |   0.96 | ridge              |            2.90 |      574.00 |                   3.24 |
| gfs_seamless                                                                  | 1913 |  2.95 |  -0.68 |   0.96 | ridge              |            2.90 |      574.00 |                   3.24 |
| gfs_hrrr                                                                      | 1913 |  2.95 |  -0.68 |   0.96 | ridge              |            2.90 |      574.00 |                   3.24 |
| ukmo_seamless                                                                 | 1913 |  3.39 |  -0.22 |   0.93 | ridge              |            3.24 |      574.00 |                   3.73 |
| gem_seamless                                                                  | 1913 |  2.62 |  -0.58 |   0.98 | ridge              |            3.31 |      574.00 |                   3.76 |
| jma_seamless                                                                  | 1913 |  2.89 |  -0.43 |   0.95 | ridge              |            3.91 |      574.00 |                   4.58 |
| meteofrance_seamless                                                          | 1913 |  3.09 |  -0.21 |   0.97 | ridge              |            4.34 |      574.00 |                   5.54 |

### gust_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  4.41 |   3.93 |   0.86 | ridge              |            1.84 |      574.00 |                   1.91 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  4.41 |   3.93 |   0.86 | ridge              |            1.84 |      574.00 |                   1.91 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                               | 1913 |  3.97 |   3.34 |   0.86 | ridge              |            1.87 |      574.00 |                   1.93 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  4.27 |   3.77 |   0.86 | ridge              |            1.89 |      574.00 |                   1.95 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1913 |  4.75 |   4.43 |   0.85 | ridge              |            1.92 |      574.00 |                   2.01 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  4.24 |   3.76 |   0.85 | ridge              |            1.94 |      574.00 |                   2.05 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  4.80 |   4.34 |   0.84 | ridge              |            1.94 |      574.00 |                   1.97 |
| knmi_seamless                                                                 | 1913 |  6.02 |   5.83 |   0.84 | ridge              |            1.95 |      574.00 |                   1.97 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1913 |  3.86 |   3.08 |   0.86 | ridge              |            1.97 |      574.00 |                   1.97 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 1913 |  3.72 |   2.66 |   0.84 | ridge              |            1.98 |      574.00 |                   1.97 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1913 |  3.88 |   2.95 |   0.83 | ridge              |            1.98 |      574.00 |                   1.97 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1913 |  3.34 |   2.09 |   0.85 | ridge              |            1.99 |      574.00 |                   1.98 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1913 |  4.30 |   3.76 |   0.84 | ridge              |            2.01 |      574.00 |                   2.02 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  4.09 |   3.50 |   0.84 | ridge              |            2.02 |      574.00 |                   2.07 |
| ecmwf_ifs025                                                                  | 1913 |  7.25 |   7.13 |   0.84 | ridge              |            2.03 |      574.00 |                   1.94 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1913 |  3.61 |   2.73 |   0.83 | ridge              |            2.05 |      574.00 |                   2.13 |
| ncep_nbm_conus                                                                | 1913 |  3.58 |   2.46 |   0.82 | ridge              |            2.11 |      574.00 |                   2.21 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 1913 |  4.11 |   3.13 |   0.80 | ridge              |            2.12 |      574.00 |                   2.10 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 1913 |  4.35 |   3.35 |   0.79 | ridge              |            2.16 |      574.00 |                   2.08 |
| icon_seamless                                                                 | 1913 |  5.47 |   5.06 |   0.82 | ridge              |            2.17 |      574.00 |                   1.99 |
| gem_seamless                                                                  | 1913 |  3.78 |   1.72 |   0.81 | ridge              |            2.25 |      574.00 |                   2.06 |
| best_match                                                                    | 1913 |  4.92 |   3.80 |   0.75 | ridge              |            2.28 |      574.00 |                   2.08 |
| gfs_seamless                                                                  | 1913 |  4.92 |   3.80 |   0.75 | ridge              |            2.28 |      574.00 |                   2.08 |
| gfs_hrrr                                                                      | 1913 |  4.92 |   3.80 |   0.75 | ridge              |            2.28 |      574.00 |                   2.08 |
| ukmo_seamless                                                                 | 1913 |  4.01 |   3.00 |   0.78 | ridge              |            2.29 |      574.00 |                   2.23 |
| meteofrance_seamless                                                          | 1913 |  5.68 |   5.34 |   0.73 | ridge              |            2.43 |      574.00 |                   2.33 |

### humidity_pct

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  5.87 |   1.51 |   0.95 | bias               |            4.97 |      574.00 |                   5.46 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  5.97 |   1.49 |   0.95 | bias               |            5.02 |      574.00 |                   5.34 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  5.97 |   1.49 |   0.95 | bias               |            5.02 |      574.00 |                   5.34 |
| ecmwf_aifs025_single                                                          | 1913 |  6.82 |   2.24 |   0.94 | bias               |            5.37 |      574.00 |                   5.89 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 1913 |  6.30 |   2.31 |   0.94 | bias               |            5.50 |      574.00 |                   5.96 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1913 |  7.06 |   2.65 |   0.93 | bias               |            5.51 |      574.00 |                   6.31 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                               | 1913 |  6.80 |   2.15 |   0.93 | bias               |            5.63 |      574.00 |                   5.82 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 1913 |  6.69 |   3.17 |   0.94 | bias               |            5.65 |      574.00 |                   6.06 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1913 |  6.39 |   2.55 |   0.94 | bias               |            5.65 |      574.00 |                   6.38 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1913 |  7.08 |   2.75 |   0.93 | bias               |            5.66 |      574.00 |                   6.68 |
| ecmwf_ifs025                                                                  | 1913 |  6.94 |   0.66 |   0.92 | bias               |            5.74 |      574.00 |                   6.48 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1913 |  7.66 |   3.82 |   0.93 | bias               |            5.75 |      574.00 |                   6.86 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  7.10 |   3.08 |   0.92 | bias               |            5.78 |      574.00 |                   6.94 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 1913 |  6.63 |   2.35 |   0.93 | bias               |            5.79 |      574.00 |                   6.26 |
| knmi_seamless                                                                 | 1913 |  7.21 |   0.25 |   0.92 | bias               |            6.02 |      574.00 |                   6.46 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  7.67 |   3.65 |   0.92 | bias               |            6.13 |      574.00 |                   6.79 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1913 |  7.39 |   3.10 |   0.92 | bias               |            6.21 |      574.00 |                   6.51 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  8.01 |   4.25 |   0.92 | bias               |            6.33 |      574.00 |                   7.52 |
| ncep_nbm_conus                                                                | 1913 |  8.79 |   5.60 |   0.91 | bias               |            6.51 |      574.00 |                   6.67 |
| icon_seamless                                                                 | 1913 |  7.85 |   2.04 |   0.89 | bias               |            6.53 |      574.00 |                   8.07 |
| best_match                                                                    | 1913 |  7.57 |   0.73 |   0.87 | bias               |            6.71 |      574.00 |                   7.17 |
| gfs_hrrr                                                                      | 1913 |  7.57 |   0.73 |   0.87 | bias               |            6.71 |      574.00 |                   7.17 |
| gfs_seamless                                                                  | 1913 |  7.57 |   0.73 |   0.87 | bias               |            6.71 |      574.00 |                   7.17 |
| gem_seamless                                                                  | 1913 |  7.77 |   0.60 |   0.90 | bias               |            6.94 |      574.00 |                   7.33 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1913 |  8.82 |   5.35 |   0.90 | bias               |            6.98 |      574.00 |                   7.89 |
| meteofrance_seamless                                                          | 1913 |  9.16 |  -4.50 |   0.88 | ridge              |            8.05 |      574.00 |                  10.70 |
| ukmo_seamless                                                                 | 1913 | 10.06 |   5.11 |   0.82 | bias               |            9.20 |      574.00 |                  10.42 |
| jma_seamless                                                                  | 1913 | 11.14 |   6.93 |   0.74 | ridge              |           10.91 |      574.00 |                  13.99 |

### precip_in

| candidate                                                                     |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                    | 2327 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                  | 2327 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                      | 2327 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 2327 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 2327 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 2327 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                 | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus       | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                          | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 2327 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                               | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                 | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                             | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                            | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                  | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                  | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                | 2327 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                 | 2327 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                  | 2327 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                          | 2327 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 9498 |  1.48 |  -0.62 |   0.94 | bias               |            1.04 |     2850.00 |                   0.50 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 9498 |  1.59 |  -0.75 |   0.94 | bias               |            1.05 |     2850.00 |                   0.53 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 9498 |  1.65 |  -0.82 |   0.93 | bias               |            1.06 |     2850.00 |                   0.48 |
| ecmwf_ifs025                                                                  | 9498 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2850.00 |                   0.49 |
| knmi_seamless                                                                 | 9498 |  1.39 |  -0.49 |   0.93 | bias               |            1.06 |     2850.00 |                   0.49 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 9498 |  1.50 |  -0.64 |   0.93 | bias               |            1.06 |     2850.00 |                   0.58 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus       | 9498 |  1.50 |  -0.64 |   0.93 | bias               |            1.06 |     2850.00 |                   0.58 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 9498 |  1.32 |  -0.43 |   0.94 | bias               |            1.08 |     2850.00 |                   0.51 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                               | 9498 |  1.29 |  -0.38 |   0.94 | bias               |            1.09 |     2850.00 |                   0.53 |
| ecmwf_aifs025_single                                                          | 9498 |  1.41 |  -0.46 |   0.93 | bias               |            1.09 |     2850.00 |                   0.51 |
| meteofrance_seamless                                                          | 9498 |  1.31 |  -0.30 |   0.94 | bias               |            1.10 |     2850.00 |                   0.64 |
| icon_seamless                                                                 | 9498 |  1.30 |  -0.35 |   0.94 | bias               |            1.15 |     2850.00 |                   0.67 |
| blend:icon_seamless+ncep_nbm_conus                                            | 9498 |  1.30 |  -0.35 |   0.94 | bias               |            1.15 |     2850.00 |                   0.67 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 9498 |  1.25 |  -0.31 |   0.94 | bias               |            1.15 |     2850.00 |                   0.64 |
| jma_seamless                                                                  | 9498 |  1.50 |  -0.62 |   0.94 | bias               |            1.15 |     2850.00 |                   0.55 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 9498 |  1.95 |  -1.15 |   0.93 | bias               |            1.16 |     2850.00 |                   0.57 |
| ukmo_seamless                                                                 | 9498 |  1.95 |  -1.15 |   0.93 | bias               |            1.16 |     2850.00 |                   0.57 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 9498 |  1.74 |  -0.90 |   0.93 | bias               |            1.17 |     2850.00 |                   0.65 |
| gem_seamless                                                                  | 9498 |  1.24 |  -0.27 |   0.94 | bias               |            1.19 |     2850.00 |                   0.66 |
| blend:gem_seamless+ncep_nbm_conus                                             | 9498 |  1.24 |  -0.27 |   0.94 | bias               |            1.19 |     2850.00 |                   0.66 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 9498 |  1.64 |  -0.79 |   0.93 | raw                |            1.55 |     2850.00 |                   1.55 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 9498 |  1.83 |  -1.01 |   0.93 | raw                |            1.71 |     2850.00 |                   1.84 |
| best_match                                                                    | 9498 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2850.00 |                   2.52 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 9498 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2850.00 |                   2.52 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 9498 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2850.00 |                   2.52 |
| gfs_seamless                                                                  | 9498 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2850.00 |                   2.52 |
| gfs_hrrr                                                                      | 9498 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2850.00 |                   2.52 |

### temp_f

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ecmwf_ifs025                                                                  | 1913 |  3.18 |  -0.87 |   0.95 | bias               |            2.24 |      574.00 |                   2.66 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  3.49 |  -1.30 |   0.95 | bias               |            2.38 |      574.00 |                   3.10 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 1913 |  3.33 |  -1.06 |   0.95 | bias               |            2.40 |      574.00 |                   3.02 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  3.18 |  -0.70 |   0.95 | bias               |            2.41 |      574.00 |                   3.04 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  3.18 |  -0.70 |   0.95 | bias               |            2.41 |      574.00 |                   3.04 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  3.46 |  -1.21 |   0.95 | bias               |            2.43 |      574.00 |                   3.08 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1913 |  3.44 |  -1.29 |   0.95 | bias               |            2.43 |      574.00 |                   3.14 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  3.24 |  -0.84 |   0.95 | bias               |            2.44 |      574.00 |                   3.13 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 1913 |  3.49 |  -1.33 |   0.95 | bias               |            2.45 |      574.00 |                   3.12 |
| ecmwf_aifs025_single                                                          | 1913 |  3.57 |  -1.51 |   0.95 | bias               |            2.45 |      574.00 |                   2.81 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1913 |  3.40 |  -1.06 |   0.95 | bias               |            2.45 |      574.00 |                   3.18 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                               | 1913 |  3.22 |  -0.70 |   0.95 | bias               |            2.45 |      574.00 |                   2.98 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1913 |  3.47 |  -1.15 |   0.95 | bias               |            2.46 |      574.00 |                   3.17 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1913 |  3.77 |  -1.74 |   0.94 | bias               |            2.47 |      574.00 |                   3.16 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 1913 |  3.46 |  -1.30 |   0.95 | bias               |            2.49 |      574.00 |                   3.22 |
| knmi_seamless                                                                 | 1913 |  3.21 |  -0.15 |   0.95 | raw                |            2.50 |      574.00 |                   3.00 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  3.73 |  -1.66 |   0.94 | bias               |            2.50 |      574.00 |                   3.33 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1913 |  3.39 |  -0.97 |   0.95 | bias               |            2.50 |      574.00 |                   2.93 |
| gfs_seamless                                                                  | 1913 |  3.52 |  -1.23 |   0.94 | ridge              |            2.56 |      574.00 |                   3.11 |
| best_match                                                                    | 1913 |  3.52 |  -1.23 |   0.94 | ridge              |            2.56 |      574.00 |                   3.11 |
| gfs_hrrr                                                                      | 1913 |  3.52 |  -1.23 |   0.94 | ridge              |            2.56 |      574.00 |                   3.11 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1913 |  3.70 |  -1.46 |   0.95 | bias               |            2.56 |      574.00 |                   3.39 |
| gem_seamless                                                                  | 1913 |  3.39 |  -0.51 |   0.94 | ridge              |            2.59 |      574.00 |                   2.77 |
| ncep_nbm_conus                                                                | 1913 |  3.71 |  -1.43 |   0.94 | bias               |            2.60 |      574.00 |                   3.12 |
| meteofrance_seamless                                                          | 1913 |  3.61 |   1.90 |   0.93 | ridge              |            2.68 |      574.00 |                   3.24 |
| ukmo_seamless                                                                 | 1913 |  4.08 |  -2.05 |   0.91 | bias               |            2.88 |      574.00 |                   3.64 |
| icon_seamless                                                                 | 1913 |  3.88 |  -1.50 |   0.93 | ridge              |            3.05 |      574.00 |                   3.64 |
| jma_seamless                                                                  | 1913 |  4.66 |  -2.90 |   0.92 | ridge              |            3.44 |      574.00 |                   3.76 |

### wind_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  2.89 |   2.83 |   0.74 | ridge              |            0.74 |      574.00 |                   0.69 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  2.89 |   2.83 |   0.74 | ridge              |            0.74 |      574.00 |                   0.69 |
| knmi_seamless                                                                 | 1913 |  3.11 |   3.03 |   0.74 | ridge              |            0.75 |      574.00 |                   0.68 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1913 |  3.08 |   3.03 |   0.74 | ridge              |            0.75 |      574.00 |                   0.68 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1913 |  2.79 |   2.73 |   0.73 | ridge              |            0.75 |      574.00 |                   0.72 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                               | 1913 |  2.71 |   2.62 |   0.72 | ridge              |            0.75 |      574.00 |                   0.71 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1913 |  2.58 |   2.51 |   0.72 | ridge              |            0.75 |      574.00 |                   0.72 |
| ecmwf_ifs025                                                                  | 1913 |  3.46 |   3.40 |   0.74 | ridge              |            0.76 |      574.00 |                   0.63 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  2.76 |   2.68 |   0.71 | ridge              |            0.76 |      574.00 |                   0.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1913 |  2.55 |   2.48 |   0.70 | ridge              |            0.77 |      574.00 |                   0.73 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 1913 |  2.78 |   2.71 |   0.70 | ridge              |            0.78 |      574.00 |                   0.69 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1913 |  2.65 |   2.57 |   0.69 | ridge              |            0.78 |      574.00 |                   0.76 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 1913 |  2.99 |   2.92 |   0.69 | ridge              |            0.78 |      574.00 |                   0.70 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1913 |  2.84 |   2.77 |   0.70 | ridge              |            0.78 |      574.00 |                   0.69 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1913 |  2.54 |   2.42 |   0.67 | ridge              |            0.79 |      574.00 |                   0.72 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 1913 |  2.60 |   2.53 |   0.69 | ridge              |            0.79 |      574.00 |                   0.75 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 1913 |  3.10 |   3.04 |   0.69 | ridge              |            0.79 |      574.00 |                   0.68 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1913 |  2.61 |   2.50 |   0.67 | ridge              |            0.80 |      574.00 |                   0.76 |
| ncep_nbm_conus                                                                | 1913 |  2.73 |   2.57 |   0.64 | ridge              |            0.81 |      574.00 |                   0.77 |
| icon_seamless                                                                 | 1913 |  2.66 |   2.58 |   0.70 | ridge              |            0.81 |      574.00 |                   0.75 |
| gem_seamless                                                                  | 1913 |  2.42 |   2.28 |   0.66 | ridge              |            0.82 |      574.00 |                   0.69 |
| jma_seamless                                                                  | 1913 |  2.24 |   2.12 |   0.63 | ridge              |            0.83 |      574.00 |                   0.77 |
| ecmwf_aifs025_single                                                          | 1913 |  3.08 |   2.96 |   0.69 | ridge              |            0.83 |      574.00 |                   0.72 |
| best_match                                                                    | 1913 |  3.36 |   3.28 |   0.66 | ridge              |            0.84 |      574.00 |                   0.67 |
| gfs_hrrr                                                                      | 1913 |  3.36 |   3.28 |   0.66 | ridge              |            0.84 |      574.00 |                   0.67 |
| gfs_seamless                                                                  | 1913 |  3.36 |   3.28 |   0.66 | ridge              |            0.84 |      574.00 |                   0.67 |
| meteofrance_seamless                                                          | 1913 |  1.60 |   1.28 |   0.55 | ridge              |            0.85 |      574.00 |                   0.72 |
| ukmo_seamless                                                                 | 1913 |  2.62 |   2.44 |   0.63 | ridge              |            0.87 |      574.00 |                   0.75 |

## Regional skill — KHIE, Whitefield NH, every season

Ranks models with 13k hours and two winters; the site record above decides. KHIE is 16 km east and is not this hollow: over the hours both stations recorded, temperature correlates 0.88 and dew point 0.92, but wind only 0.57.

### dewpoint_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13397 |  1.97 |   0.81 |   2.64 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13397 |  2.00 |   0.48 |   2.64 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13397 |  2.01 |   0.62 |   2.71 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13397 |  2.04 |   0.92 |   2.69 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13397 |  2.06 |   0.28 |   2.77 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13397 |  2.09 |   1.01 |   2.75 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13397 |  2.10 |   0.55 |   2.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13397 |  2.10 |   0.93 |   2.89 |
| ncep_nbm_conus                                                                | 13260 |  2.15 |   0.23 |   2.81 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13397 |  2.16 |   1.21 |   2.95 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13397 |  2.25 |   0.66 |   2.94 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13397 |  2.27 |   1.24 |   3.13 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13397 |  2.35 |   1.56 |   3.21 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13397 |  2.40 |   1.68 |   3.07 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13397 |  2.47 |   1.74 |   3.38 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13397 |  2.53 |   1.50 |   3.39 |
| gem_seamless                                                                  | 13397 |  2.53 |   0.33 |   3.44 |
| knmi_seamless                                                                 | 13397 |  2.53 |   1.31 |   3.39 |
| metno_seamless                                                                | 13397 |  2.53 |   1.31 |   3.39 |
| best_match                                                                    | 13397 |  2.77 |   0.87 |   3.59 |
| gfs_hrrr                                                                      | 13397 |  2.77 |   0.87 |   3.59 |
| gfs_seamless                                                                  | 13397 |  2.77 |   0.87 |   3.59 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13397 |  2.81 |   2.21 |   3.65 |
| icon_seamless                                                                 | 13397 |  3.07 |   2.22 |   4.18 |
| jma_seamless                                                                  | 13397 |  3.27 |   1.93 |   4.33 |
| ecmwf_ifs025                                                                  | 13397 |  3.29 |   2.72 |   4.21 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13397 |  3.56 |   3.15 |   4.51 |
| ukmo_seamless                                                                 | 13397 |  3.69 |   2.72 |   4.86 |
| ecmwf_aifs025_single                                                          | 13397 |  3.95 |   3.58 |   4.95 |
| meteofrance_seamless                                                          | 13397 |  7.29 |   7.09 |   8.37 |

### gust_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| gem_seamless                                                                  | 13288 |  4.59 |   3.01 |   6.56 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13288 |  4.76 |   3.42 |   6.21 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13288 |  5.22 |   4.22 |   6.59 |
| ncep_nbm_conus                                                                | 13154 |  5.30 |   3.84 |   6.71 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13288 |  5.77 |   4.83 |   7.10 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13288 |  5.82 |   4.83 |   7.27 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13288 |  5.83 |   5.04 |   7.17 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13288 |  5.98 |   5.11 |   7.30 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13288 |  6.06 |   5.16 |   7.64 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13288 |  6.25 |   5.27 |   7.55 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13288 |  6.49 |   5.75 |   7.77 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13288 |  6.56 |   5.93 |   7.86 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13288 |  6.60 |   5.75 |   7.92 |
| best_match                                                                    | 13288 |  6.62 |   5.83 |   8.57 |
| gfs_seamless                                                                  | 13288 |  6.62 |   5.83 |   8.57 |
| gfs_hrrr                                                                      | 13288 |  6.62 |   5.83 |   8.57 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13288 |  6.84 |   6.06 |   8.09 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13288 |  7.04 |   6.49 |   8.40 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13288 |  7.46 |   7.08 |   8.94 |
| ukmo_seamless                                                                 | 13288 |  7.48 |   6.68 |   8.90 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13288 |  7.63 |   7.03 |   8.87 |
| icon_seamless                                                                 | 13288 |  8.23 |   7.64 |   9.73 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13288 |  8.67 |   8.32 |  10.11 |
| metno_seamless                                                                | 13288 |  8.92 |   8.48 |  10.34 |
| knmi_seamless                                                                 | 13288 |  8.92 |   8.48 |  10.34 |
| meteofrance_seamless                                                          | 13288 | 10.08 |   9.62 |  12.01 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13288 | 13.72 |  13.64 |  15.42 |
| ecmwf_ifs025                                                                  | 13288 | 13.72 |  13.64 |  15.42 |

### humidity_pct

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13397 |  6.98 |  -0.04 |   9.01 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13397 |  7.04 |   1.54 |   9.19 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13397 |  7.24 |  -0.76 |   9.42 |
| ncep_nbm_conus                                                                | 13260 |  7.49 |  -1.12 |   9.88 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13397 |  7.49 |  -1.53 |   9.74 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13397 |  7.54 |  -2.14 |   9.92 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13397 |  8.14 |  -2.97 |  10.75 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13397 |  8.17 |  -2.53 |  10.74 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13397 |  8.35 |  -2.65 |  10.89 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13397 |  8.55 |  -2.50 |  11.01 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13397 |  8.56 |  -2.89 |  11.27 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13397 |  8.59 |  -1.86 |  10.88 |
| ukmo_seamless                                                                 | 13397 |  8.69 |   4.10 |  11.60 |
| icon_seamless                                                                 | 13397 |  8.73 |  -3.15 |  11.68 |
| metno_seamless                                                                | 13397 |  8.77 |  -1.84 |  11.57 |
| knmi_seamless                                                                 | 13397 |  8.77 |  -1.84 |  11.57 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13397 |  8.80 |  -2.49 |  11.20 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13397 |  9.00 |  -3.20 |  11.63 |
| jma_seamless                                                                  | 13397 |  9.10 |   3.05 |  11.90 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13397 |  9.56 |  -1.73 |  12.51 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13397 |  9.63 |  -2.94 |  12.24 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13397 |  9.67 |  -2.58 |  12.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13397 |  9.75 |  -0.30 |  12.52 |
| ecmwf_aifs025_single                                                          | 13397 |  9.78 |  -1.18 |  12.64 |
| ecmwf_ifs025                                                                  | 13397 | 10.19 |   0.57 |  13.01 |
| gem_seamless                                                                  | 13397 | 10.90 |  -4.59 |  14.89 |
| gfs_hrrr                                                                      | 13397 | 11.74 |  -3.84 |  14.91 |
| gfs_seamless                                                                  | 13397 | 11.74 |  -3.84 |  14.91 |
| best_match                                                                    | 13397 | 11.74 |  -3.84 |  14.91 |
| meteofrance_seamless                                                          | 13397 | 11.91 |   2.58 |  14.84 |

### temp_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13397 |  3.06 |   1.13 |   4.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13397 |  3.07 |   1.54 |   4.13 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13397 |  3.11 |   1.36 |   4.13 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13397 |  3.11 |   1.55 |   4.25 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13397 |  3.13 |   1.39 |   4.23 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13397 |  3.18 |   1.40 |   4.27 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13397 |  3.18 |   1.38 |   4.30 |
| ncep_nbm_conus                                                                | 13260 |  3.19 |   0.42 |   4.02 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13397 |  3.19 |   1.58 |   4.33 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13397 |  3.26 |   1.18 |   4.36 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13397 |  3.29 |   1.65 |   4.42 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13397 |  3.32 |   0.70 |   4.25 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13397 |  3.32 |   1.86 |   4.56 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13397 |  3.33 |   1.84 |   4.45 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13397 |  3.37 |   1.55 |   4.45 |
| gfs_hrrr                                                                      | 13397 |  3.39 |   1.83 |   4.51 |
| gfs_seamless                                                                  | 13397 |  3.39 |   1.83 |   4.51 |
| best_match                                                                    | 13397 |  3.39 |   1.83 |   4.51 |
| metno_seamless                                                                | 13397 |  3.39 |   1.80 |   4.65 |
| knmi_seamless                                                                 | 13397 |  3.39 |   1.80 |   4.65 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13397 |  3.51 |   2.33 |   4.93 |
| jma_seamless                                                                  | 13397 |  3.59 |   0.53 |   4.75 |
| gem_seamless                                                                  | 13397 |  3.74 |   1.91 |   5.37 |
| ukmo_seamless                                                                 | 13397 |  3.79 |   0.98 |   4.95 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13397 |  3.91 |   2.67 |   5.63 |
| ecmwf_ifs025                                                                  | 13397 |  4.06 |   2.30 |   5.68 |
| icon_seamless                                                                 | 13397 |  4.14 |   3.23 |   5.72 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13397 |  4.29 |   3.04 |   6.07 |
| ecmwf_aifs025_single                                                          | 13397 |  4.75 |   3.78 |   6.63 |
| meteofrance_seamless                                                          | 13397 |  6.35 |   5.98 |   8.23 |

### wind_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| ncep_nbm_conus                                                                | 13154 |  2.13 |   0.08 |   3.18 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13288 |  2.29 |   0.15 |   3.02 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13288 |  2.32 |   0.50 |   2.99 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13288 |  2.35 |   0.66 |   2.98 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13288 |  2.36 |   0.41 |   2.99 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13288 |  2.38 |   0.51 |   2.96 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13288 |  2.39 |   0.59 |   3.03 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13288 |  2.42 |   0.48 |   3.10 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13288 |  2.44 |   0.59 |   3.03 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13288 |  2.45 |   0.63 |   3.05 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13288 |  2.47 |   0.85 |   3.06 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13288 |  2.48 |   0.90 |   3.04 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13288 |  2.50 |   0.73 |   3.03 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13288 |  2.53 |   1.10 |   3.08 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13288 |  2.53 |   0.96 |   3.11 |
| icon_seamless                                                                 | 13288 |  2.61 |   0.92 |   3.19 |
| gem_seamless                                                                  | 13288 |  2.63 |   0.23 |   3.32 |
| jma_seamless                                                                  | 13288 |  2.68 |   0.27 |   3.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13288 |  2.70 |   1.38 |   3.23 |
| metno_seamless                                                                | 13288 |  2.78 |   1.47 |   3.44 |
| knmi_seamless                                                                 | 13288 |  2.78 |   1.47 |   3.44 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13288 |  2.79 |   1.48 |   3.41 |
| gfs_hrrr                                                                      | 13288 |  2.79 |   1.24 |   3.42 |
| best_match                                                                    | 13288 |  2.79 |   1.24 |   3.42 |
| gfs_seamless                                                                  | 13288 |  2.79 |   1.24 |   3.42 |
| ukmo_seamless                                                                 | 13288 |  2.85 |   0.88 |   3.48 |
| ecmwf_aifs025_single                                                          | 13288 |  2.94 |   1.62 |   3.65 |
| meteofrance_seamless                                                          | 13288 |  3.09 |  -0.66 |   3.94 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13288 |  3.10 |   2.10 |   3.83 |
| ecmwf_ifs025                                                                  | 13288 |  3.36 |   2.59 |   4.17 |

## Regional MAE by season (temperature)

| candidate                                                                     |   fall |   spring |   summer |   winter |
|:------------------------------------------------------------------------------|-------:|---------:|---------:|---------:|
| best_match                                                                    |   3.53 |     3.05 |     3.51 |     3.54 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       |   4.58 |     3.67 |     4.34 |     4.74 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          |   4.21 |     3.34 |     3.95 |     4.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    |   3.77 |     3.02 |     3.61 |     3.75 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         |   3.40 |     2.85 |     3.28 |     3.16 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   |   3.36 |     2.72 |     3.21 |     3.18 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                |   3.34 |     2.87 |     3.16 |     3.17 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   |   3.34 |     3.02 |     3.11 |     3.38 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               |   3.50 |     3.04 |     3.25 |     3.68 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              |   3.46 |     2.85 |     3.19 |     3.26 |
| blend:gem_seamless+ncep_nbm_conus                                             |   3.55 |     3.04 |     3.17 |     3.32 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       |   3.28 |     2.70 |     3.23 |     3.06 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    |   3.24 |     2.88 |     3.22 |     3.10 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 |   3.21 |     2.87 |     3.14 |     2.98 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless |   3.51 |     2.93 |     3.36 |     3.44 |
| blend:icon_seamless+ncep_nbm_conus                                            |   3.42 |     3.17 |     3.21 |     3.71 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              |   3.55 |     3.15 |     3.33 |     3.52 |
| blend:ncep_nbm_conus+ukmo_seamless                                            |   3.63 |     3.13 |     3.33 |     3.11 |
| ecmwf_aifs025_single                                                          |   4.98 |     4.07 |     4.94 |     5.14 |
| ecmwf_ifs025                                                                  |   4.42 |     3.54 |     3.96 |     4.56 |
| gem_seamless                                                                  |   3.96 |     3.44 |     3.64 |     4.06 |
| gfs_hrrr                                                                      |   3.53 |     3.05 |     3.51 |     3.54 |
| gfs_seamless                                                                  |   3.53 |     3.05 |     3.51 |     3.54 |
| icon_seamless                                                                 |   4.13 |     3.90 |     3.85 |     5.16 |
| jma_seamless                                                                  |   3.34 |     3.92 |     3.28 |     4.02 |
| knmi_seamless                                                                 |   3.64 |     2.88 |     3.55 |     3.57 |
| meteofrance_seamless                                                          |   6.88 |     5.21 |     6.08 |     7.95 |
| metno_seamless                                                                |   3.64 |     2.88 |     3.55 |     3.57 |
| ncep_nbm_conus                                                                |   3.46 |     3.12 |     3.09 |     3.07 |
| ukmo_seamless                                                                 |   4.17 |     3.46 |     3.92 |     3.49 |

## MAE by lead time, days 1-7 (previous-runs, site)

### gust_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 7.02 |   3.60 |   3.83 |   4.14 |   4.39 |   4.90 |   4.57 |
| gem_seamless         | 4.14 |   3.92 |   4.21 |   3.98 |   4.40 |   4.69 |   5.44 |
| gfs_hrrr             | 7.02 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 7.02 |   3.60 |   3.83 |   4.14 |   4.39 |   4.90 |   4.57 |
| icon_seamless        | 5.53 |   5.59 |   5.67 |   6.21 |   6.30 |   6.60 | nan    |
| meteofrance_seamless | 5.86 |   5.78 |   5.95 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.60 |   3.74 |   3.96 |   4.13 |   4.04 |   4.14 |   4.04 |
| ukmo_seamless        | 4.59 |   4.93 |   4.63 |   5.01 |   5.07 |   5.41 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 12.40 |  10.15 |  11.17 |  11.58 |  12.14 |  13.03 |  13.55 |
| ecmwf_aifs025_single |  6.84 |   7.38 |   7.96 |   8.03 |   9.01 |   8.91 |  10.15 |
| ecmwf_ifs025         |  8.11 |   8.69 |   9.36 |   9.74 |  10.52 |  10.80 |  11.51 |
| gem_seamless         |  9.43 |  10.64 |  10.09 |  10.59 |  11.44 |  12.22 |  12.99 |
| gfs_hrrr             | 12.40 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 12.40 |  10.15 |  11.17 |  11.58 |  12.14 |  13.03 |  13.55 |
| icon_seamless        |  8.90 |   9.09 |   9.46 |   9.69 |  11.19 |  11.60 | nan    |
| jma_seamless         | 11.68 |  11.46 |  12.42 |  12.79 |  12.87 |  14.22 |  15.00 |
| knmi_seamless        |  8.77 |   9.20 |   9.61 |   9.90 |  10.63 |  11.00 |  11.91 |
| meteofrance_seamless | 10.24 |  10.87 |  10.94 | nan    | nan    | nan    | nan    |
| metno_seamless       |  8.77 |   9.20 |   9.61 |   9.90 |  10.63 |  11.00 |  11.91 |
| ncep_nbm_conus       |  9.60 |   9.81 |  10.06 |  10.40 |  10.96 |  11.52 |  11.85 |
| ukmo_seamless        | 10.87 |  11.63 |  12.60 |  12.12 |  13.07 |  13.46 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 3.75 |   4.66 |   4.80 |   5.04 |   5.53 |   5.97 |   5.91 |
| ecmwf_aifs025_single | 3.44 |   3.58 |   3.80 |   3.87 |   4.14 |   4.43 |   4.55 |
| ecmwf_ifs025         | 3.43 |   3.63 |   3.85 |   4.36 |   4.41 |   4.76 |   4.99 |
| gem_seamless         | 3.82 |   4.86 |   4.39 |   4.76 |   5.11 |   5.36 |   5.69 |
| gfs_hrrr             | 3.75 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 3.75 |   4.66 |   4.80 |   5.04 |   5.53 |   5.97 |   5.91 |
| icon_seamless        | 4.19 |   4.41 |   4.49 |   4.60 |   4.91 |   5.40 | nan    |
| jma_seamless         | 4.79 |   4.97 |   5.02 |   5.30 |   5.55 |   6.13 |   6.06 |
| knmi_seamless        | 3.59 |   3.75 |   3.98 |   4.43 |   4.39 |   4.76 |   5.07 |
| meteofrance_seamless | 4.29 |   4.34 |   4.68 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.59 |   3.75 |   3.98 |   4.43 |   4.39 |   4.76 |   5.07 |
| ncep_nbm_conus       | 4.03 |   4.26 |   4.28 |   4.37 |   4.62 |   4.65 |   4.66 |
| ukmo_seamless        | 4.04 |   4.28 |   4.47 |   4.37 |   4.55 |   4.83 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.52 |   2.61 |   2.51 |   2.70 |   2.68 |   2.64 |   2.41 |
| ecmwf_aifs025_single | 3.20 |   3.19 |   3.23 |   3.32 |   3.39 |   3.48 |   3.36 |
| ecmwf_ifs025         | 3.44 |   3.53 |   3.40 |   3.63 |   3.79 |   3.51 |   3.29 |
| gem_seamless         | 2.58 |   2.12 |   1.96 |   1.90 |   1.95 |   1.92 |   2.12 |
| gfs_hrrr             | 4.52 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.52 |   2.61 |   2.51 |   2.70 |   2.68 |   2.64 |   2.41 |
| icon_seamless        | 2.68 |   2.72 |   2.74 |   2.86 |   2.86 |   2.98 | nan    |
| jma_seamless         | 2.14 |   2.25 |   2.29 |   2.34 |   2.49 |   2.33 |   2.12 |
| knmi_seamless        | 3.08 |   3.21 |   3.11 |   3.36 |   3.57 |   3.31 |   3.13 |
| meteofrance_seamless | 1.62 |   1.62 |   1.67 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.08 |   3.21 |   3.11 |   3.36 |   3.57 |   3.31 |   3.13 |
| ncep_nbm_conus       | 2.68 |   2.69 |   2.74 |   2.80 |   2.58 |   2.52 |   2.34 |
| ukmo_seamless        | 2.83 |   2.96 |   2.73 |   2.92 |   2.89 |   3.02 | nan    |
