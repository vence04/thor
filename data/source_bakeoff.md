# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-10-18.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Source in use, per variable

| variable | source |
|---|---|
| dewpoint_f | ncep_nbm_conus |
| gust_mph | blend of gem_seamless, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| humidity_pct | blend of gfs_hrrr, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| precip_in | best_match |
| pressure_abs_hpa | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |
| temp_f | blend of knmi_seamless, ncep_nbm_conus, ukmo_seamless |
| wind_mph | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |

## Site skill, shortlisted candidates (lower MAE = better)

### dewpoint_f

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ncep_nbm_conus                                                                | 1798 |  2.33 |   0.63 |   0.98 | bias               |            1.48 |      540.00 |                   1.53 |
| icon_seamless                                                                 | 1798 |  2.51 |  -0.78 |   0.98 | bias               |            1.51 |      540.00 |                   1.45 |
| ecmwf_ifs025                                                                  | 1798 |  2.66 |  -0.65 |   0.98 | bias               |            1.69 |      540.00 |                   1.69 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1798 |  2.12 |  -0.25 |   0.98 | ridge              |            1.83 |      540.00 |                   2.17 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  2.19 |  -0.28 |   0.98 | ridge              |            1.92 |      540.00 |                   2.39 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1798 |  2.59 |   0.19 |   0.97 | ridge              |            1.93 |      540.00 |                   2.23 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1798 |  2.05 |  -0.16 |   0.98 | ridge              |            1.94 |      540.00 |                   2.41 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1798 |  2.16 |  -0.24 |   0.99 | ridge              |            1.94 |      540.00 |                   2.45 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1798 |  2.34 |  -0.15 |   0.98 | ridge              |            1.96 |      540.00 |                   2.42 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1798 |  2.20 |  -0.08 |   0.98 | ridge              |            1.96 |      540.00 |                   2.43 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1798 |  2.46 |   0.07 |   0.98 | ridge              |            1.96 |      540.00 |                   2.37 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1798 |  2.20 |   0.03 |   0.98 | ridge              |            2.04 |      540.00 |                   2.58 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  2.12 |  -0.16 |   0.99 | ridge              |            2.05 |      540.00 |                   2.58 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1798 |  2.14 |  -0.16 |   0.99 | ridge              |            2.11 |      540.00 |                   2.59 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1798 |  2.30 |   0.23 |   0.98 | ridge              |            2.19 |      540.00 |                   2.77 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1798 |  2.30 |   0.23 |   0.98 | ridge              |            2.19 |      540.00 |                   2.77 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1798 |  2.38 |   0.09 |   0.98 | ridge              |            2.31 |      540.00 |                   2.92 |
| ecmwf_aifs025_single                                                          | 1798 |  2.50 |  -0.54 |   0.98 | ridge              |            2.45 |      540.00 |                   3.00 |
| gem_seamless                                                                  | 1798 |  2.64 |  -0.57 |   0.97 | ridge              |            2.59 |      540.00 |                   3.31 |
| ukmo_seamless                                                                 | 1798 |  3.36 |  -0.24 |   0.94 | ridge              |            2.63 |      540.00 |                   3.05 |
| knmi_seamless                                                                 | 1798 |  2.64 |  -0.17 |   0.98 | ridge              |            2.64 |      540.00 |                   3.33 |
| metno_seamless                                                                | 1798 |  2.64 |  -0.17 |   0.98 | ridge              |            2.64 |      540.00 |                   3.33 |
| best_match                                                                    | 1798 |  2.89 |  -0.53 |   0.97 | ridge              |            2.71 |      540.00 |                   3.17 |
| gfs_seamless                                                                  | 1798 |  2.89 |  -0.53 |   0.97 | ridge              |            2.71 |      540.00 |                   3.17 |
| gfs_hrrr                                                                      | 1798 |  2.89 |  -0.53 |   0.97 | ridge              |            2.71 |      540.00 |                   3.17 |
| jma_seamless                                                                  | 1798 |  2.89 |  -0.51 |   0.94 | ridge              |            2.83 |      540.00 |                   3.35 |
| meteofrance_seamless                                                          | 1798 |  3.07 |  -0.20 |   0.96 | ridge              |            3.66 |      540.00 |                   4.16 |

### gust_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  4.50 |   4.03 |   0.86 | ridge              |            2.01 |      540.00 |                   2.13 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  4.36 |   3.86 |   0.86 | ridge              |            2.04 |      540.00 |                   2.13 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1798 |  4.86 |   4.54 |   0.84 | ridge              |            2.07 |      540.00 |                   2.21 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1798 |  4.32 |   3.86 |   0.85 | ridge              |            2.08 |      540.00 |                   2.22 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1798 |  4.67 |   4.26 |   0.85 | ridge              |            2.10 |      540.00 |                   2.23 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1798 |  4.67 |   4.26 |   0.85 | ridge              |            2.10 |      540.00 |                   2.23 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1798 |  5.14 |   4.84 |   0.84 | ridge              |            2.11 |      540.00 |                   2.26 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1798 |  4.90 |   4.44 |   0.83 | ridge              |            2.15 |      540.00 |                   2.24 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1798 |  4.37 |   3.83 |   0.84 | ridge              |            2.17 |      540.00 |                   2.22 |
| metno_seamless                                                                | 1798 |  6.19 |   6.00 |   0.82 | ridge              |            2.21 |      540.00 |                   2.37 |
| knmi_seamless                                                                 | 1798 |  6.19 |   6.00 |   0.82 | ridge              |            2.21 |      540.00 |                   2.37 |
| ecmwf_ifs025                                                                  | 1798 |  7.41 |   7.30 |   0.81 | ridge              |            2.36 |      540.00 |                   2.44 |
| icon_seamless                                                                 | 1798 |  5.57 |   5.15 |   0.81 | ridge              |            2.41 |      540.00 |                   2.40 |
| ukmo_seamless                                                                 | 1798 |  4.07 |   3.05 |   0.79 | ridge              |            2.46 |      540.00 |                   2.65 |
| best_match                                                                    | 1798 |  4.99 |   3.85 |   0.73 | ridge              |            2.55 |      540.00 |                   2.58 |
| gfs_seamless                                                                  | 1798 |  4.99 |   3.85 |   0.73 | ridge              |            2.55 |      540.00 |                   2.58 |
| gfs_hrrr                                                                      | 1798 |  4.99 |   3.85 |   0.73 | ridge              |            2.55 |      540.00 |                   2.58 |
| ncep_nbm_conus                                                                | 1798 |  3.63 |   2.51 |   0.83 | bias               |            2.71 |      540.00 |                   2.85 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1798 |  3.66 |   2.78 |   0.84 | bias               |            2.72 |      540.00 |                   2.86 |
| meteofrance_seamless                                                          | 1798 |  5.81 |   5.48 |   0.71 | ridge              |            2.72 |      540.00 |                   2.98 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1798 |  3.39 |   2.15 |   0.85 | bias               |            2.74 |      540.00 |                   2.90 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1798 |  3.92 |   3.15 |   0.85 | bias               |            2.99 |      540.00 |                   3.14 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1798 |  3.77 |   2.71 |   0.84 | bias               |            3.14 |      540.00 |                   3.16 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1798 |  3.94 |   3.01 |   0.83 | bias               |            3.27 |      540.00 |                   3.22 |
| gem_seamless                                                                  | 1798 |  3.87 |   1.78 |   0.80 | bias               |            3.87 |      540.00 |                   4.20 |

### humidity_pct

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  5.85 |   1.09 |   0.95 | bias               |            4.56 |      540.00 |                   4.61 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1798 |  5.76 |   1.16 |   0.95 | bias               |            4.57 |      540.00 |                   4.51 |
| ecmwf_aifs025_single                                                          | 1798 |  6.74 |   2.11 |   0.93 | bias               |            4.84 |      540.00 |                   5.19 |
| ecmwf_ifs025                                                                  | 1798 |  6.81 |   0.57 |   0.93 | bias               |            4.85 |      540.00 |                   5.11 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1798 |  6.06 |   1.82 |   0.95 | bias               |            4.93 |      540.00 |                   4.94 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1798 |  6.75 |   2.13 |   0.94 | bias               |            4.99 |      540.00 |                   4.84 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  6.71 |   2.45 |   0.94 | bias               |            5.19 |      540.00 |                   4.93 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1798 |  6.86 |   1.68 |   0.92 | bias               |            5.24 |      540.00 |                   5.26 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1798 |  6.13 |   2.07 |   0.95 | bias               |            5.27 |      540.00 |                   5.22 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1798 |  7.01 |   2.51 |   0.92 | bias               |            5.28 |      540.00 |                   5.28 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1798 |  7.01 |   2.51 |   0.92 | bias               |            5.28 |      540.00 |                   5.28 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1798 |  6.84 |   2.17 |   0.93 | bias               |            5.29 |      540.00 |                   5.20 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1798 |  7.27 |   3.18 |   0.94 | bias               |            5.34 |      540.00 |                   4.89 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1798 |  7.08 |   2.53 |   0.92 | bias               |            5.50 |      540.00 |                   5.68 |
| knmi_seamless                                                                 | 1798 |  7.16 |   0.01 |   0.91 | bias               |            5.54 |      540.00 |                   5.62 |
| metno_seamless                                                                | 1798 |  7.16 |   0.01 |   0.91 | bias               |            5.54 |      540.00 |                   5.62 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1798 |  7.44 |   3.17 |   0.92 | bias               |            6.02 |      540.00 |                   6.05 |
| meteofrance_seamless                                                          | 1798 |  9.03 |  -5.15 |   0.91 | ridge              |            6.11 |      540.00 |                   6.65 |
| ncep_nbm_conus                                                                | 1798 |  8.41 |   5.02 |   0.91 | bias               |            6.19 |      540.00 |                   6.06 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1798 |  8.44 |   4.76 |   0.90 | bias               |            7.04 |      540.00 |                   7.11 |
| best_match                                                                    | 1798 |  7.41 |   0.39 |   0.90 | ridge              |            7.27 |      540.00 |                   7.18 |
| gfs_hrrr                                                                      | 1798 |  7.41 |   0.39 |   0.90 | ridge              |            7.27 |      540.00 |                   7.18 |
| gfs_seamless                                                                  | 1798 |  7.41 |   0.39 |   0.90 | ridge              |            7.27 |      540.00 |                   7.18 |
| icon_seamless                                                                 | 1798 |  7.50 |   1.35 |   0.92 | ridge              |            7.36 |      540.00 |                   7.03 |
| gem_seamless                                                                  | 1798 |  7.60 |   0.03 |   0.91 | ridge              |            7.55 |      540.00 |                   7.66 |
| jma_seamless                                                                  | 1798 | 10.29 |   5.86 |   0.84 | ridge              |            9.46 |      540.00 |                   9.34 |
| ukmo_seamless                                                                 | 1798 |  9.75 |   4.49 |   0.84 | bias               |            9.57 |      540.00 |                  10.35 |

### precip_in

| candidate                                                                     |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                    | 2212 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                  | 2212 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                      | 2212 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                 | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                          | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                 | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                             | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                            | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                  | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus                                            | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:metno_seamless+ncep_nbm_conus                                           | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                  | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                | 2212 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                 | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                  | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                          | 2212 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 9383 |  1.48 |  -0.61 |   0.93 | bias               |            1.04 |     2815.00 |                   0.40 |
| ecmwf_ifs025                                                                  | 9383 |  1.39 |  -0.48 |   0.93 | bias               |            1.05 |     2815.00 |                   0.39 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 9383 |  1.65 |  -0.81 |   0.93 | bias               |            1.06 |     2815.00 |                   0.41 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 9383 |  1.50 |  -0.63 |   0.93 | bias               |            1.06 |     2815.00 |                   0.44 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 9383 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2815.00 |                   0.40 |
| blend:metno_seamless+ncep_nbm_conus                                           | 9383 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2815.00 |                   0.40 |
| knmi_seamless                                                                 | 9383 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2815.00 |                   0.40 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 9383 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2815.00 |                   0.40 |
| metno_seamless                                                                | 9383 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2815.00 |                   0.40 |
| ecmwf_aifs025_single                                                          | 9383 |  1.41 |  -0.46 |   0.93 | bias               |            1.08 |     2815.00 |                   0.45 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 9383 |  1.32 |  -0.43 |   0.93 | bias               |            1.08 |     2815.00 |                   0.48 |
| meteofrance_seamless                                                          | 9383 |  1.31 |  -0.29 |   0.93 | bias               |            1.09 |     2815.00 |                   0.50 |
| blend:icon_seamless+ncep_nbm_conus                                            | 9383 |  1.31 |  -0.34 |   0.93 | bias               |            1.15 |     2815.00 |                   0.60 |
| icon_seamless                                                                 | 9383 |  1.31 |  -0.34 |   0.93 | bias               |            1.15 |     2815.00 |                   0.60 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 9383 |  1.26 |  -0.30 |   0.93 | bias               |            1.15 |     2815.00 |                   0.55 |
| jma_seamless                                                                  | 9383 |  1.51 |  -0.62 |   0.93 | bias               |            1.17 |     2815.00 |                   0.61 |
| gem_seamless                                                                  | 9383 |  1.24 |  -0.26 |   0.93 | bias               |            1.19 |     2815.00 |                   0.55 |
| blend:gem_seamless+ncep_nbm_conus                                             | 9383 |  1.24 |  -0.26 |   0.93 | bias               |            1.19 |     2815.00 |                   0.55 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 9383 |  1.64 |  -0.78 |   0.93 | raw                |            1.51 |     2815.00 |                   1.19 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 9383 |  1.74 |  -0.89 |   0.93 | raw                |            1.57 |     2815.00 |                   1.32 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 9383 |  1.83 |  -1.00 |   0.93 | raw                |            1.67 |     2815.00 |                   1.45 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 9383 |  1.95 |  -1.14 |   0.93 | raw                |            1.82 |     2815.00 |                   1.49 |
| ukmo_seamless                                                                 | 9383 |  1.95 |  -1.14 |   0.93 | raw                |            1.82 |     2815.00 |                   1.49 |
| best_match                                                                    | 9383 |  2.13 |  -1.29 |   0.92 | raw                |            1.87 |     2815.00 |                   1.95 |
| gfs_hrrr                                                                      | 9383 |  2.13 |  -1.29 |   0.92 | raw                |            1.87 |     2815.00 |                   1.95 |
| gfs_seamless                                                                  | 9383 |  2.13 |  -1.29 |   0.92 | raw                |            1.87 |     2815.00 |                   1.95 |

### temp_f

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1798 |  3.32 |  -0.93 |   0.96 | bias               |            1.95 |      540.00 |                   1.97 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1798 |  3.62 |  -1.46 |   0.95 | bias               |            2.05 |      540.00 |                   2.02 |
| ecmwf_ifs025                                                                  | 1798 |  3.09 |  -0.65 |   0.96 | ridge              |            2.08 |      540.00 |                   2.18 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1798 |  3.20 |  -0.78 |   0.96 | ridge              |            2.11 |      540.00 |                   2.18 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  3.06 |  -0.41 |   0.96 | ridge              |            2.12 |      540.00 |                   2.21 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1798 |  3.28 |  -1.00 |   0.96 | ridge              |            2.13 |      540.00 |                   2.18 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1798 |  3.10 |  -0.54 |   0.97 | ridge              |            2.15 |      540.00 |                   2.27 |
| ecmwf_aifs025_single                                                          | 1798 |  3.46 |  -1.28 |   0.95 | ridge              |            2.16 |      540.00 |                   2.18 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1798 |  3.29 |  -0.72 |   0.95 | ridge              |            2.22 |      540.00 |                   2.28 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1798 |  3.19 |  -0.52 |   0.96 | ridge              |            2.26 |      540.00 |                   2.39 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1798 |  3.19 |  -0.52 |   0.96 | ridge              |            2.26 |      540.00 |                   2.39 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1798 |  3.13 |  -0.30 |   0.96 | ridge              |            2.27 |      540.00 |                   2.40 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1798 |  3.25 |  -0.76 |   0.96 | ridge              |            2.27 |      540.00 |                   2.41 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  3.33 |  -1.00 |   0.96 | ridge              |            2.28 |      540.00 |                   2.44 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1798 |  3.32 |  -0.85 |   0.96 | ridge              |            2.31 |      540.00 |                   2.44 |
| meteofrance_seamless                                                          | 1798 |  3.60 |   2.23 |   0.95 | ridge              |            2.33 |      540.00 |                   2.45 |
| knmi_seamless                                                                 | 1798 |  3.12 |   0.13 |   0.96 | ridge              |            2.40 |      540.00 |                   2.57 |
| metno_seamless                                                                | 1798 |  3.12 |   0.13 |   0.96 | ridge              |            2.40 |      540.00 |                   2.57 |
| gfs_seamless                                                                  | 1798 |  3.33 |  -0.91 |   0.96 | ridge              |            2.41 |      540.00 |                   2.54 |
| best_match                                                                    | 1798 |  3.33 |  -0.91 |   0.96 | ridge              |            2.41 |      540.00 |                   2.54 |
| gfs_hrrr                                                                      | 1798 |  3.33 |  -0.91 |   0.96 | ridge              |            2.41 |      540.00 |                   2.54 |
| ncep_nbm_conus                                                                | 1798 |  3.59 |  -1.17 |   0.94 | ridge              |            2.43 |      540.00 |                   2.58 |
| gem_seamless                                                                  | 1798 |  3.31 |  -0.26 |   0.95 | ridge              |            2.46 |      540.00 |                   2.49 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1798 |  3.52 |  -1.15 |   0.96 | ridge              |            2.53 |      540.00 |                   2.72 |
| ukmo_seamless                                                                 | 1798 |  3.91 |  -1.76 |   0.93 | ridge              |            2.59 |      540.00 |                   2.61 |
| icon_seamless                                                                 | 1798 |  3.65 |  -1.12 |   0.95 | ridge              |            3.14 |      540.00 |                   3.49 |
| jma_seamless                                                                  | 1798 |  4.43 |  -2.56 |   0.94 | ridge              |            3.62 |      540.00 |                   4.13 |

### wind_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  2.95 |   2.90 |   0.75 | ridge              |            0.77 |      540.00 |                   0.77 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1798 |  2.85 |   2.80 |   0.74 | ridge              |            0.77 |      540.00 |                   0.78 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1798 |  2.62 |   2.56 |   0.74 | ridge              |            0.77 |      540.00 |                   0.77 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1798 |  3.04 |   2.97 |   0.74 | ridge              |            0.78 |      540.00 |                   0.79 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1798 |  2.96 |   2.88 |   0.73 | ridge              |            0.78 |      540.00 |                   0.79 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1798 |  2.96 |   2.88 |   0.73 | ridge              |            0.78 |      540.00 |                   0.79 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1798 |  2.58 |   2.51 |   0.72 | ridge              |            0.78 |      540.00 |                   0.76 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1798 |  3.15 |   3.11 |   0.73 | ridge              |            0.78 |      540.00 |                   0.77 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1798 |  2.68 |   2.62 |   0.71 | ridge              |            0.79 |      540.00 |                   0.78 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1798 |  2.82 |   2.75 |   0.73 | ridge              |            0.79 |      540.00 |                   0.79 |
| metno_seamless                                                                | 1798 |  3.21 |   3.13 |   0.74 | ridge              |            0.80 |      540.00 |                   0.81 |
| knmi_seamless                                                                 | 1798 |  3.21 |   3.13 |   0.74 | ridge              |            0.80 |      540.00 |                   0.81 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1798 |  2.57 |   2.47 |   0.70 | ridge              |            0.80 |      540.00 |                   0.79 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1798 |  2.82 |   2.75 |   0.70 | ridge              |            0.81 |      540.00 |                   0.77 |
| icon_seamless                                                                 | 1798 |  2.67 |   2.60 |   0.72 | ridge              |            0.81 |      540.00 |                   0.79 |
| ecmwf_ifs025                                                                  | 1798 |  3.54 |   3.48 |   0.75 | ridge              |            0.82 |      540.00 |                   0.81 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1798 |  2.87 |   2.81 |   0.70 | ridge              |            0.82 |      540.00 |                   0.78 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1798 |  2.65 |   2.56 |   0.69 | ridge              |            0.82 |      540.00 |                   0.82 |
| ncep_nbm_conus                                                                | 1798 |  2.79 |   2.63 |   0.66 | ridge              |            0.83 |      540.00 |                   0.83 |
| gem_seamless                                                                  | 1798 |  2.44 |   2.31 |   0.69 | ridge              |            0.85 |      540.00 |                   0.84 |
| jma_seamless                                                                  | 1798 |  2.26 |   2.15 |   0.63 | ridge              |            0.89 |      540.00 |                   0.89 |
| ecmwf_aifs025_single                                                          | 1798 |  3.14 |   3.04 |   0.69 | ridge              |            0.89 |      540.00 |                   0.89 |
| best_match                                                                    | 1798 |  3.39 |   3.31 |   0.61 | ridge              |            0.89 |      540.00 |                   0.85 |
| gfs_hrrr                                                                      | 1798 |  3.39 |   3.31 |   0.61 | ridge              |            0.89 |      540.00 |                   0.85 |
| gfs_seamless                                                                  | 1798 |  3.39 |   3.31 |   0.61 | ridge              |            0.89 |      540.00 |                   0.85 |
| ukmo_seamless                                                                 | 1798 |  2.66 |   2.48 |   0.65 | ridge              |            0.90 |      540.00 |                   0.90 |
| meteofrance_seamless                                                          | 1798 |  1.58 |   1.25 |   0.61 | bias               |            1.14 |      540.00 |                   1.13 |

## Regional skill — KHIE, Whitefield NH, every season

Ranks models with 13k hours and two winters; the site record above decides. KHIE is 16 km east and is not this hollow: over the hours both stations recorded, temperature correlates 0.88 and dew point 0.92, but wind only 0.57.

### dewpoint_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13230 |  1.97 |   0.81 |   2.63 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13230 |  2.00 |   0.47 |   2.64 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13230 |  2.04 |   0.92 |   2.69 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13230 |  2.06 |   0.27 |   2.77 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13230 |  2.08 |   0.77 |   2.81 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13230 |  2.09 |   1.01 |   2.75 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13230 |  2.10 |   0.92 |   2.89 |
| ncep_nbm_conus                                                                | 13093 |  2.14 |   0.20 |   2.79 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13230 |  2.16 |   1.20 |   2.95 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13230 |  2.17 |   0.95 |   2.95 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13230 |  2.26 |   1.22 |   3.12 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13230 |  2.34 |   1.56 |   3.20 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13230 |  2.34 |   1.42 |   3.17 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13230 |  2.40 |   1.68 |   3.08 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13230 |  2.51 |   1.48 |   3.37 |
| knmi_seamless                                                                 | 13230 |  2.52 |   1.31 |   3.37 |
| metno_seamless                                                                | 13230 |  2.52 |   1.31 |   3.37 |
| gem_seamless                                                                  | 13230 |  2.53 |   0.34 |   3.45 |
| best_match                                                                    | 13230 |  2.77 |   0.88 |   3.59 |
| gfs_seamless                                                                  | 13230 |  2.77 |   0.88 |   3.59 |
| gfs_hrrr                                                                      | 13230 |  2.77 |   0.88 |   3.59 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13230 |  2.81 |   2.22 |   3.66 |
| icon_seamless                                                                 | 13230 |  3.07 |   2.21 |   4.18 |
| jma_seamless                                                                  | 13230 |  3.25 |   1.90 |   4.31 |
| ecmwf_ifs025                                                                  | 13230 |  3.28 |   2.73 |   4.20 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13230 |  3.56 |   3.16 |   4.50 |
| ukmo_seamless                                                                 | 13230 |  3.66 |   2.71 |   4.83 |
| ecmwf_aifs025_single                                                          | 13230 |  3.95 |   3.59 |   4.95 |
| meteofrance_seamless                                                          | 13230 |  7.26 |   7.06 |   8.35 |

### gust_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| gem_seamless                                                                  | 13121 |  4.62 |   3.03 |   6.59 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13121 |  4.78 |   3.44 |   6.24 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13121 |  5.25 |   4.24 |   6.62 |
| ncep_nbm_conus                                                                | 12987 |  5.33 |   3.86 |   6.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13121 |  5.79 |   4.85 |   7.13 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13121 |  5.86 |   5.06 |   7.20 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13121 |  6.29 |   5.29 |   7.58 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13121 |  6.52 |   5.77 |   7.80 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13121 |  6.59 |   5.96 |   7.89 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13121 |  6.63 |   5.77 |   7.95 |
| best_match                                                                    | 13121 |  6.65 |   5.85 |   8.60 |
| gfs_hrrr                                                                      | 13121 |  6.65 |   5.85 |   8.60 |
| gfs_seamless                                                                  | 13121 |  6.65 |   5.85 |   8.60 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13121 |  6.96 |   6.20 |   8.26 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13121 |  7.07 |   6.52 |   8.43 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13121 |  7.10 |   6.37 |   8.34 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13121 |  7.50 |   7.11 |   8.97 |
| ukmo_seamless                                                                 | 13121 |  7.52 |   6.71 |   8.94 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13121 |  7.60 |   6.97 |   8.91 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13121 |  7.66 |   7.06 |   8.90 |
| icon_seamless                                                                 | 13121 |  8.26 |   7.66 |   9.77 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13121 |  8.71 |   8.36 |  10.15 |
| metno_seamless                                                                | 13121 |  8.96 |   8.51 |  10.38 |
| knmi_seamless                                                                 | 13121 |  8.96 |   8.51 |  10.38 |
| meteofrance_seamless                                                          | 13121 | 10.14 |   9.67 |  12.06 |
| ecmwf_ifs025                                                                  | 13121 | 13.78 |  13.70 |  15.48 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13121 | 13.78 |  13.70 |  15.48 |

### humidity_pct

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13230 |  6.99 |   0.47 |   9.01 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13230 |  7.00 |   1.59 |   9.12 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13230 |  7.17 |  -0.69 |   9.30 |
| ncep_nbm_conus                                                                | 13093 |  7.44 |  -1.10 |   9.80 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13230 |  7.44 |  -1.46 |   9.66 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13230 |  7.45 |  -1.40 |   9.75 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13230 |  7.49 |  -2.10 |   9.85 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13230 |  7.73 |  -1.51 |  10.13 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13230 |  8.07 |  -2.88 |  10.63 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13230 |  8.26 |  -2.55 |  10.74 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13230 |  8.47 |  -2.79 |  11.13 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13230 |  8.47 |  -2.42 |  10.89 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13230 |  8.51 |  -1.78 |  10.77 |
| ukmo_seamless                                                                 | 13230 |  8.65 |   4.16 |  11.53 |
| knmi_seamless                                                                 | 13230 |  8.68 |  -1.72 |  11.38 |
| metno_seamless                                                                | 13230 |  8.68 |  -1.72 |  11.38 |
| icon_seamless                                                                 | 13230 |  8.69 |  -3.10 |  11.61 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13230 |  8.91 |  -3.11 |  11.50 |
| jma_seamless                                                                  | 13230 |  9.11 |   3.02 |  11.92 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13230 |  9.43 |  -1.55 |  12.27 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13230 |  9.57 |  -2.44 |  12.27 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13230 |  9.63 |  -0.11 |  12.29 |
| ecmwf_aifs025_single                                                          | 13230 |  9.66 |  -1.00 |  12.43 |
| ecmwf_ifs025                                                                  | 13230 | 10.06 |   0.78 |  12.77 |
| gem_seamless                                                                  | 13230 | 10.76 |  -4.41 |  14.67 |
| best_match                                                                    | 13230 | 11.65 |  -3.78 |  14.82 |
| gfs_hrrr                                                                      | 13230 | 11.65 |  -3.78 |  14.82 |
| gfs_seamless                                                                  | 13230 | 11.65 |  -3.78 |  14.82 |
| meteofrance_seamless                                                          | 13230 | 11.85 |   2.69 |  14.75 |

### temp_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13230 |  3.04 |   1.51 |   4.09 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13230 |  3.06 |   1.08 |   3.99 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13230 |  3.08 |   1.52 |   4.19 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13230 |  3.10 |   1.36 |   4.18 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13230 |  3.11 |   1.30 |   4.13 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13230 |  3.14 |   1.37 |   4.23 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13230 |  3.16 |   1.54 |   4.29 |
| ncep_nbm_conus                                                                | 13093 |  3.17 |   0.39 |   3.98 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13230 |  3.19 |   1.03 |   4.17 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13230 |  3.22 |   1.13 |   4.31 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13230 |  3.26 |   1.61 |   4.38 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13230 |  3.28 |   0.67 |   4.21 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13230 |  3.29 |   1.82 |   4.51 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13230 |  3.31 |   1.81 |   4.41 |
| metno_seamless                                                                | 13230 |  3.36 |   1.75 |   4.60 |
| knmi_seamless                                                                 | 13230 |  3.36 |   1.75 |   4.60 |
| gfs_hrrr                                                                      | 13230 |  3.36 |   1.82 |   4.47 |
| gfs_seamless                                                                  | 13230 |  3.36 |   1.82 |   4.47 |
| best_match                                                                    | 13230 |  3.36 |   1.82 |   4.47 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13230 |  3.47 |   2.29 |   4.87 |
| jma_seamless                                                                  | 13230 |  3.58 |   0.51 |   4.75 |
| gem_seamless                                                                  | 13230 |  3.69 |   1.85 |   5.29 |
| ukmo_seamless                                                                 | 13230 |  3.75 |   0.95 |   4.90 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13230 |  3.85 |   2.60 |   5.53 |
| ecmwf_ifs025                                                                  | 13230 |  4.00 |   2.23 |   5.58 |
| icon_seamless                                                                 | 13230 |  4.12 |   3.21 |   5.70 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13230 |  4.22 |   2.97 |   5.97 |
| ecmwf_aifs025_single                                                          | 13230 |  4.69 |   3.72 |   6.54 |
| meteofrance_seamless                                                          | 13230 |  6.29 |   5.92 |   8.15 |

### wind_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| ncep_nbm_conus                                                                | 12987 |  2.14 |   0.08 |   3.19 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13121 |  2.30 |   0.15 |   3.03 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13121 |  2.33 |   0.50 |   3.01 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13121 |  2.37 |   0.41 |   3.00 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13121 |  2.39 |   0.52 |   2.97 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13121 |  2.40 |   0.79 |   3.11 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13121 |  2.43 |   0.48 |   3.11 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13121 |  2.45 |   0.59 |   3.03 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13121 |  2.49 |   0.90 |   3.05 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13121 |  2.50 |   0.81 |   3.12 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13121 |  2.50 |   0.73 |   3.04 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13121 |  2.51 |   1.01 |   3.18 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13121 |  2.54 |   1.10 |   3.09 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13121 |  2.54 |   0.97 |   3.12 |
| icon_seamless                                                                 | 13121 |  2.62 |   0.92 |   3.20 |
| gem_seamless                                                                  | 13121 |  2.64 |   0.22 |   3.33 |
| jma_seamless                                                                  | 13121 |  2.68 |   0.26 |   3.33 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13121 |  2.71 |   1.39 |   3.24 |
| metno_seamless                                                                | 13121 |  2.79 |   1.47 |   3.45 |
| knmi_seamless                                                                 | 13121 |  2.79 |   1.47 |   3.45 |
| gfs_hrrr                                                                      | 13121 |  2.80 |   1.24 |   3.43 |
| gfs_seamless                                                                  | 13121 |  2.80 |   1.24 |   3.43 |
| best_match                                                                    | 13121 |  2.80 |   1.24 |   3.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13121 |  2.80 |   1.49 |   3.43 |
| ukmo_seamless                                                                 | 13121 |  2.85 |   0.87 |   3.49 |
| ecmwf_aifs025_single                                                          | 13121 |  2.95 |   1.63 |   3.67 |
| meteofrance_seamless                                                          | 13121 |  3.10 |  -0.68 |   3.95 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13121 |  3.12 |   2.12 |   3.85 |
| ecmwf_ifs025                                                                  | 13121 |  3.38 |   2.60 |   4.18 |

## Regional MAE by season (temperature)

| candidate                                                                     |   fall |   spring |   summer |   winter |
|:------------------------------------------------------------------------------|-------:|---------:|---------:|---------:|
| best_match                                                                    |   3.41 |     3.05 |     3.51 |     3.54 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       |   4.35 |     3.67 |     4.34 |     4.74 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          |   3.99 |     3.34 |     3.95 |     4.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    |   3.61 |     3.02 |     3.61 |     3.75 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         |   3.27 |     2.85 |     3.28 |     3.16 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   |   3.22 |     2.72 |     3.21 |     3.18 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                |   3.21 |     2.87 |     3.16 |     3.17 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   |   3.23 |     3.02 |     3.11 |     3.38 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               |   3.37 |     3.04 |     3.25 |     3.68 |
| blend:gem_seamless+ncep_nbm_conus                                             |   3.42 |     3.04 |     3.17 |     3.32 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       |   3.16 |     2.70 |     3.23 |     3.06 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless |   3.38 |     2.93 |     3.36 |     3.44 |
| blend:icon_seamless+ncep_nbm_conus                                            |   3.33 |     3.17 |     3.21 |     3.71 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             |   3.28 |     2.79 |     3.24 |     3.16 |
| blend:knmi_seamless+ncep_nbm_conus                                            |   3.25 |     2.81 |     3.14 |     3.05 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              |   3.39 |     2.92 |     3.31 |     3.09 |
| blend:ncep_nbm_conus+ukmo_seamless                                            |   3.51 |     3.13 |     3.33 |     3.11 |
| ecmwf_aifs025_single                                                          |   4.76 |     4.07 |     4.94 |     5.14 |
| ecmwf_ifs025                                                                  |   4.18 |     3.54 |     3.96 |     4.56 |
| gem_seamless                                                                  |   3.78 |     3.44 |     3.64 |     4.06 |
| gfs_hrrr                                                                      |   3.41 |     3.05 |     3.51 |     3.54 |
| gfs_seamless                                                                  |   3.41 |     3.05 |     3.51 |     3.54 |
| icon_seamless                                                                 |   4.04 |     3.90 |     3.85 |     5.16 |
| jma_seamless                                                                  |   3.30 |     3.92 |     3.28 |     4.02 |
| knmi_seamless                                                                 |   3.50 |     2.88 |     3.55 |     3.57 |
| meteofrance_seamless                                                          |   6.69 |     5.21 |     6.08 |     7.95 |
| metno_seamless                                                                |   3.50 |     2.88 |     3.55 |     3.57 |
| ncep_nbm_conus                                                                |   3.39 |     3.12 |     3.09 |     3.07 |
| ukmo_seamless                                                                 |   4.01 |     3.46 |     3.92 |     3.49 |

## MAE by lead time, days 1-7 (previous-runs, site)

### gust_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 6.87 |   3.57 |   3.84 |   4.15 |   4.42 |   4.93 |   4.73 |
| gem_seamless         | 4.16 |   4.03 |   4.16 |   4.06 |   4.34 |   4.84 |   5.59 |
| gfs_hrrr             | 6.87 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 6.87 |   3.57 |   3.84 |   4.15 |   4.42 |   4.93 |   4.73 |
| icon_seamless        | 5.43 |   5.50 |   5.63 |   5.97 |   6.08 |   6.44 | nan    |
| meteofrance_seamless | 6.06 |   6.00 |   6.09 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.52 |   3.64 |   3.81 |   4.03 |   4.02 |   4.14 |   4.08 |
| ukmo_seamless        | 4.43 |   4.76 |   4.51 |   4.86 |   5.05 |   5.25 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 12.43 |   9.68 |  10.80 |  11.47 |  11.81 |  13.22 |  13.20 |
| ecmwf_aifs025_single |  6.60 |   7.03 |   7.66 |   7.95 |   9.04 |   9.05 |  10.45 |
| ecmwf_ifs025         |  7.79 |   8.33 |   9.08 |   9.47 |  10.51 |  10.65 |  11.68 |
| gem_seamless         |  9.38 |  10.25 |  10.00 |  10.50 |  11.44 |  12.37 |  12.98 |
| gfs_hrrr             | 12.43 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 12.43 |   9.68 |  10.80 |  11.47 |  11.81 |  13.22 |  13.20 |
| icon_seamless        |  8.30 |   8.51 |   8.86 |   9.45 |  10.71 |  11.60 | nan    |
| jma_seamless         | 10.85 |  10.78 |  11.86 |  12.22 |  12.68 |  14.29 |  15.49 |
| knmi_seamless        |  8.49 |   8.91 |   9.39 |   9.77 |  10.78 |  10.90 |  12.09 |
| meteofrance_seamless |  9.90 |  10.48 |  10.69 | nan    | nan    | nan    | nan    |
| metno_seamless       |  8.49 |   8.91 |   9.39 |   9.77 |  10.78 |  10.90 |  12.09 |
| ncep_nbm_conus       |  8.92 |   9.16 |   9.42 |   9.88 |  10.41 |  10.95 |  11.33 |
| ukmo_seamless        | 10.72 |  11.15 |  11.83 |  11.68 |  13.08 |  13.22 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 3.54 |   4.56 |   4.71 |   5.05 |   5.45 |   5.95 |   5.90 |
| ecmwf_aifs025_single | 3.30 |   3.43 |   3.62 |   3.76 |   4.09 |   4.36 |   4.48 |
| ecmwf_ifs025         | 3.28 |   3.44 |   3.65 |   4.09 |   4.18 |   4.68 |   4.86 |
| gem_seamless         | 3.64 |   4.46 |   4.12 |   4.59 |   4.98 |   5.20 |   5.61 |
| gfs_hrrr             | 3.54 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 3.54 |   4.56 |   4.71 |   5.05 |   5.45 |   5.95 |   5.90 |
| icon_seamless        | 3.82 |   4.02 |   4.19 |   4.32 |   4.70 |   5.10 | nan    |
| jma_seamless         | 4.54 |   4.72 |   4.78 |   5.10 |   5.38 |   5.98 |   6.04 |
| knmi_seamless        | 3.41 |   3.56 |   3.81 |   4.17 |   4.18 |   4.68 |   4.92 |
| meteofrance_seamless | 4.09 |   4.16 |   4.50 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.41 |   3.56 |   3.81 |   4.17 |   4.18 |   4.68 |   4.92 |
| ncep_nbm_conus       | 3.85 |   4.03 |   4.06 |   4.20 |   4.46 |   4.47 |   4.51 |
| ukmo_seamless        | 3.89 |   4.15 |   4.29 |   4.31 |   4.47 |   4.71 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.49 |   2.60 |   2.53 |   2.70 |   2.66 |   2.63 |   2.38 |
| ecmwf_aifs025_single | 3.16 |   3.15 |   3.19 |   3.31 |   3.36 |   3.44 |   3.36 |
| ecmwf_ifs025         | 3.48 |   3.54 |   3.34 |   3.55 |   3.70 |   3.40 |   3.35 |
| gem_seamless         | 2.54 |   2.11 |   1.91 |   1.88 |   1.92 |   1.92 |   2.14 |
| gfs_hrrr             | 4.49 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.49 |   2.60 |   2.53 |   2.70 |   2.66 |   2.63 |   2.38 |
| icon_seamless        | 2.63 |   2.67 |   2.73 |   2.76 |   2.77 |   2.90 | nan    |
| jma_seamless         | 2.10 |   2.21 |   2.24 |   2.25 |   2.39 |   2.23 |   2.08 |
| knmi_seamless        | 3.09 |   3.21 |   3.04 |   3.25 |   3.43 |   3.21 |   3.19 |
| meteofrance_seamless | 1.58 |   1.60 |   1.62 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.09 |   3.21 |   3.04 |   3.25 |   3.43 |   3.21 |   3.19 |
| ncep_nbm_conus       | 2.65 |   2.63 |   2.66 |   2.74 |   2.52 |   2.48 |   2.31 |
| ukmo_seamless        | 2.77 |   2.90 |   2.70 |   2.87 |   2.87 |   2.96 | nan    |
