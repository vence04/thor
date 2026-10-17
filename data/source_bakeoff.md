# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-10-12.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Source in use, per variable

| variable | source |
|---|---|
| dewpoint_f | blend of icon_seamless, ncep_nbm_conus |
| gust_mph | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |
| humidity_pct | blend of gfs_hrrr, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| precip_in | best_match |
| pressure_abs_hpa | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |
| temp_f | ecmwf_ifs025 |
| wind_mph | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |

## Site skill, shortlisted candidates (lower MAE = better)

### dewpoint_f

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+ncep_nbm_conus                                            | 1649 |  2.27 |  -0.07 |   0.97 | raw                |            1.51 |      495.00 |                   1.35 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  2.20 |  -0.13 |   0.97 | raw                |            1.58 |      495.00 |                   1.31 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1649 |  2.38 |   0.26 |   0.97 | raw                |            1.58 |      495.00 |                   1.50 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1649 |  2.38 |   0.26 |   0.97 | raw                |            1.58 |      495.00 |                   1.50 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1649 |  2.12 |  -0.13 |   0.97 | raw                |            1.58 |      495.00 |                   1.35 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1649 |  2.24 |  -0.23 |   0.97 | raw                |            1.59 |      495.00 |                   1.31 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1649 |  2.22 |  -0.11 |   0.97 | raw                |            1.59 |      495.00 |                   1.37 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1649 |  2.28 |   0.05 |   0.97 | raw                |            1.60 |      495.00 |                   1.40 |
| ncep_nbm_conus                                                                | 1649 |  2.39 |   0.65 |   0.97 | bias               |            1.66 |      495.00 |                   1.53 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1649 |  2.19 |  -0.19 |   0.97 | raw                |            1.69 |      495.00 |                   1.50 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  2.26 |  -0.24 |   0.97 | raw                |            1.69 |      495.00 |                   1.37 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1649 |  2.43 |  -0.10 |   0.97 | raw                |            1.69 |      495.00 |                   1.49 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1649 |  2.47 |   0.13 |   0.97 | raw                |            1.71 |      495.00 |                   1.56 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1649 |  2.55 |   0.14 |   0.96 | bias               |            1.73 |      495.00 |                   1.49 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1649 |  2.67 |   0.27 |   0.95 | bias               |            1.91 |      495.00 |                   1.74 |
| ecmwf_aifs025_single                                                          | 1649 |  2.55 |  -0.48 |   0.96 | raw                |            1.97 |      495.00 |                   1.65 |
| metno_seamless                                                                | 1649 |  2.75 |  -0.13 |   0.96 | raw                |            2.11 |      495.00 |                   1.86 |
| knmi_seamless                                                                 | 1649 |  2.75 |  -0.13 |   0.96 | raw                |            2.11 |      495.00 |                   1.86 |
| icon_seamless                                                                 | 1649 |  2.61 |  -0.79 |   0.96 | raw                |            2.17 |      495.00 |                   1.82 |
| ecmwf_ifs025                                                                  | 1649 |  2.75 |  -0.65 |   0.96 | raw                |            2.18 |      495.00 |                   1.88 |
| gem_seamless                                                                  | 1649 |  2.74 |  -0.55 |   0.95 | raw                |            2.28 |      495.00 |                   1.77 |
| best_match                                                                    | 1649 |  3.00 |  -0.48 |   0.94 | ridge              |            2.39 |      495.00 |                   2.69 |
| gfs_seamless                                                                  | 1649 |  3.00 |  -0.48 |   0.94 | ridge              |            2.39 |      495.00 |                   2.69 |
| gfs_hrrr                                                                      | 1649 |  3.00 |  -0.48 |   0.94 | ridge              |            2.39 |      495.00 |                   2.69 |
| ukmo_seamless                                                                 | 1649 |  3.41 |  -0.11 |   0.90 | ridge              |            2.45 |      495.00 |                   2.70 |
| jma_seamless                                                                  | 1649 |  2.87 |  -0.38 |   0.93 | ridge              |            2.47 |      495.00 |                   2.96 |
| meteofrance_seamless                                                          | 1649 |  3.14 |  -0.31 |   0.94 | raw                |            2.88 |      495.00 |                   2.15 |

### gust_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1649 |  4.77 |   4.44 |   0.88 | ridge              |            1.82 |      495.00 |                   1.80 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1649 |  5.01 |   4.70 |   0.88 | ridge              |            1.84 |      495.00 |                   1.82 |
| knmi_seamless                                                                 | 1649 |  6.09 |   5.90 |   0.85 | ridge              |            1.93 |      495.00 |                   1.89 |
| metno_seamless                                                                | 1649 |  6.09 |   5.90 |   0.85 | ridge              |            1.93 |      495.00 |                   1.89 |
| ecmwf_ifs025                                                                  | 1649 |  7.24 |   7.12 |   0.83 | ridge              |            2.17 |      495.00 |                   2.07 |
| icon_seamless                                                                 | 1649 |  5.52 |   5.10 |   0.83 | ridge              |            2.26 |      495.00 |                   2.28 |
| ncep_nbm_conus                                                                | 1649 |  3.47 |   2.29 |   0.87 | bias               |            2.27 |      495.00 |                   2.19 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1649 |  3.31 |   2.03 |   0.88 | bias               |            2.37 |      495.00 |                   2.39 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1649 |  3.55 |   2.66 |   0.87 | bias               |            2.39 |      495.00 |                   2.39 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1649 |  3.85 |   3.05 |   0.88 | bias               |            2.61 |      495.00 |                   2.76 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1649 |  3.65 |   2.57 |   0.87 | bias               |            2.68 |      495.00 |                   2.51 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1649 |  4.22 |   3.74 |   0.88 | bias               |            2.74 |      495.00 |                   2.79 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1649 |  4.27 |   3.70 |   0.87 | bias               |            2.75 |      495.00 |                   2.85 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1649 |  3.82 |   2.88 |   0.86 | bias               |            2.83 |      495.00 |                   2.64 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1649 |  4.53 |   4.10 |   0.88 | bias               |            2.84 |      495.00 |                   2.87 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1649 |  4.53 |   4.10 |   0.88 | bias               |            2.84 |      495.00 |                   2.87 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  4.27 |   3.76 |   0.89 | bias               |            2.86 |      495.00 |                   2.99 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  4.38 |   3.90 |   0.89 | bias               |            2.90 |      495.00 |                   2.91 |
| ukmo_seamless                                                                 | 1649 |  3.99 |   3.02 |   0.83 | bias               |            3.05 |      495.00 |                   3.20 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1649 |  4.75 |   4.28 |   0.87 | bias               |            3.14 |      495.00 |                   3.02 |
| gem_seamless                                                                  | 1649 |  3.83 |   1.77 |   0.82 | bias               |            3.26 |      495.00 |                   3.39 |
| best_match                                                                    | 1649 |  4.80 |   3.66 |   0.76 | bias               |            4.29 |      495.00 |                   3.70 |
| gfs_seamless                                                                  | 1649 |  4.80 |   3.66 |   0.76 | bias               |            4.29 |      495.00 |                   3.70 |
| gfs_hrrr                                                                      | 1649 |  4.80 |   3.66 |   0.76 | bias               |            4.29 |      495.00 |                   3.70 |
| meteofrance_seamless                                                          | 1649 |  5.60 |   5.25 |   0.80 | bias               |            4.78 |      495.00 |                   4.72 |

### humidity_pct

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1649 |  5.91 |   1.32 |   0.95 | ridge              |            5.95 |      495.00 |                   5.62 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  6.04 |   1.23 |   0.95 | ridge              |            6.00 |      495.00 |                   5.87 |
| meteofrance_seamless                                                          | 1649 |  9.29 |  -5.40 |   0.91 | ridge              |            6.12 |      495.00 |                   5.75 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  6.98 |   2.68 |   0.94 | ridge              |            6.13 |      495.00 |                   5.89 |
| ecmwf_aifs025_single                                                          | 1649 |  6.93 |   2.09 |   0.93 | ridge              |            6.24 |      495.00 |                   6.23 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1649 |  6.30 |   2.21 |   0.94 | ridge              |            6.27 |      495.00 |                   5.97 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1649 |  7.10 |   2.40 |   0.93 | ridge              |            6.34 |      495.00 |                   5.94 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1649 |  6.26 |   1.90 |   0.94 | ridge              |            6.38 |      495.00 |                   6.22 |
| ecmwf_ifs025                                                                  | 1649 |  7.04 |   0.59 |   0.93 | ridge              |            6.45 |      495.00 |                   6.17 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1649 |  7.04 |   2.25 |   0.94 | ridge              |            6.54 |      495.00 |                   6.38 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1649 |  7.10 |   1.86 |   0.93 | ridge              |            6.62 |      495.00 |                   6.48 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1649 |  7.26 |   2.67 |   0.93 | ridge              |            6.72 |      495.00 |                   6.57 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1649 |  7.26 |   2.67 |   0.93 | ridge              |            6.72 |      495.00 |                   6.57 |
| knmi_seamless                                                                 | 1649 |  7.36 |   0.23 |   0.92 | ridge              |            6.76 |      495.00 |                   6.68 |
| metno_seamless                                                                | 1649 |  7.36 |   0.23 |   0.92 | ridge              |            6.76 |      495.00 |                   6.68 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1649 |  7.71 |   3.41 |   0.92 | ridge              |            6.79 |      495.00 |                   6.43 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1649 |  7.57 |   3.33 |   0.93 | ridge              |            6.86 |      495.00 |                   6.42 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1649 |  7.36 |   2.60 |   0.92 | ridge              |            7.05 |      495.00 |                   7.08 |
| gfs_seamless                                                                  | 1649 |  7.57 |   0.50 |   0.86 | ridge              |            7.20 |      495.00 |                   6.88 |
| best_match                                                                    | 1649 |  7.57 |   0.50 |   0.86 | ridge              |            7.20 |      495.00 |                   6.88 |
| gfs_hrrr                                                                      | 1649 |  7.57 |   0.50 |   0.86 | ridge              |            7.20 |      495.00 |                   6.88 |
| icon_seamless                                                                 | 1649 |  7.77 |   1.56 |   0.90 | ridge              |            7.26 |      495.00 |                   6.66 |
| gem_seamless                                                                  | 1649 |  7.93 |   0.08 |   0.90 | ridge              |            7.53 |      495.00 |                   7.62 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1649 |  8.72 |   4.99 |   0.91 | ridge              |            7.53 |      495.00 |                   7.10 |
| ncep_nbm_conus                                                                | 1649 |  8.66 |   5.11 |   0.91 | ridge              |            7.75 |      495.00 |                   7.54 |
| jma_seamless                                                                  | 1649 | 10.53 |   6.40 |   0.83 | ridge              |            8.56 |      495.00 |                   8.48 |
| ukmo_seamless                                                                 | 1649 |  9.98 |   4.87 |   0.85 | ridge              |            8.71 |      495.00 |                   8.30 |

### precip_in

| candidate                                                                     |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                    | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                  | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                      | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                 | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                          | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 2063 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                 | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                  | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                            | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                             | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                  | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:metno_seamless+ncep_nbm_conus                                           | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus                                            | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                | 2063 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                 | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                  | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                          | 2063 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 9234 |  1.49 |  -0.61 |   0.93 | bias               |            1.05 |     2770.00 |                   0.40 |
| ecmwf_ifs025                                                                  | 9234 |  1.40 |  -0.47 |   0.93 | bias               |            1.07 |     2770.00 |                   0.40 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 9234 |  1.40 |  -0.48 |   0.93 | bias               |            1.07 |     2770.00 |                   0.41 |
| blend:metno_seamless+ncep_nbm_conus                                           | 9234 |  1.40 |  -0.48 |   0.93 | bias               |            1.07 |     2770.00 |                   0.41 |
| knmi_seamless                                                                 | 9234 |  1.40 |  -0.48 |   0.93 | bias               |            1.07 |     2770.00 |                   0.41 |
| metno_seamless                                                                | 9234 |  1.40 |  -0.48 |   0.93 | bias               |            1.07 |     2770.00 |                   0.41 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 9234 |  1.40 |  -0.48 |   0.93 | bias               |            1.07 |     2770.00 |                   0.41 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 9234 |  1.33 |  -0.42 |   0.93 | bias               |            1.09 |     2770.00 |                   0.42 |
| ecmwf_aifs025_single                                                          | 9234 |  1.42 |  -0.45 |   0.93 | bias               |            1.10 |     2770.00 |                   0.45 |
| meteofrance_seamless                                                          | 9234 |  1.32 |  -0.28 |   0.93 | bias               |            1.11 |     2770.00 |                   0.50 |
| blend:icon_seamless+ncep_nbm_conus                                            | 9234 |  1.32 |  -0.34 |   0.93 | bias               |            1.15 |     2770.00 |                   0.54 |
| icon_seamless                                                                 | 9234 |  1.32 |  -0.34 |   0.93 | bias               |            1.15 |     2770.00 |                   0.54 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 9234 |  1.27 |  -0.30 |   0.93 | bias               |            1.15 |     2770.00 |                   0.52 |
| jma_seamless                                                                  | 9234 |  1.52 |  -0.61 |   0.93 | bias               |            1.18 |     2770.00 |                   0.44 |
| blend:gem_seamless+ncep_nbm_conus                                             | 9234 |  1.25 |  -0.26 |   0.93 | bias               |            1.20 |     2770.00 |                   0.56 |
| gem_seamless                                                                  | 9234 |  1.25 |  -0.26 |   0.93 | bias               |            1.20 |     2770.00 |                   0.56 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 9234 |  1.51 |  -0.62 |   0.93 | raw                |            1.39 |     2770.00 |                   0.84 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 9234 |  1.64 |  -0.77 |   0.93 | raw                |            1.49 |     2770.00 |                   1.05 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 9234 |  1.66 |  -0.81 |   0.93 | raw                |            1.54 |     2770.00 |                   0.99 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 9234 |  1.74 |  -0.88 |   0.93 | raw                |            1.54 |     2770.00 |                   1.12 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 9234 |  1.83 |  -0.99 |   0.93 | raw                |            1.63 |     2770.00 |                   1.26 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 9234 |  1.95 |  -1.13 |   0.93 | raw                |            1.79 |     2770.00 |                   1.34 |
| ukmo_seamless                                                                 | 9234 |  1.95 |  -1.13 |   0.93 | raw                |            1.79 |     2770.00 |                   1.34 |
| best_match                                                                    | 9234 |  2.12 |  -1.27 |   0.92 | raw                |            1.80 |     2770.00 |                   1.63 |
| gfs_hrrr                                                                      | 9234 |  2.12 |  -1.27 |   0.92 | raw                |            1.80 |     2770.00 |                   1.63 |
| gfs_seamless                                                                  | 9234 |  2.12 |  -1.27 |   0.92 | raw                |            1.80 |     2770.00 |                   1.63 |

### temp_f

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1649 |  3.33 |  -0.76 |   0.95 | ridge              |            2.29 |      495.00 |                   1.92 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1649 |  3.41 |  -0.98 |   0.95 | ridge              |            2.31 |      495.00 |                   1.89 |
| best_match                                                                    | 1649 |  3.45 |  -0.89 |   0.94 | ridge              |            2.35 |      495.00 |                   2.01 |
| gfs_seamless                                                                  | 1649 |  3.45 |  -0.89 |   0.94 | ridge              |            2.35 |      495.00 |                   2.01 |
| gfs_hrrr                                                                      | 1649 |  3.45 |  -0.89 |   0.94 | ridge              |            2.35 |      495.00 |                   2.01 |
| ecmwf_ifs025                                                                  | 1649 |  3.21 |  -0.65 |   0.95 | raw                |            2.36 |      495.00 |                   1.91 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  3.18 |  -0.40 |   0.95 | ridge              |            2.38 |      495.00 |                   1.96 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1649 |  3.22 |  -0.54 |   0.95 | ridge              |            2.39 |      495.00 |                   1.95 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1649 |  3.47 |  -0.86 |   0.95 | ridge              |            2.41 |      495.00 |                   2.00 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1649 |  3.41 |  -0.70 |   0.95 | ridge              |            2.44 |      495.00 |                   2.11 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  3.47 |  -1.02 |   0.95 | ridge              |            2.45 |      495.00 |                   1.92 |
| knmi_seamless                                                                 | 1649 |  3.24 |   0.13 |   0.95 | ridge              |            2.54 |      495.00 |                   2.10 |
| metno_seamless                                                                | 1649 |  3.24 |   0.13 |   0.95 | ridge              |            2.54 |      495.00 |                   2.10 |
| gem_seamless                                                                  | 1649 |  3.45 |  -0.21 |   0.94 | ridge              |            2.56 |      495.00 |                   2.39 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1649 |  3.25 |  -0.31 |   0.95 | ridge              |            2.58 |      495.00 |                   2.13 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1649 |  3.39 |  -0.77 |   0.95 | ridge              |            2.58 |      495.00 |                   2.04 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1649 |  3.67 |  -1.18 |   0.94 | ridge              |            2.60 |      495.00 |                   2.10 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1649 |  3.45 |  -0.93 |   0.95 | ridge              |            2.61 |      495.00 |                   2.08 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1649 |  3.75 |  -1.46 |   0.94 | ridge              |            2.61 |      495.00 |                   2.07 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1649 |  3.32 |  -0.52 |   0.95 | ridge              |            2.61 |      495.00 |                   2.18 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1649 |  3.32 |  -0.52 |   0.95 | ridge              |            2.61 |      495.00 |                   2.18 |
| ncep_nbm_conus                                                                | 1649 |  3.69 |  -1.18 |   0.94 | ridge              |            2.71 |      495.00 |                   2.34 |
| ukmo_seamless                                                                 | 1649 |  4.00 |  -1.74 |   0.92 | ridge              |            2.80 |      495.00 |                   2.28 |
| icon_seamless                                                                 | 1649 |  3.82 |  -1.17 |   0.93 | ridge              |            2.86 |      495.00 |                   2.25 |
| ecmwf_aifs025_single                                                          | 1649 |  3.55 |  -1.21 |   0.94 | raw                |            2.97 |      495.00 |                   2.41 |
| meteofrance_seamless                                                          | 1649 |  3.66 |   2.28 |   0.94 | bias               |            3.89 |      495.00 |                   3.52 |
| jma_seamless                                                                  | 1649 |  4.59 |  -2.64 |   0.91 | raw                |            4.19 |      495.00 |                   3.11 |

### wind_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1649 |  2.77 |   2.71 |   0.81 | ridge              |            0.68 |      495.00 |                   0.75 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1649 |  2.85 |   2.76 |   0.81 | ridge              |            0.69 |      495.00 |                   0.75 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1649 |  2.85 |   2.76 |   0.81 | ridge              |            0.69 |      495.00 |                   0.75 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1649 |  2.93 |   2.86 |   0.81 | ridge              |            0.69 |      495.00 |                   0.76 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1649 |  2.72 |   2.65 |   0.80 | ridge              |            0.69 |      495.00 |                   0.76 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  2.54 |   2.48 |   0.80 | ridge              |            0.70 |      495.00 |                   0.75 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1649 |  2.89 |   2.83 |   0.79 | ridge              |            0.70 |      495.00 |                   0.75 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1649 |  2.58 |   2.51 |   0.79 | ridge              |            0.71 |      495.00 |                   0.76 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1649 |  3.08 |   3.03 |   0.78 | ridge              |            0.71 |      495.00 |                   0.76 |
| knmi_seamless                                                                 | 1649 |  3.13 |   3.05 |   0.80 | ridge              |            0.71 |      495.00 |                   0.78 |
| metno_seamless                                                                | 1649 |  3.13 |   3.05 |   0.80 | ridge              |            0.71 |      495.00 |                   0.78 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1649 |  2.51 |   2.44 |   0.78 | ridge              |            0.72 |      495.00 |                   0.77 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1649 |  2.55 |   2.45 |   0.76 | ridge              |            0.73 |      495.00 |                   0.81 |
| ncep_nbm_conus                                                                | 1649 |  2.63 |   2.47 |   0.75 | ridge              |            0.74 |      495.00 |                   0.81 |
| icon_seamless                                                                 | 1649 |  2.62 |   2.55 |   0.77 | ridge              |            0.75 |      495.00 |                   0.82 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1649 |  2.49 |   2.39 |   0.75 | ridge              |            0.76 |      495.00 |                   0.80 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1649 |  2.75 |   2.68 |   0.73 | ridge              |            0.76 |      495.00 |                   0.79 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1649 |  2.82 |   2.75 |   0.73 | ridge              |            0.76 |      495.00 |                   0.80 |
| ecmwf_ifs025                                                                  | 1649 |  3.45 |   3.39 |   0.79 | ridge              |            0.77 |      495.00 |                   0.84 |
| jma_seamless                                                                  | 1649 |  2.15 |   2.02 |   0.73 | ridge              |            0.78 |      495.00 |                   0.87 |
| ecmwf_aifs025_single                                                          | 1649 |  2.99 |   2.87 |   0.78 | ridge              |            0.80 |      495.00 |                   0.89 |
| ukmo_seamless                                                                 | 1649 |  2.61 |   2.43 |   0.70 | ridge              |            0.83 |      495.00 |                   0.93 |
| gem_seamless                                                                  | 1649 |  2.43 |   2.30 |   0.68 | ridge              |            0.84 |      495.00 |                   0.88 |
| best_match                                                                    | 1649 |  3.37 |   3.28 |   0.63 | ridge              |            0.86 |      495.00 |                   0.92 |
| gfs_hrrr                                                                      | 1649 |  3.37 |   3.28 |   0.63 | ridge              |            0.86 |      495.00 |                   0.92 |
| gfs_seamless                                                                  | 1649 |  3.37 |   3.28 |   0.63 | ridge              |            0.86 |      495.00 |                   0.92 |
| meteofrance_seamless                                                          | 1649 |  1.56 |   1.21 |   0.65 | bias               |            1.07 |      495.00 |                   1.19 |

## Regional skill — KHIE, Whitefield NH, every season

Ranks models with 13k hours and two winters; the site record above decides. KHIE is 16 km east and is not this hollow: over the hours both stations recorded, temperature correlates 0.88 and dew point 0.92, but wind only 0.57.

### dewpoint_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13185 |  1.97 |   0.81 |   2.63 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13185 |  2.00 |   0.47 |   2.64 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13185 |  2.04 |   0.92 |   2.69 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13185 |  2.06 |   0.27 |   2.77 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13185 |  2.08 |   0.77 |   2.81 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13185 |  2.09 |   1.01 |   2.75 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13185 |  2.10 |   0.92 |   2.89 |
| ncep_nbm_conus                                                                | 13048 |  2.14 |   0.20 |   2.79 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13185 |  2.15 |   1.20 |   2.95 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13185 |  2.17 |   0.95 |   2.95 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13185 |  2.26 |   1.22 |   3.12 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13185 |  2.33 |   1.56 |   3.20 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13185 |  2.34 |   1.42 |   3.17 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13185 |  2.40 |   1.69 |   3.08 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13185 |  2.51 |   1.48 |   3.37 |
| knmi_seamless                                                                 | 13185 |  2.52 |   1.32 |   3.37 |
| metno_seamless                                                                | 13185 |  2.52 |   1.32 |   3.37 |
| gem_seamless                                                                  | 13185 |  2.53 |   0.34 |   3.45 |
| best_match                                                                    | 13185 |  2.77 |   0.88 |   3.59 |
| gfs_seamless                                                                  | 13185 |  2.77 |   0.88 |   3.59 |
| gfs_hrrr                                                                      | 13185 |  2.77 |   0.88 |   3.59 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13185 |  2.81 |   2.22 |   3.66 |
| icon_seamless                                                                 | 13185 |  3.06 |   2.21 |   4.18 |
| jma_seamless                                                                  | 13185 |  3.25 |   1.91 |   4.31 |
| ecmwf_ifs025                                                                  | 13185 |  3.28 |   2.73 |   4.21 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13185 |  3.56 |   3.16 |   4.50 |
| ukmo_seamless                                                                 | 13185 |  3.66 |   2.72 |   4.83 |
| ecmwf_aifs025_single                                                          | 13185 |  3.95 |   3.59 |   4.95 |
| meteofrance_seamless                                                          | 13185 |  7.27 |   7.07 |   8.35 |

### gust_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| gem_seamless                                                                  | 13076 |  4.62 |   3.03 |   6.60 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13076 |  4.79 |   3.44 |   6.25 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13076 |  5.25 |   4.25 |   6.62 |
| ncep_nbm_conus                                                                | 12942 |  5.34 |   3.86 |   6.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13076 |  5.79 |   4.85 |   7.13 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13076 |  5.86 |   5.06 |   7.20 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13076 |  6.29 |   5.30 |   7.58 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13076 |  6.52 |   5.77 |   7.81 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13076 |  6.60 |   5.96 |   7.89 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13076 |  6.63 |   5.77 |   7.95 |
| best_match                                                                    | 13076 |  6.66 |   5.86 |   8.61 |
| gfs_hrrr                                                                      | 13076 |  6.66 |   5.86 |   8.61 |
| gfs_seamless                                                                  | 13076 |  6.66 |   5.86 |   8.61 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13076 |  6.96 |   6.20 |   8.26 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13076 |  7.07 |   6.52 |   8.44 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13076 |  7.10 |   6.37 |   8.35 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13076 |  7.50 |   7.11 |   8.97 |
| ukmo_seamless                                                                 | 13076 |  7.52 |   6.71 |   8.95 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13076 |  7.60 |   6.97 |   8.92 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13076 |  7.66 |   7.06 |   8.90 |
| icon_seamless                                                                 | 13076 |  8.26 |   7.66 |   9.77 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13076 |  8.71 |   8.36 |  10.16 |
| metno_seamless                                                                | 13076 |  8.96 |   8.51 |  10.38 |
| knmi_seamless                                                                 | 13076 |  8.96 |   8.51 |  10.38 |
| meteofrance_seamless                                                          | 13076 | 10.14 |   9.68 |  12.06 |
| ecmwf_ifs025                                                                  | 13076 | 13.78 |  13.70 |  15.48 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13076 | 13.78 |  13.70 |  15.48 |

### humidity_pct

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13185 |  6.97 |   0.50 |   8.99 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13185 |  6.98 |   1.62 |   9.10 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13185 |  7.16 |  -0.66 |   9.28 |
| ncep_nbm_conus                                                                | 13048 |  7.43 |  -1.07 |   9.79 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13185 |  7.43 |  -1.43 |   9.65 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13185 |  7.44 |  -1.38 |   9.74 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13185 |  7.48 |  -2.08 |   9.84 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13185 |  7.72 |  -1.48 |  10.11 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13185 |  8.06 |  -2.85 |  10.62 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13185 |  8.24 |  -2.52 |  10.72 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13185 |  8.45 |  -2.39 |  10.87 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13185 |  8.45 |  -2.76 |  11.11 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13185 |  8.49 |  -1.75 |  10.74 |
| ukmo_seamless                                                                 | 13185 |  8.63 |   4.21 |  11.51 |
| knmi_seamless                                                                 | 13185 |  8.66 |  -1.68 |  11.37 |
| metno_seamless                                                                | 13185 |  8.66 |  -1.68 |  11.37 |
| icon_seamless                                                                 | 13185 |  8.68 |  -3.08 |  11.61 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13185 |  8.89 |  -3.08 |  11.48 |
| jma_seamless                                                                  | 13185 |  9.12 |   3.04 |  11.93 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13185 |  9.41 |  -1.51 |  12.25 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13185 |  9.55 |  -2.41 |  12.25 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13185 |  9.62 |  -0.08 |  12.28 |
| ecmwf_aifs025_single                                                          | 13185 |  9.65 |  -0.97 |  12.43 |
| ecmwf_ifs025                                                                  | 13185 | 10.05 |   0.82 |  12.76 |
| gem_seamless                                                                  | 13185 | 10.73 |  -4.38 |  14.65 |
| best_match                                                                    | 13185 | 11.64 |  -3.75 |  14.80 |
| gfs_hrrr                                                                      | 13185 | 11.64 |  -3.75 |  14.80 |
| gfs_seamless                                                                  | 13185 | 11.64 |  -3.75 |  14.80 |
| meteofrance_seamless                                                          | 13185 | 11.83 |   2.75 |  14.73 |

### temp_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13185 |  3.03 |   1.50 |   4.08 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13185 |  3.06 |   1.07 |   3.99 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13185 |  3.07 |   1.51 |   4.19 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13185 |  3.09 |   1.35 |   4.17 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13185 |  3.11 |   1.29 |   4.13 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13185 |  3.13 |   1.36 |   4.22 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13185 |  3.15 |   1.53 |   4.28 |
| ncep_nbm_conus                                                                | 13048 |  3.16 |   0.38 |   3.98 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13185 |  3.18 |   1.02 |   4.16 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13185 |  3.22 |   1.12 |   4.30 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13185 |  3.25 |   1.60 |   4.37 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13185 |  3.28 |   0.66 |   4.20 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13185 |  3.29 |   1.81 |   4.50 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13185 |  3.30 |   1.80 |   4.41 |
| metno_seamless                                                                | 13185 |  3.35 |   1.74 |   4.59 |
| knmi_seamless                                                                 | 13185 |  3.35 |   1.74 |   4.59 |
| gfs_hrrr                                                                      | 13185 |  3.36 |   1.81 |   4.47 |
| gfs_seamless                                                                  | 13185 |  3.36 |   1.81 |   4.47 |
| best_match                                                                    | 13185 |  3.36 |   1.81 |   4.47 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13185 |  3.46 |   2.28 |   4.86 |
| jma_seamless                                                                  | 13185 |  3.58 |   0.50 |   4.75 |
| gem_seamless                                                                  | 13185 |  3.68 |   1.84 |   5.28 |
| ukmo_seamless                                                                 | 13185 |  3.74 |   0.94 |   4.89 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13185 |  3.85 |   2.59 |   5.53 |
| ecmwf_ifs025                                                                  | 13185 |  3.99 |   2.22 |   5.57 |
| icon_seamless                                                                 | 13185 |  4.11 |   3.20 |   5.70 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13185 |  4.22 |   2.96 |   5.96 |
| ecmwf_aifs025_single                                                          | 13185 |  4.68 |   3.71 |   6.54 |
| meteofrance_seamless                                                          | 13185 |  6.28 |   5.91 |   8.14 |

### wind_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| ncep_nbm_conus                                                                | 12942 |  2.15 |   0.08 |   3.20 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13076 |  2.31 |   0.15 |   3.03 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13076 |  2.33 |   0.50 |   3.01 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13076 |  2.37 |   0.41 |   3.00 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13076 |  2.39 |   0.51 |   2.97 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 13076 |  2.40 |   0.78 |   3.12 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13076 |  2.43 |   0.48 |   3.12 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13076 |  2.45 |   0.59 |   3.04 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13076 |  2.49 |   0.90 |   3.05 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 13076 |  2.50 |   0.81 |   3.12 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13076 |  2.50 |   0.73 |   3.04 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 13076 |  2.51 |   1.01 |   3.18 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13076 |  2.54 |   1.10 |   3.09 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13076 |  2.54 |   0.96 |   3.12 |
| icon_seamless                                                                 | 13076 |  2.62 |   0.91 |   3.20 |
| gem_seamless                                                                  | 13076 |  2.64 |   0.22 |   3.33 |
| jma_seamless                                                                  | 13076 |  2.68 |   0.25 |   3.33 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13076 |  2.71 |   1.38 |   3.24 |
| metno_seamless                                                                | 13076 |  2.79 |   1.47 |   3.45 |
| knmi_seamless                                                                 | 13076 |  2.79 |   1.47 |   3.45 |
| gfs_hrrr                                                                      | 13076 |  2.80 |   1.23 |   3.43 |
| gfs_seamless                                                                  | 13076 |  2.80 |   1.23 |   3.43 |
| best_match                                                                    | 13076 |  2.80 |   1.23 |   3.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13076 |  2.80 |   1.48 |   3.43 |
| ukmo_seamless                                                                 | 13076 |  2.85 |   0.87 |   3.49 |
| ecmwf_aifs025_single                                                          | 13076 |  2.96 |   1.63 |   3.67 |
| meteofrance_seamless                                                          | 13076 |  3.10 |  -0.68 |   3.95 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13076 |  3.12 |   2.12 |   3.85 |
| ecmwf_ifs025                                                                  | 13076 |  3.38 |   2.60 |   4.19 |

## Regional MAE by season (temperature)

| candidate                                                                     |   fall |   spring |   summer |   winter |
|:------------------------------------------------------------------------------|-------:|---------:|---------:|---------:|
| best_match                                                                    |   3.38 |     3.05 |     3.51 |     3.54 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       |   4.32 |     3.67 |     4.34 |     4.74 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          |   3.96 |     3.34 |     3.95 |     4.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    |   3.58 |     3.02 |     3.61 |     3.75 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         |   3.24 |     2.85 |     3.28 |     3.16 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   |   3.20 |     2.72 |     3.21 |     3.18 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                |   3.19 |     2.87 |     3.16 |     3.17 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   |   3.21 |     3.02 |     3.11 |     3.38 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               |   3.35 |     3.04 |     3.25 |     3.68 |
| blend:gem_seamless+ncep_nbm_conus                                             |   3.40 |     3.04 |     3.17 |     3.32 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       |   3.14 |     2.70 |     3.23 |     3.06 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless |   3.36 |     2.93 |     3.36 |     3.44 |
| blend:icon_seamless+ncep_nbm_conus                                            |   3.31 |     3.17 |     3.21 |     3.71 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             |   3.26 |     2.79 |     3.24 |     3.16 |
| blend:knmi_seamless+ncep_nbm_conus                                            |   3.23 |     2.81 |     3.14 |     3.05 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              |   3.37 |     2.92 |     3.31 |     3.09 |
| blend:ncep_nbm_conus+ukmo_seamless                                            |   3.49 |     3.13 |     3.33 |     3.11 |
| ecmwf_aifs025_single                                                          |   4.73 |     4.07 |     4.94 |     5.14 |
| ecmwf_ifs025                                                                  |   4.15 |     3.54 |     3.96 |     4.56 |
| gem_seamless                                                                  |   3.75 |     3.44 |     3.64 |     4.06 |
| gfs_hrrr                                                                      |   3.38 |     3.05 |     3.51 |     3.54 |
| gfs_seamless                                                                  |   3.38 |     3.05 |     3.51 |     3.54 |
| icon_seamless                                                                 |   4.01 |     3.90 |     3.85 |     5.16 |
| jma_seamless                                                                  |   3.30 |     3.92 |     3.28 |     4.02 |
| knmi_seamless                                                                 |   3.48 |     2.88 |     3.55 |     3.57 |
| meteofrance_seamless                                                          |   6.64 |     5.21 |     6.08 |     7.95 |
| metno_seamless                                                                |   3.48 |     2.88 |     3.55 |     3.57 |
| ncep_nbm_conus                                                                |   3.38 |     3.12 |     3.09 |     3.07 |
| ukmo_seamless                                                                 |   3.98 |     3.46 |     3.92 |     3.49 |

## MAE by lead time, days 1-7 (previous-runs, site)

### gust_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 6.69 |   3.46 |   3.55 |   3.73 |   3.97 |   4.48 |   4.62 |
| gem_seamless         | 4.07 |   3.95 |   4.12 |   3.95 |   4.12 |   4.57 |   5.01 |
| gfs_hrrr             | 6.69 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 6.69 |   3.46 |   3.55 |   3.73 |   3.97 |   4.48 |   4.62 |
| icon_seamless        | 5.48 |   5.49 |   5.60 |   5.79 |   5.73 |   5.66 | nan    |
| meteofrance_seamless | 5.79 |   5.61 |   5.71 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.36 |   3.50 |   3.57 |   3.61 |   3.66 |   3.76 |   3.78 |
| ukmo_seamless        | 4.40 |   4.70 |   4.36 |   4.59 |   4.68 |   4.52 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 12.65 |  10.05 |  11.25 |  12.00 |  11.88 |  13.75 |  13.56 |
| ecmwf_aifs025_single |  6.75 |   7.22 |   7.85 |   8.18 |   9.36 |   9.28 |  10.07 |
| ecmwf_ifs025         |  7.93 |   8.43 |   9.31 |   9.85 |  10.92 |  11.12 |  11.17 |
| gem_seamless         |  9.80 |  10.55 |  10.36 |  10.86 |  11.83 |  12.59 |  13.30 |
| gfs_hrrr             | 12.65 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 12.65 |  10.05 |  11.25 |  12.00 |  11.88 |  13.75 |  13.56 |
| icon_seamless        |  8.49 |   8.59 |   8.92 |   9.79 |  10.82 |  11.59 | nan    |
| jma_seamless         | 10.99 |  11.08 |  12.24 |  12.52 |  13.27 |  14.49 |  15.63 |
| knmi_seamless        |  8.55 |   8.94 |   9.52 |  10.07 |  11.10 |  11.26 |  11.45 |
| meteofrance_seamless | 10.15 |  10.77 |  11.00 | nan    | nan    | nan    | nan    |
| metno_seamless       |  8.55 |   8.94 |   9.52 |  10.07 |  11.10 |  11.26 |  11.45 |
| ncep_nbm_conus       |  9.13 |   9.37 |   9.60 |  10.15 |  10.57 |  10.78 |  11.15 |
| ukmo_seamless        | 10.63 |  11.01 |  11.79 |  11.44 |  12.83 |  12.73 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 3.54 |   4.63 |   4.78 |   5.12 |   5.26 |   5.73 |   5.75 |
| ecmwf_aifs025_single | 3.36 |   3.51 |   3.66 |   3.78 |   3.99 |   4.11 |   4.10 |
| ecmwf_ifs025         | 3.34 |   3.48 |   3.64 |   4.06 |   4.14 |   4.50 |   4.51 |
| gem_seamless         | 3.69 |   4.47 |   4.06 |   4.56 |   4.75 |   4.92 |   5.26 |
| gfs_hrrr             | 3.54 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 3.54 |   4.63 |   4.78 |   5.12 |   5.26 |   5.73 |   5.75 |
| icon_seamless        | 3.93 |   4.06 |   4.26 |   4.30 |   4.56 |   5.01 | nan    |
| jma_seamless         | 4.62 |   4.86 |   4.86 |   5.06 |   5.31 |   5.85 |   5.87 |
| knmi_seamless        | 3.46 |   3.58 |   3.78 |   4.14 |   4.17 |   4.56 |   4.61 |
| meteofrance_seamless | 4.17 |   4.24 |   4.58 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.46 |   3.58 |   3.78 |   4.14 |   4.17 |   4.56 |   4.61 |
| ncep_nbm_conus       | 3.88 |   4.02 |   4.02 |   4.11 |   4.30 |   4.37 |   4.36 |
| ukmo_seamless        | 3.99 |   4.21 |   4.31 |   4.26 |   4.41 |   4.61 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.51 |   2.63 |   2.47 |   2.50 |   2.43 |   2.44 |   2.35 |
| ecmwf_aifs025_single | 3.05 |   3.03 |   3.07 |   3.16 |   3.18 |   3.14 |   3.10 |
| ecmwf_ifs025         | 3.42 |   3.48 |   3.28 |   3.42 |   3.52 |   3.10 |   3.10 |
| gem_seamless         | 2.53 |   2.10 |   1.85 |   1.80 |   1.84 |   1.78 |   1.91 |
| gfs_hrrr             | 4.51 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.51 |   2.63 |   2.47 |   2.50 |   2.43 |   2.44 |   2.35 |
| icon_seamless        | 2.64 |   2.67 |   2.71 |   2.67 |   2.61 |   2.54 | nan    |
| jma_seamless         | 2.00 |   2.09 |   2.15 |   2.08 |   2.27 |   2.12 |   2.02 |
| knmi_seamless        | 3.06 |   3.18 |   3.00 |   3.14 |   3.27 |   2.88 |   2.96 |
| meteofrance_seamless | 1.57 |   1.55 |   1.57 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.06 |   3.18 |   3.00 |   3.14 |   3.27 |   2.88 |   2.96 |
| ncep_nbm_conus       | 2.53 |   2.51 |   2.47 |   2.38 |   2.14 |   2.07 |   1.97 |
| ukmo_seamless        | 2.77 |   2.90 |   2.66 |   2.75 |   2.65 |   2.60 | nan    |
