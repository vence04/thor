# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-10-17.
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
| ncep_nbm_conus                                                                | 1768 |  2.35 |   0.64 |   0.97 | bias               |            1.50 |      531.00 |                   1.59 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1768 |  2.14 |  -0.24 |   0.98 | ridge              |            1.65 |      531.00 |                   1.94 |
| ecmwf_ifs025                                                                  | 1768 |  2.67 |  -0.62 |   0.97 | bias               |            1.72 |      531.00 |                   1.76 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  2.20 |  -0.26 |   0.98 | ridge              |            1.75 |      531.00 |                   2.14 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1768 |  2.06 |  -0.15 |   0.98 | ridge              |            1.75 |      531.00 |                   2.17 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1768 |  2.17 |  -0.24 |   0.98 | ridge              |            1.76 |      531.00 |                   2.19 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1768 |  2.35 |  -0.13 |   0.98 | ridge              |            1.79 |      531.00 |                   2.14 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1768 |  2.61 |   0.20 |   0.96 | ridge              |            1.79 |      531.00 |                   2.04 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1768 |  2.21 |  -0.07 |   0.98 | ridge              |            1.80 |      531.00 |                   2.16 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1768 |  2.48 |   0.09 |   0.97 | ridge              |            1.80 |      531.00 |                   2.13 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  2.13 |  -0.15 |   0.98 | ridge              |            1.86 |      531.00 |                   2.31 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1768 |  2.22 |   0.04 |   0.98 | ridge              |            1.86 |      531.00 |                   2.36 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1768 |  2.15 |  -0.14 |   0.98 | ridge              |            1.92 |      531.00 |                   2.32 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1768 |  2.31 |   0.24 |   0.98 | ridge              |            2.01 |      531.00 |                   2.51 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1768 |  2.31 |   0.24 |   0.98 | ridge              |            2.01 |      531.00 |                   2.51 |
| icon_seamless                                                                 | 1768 |  2.52 |  -0.78 |   0.97 | ridge              |            2.02 |      531.00 |                   2.38 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1768 |  2.39 |   0.11 |   0.98 | ridge              |            2.12 |      531.00 |                   2.64 |
| ecmwf_aifs025_single                                                          | 1768 |  2.50 |  -0.51 |   0.97 | ridge              |            2.26 |      531.00 |                   2.78 |
| gem_seamless                                                                  | 1768 |  2.65 |  -0.56 |   0.97 | ridge              |            2.35 |      531.00 |                   3.02 |
| metno_seamless                                                                | 1768 |  2.65 |  -0.15 |   0.97 | ridge              |            2.42 |      531.00 |                   3.00 |
| knmi_seamless                                                                 | 1768 |  2.65 |  -0.15 |   0.97 | ridge              |            2.42 |      531.00 |                   3.00 |
| ukmo_seamless                                                                 | 1768 |  3.39 |  -0.23 |   0.92 | ridge              |            2.46 |      531.00 |                   2.79 |
| best_match                                                                    | 1768 |  2.90 |  -0.53 |   0.96 | ridge              |            2.47 |      531.00 |                   2.86 |
| gfs_seamless                                                                  | 1768 |  2.90 |  -0.53 |   0.96 | ridge              |            2.47 |      531.00 |                   2.86 |
| gfs_hrrr                                                                      | 1768 |  2.90 |  -0.53 |   0.96 | ridge              |            2.47 |      531.00 |                   2.86 |
| jma_seamless                                                                  | 1768 |  2.89 |  -0.47 |   0.93 | ridge              |            2.64 |      531.00 |                   3.12 |
| meteofrance_seamless                                                          | 1768 |  3.08 |  -0.17 |   0.94 | bias               |            2.71 |      531.00 |                   2.32 |

### gust_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  4.51 |   4.03 |   0.86 | ridge              |            1.98 |      531.00 |                   2.07 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  4.36 |   3.86 |   0.86 | ridge              |            2.02 |      531.00 |                   2.09 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1768 |  4.86 |   4.54 |   0.85 | ridge              |            2.05 |      531.00 |                   2.15 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1768 |  4.32 |   3.86 |   0.85 | ridge              |            2.05 |      531.00 |                   2.16 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1768 |  4.67 |   4.26 |   0.85 | ridge              |            2.08 |      531.00 |                   2.17 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1768 |  4.67 |   4.26 |   0.85 | ridge              |            2.08 |      531.00 |                   2.17 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1768 |  5.14 |   4.84 |   0.84 | ridge              |            2.09 |      531.00 |                   2.19 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1768 |  4.90 |   4.45 |   0.84 | ridge              |            2.12 |      531.00 |                   2.20 |
| knmi_seamless                                                                 | 1768 |  6.18 |   5.99 |   0.82 | ridge              |            2.19 |      531.00 |                   2.30 |
| metno_seamless                                                                | 1768 |  6.18 |   5.99 |   0.82 | ridge              |            2.19 |      531.00 |                   2.30 |
| ecmwf_ifs025                                                                  | 1768 |  7.41 |   7.30 |   0.81 | ridge              |            2.36 |      531.00 |                   2.40 |
| icon_seamless                                                                 | 1768 |  5.57 |   5.14 |   0.80 | ridge              |            2.41 |      531.00 |                   2.41 |
| ukmo_seamless                                                                 | 1768 |  4.07 |   3.05 |   0.79 | ridge              |            2.45 |      531.00 |                   2.63 |
| best_match                                                                    | 1768 |  5.00 |   3.86 |   0.74 | ridge              |            2.55 |      531.00 |                   2.59 |
| gfs_hrrr                                                                      | 1768 |  5.00 |   3.86 |   0.74 | ridge              |            2.55 |      531.00 |                   2.59 |
| gfs_seamless                                                                  | 1768 |  5.00 |   3.86 |   0.74 | ridge              |            2.55 |      531.00 |                   2.59 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1768 |  3.66 |   2.79 |   0.84 | bias               |            2.63 |      531.00 |                   2.67 |
| ncep_nbm_conus                                                                | 1768 |  3.63 |   2.53 |   0.84 | bias               |            2.63 |      531.00 |                   2.68 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1768 |  3.39 |   2.16 |   0.86 | bias               |            2.65 |      531.00 |                   2.72 |
| meteofrance_seamless                                                          | 1768 |  5.83 |   5.50 |   0.71 | ridge              |            2.75 |      531.00 |                   2.93 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1768 |  3.93 |   3.15 |   0.86 | bias               |            2.89 |      531.00 |                   2.97 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1768 |  4.38 |   3.84 |   0.84 | bias               |            2.89 |      531.00 |                   2.84 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1768 |  3.77 |   2.72 |   0.84 | bias               |            3.05 |      531.00 |                   2.97 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1768 |  3.94 |   3.02 |   0.83 | bias               |            3.18 |      531.00 |                   3.03 |
| gem_seamless                                                                  | 1768 |  3.87 |   1.78 |   0.80 | bias               |            3.80 |      531.00 |                   4.03 |

### humidity_pct

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  5.87 |   1.11 |   0.95 | bias               |            4.52 |      531.00 |                   4.56 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1768 |  5.78 |   1.16 |   0.95 | bias               |            4.55 |      531.00 |                   4.44 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  6.77 |   2.48 |   0.93 | bias               |            5.21 |      531.00 |                   4.85 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1768 |  6.16 |   2.05 |   0.95 | bias               |            5.23 |      531.00 |                   5.09 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1768 |  7.05 |   2.55 |   0.92 | bias               |            5.24 |      531.00 |                   5.20 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1768 |  7.05 |   2.55 |   0.92 | bias               |            5.24 |      531.00 |                   5.20 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1768 |  6.90 |   2.21 |   0.93 | bias               |            5.27 |      531.00 |                   5.02 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1768 |  7.50 |   3.22 |   0.91 | bias               |            5.92 |      531.00 |                   5.74 |
| meteofrance_seamless                                                          | 1768 |  8.98 |  -5.09 |   0.92 | ridge              |            5.99 |      531.00 |                   6.53 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1768 |  6.07 |   1.80 |   0.94 | ridge              |            6.08 |      531.00 |                   6.19 |
| ncep_nbm_conus                                                                | 1768 |  8.46 |   5.04 |   0.91 | bias               |            6.12 |      531.00 |                   5.94 |
| ecmwf_aifs025_single                                                          | 1768 |  6.78 |   2.14 |   0.93 | ridge              |            6.15 |      531.00 |                   6.27 |
| ecmwf_ifs025                                                                  | 1768 |  6.85 |   0.60 |   0.93 | ridge              |            6.29 |      531.00 |                   6.17 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1768 |  6.79 |   2.14 |   0.94 | ridge              |            6.45 |      531.00 |                   6.46 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1768 |  6.90 |   1.72 |   0.92 | ridge              |            6.60 |      531.00 |                   6.49 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1768 |  7.32 |   3.18 |   0.93 | ridge              |            6.79 |      531.00 |                   6.56 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1768 |  7.12 |   2.55 |   0.92 | ridge              |            6.87 |      531.00 |                   7.10 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1768 |  8.51 |   4.79 |   0.90 | bias               |            6.87 |      531.00 |                   6.65 |
| metno_seamless                                                                | 1768 |  7.19 |   0.06 |   0.91 | ridge              |            7.00 |      531.00 |                   6.76 |
| knmi_seamless                                                                 | 1768 |  7.19 |   0.06 |   0.91 | ridge              |            7.00 |      531.00 |                   6.76 |
| best_match                                                                    | 1768 |  7.42 |   0.32 |   0.89 | ridge              |            7.38 |      531.00 |                   7.12 |
| gfs_hrrr                                                                      | 1768 |  7.42 |   0.32 |   0.89 | ridge              |            7.38 |      531.00 |                   7.12 |
| gfs_seamless                                                                  | 1768 |  7.42 |   0.32 |   0.89 | ridge              |            7.38 |      531.00 |                   7.12 |
| gem_seamless                                                                  | 1768 |  7.64 |   0.05 |   0.91 | ridge              |            7.52 |      531.00 |                   7.75 |
| icon_seamless                                                                 | 1768 |  7.55 |   1.32 |   0.91 | ridge              |            7.55 |      531.00 |                   7.14 |
| ukmo_seamless                                                                 | 1768 |  9.81 |   4.54 |   0.82 | ridge              |            9.58 |      531.00 |                   9.35 |
| jma_seamless                                                                  | 1768 | 10.35 |   5.93 |   0.82 | ridge              |            9.82 |      531.00 |                   9.35 |

### precip_in

| candidate                                                                     |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                    | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                  | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                      | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                 | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                          | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                 | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                             | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                            | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                  | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus                                            | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:metno_seamless+ncep_nbm_conus                                           | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                  | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                | 2182 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                 | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                  | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                          | 2182 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 9353 |  1.48 |  -0.61 |   0.93 | bias               |            1.04 |     2806.00 |                   0.40 |
| ecmwf_ifs025                                                                  | 9353 |  1.39 |  -0.48 |   0.93 | bias               |            1.05 |     2806.00 |                   0.40 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 9353 |  1.50 |  -0.63 |   0.93 | bias               |            1.06 |     2806.00 |                   0.44 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 9353 |  1.65 |  -0.81 |   0.93 | bias               |            1.06 |     2806.00 |                   0.42 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 9353 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2806.00 |                   0.40 |
| blend:metno_seamless+ncep_nbm_conus                                           | 9353 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2806.00 |                   0.40 |
| knmi_seamless                                                                 | 9353 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2806.00 |                   0.40 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 9353 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2806.00 |                   0.40 |
| metno_seamless                                                                | 9353 |  1.39 |  -0.48 |   0.93 | bias               |            1.06 |     2806.00 |                   0.40 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 9353 |  1.32 |  -0.42 |   0.93 | bias               |            1.08 |     2806.00 |                   0.46 |
| ecmwf_aifs025_single                                                          | 9353 |  1.41 |  -0.45 |   0.93 | bias               |            1.08 |     2806.00 |                   0.46 |
| meteofrance_seamless                                                          | 9353 |  1.31 |  -0.29 |   0.93 | bias               |            1.09 |     2806.00 |                   0.51 |
| blend:icon_seamless+ncep_nbm_conus                                            | 9353 |  1.31 |  -0.34 |   0.93 | bias               |            1.15 |     2806.00 |                   0.58 |
| icon_seamless                                                                 | 9353 |  1.31 |  -0.34 |   0.93 | bias               |            1.15 |     2806.00 |                   0.58 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 9353 |  1.26 |  -0.30 |   0.93 | bias               |            1.15 |     2806.00 |                   0.53 |
| jma_seamless                                                                  | 9353 |  1.51 |  -0.62 |   0.93 | bias               |            1.17 |     2806.00 |                   0.60 |
| gem_seamless                                                                  | 9353 |  1.24 |  -0.26 |   0.93 | bias               |            1.19 |     2806.00 |                   0.55 |
| blend:gem_seamless+ncep_nbm_conus                                             | 9353 |  1.24 |  -0.26 |   0.93 | bias               |            1.19 |     2806.00 |                   0.55 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 9353 |  1.64 |  -0.77 |   0.93 | raw                |            1.50 |     2806.00 |                   1.15 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 9353 |  1.74 |  -0.88 |   0.93 | raw                |            1.56 |     2806.00 |                   1.28 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 9353 |  1.83 |  -0.99 |   0.93 | raw                |            1.66 |     2806.00 |                   1.41 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 9353 |  1.95 |  -1.14 |   0.93 | raw                |            1.81 |     2806.00 |                   1.49 |
| ukmo_seamless                                                                 | 9353 |  1.95 |  -1.14 |   0.93 | raw                |            1.81 |     2806.00 |                   1.49 |
| best_match                                                                    | 9353 |  2.13 |  -1.29 |   0.92 | raw                |            1.85 |     2806.00 |                   1.88 |
| gfs_hrrr                                                                      | 9353 |  2.13 |  -1.29 |   0.92 | raw                |            1.85 |     2806.00 |                   1.88 |
| gfs_seamless                                                                  | 9353 |  2.13 |  -1.29 |   0.92 | raw                |            1.85 |     2806.00 |                   1.88 |

### temp_f

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ecmwf_ifs025                                                                  | 1768 |  3.11 |  -0.63 |   0.96 | ridge              |            2.09 |      531.00 |                   2.13 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1768 |  3.22 |  -0.76 |   0.95 | ridge              |            2.09 |      531.00 |                   2.18 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  3.08 |  -0.40 |   0.96 | ridge              |            2.10 |      531.00 |                   2.16 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1768 |  3.29 |  -0.98 |   0.95 | ridge              |            2.10 |      531.00 |                   2.12 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1768 |  3.12 |  -0.52 |   0.96 | ridge              |            2.14 |      531.00 |                   2.17 |
| ecmwf_aifs025_single                                                          | 1768 |  3.46 |  -1.24 |   0.94 | ridge              |            2.18 |      531.00 |                   2.15 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1768 |  3.31 |  -0.70 |   0.95 | ridge              |            2.20 |      531.00 |                   2.32 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1768 |  3.34 |  -0.92 |   0.95 | ridge              |            2.21 |      531.00 |                   2.22 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  3.35 |  -0.98 |   0.96 | ridge              |            2.24 |      531.00 |                   2.33 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1768 |  3.28 |  -0.75 |   0.95 | ridge              |            2.25 |      531.00 |                   2.27 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1768 |  3.22 |  -0.51 |   0.95 | ridge              |            2.26 |      531.00 |                   2.32 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1768 |  3.22 |  -0.51 |   0.95 | ridge              |            2.26 |      531.00 |                   2.32 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1768 |  3.16 |  -0.29 |   0.95 | ridge              |            2.26 |      531.00 |                   2.31 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1768 |  3.64 |  -1.46 |   0.94 | ridge              |            2.26 |      531.00 |                   2.27 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1768 |  3.35 |  -0.84 |   0.95 | ridge              |            2.27 |      531.00 |                   2.38 |
| meteofrance_seamless                                                          | 1768 |  3.61 |   2.25 |   0.93 | ridge              |            2.33 |      531.00 |                   2.39 |
| knmi_seamless                                                                 | 1768 |  3.15 |   0.14 |   0.95 | ridge              |            2.36 |      531.00 |                   2.41 |
| metno_seamless                                                                | 1768 |  3.15 |   0.14 |   0.95 | ridge              |            2.36 |      531.00 |                   2.41 |
| gfs_seamless                                                                  | 1768 |  3.34 |  -0.87 |   0.95 | ridge              |            2.37 |      531.00 |                   2.39 |
| best_match                                                                    | 1768 |  3.34 |  -0.87 |   0.95 | ridge              |            2.37 |      531.00 |                   2.39 |
| gfs_hrrr                                                                      | 1768 |  3.34 |  -0.87 |   0.95 | ridge              |            2.37 |      531.00 |                   2.39 |
| gem_seamless                                                                  | 1768 |  3.33 |  -0.24 |   0.94 | ridge              |            2.40 |      531.00 |                   2.55 |
| ncep_nbm_conus                                                                | 1768 |  3.62 |  -1.16 |   0.93 | ridge              |            2.44 |      531.00 |                   2.55 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1768 |  3.55 |  -1.13 |   0.95 | ridge              |            2.49 |      531.00 |                   2.59 |
| ukmo_seamless                                                                 | 1768 |  3.91 |  -1.75 |   0.92 | ridge              |            2.54 |      531.00 |                   2.45 |
| icon_seamless                                                                 | 1768 |  3.67 |  -1.10 |   0.94 | ridge              |            3.03 |      531.00 |                   3.21 |
| jma_seamless                                                                  | 1768 |  4.45 |  -2.56 |   0.92 | ridge              |            3.46 |      531.00 |                   3.73 |

### wind_mph

| candidate                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 1768 |  2.85 |   2.79 |   0.75 | ridge              |            0.75 |      531.00 |                   0.75 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  2.96 |   2.91 |   0.76 | ridge              |            0.76 |      531.00 |                   0.75 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 1768 |  2.62 |   2.57 |   0.75 | ridge              |            0.76 |      531.00 |                   0.76 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                             | 1768 |  3.04 |   2.97 |   0.75 | ridge              |            0.76 |      531.00 |                   0.77 |
| blend:metno_seamless+ncep_nbm_conus                                           | 1768 |  2.96 |   2.89 |   0.74 | ridge              |            0.76 |      531.00 |                   0.77 |
| blend:knmi_seamless+ncep_nbm_conus                                            | 1768 |  2.96 |   2.89 |   0.74 | ridge              |            0.76 |      531.00 |                   0.77 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 1768 |  3.15 |   3.11 |   0.74 | ridge              |            0.76 |      531.00 |                   0.75 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 1768 |  2.59 |   2.52 |   0.73 | ridge              |            0.76 |      531.00 |                   0.75 |
| blend:knmi_seamless+ncep_nbm_conus+ukmo_seamless                              | 1768 |  2.82 |   2.75 |   0.74 | ridge              |            0.77 |      531.00 |                   0.77 |
| blend:icon_seamless+ncep_nbm_conus                                            | 1768 |  2.68 |   2.62 |   0.72 | ridge              |            0.77 |      531.00 |                   0.77 |
| metno_seamless                                                                | 1768 |  3.20 |   3.13 |   0.75 | ridge              |            0.78 |      531.00 |                   0.78 |
| knmi_seamless                                                                 | 1768 |  3.20 |   3.13 |   0.75 | ridge              |            0.78 |      531.00 |                   0.78 |
| blend:gem_seamless+ncep_nbm_conus                                             | 1768 |  2.58 |   2.48 |   0.71 | ridge              |            0.79 |      531.00 |                   0.78 |
| blend:gem_seamless+gfs_hrrr+ncep_nbm_conus                                    | 1768 |  2.82 |   2.76 |   0.71 | ridge              |            0.79 |      531.00 |                   0.76 |
| icon_seamless                                                                 | 1768 |  2.67 |   2.60 |   0.72 | ridge              |            0.79 |      531.00 |                   0.78 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 1768 |  2.88 |   2.81 |   0.71 | ridge              |            0.80 |      531.00 |                   0.77 |
| ecmwf_ifs025                                                                  | 1768 |  3.54 |   3.49 |   0.76 | ridge              |            0.80 |      531.00 |                   0.79 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 1768 |  2.66 |   2.56 |   0.70 | ridge              |            0.80 |      531.00 |                   0.81 |
| ncep_nbm_conus                                                                | 1768 |  2.79 |   2.65 |   0.67 | ridge              |            0.82 |      531.00 |                   0.82 |
| gem_seamless                                                                  | 1768 |  2.44 |   2.31 |   0.69 | ridge              |            0.84 |      531.00 |                   0.83 |
| jma_seamless                                                                  | 1768 |  2.27 |   2.15 |   0.64 | ridge              |            0.88 |      531.00 |                   0.90 |
| ecmwf_aifs025_single                                                          | 1768 |  3.14 |   3.04 |   0.69 | ridge              |            0.88 |      531.00 |                   0.89 |
| best_match                                                                    | 1768 |  3.39 |   3.32 |   0.62 | ridge              |            0.88 |      531.00 |                   0.85 |
| gfs_hrrr                                                                      | 1768 |  3.39 |   3.32 |   0.62 | ridge              |            0.88 |      531.00 |                   0.85 |
| gfs_seamless                                                                  | 1768 |  3.39 |   3.32 |   0.62 | ridge              |            0.88 |      531.00 |                   0.85 |
| ukmo_seamless                                                                 | 1768 |  2.66 |   2.48 |   0.66 | ridge              |            0.89 |      531.00 |                   0.89 |
| meteofrance_seamless                                                          | 1768 |  1.58 |   1.25 |   0.62 | bias               |            1.13 |      531.00 |                   1.12 |

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
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13185 |  8.06 |  -2.86 |  10.62 |
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
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13185 |  3.15 |   1.54 |   4.28 |
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
| best_match           | 6.86 |   3.63 |   3.84 |   4.12 |   4.27 |   4.80 |   4.69 |
| gem_seamless         | 4.23 |   4.08 |   4.22 |   4.06 |   4.28 |   4.78 |   5.35 |
| gfs_hrrr             | 6.86 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 6.86 |   3.63 |   3.84 |   4.12 |   4.27 |   4.80 |   4.69 |
| icon_seamless        | 5.51 |   5.59 |   5.68 |   5.86 |   5.93 |   6.14 | nan    |
| meteofrance_seamless | 6.09 |   6.03 |   6.09 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.55 |   3.63 |   3.76 |   3.90 |   3.88 |   4.01 |   3.95 |
| ukmo_seamless        | 4.52 |   4.80 |   4.53 |   4.78 |   4.93 |   4.99 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 12.23 |   9.61 |  10.85 |  11.54 |  11.61 |  13.40 |  13.19 |
| ecmwf_aifs025_single |  6.58 |   7.02 |   7.65 |   7.94 |   9.04 |   9.01 |  10.27 |
| ecmwf_ifs025         |  7.72 |   8.22 |   9.00 |   9.50 |  10.54 |  10.87 |  11.71 |
| gem_seamless         |  9.36 |  10.22 |  10.02 |  10.49 |  11.50 |  12.54 |  13.10 |
| gfs_hrrr             | 12.23 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 12.23 |   9.61 |  10.85 |  11.54 |  11.61 |  13.40 |  13.19 |
| icon_seamless        |  8.22 |   8.42 |   8.82 |   9.62 |  10.75 |  11.65 | nan    |
| jma_seamless         | 10.76 |  10.80 |  11.86 |  12.21 |  12.75 |  14.18 |  15.60 |
| knmi_seamless        |  8.40 |   8.80 |   9.30 |   9.76 |  10.78 |  11.05 |  12.11 |
| meteofrance_seamless |  9.74 |  10.34 |  10.53 | nan    | nan    | nan    | nan    |
| metno_seamless       |  8.40 |   8.80 |   9.30 |   9.76 |  10.78 |  11.05 |  12.11 |
| ncep_nbm_conus       |  8.91 |   9.14 |   9.42 |   9.96 |  10.44 |  10.91 |  11.27 |
| ukmo_seamless        | 10.59 |  11.00 |  11.60 |  11.24 |  12.68 |  12.98 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 3.49 |   4.53 |   4.71 |   5.07 |   5.40 |   5.90 |   5.87 |
| ecmwf_aifs025_single | 3.29 |   3.43 |   3.62 |   3.76 |   4.02 |   4.27 |   4.39 |
| ecmwf_ifs025         | 3.29 |   3.44 |   3.63 |   4.08 |   4.20 |   4.68 |   4.85 |
| gem_seamless         | 3.62 |   4.40 |   4.09 |   4.57 |   4.91 |   5.13 |   5.58 |
| gfs_hrrr             | 3.49 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 3.49 |   4.53 |   4.71 |   5.07 |   5.40 |   5.90 |   5.87 |
| icon_seamless        | 3.80 |   3.99 |   4.17 |   4.26 |   4.69 |   5.06 | nan    |
| jma_seamless         | 4.54 |   4.73 |   4.81 |   5.10 |   5.29 |   5.92 |   6.00 |
| knmi_seamless        | 3.40 |   3.55 |   3.78 |   4.14 |   4.19 |   4.69 |   4.92 |
| meteofrance_seamless | 4.06 |   4.14 |   4.49 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.40 |   3.55 |   3.78 |   4.14 |   4.19 |   4.69 |   4.92 |
| ncep_nbm_conus       | 3.84 |   4.00 |   4.02 |   4.12 |   4.38 |   4.41 |   4.45 |
| ukmo_seamless        | 3.85 |   4.13 |   4.25 |   4.23 |   4.39 |   4.65 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.52 |   2.66 |   2.52 |   2.66 |   2.54 |   2.54 |   2.33 |
| ecmwf_aifs025_single | 3.21 |   3.18 |   3.20 |   3.28 |   3.28 |   3.32 |   3.23 |
| ecmwf_ifs025         | 3.55 |   3.58 |   3.36 |   3.52 |   3.63 |   3.27 |   3.26 |
| gem_seamless         | 2.56 |   2.14 |   1.91 |   1.86 |   1.90 |   1.87 |   2.04 |
| gfs_hrrr             | 4.52 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.52 |   2.66 |   2.52 |   2.66 |   2.54 |   2.54 |   2.33 |
| icon_seamless        | 2.67 |   2.72 |   2.76 |   2.72 |   2.69 |   2.77 | nan    |
| jma_seamless         | 2.14 |   2.22 |   2.24 |   2.21 |   2.34 |   2.15 |   1.99 |
| knmi_seamless        | 3.18 |   3.27 |   3.07 |   3.23 |   3.37 |   3.08 |   3.10 |
| meteofrance_seamless | 1.58 |   1.60 |   1.62 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.18 |   3.27 |   3.07 |   3.23 |   3.37 |   3.08 |   3.10 |
| ncep_nbm_conus       | 2.72 |   2.67 |   2.66 |   2.64 |   2.35 |   2.32 |   2.16 |
| ukmo_seamless        | 2.85 |   2.96 |   2.72 |   2.83 |   2.78 |   2.81 | nan    |
