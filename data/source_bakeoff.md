# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-11-15.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Source in use, per variable

| variable | source |
|---|---|
| dewpoint_f | blend of gem_seamless, gfs_seamless, ncep_nbm_conus |
| gust_mph | blend of gem_seamless, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| humidity_pct | blend of gfs_hrrr, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| precip_in | best_match |
| pressure_abs_hpa | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |
| temp_f | meteofrance_seamless |
| wind_mph | ecmwf_ifs025 |

## Site skill, shortlisted candidates (lower MAE = better)

### dewpoint_f

| candidate                                                                                                                                                                                                    |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                               | 523 |  1.29 |  -0.84 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                              | 523 |  1.33 |  -0.69 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                            | 523 |  1.34 |  -0.29 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                           | 523 |  1.37 |  -0.57 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                              | 523 |  1.41 |  -0.35 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                               | 523 |  1.44 |   0.36 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 523 |  1.45 |  -0.44 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                | 523 |  1.45 |  -0.80 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 523 |  1.47 |  -0.69 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 523 |  1.47 |  -0.69 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                        | 523 |  1.55 |  -0.80 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.019+gem_seamless=0.162+gfs_hrrr=0.031+gfs_seamless=0.031+icon_seamless=0.02+knmi_seamless=0.064+meteofrance_seamless=0.096+metno_seamless=0.064+ncep_nbm_conus=0.01+ukmo_seamless=0.115 | 523 |  1.58 |  -0.67 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                        | 523 |  1.61 |  -1.09 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 523 |  1.65 |  -0.90 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.01+gfs_seamless=0.01+icon_seamless=0.202+jma_seamless=0.022+knmi_seamless=0.048+metno_seamless=0.048+ncep_nbm_conus=0.031                                                                   | 523 |  1.71 |  -0.99 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                | 523 |  1.76 |  -0.60 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                             | 523 |  1.78 |  -0.70 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                   | 523 |  1.80 |  -1.18 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                 | 523 |  1.89 |  -0.94 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                                                                                                                                                         | 523 |  2.02 |  -0.93 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                           | 523 |  2.05 |  -0.30 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                | 523 |  2.09 |  -1.50 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                | 523 |  2.19 |  -0.46 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                 | 523 |  2.21 |  -0.75 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                 | 523 |  2.51 |   0.36 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                                                         | 523 |  2.61 |   0.79 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                                                                   | 523 |  2.68 |  -1.95 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                 | 523 |  2.68 |  -1.95 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                     | 523 |  2.68 |  -1.95 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                | 523 |  3.24 |  -0.95 |    nan |                nan |             nan |         nan |                    nan |

### gust_mph

| candidate                                                                                                                                                                                                    |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ecmwf_ifs025                                                                                                                                                                                                 | 2327 |  7.29 |   7.19 |   0.80 | ridge              |            1.93 |      698.00 |                   1.90 |
| knmi_seamless                                                                                                                                                                                                | 2327 |  6.01 |   5.82 |   0.78 | ridge              |            1.96 |      698.00 |                   1.97 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                        | 2327 |  4.89 |   4.62 |   0.78 | ridge              |            1.96 |      698.00 |                   1.96 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 2327 |  4.42 |   3.97 |   0.78 | ridge              |            1.97 |      698.00 |                   1.98 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 2327 |  4.42 |   3.97 |   0.78 | ridge              |            1.97 |      698.00 |                   1.98 |
| stack:gfs_hrrr=0.01+gfs_seamless=0.01+icon_seamless=0.202+jma_seamless=0.022+knmi_seamless=0.048+metno_seamless=0.048+ncep_nbm_conus=0.031                                                                   | 2327 |  5.14 |   4.85 |   0.79 | ridge              |            1.98 |      698.00 |                   2.00 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                              | 2327 |  3.93 |   3.32 |   0.78 | ridge              |            1.99 |      698.00 |                   2.01 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 2327 |  4.20 |   3.70 |   0.79 | ridge              |            2.00 |      698.00 |                   2.01 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 2327 |  4.85 |   4.44 |   0.76 | ridge              |            2.01 |      698.00 |                   2.04 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                | 2327 |  4.71 |   4.39 |   0.78 | ridge              |            2.03 |      698.00 |                   2.05 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                           | 2327 |  4.21 |   3.65 |   0.77 | ridge              |            2.03 |      698.00 |                   2.04 |
| stack:ecmwf_ifs025=0.019+gem_seamless=0.162+gfs_hrrr=0.031+gfs_seamless=0.031+icon_seamless=0.02+knmi_seamless=0.064+meteofrance_seamless=0.096+metno_seamless=0.064+ncep_nbm_conus=0.01+ukmo_seamless=0.115 | 2327 |  4.28 |   3.87 |   0.78 | ridge              |            2.03 |      698.00 |                   2.06 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                              | 2327 |  3.80 |   3.00 |   0.77 | ridge              |            2.08 |      698.00 |                   2.10 |
| icon_seamless                                                                                                                                                                                                | 2327 |  5.31 |   4.84 |   0.76 | ridge              |            2.08 |      698.00 |                   2.15 |
| ncep_nbm_conus                                                                                                                                                                                               | 2327 |  3.53 |   2.46 |   0.74 | ridge              |            2.12 |      698.00 |                   2.03 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                               | 2327 |  3.74 |   2.73 |   0.74 | ridge              |            2.12 |      698.00 |                   2.14 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                            | 2327 |  3.32 |   2.07 |   0.75 | ridge              |            2.12 |      698.00 |                   2.13 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                             | 2327 |  4.07 |   3.44 |   0.75 | ridge              |            2.16 |      698.00 |                   2.22 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                        | 2327 |  3.94 |   3.05 |   0.73 | ridge              |            2.17 |      698.00 |                   2.26 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                | 2327 |  4.16 |   3.25 |   0.71 | ridge              |            2.18 |      698.00 |                   2.19 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                   | 2327 |  4.45 |   3.52 |   0.70 | ridge              |            2.23 |      698.00 |                   2.29 |
| meteofrance_seamless                                                                                                                                                                                         | 2327 |  5.50 |   5.14 |   0.67 | ridge              |            2.23 |      698.00 |                   2.05 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                           | 2327 |  3.65 |   2.73 |   0.72 | ridge              |            2.25 |      698.00 |                   2.34 |
| best_match                                                                                                                                                                                                   | 2327 |  5.08 |   4.05 |   0.66 | ridge              |            2.33 |      698.00 |                   2.47 |
| gfs_hrrr                                                                                                                                                                                                     | 2327 |  5.08 |   4.05 |   0.66 | ridge              |            2.33 |      698.00 |                   2.47 |
| gfs_seamless                                                                                                                                                                                                 | 2327 |  5.08 |   4.05 |   0.66 | ridge              |            2.33 |      698.00 |                   2.47 |
| gem_seamless                                                                                                                                                                                                 | 2327 |  3.83 |   1.69 |   0.69 | ridge              |            2.34 |      698.00 |                   2.37 |
| ukmo_seamless                                                                                                                                                                                                | 2327 |  4.12 |   3.01 |   0.65 | ridge              |            2.49 |      698.00 |                   2.69 |

### humidity_pct

| candidate                                                                                                                                                                                                    |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 523 |  6.41 |   4.02 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 523 |  6.92 |   4.61 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 523 |  6.92 |   4.61 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                        | 523 |  7.13 |   4.84 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                   | 523 |  7.13 |   4.29 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                               | 523 |  7.48 |   5.28 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                                                                   | 523 |  7.48 |   1.62 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                                                                                                                                                         | 523 |  7.48 |   5.09 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                     | 523 |  7.48 |   1.62 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                 | 523 |  7.48 |   1.62 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.019+gem_seamless=0.162+gfs_hrrr=0.031+gfs_seamless=0.031+icon_seamless=0.02+knmi_seamless=0.064+meteofrance_seamless=0.096+metno_seamless=0.064+ncep_nbm_conus=0.01+ukmo_seamless=0.115 | 523 |  7.49 |   4.54 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                | 523 |  7.67 |   3.61 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                | 523 |  7.71 |   5.62 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                 | 523 |  7.72 |   3.87 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                        | 523 |  7.75 |   4.93 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                              | 523 |  8.25 |   5.95 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                | 523 |  8.62 |   6.12 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.01+gfs_seamless=0.01+icon_seamless=0.202+jma_seamless=0.022+knmi_seamless=0.048+metno_seamless=0.048+ncep_nbm_conus=0.031                                                                   | 523 |  8.64 |   6.10 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                                                         | 523 |  8.96 |   3.53 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                              | 523 |  9.26 |   6.92 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                            | 523 |  9.37 |   7.12 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                 | 523 |  9.45 |   4.61 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 523 |  9.67 |   7.27 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                           | 523 | 10.01 |   8.08 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                | 523 | 10.09 |   6.54 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                             | 523 | 10.27 |   7.79 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                           | 523 | 10.87 |   8.41 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                               | 523 | 11.18 |   9.62 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                | 523 | 13.05 |   7.20 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                 | 523 | 15.52 |  11.99 |    nan |                nan |             nan |         nan |                    nan |

### precip_in

| candidate                                                                                                                                                                                                    |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                                                                                                                                                   | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                 | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                     | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                        | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                   | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.019+gem_seamless=0.162+gfs_hrrr=0.031+gfs_seamless=0.031+icon_seamless=0.02+knmi_seamless=0.064+meteofrance_seamless=0.096+metno_seamless=0.064+ncep_nbm_conus=0.01+ukmo_seamless=0.115 | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                        | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                               | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                             | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                              | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.01+gfs_seamless=0.01+icon_seamless=0.202+jma_seamless=0.022+knmi_seamless=0.048+metno_seamless=0.048+ncep_nbm_conus=0.031                                                                   | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                | 2740 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                              | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                           | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                                                         | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                            | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                 | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                           | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                 | 2740 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                               | 2740 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                | 2740 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                 | 2740 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                                                                                                                                                         | 2740 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                                                                                                                                                    |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                | 9912 |  1.45 |  -0.63 |   0.95 | bias               |            1.02 |     2974.00 |                   0.34 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                        | 9912 |  1.48 |  -0.66 |   0.95 | bias               |            1.02 |     2974.00 |                   0.31 |
| stack:ecmwf_ifs025=0.019+gem_seamless=0.162+gfs_hrrr=0.031+gfs_seamless=0.031+icon_seamless=0.02+knmi_seamless=0.064+meteofrance_seamless=0.096+metno_seamless=0.064+ncep_nbm_conus=0.01+ukmo_seamless=0.115 | 9912 |  1.44 |  -0.61 |   0.95 | bias               |            1.03 |     2974.00 |                   0.31 |
| ecmwf_ifs025                                                                                                                                                                                                 | 9912 |  1.36 |  -0.49 |   0.95 | bias               |            1.03 |     2974.00 |                   0.31 |
| knmi_seamless                                                                                                                                                                                                | 9912 |  1.36 |  -0.49 |   0.95 | bias               |            1.04 |     2974.00 |                   0.36 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                             | 9912 |  1.57 |  -0.76 |   0.95 | bias               |            1.04 |     2974.00 |                   0.37 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 9912 |  1.47 |  -0.64 |   0.95 | bias               |            1.04 |     2974.00 |                   0.32 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 9912 |  1.47 |  -0.64 |   0.95 | bias               |            1.04 |     2974.00 |                   0.32 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 9912 |  1.29 |  -0.44 |   0.95 | bias               |            1.04 |     2974.00 |                   0.35 |
| stack:gfs_hrrr=0.01+gfs_seamless=0.01+icon_seamless=0.202+jma_seamless=0.022+knmi_seamless=0.048+metno_seamless=0.048+ncep_nbm_conus=0.031                                                                   | 9912 |  1.33 |  -0.47 |   0.95 | bias               |            1.05 |     2974.00 |                   0.35 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                              | 9912 |  1.26 |  -0.38 |   0.95 | bias               |            1.06 |     2974.00 |                   0.35 |
| ecmwf_aifs025_single                                                                                                                                                                                         | 9912 |  1.38 |  -0.47 |   0.95 | bias               |            1.06 |     2974.00 |                   0.35 |
| meteofrance_seamless                                                                                                                                                                                         | 9912 |  1.28 |  -0.31 |   0.95 | bias               |            1.08 |     2974.00 |                   0.34 |
| jma_seamless                                                                                                                                                                                                 | 9912 |  1.47 |  -0.62 |   0.95 | bias               |            1.10 |     2974.00 |                   0.39 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                              | 9912 |  1.23 |  -0.32 |   0.95 | bias               |            1.12 |     2974.00 |                   0.41 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                           | 9912 |  1.28 |  -0.36 |   0.95 | bias               |            1.13 |     2974.00 |                   0.42 |
| icon_seamless                                                                                                                                                                                                | 9912 |  1.28 |  -0.36 |   0.95 | bias               |            1.13 |     2974.00 |                   0.42 |
| gem_seamless                                                                                                                                                                                                 | 9912 |  1.21 |  -0.28 |   0.95 | bias               |            1.15 |     2974.00 |                   0.41 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                            | 9912 |  1.21 |  -0.28 |   0.95 | bias               |            1.15 |     2974.00 |                   0.41 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                               | 9912 |  1.61 |  -0.80 |   0.94 | raw                |            1.57 |     2974.00 |                   0.81 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 9912 |  1.71 |  -0.91 |   0.94 | raw                |            1.63 |     2974.00 |                   0.90 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                        | 9912 |  1.81 |  -1.02 |   0.94 | raw                |            1.74 |     2974.00 |                   0.98 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                           | 9912 |  1.92 |  -1.16 |   0.94 | raw                |            1.86 |     2974.00 |                   1.14 |
| ukmo_seamless                                                                                                                                                                                                | 9912 |  1.92 |  -1.16 |   0.94 | raw                |            1.86 |     2974.00 |                   1.14 |
| gfs_hrrr                                                                                                                                                                                                     | 9912 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2974.00 |                   1.21 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                | 9912 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2974.00 |                   1.21 |
| best_match                                                                                                                                                                                                   | 9912 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2974.00 |                   1.21 |
| gfs_seamless                                                                                                                                                                                                 | 9912 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2974.00 |                   1.21 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                   | 9912 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2974.00 |                   1.21 |

### temp_f

| candidate                                                                                                                                                                                                    |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| meteofrance_seamless                                                                                                                                                                                         | 523 |  2.48 |  -0.62 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                 | 523 |  2.79 |  -2.24 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                | 523 |  2.95 |  -1.93 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_aifs025_single                                                                                                                                                                                         | 523 |  3.12 |  -2.85 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 523 |  3.16 |  -2.59 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 523 |  3.16 |  -2.59 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 523 |  3.19 |  -2.67 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.019+gem_seamless=0.162+gfs_hrrr=0.031+gfs_seamless=0.031+icon_seamless=0.02+knmi_seamless=0.064+meteofrance_seamless=0.096+metno_seamless=0.064+ncep_nbm_conus=0.01+ukmo_seamless=0.115 | 523 |  3.20 |  -2.54 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                        | 523 |  3.21 |  -2.78 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                              | 523 |  3.22 |  -2.66 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                               | 523 |  3.46 |  -3.04 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                            | 523 |  3.51 |  -3.03 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                | 523 |  3.52 |  -3.08 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                   | 523 |  3.54 |  -3.17 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                | 523 |  3.57 |  -3.23 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 523 |  3.62 |  -3.22 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                 | 523 |  3.62 |  -2.65 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                        | 523 |  3.65 |  -3.25 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                 | 523 |  3.65 |  -3.05 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                                                                   | 523 |  3.65 |  -3.05 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                     | 523 |  3.65 |  -3.05 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                              | 523 |  3.78 |  -3.36 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.01+gfs_seamless=0.01+icon_seamless=0.202+jma_seamless=0.022+knmi_seamless=0.048+metno_seamless=0.048+ncep_nbm_conus=0.031                                                                   | 523 |  3.83 |  -3.38 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                               | 523 |  3.84 |  -3.41 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                           | 523 |  4.03 |  -3.76 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                           | 523 |  4.07 |  -3.72 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                             | 523 |  4.12 |  -3.85 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                 | 523 |  4.44 |  -4.11 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                | 523 |  4.47 |  -4.02 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                | 523 |  4.68 |  -4.10 |    nan |                nan |             nan |         nan |                    nan |

### wind_mph

| candidate                                                                                                                                                                                                    |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ecmwf_ifs025                                                                                                                                                                                                 | 2327 |  3.49 |   3.44 |   0.64 | ridge              |            0.72 |      698.00 |                   0.75 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 2327 |  3.08 |   3.04 |   0.62 | ridge              |            0.73 |      698.00 |                   0.72 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                        | 2327 |  2.73 |   2.69 |   0.63 | ridge              |            0.74 |      698.00 |                   0.74 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 2327 |  2.89 |   2.84 |   0.61 | ridge              |            0.74 |      698.00 |                   0.74 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                      | 2327 |  2.89 |   2.84 |   0.61 | ridge              |            0.74 |      698.00 |                   0.74 |
| knmi_seamless                                                                                                                                                                                                | 2327 |  3.16 |   3.08 |   0.64 | ridge              |            0.75 |      698.00 |                   0.77 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                   | 2327 |  3.07 |   3.01 |   0.56 | ridge              |            0.75 |      698.00 |                   0.73 |
| best_match                                                                                                                                                                                                   | 2327 |  3.31 |   3.23 |   0.54 | ridge              |            0.75 |      698.00 |                   0.75 |
| gfs_hrrr                                                                                                                                                                                                     | 2327 |  3.31 |   3.23 |   0.54 | ridge              |            0.75 |      698.00 |                   0.75 |
| gfs_seamless                                                                                                                                                                                                 | 2327 |  3.31 |   3.23 |   0.54 | ridge              |            0.75 |      698.00 |                   0.75 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                | 2327 |  2.96 |   2.90 |   0.55 | ridge              |            0.76 |      698.00 |                   0.74 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                               | 2327 |  2.75 |   2.68 |   0.55 | ridge              |            0.77 |      698.00 |                   0.75 |
| stack:ecmwf_ifs025=0.019+gem_seamless=0.162+gfs_hrrr=0.031+gfs_seamless=0.031+icon_seamless=0.02+knmi_seamless=0.064+meteofrance_seamless=0.096+metno_seamless=0.064+ncep_nbm_conus=0.01+ukmo_seamless=0.115 | 2327 |  2.52 |   2.45 |   0.59 | ridge              |            0.77 |      698.00 |                   0.78 |
| stack:gfs_hrrr=0.01+gfs_seamless=0.01+icon_seamless=0.202+jma_seamless=0.022+knmi_seamless=0.048+metno_seamless=0.048+ncep_nbm_conus=0.031                                                                   | 2327 |  2.73 |   2.69 |   0.62 | ridge              |            0.77 |      698.00 |                   0.78 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                        | 2327 |  2.81 |   2.75 |   0.55 | ridge              |            0.77 |      698.00 |                   0.77 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                  | 2327 |  2.56 |   2.50 |   0.59 | ridge              |            0.78 |      698.00 |                   0.79 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                              | 2327 |  2.71 |   2.63 |   0.58 | ridge              |            0.78 |      698.00 |                   0.78 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                | 2327 |  2.80 |   2.74 |   0.59 | ridge              |            0.79 |      698.00 |                   0.81 |
| meteofrance_seamless                                                                                                                                                                                         | 2327 |  1.56 |   1.23 |   0.44 | ridge              |            0.80 |      698.00 |                   0.77 |
| ecmwf_aifs025_single                                                                                                                                                                                         | 2327 |  3.10 |   3.01 |   0.57 | ridge              |            0.80 |      698.00 |                   0.79 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                              | 2327 |  2.52 |   2.45 |   0.55 | ridge              |            0.81 |      698.00 |                   0.82 |
| gem_seamless                                                                                                                                                                                                 | 2327 |  2.39 |   2.24 |   0.50 | ridge              |            0.81 |      698.00 |                   0.84 |
| jma_seamless                                                                                                                                                                                                 | 2327 |  2.21 |   2.09 |   0.52 | ridge              |            0.81 |      698.00 |                   0.82 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                            | 2327 |  2.52 |   2.41 |   0.51 | ridge              |            0.82 |      698.00 |                   0.82 |
| icon_seamless                                                                                                                                                                                                | 2327 |  2.61 |   2.53 |   0.58 | ridge              |            0.82 |      698.00 |                   0.83 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                           | 2327 |  2.62 |   2.55 |   0.55 | ridge              |            0.82 |      698.00 |                   0.82 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                             | 2327 |  2.60 |   2.52 |   0.53 | ridge              |            0.84 |      698.00 |                   0.87 |
| ncep_nbm_conus                                                                                                                                                                                               | 2327 |  2.73 |   2.57 |   0.47 | ridge              |            0.85 |      698.00 |                   0.83 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                           | 2327 |  2.64 |   2.51 |   0.48 | ridge              |            0.87 |      698.00 |                   0.90 |
| ukmo_seamless                                                                                                                                                                                                | 2327 |  2.68 |   2.45 |   0.42 | ridge              |            0.90 |      698.00 |                   0.99 |

## Regional skill — KHIE, Whitefield NH, every season

Ranks models with 13k hours and two winters; the site record above decides. KHIE is 16 km east and is not this hollow: over the hours both stations recorded, temperature correlates 0.88 and dew point 0.92, but wind only 0.57.

### dewpoint_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13880 |  1.97 |   0.80 |   2.64 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13880 |  1.99 |   0.46 |   2.64 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13880 |  2.01 |   0.62 |   2.72 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13880 |  2.04 |   0.91 |   2.69 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13880 |  2.06 |   0.27 |   2.77 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13880 |  2.08 |   0.98 |   2.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13880 |  2.09 |   0.92 |   2.88 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13880 |  2.10 |   0.52 |   2.74 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13880 |  2.16 |   1.21 |   2.96 |
| ncep_nbm_conus                                                                | 13743 |  2.16 |   0.21 |   2.83 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13880 |  2.24 |   0.63 |   2.93 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13880 |  2.27 |   1.23 |   3.14 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13880 |  2.35 |   1.56 |   3.22 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13880 |  2.39 |   1.67 |   3.07 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13880 |  2.46 |   1.72 |   3.38 |
| gem_seamless                                                                  | 13880 |  2.52 |   0.32 |   3.43 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13880 |  2.53 |   1.47 |   3.40 |
| knmi_seamless                                                                 | 13880 |  2.54 |   1.33 |   3.41 |
| metno_seamless                                                                | 13880 |  2.54 |   1.33 |   3.41 |
| best_match                                                                    | 13880 |  2.75 |   0.83 |   3.57 |
| gfs_hrrr                                                                      | 13880 |  2.75 |   0.83 |   3.57 |
| gfs_seamless                                                                  | 13880 |  2.75 |   0.83 |   3.57 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13880 |  2.82 |   2.23 |   3.66 |
| icon_seamless                                                                 | 13880 |  3.06 |   2.22 |   4.17 |
| jma_seamless                                                                  | 13880 |  3.27 |   1.94 |   4.33 |
| ecmwf_ifs025                                                                  | 13880 |  3.31 |   2.75 |   4.24 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13880 |  3.58 |   3.18 |   4.53 |
| ukmo_seamless                                                                 | 13880 |  3.67 |   2.70 |   4.84 |
| ecmwf_aifs025_single                                                          | 13880 |  3.97 |   3.60 |   4.97 |
| meteofrance_seamless                                                          | 13880 |  7.30 |   7.11 |   8.38 |

### gust_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| gem_seamless                                                                  | 13769 |  4.58 |   3.04 |   6.55 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13769 |  4.76 |   3.45 |   6.22 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13769 |  5.24 |   4.26 |   6.61 |
| ncep_nbm_conus                                                                | 13635 |  5.31 |   3.88 |   6.72 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13769 |  5.78 |   4.87 |   7.11 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13769 |  5.84 |   4.88 |   7.30 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13769 |  5.84 |   5.07 |   7.19 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13769 |  5.98 |   5.14 |   7.30 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13769 |  6.09 |   5.21 |   7.67 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13769 |  6.25 |   5.29 |   7.55 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13769 |  6.50 |   5.77 |   7.78 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13769 |  6.58 |   5.96 |   7.86 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13769 |  6.61 |   5.79 |   7.94 |
| best_match                                                                    | 13769 |  6.66 |   5.88 |   8.60 |
| gfs_seamless                                                                  | 13769 |  6.66 |   5.88 |   8.60 |
| gfs_hrrr                                                                      | 13769 |  6.66 |   5.88 |   8.60 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13769 |  6.85 |   6.09 |   8.10 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13769 |  7.06 |   6.53 |   8.42 |
| ukmo_seamless                                                                 | 13769 |  7.46 |   6.68 |   8.88 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13769 |  7.49 |   7.12 |   8.97 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13769 |  7.63 |   7.05 |   8.87 |
| icon_seamless                                                                 | 13769 |  8.25 |   7.67 |   9.75 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13769 |  8.68 |   8.35 |  10.13 |
| metno_seamless                                                                | 13769 |  8.92 |   8.49 |  10.33 |
| knmi_seamless                                                                 | 13769 |  8.92 |   8.49 |  10.33 |
| meteofrance_seamless                                                          | 13769 | 10.11 |   9.66 |  12.04 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13769 | 13.75 |  13.67 |  15.44 |
| ecmwf_ifs025                                                                  | 13769 | 13.75 |  13.67 |  15.44 |

### humidity_pct

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13880 |  7.00 |  -0.01 |   9.03 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13880 |  7.07 |   1.53 |   9.21 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13880 |  7.27 |  -0.73 |   9.44 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13880 |  7.51 |  -1.50 |   9.74 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13880 |  7.58 |  -2.05 |   9.96 |
| ncep_nbm_conus                                                                | 13743 |  7.58 |  -1.05 |   9.99 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13880 |  8.17 |  -2.92 |  10.75 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13880 |  8.21 |  -2.50 |  10.77 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13880 |  8.37 |  -2.66 |  10.91 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13880 |  8.56 |  -2.52 |  11.03 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13880 |  8.59 |  -2.87 |  11.29 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13880 |  8.60 |  -1.92 |  10.88 |
| ukmo_seamless                                                                 | 13880 |  8.72 |   4.01 |  11.63 |
| icon_seamless                                                                 | 13880 |  8.74 |  -3.04 |  11.67 |
| metno_seamless                                                                | 13880 |  8.80 |  -1.80 |  11.61 |
| knmi_seamless                                                                 | 13880 |  8.80 |  -1.80 |  11.61 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13880 |  8.81 |  -2.52 |  11.22 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13880 |  9.01 |  -3.23 |  11.63 |
| jma_seamless                                                                  | 13880 |  9.04 |   3.00 |  11.83 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13880 |  9.57 |  -1.73 |  12.51 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13880 |  9.63 |  -3.00 |  12.25 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13880 |  9.67 |  -2.62 |  12.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13880 |  9.78 |  -0.27 |  12.55 |
| ecmwf_aifs025_single                                                          | 13880 |  9.81 |  -1.16 |  12.67 |
| ecmwf_ifs025                                                                  | 13880 | 10.22 |   0.61 |  13.05 |
| gem_seamless                                                                  | 13880 | 10.89 |  -4.63 |  14.87 |
| gfs_hrrr                                                                      | 13880 | 11.74 |  -3.97 |  14.92 |
| gfs_seamless                                                                  | 13880 | 11.74 |  -3.97 |  14.92 |
| best_match                                                                    | 13880 | 11.74 |  -3.97 |  14.92 |
| meteofrance_seamless                                                          | 13880 | 11.88 |   2.61 |  14.81 |

### temp_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13880 |  3.06 |   1.12 |   4.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13880 |  3.07 |   1.54 |   4.13 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13880 |  3.10 |   1.36 |   4.13 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13880 |  3.11 |   1.56 |   4.25 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13880 |  3.12 |   1.39 |   4.22 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13880 |  3.16 |   1.40 |   4.27 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13880 |  3.18 |   1.38 |   4.31 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13880 |  3.18 |   1.58 |   4.33 |
| ncep_nbm_conus                                                                | 13743 |  3.22 |   0.39 |   4.06 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13880 |  3.26 |   1.17 |   4.37 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13880 |  3.29 |   1.64 |   4.42 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13880 |  3.31 |   0.68 |   4.25 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13880 |  3.32 |   1.84 |   4.55 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13880 |  3.34 |   1.80 |   4.45 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13880 |  3.36 |   1.53 |   4.45 |
| gfs_hrrr                                                                      | 13880 |  3.39 |   1.85 |   4.51 |
| gfs_seamless                                                                  | 13880 |  3.39 |   1.85 |   4.51 |
| best_match                                                                    | 13880 |  3.39 |   1.85 |   4.51 |
| metno_seamless                                                                | 13880 |  3.39 |   1.81 |   4.66 |
| knmi_seamless                                                                 | 13880 |  3.39 |   1.81 |   4.66 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13880 |  3.51 |   2.35 |   4.94 |
| jma_seamless                                                                  | 13880 |  3.57 |   0.56 |   4.74 |
| gem_seamless                                                                  | 13880 |  3.72 |   1.92 |   5.35 |
| ukmo_seamless                                                                 | 13880 |  3.78 |   0.98 |   4.94 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13880 |  3.91 |   2.69 |   5.63 |
| ecmwf_ifs025                                                                  | 13880 |  4.07 |   2.33 |   5.70 |
| icon_seamless                                                                 | 13880 |  4.12 |   3.20 |   5.70 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13880 |  4.29 |   3.07 |   6.08 |
| ecmwf_aifs025_single                                                          | 13880 |  4.76 |   3.81 |   6.65 |
| meteofrance_seamless                                                          | 13880 |  6.36 |   6.00 |   8.24 |

### wind_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| ncep_nbm_conus                                                                | 13635 |  2.12 |   0.09 |   3.17 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13769 |  2.28 |   0.17 |   3.01 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13769 |  2.31 |   0.51 |   2.99 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13769 |  2.34 |   0.67 |   2.97 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13769 |  2.36 |   0.42 |   2.98 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13769 |  2.37 |   0.53 |   2.95 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13769 |  2.38 |   0.61 |   3.02 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13769 |  2.42 |   0.50 |   3.09 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13769 |  2.44 |   0.61 |   3.01 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13769 |  2.45 |   0.64 |   3.04 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13769 |  2.46 |   0.87 |   3.05 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13769 |  2.47 |   0.91 |   3.03 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13769 |  2.49 |   0.75 |   3.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13769 |  2.52 |   1.11 |   3.07 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13769 |  2.53 |   0.98 |   3.10 |
| icon_seamless                                                                 | 13769 |  2.61 |   0.94 |   3.18 |
| gem_seamless                                                                  | 13769 |  2.62 |   0.24 |   3.30 |
| jma_seamless                                                                  | 13769 |  2.67 |   0.29 |   3.31 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13769 |  2.70 |   1.40 |   3.23 |
| metno_seamless                                                                | 13769 |  2.78 |   1.48 |   3.43 |
| knmi_seamless                                                                 | 13769 |  2.78 |   1.48 |   3.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13769 |  2.79 |   1.49 |   3.41 |
| gfs_hrrr                                                                      | 13769 |  2.79 |   1.26 |   3.41 |
| best_match                                                                    | 13769 |  2.79 |   1.26 |   3.41 |
| gfs_seamless                                                                  | 13769 |  2.79 |   1.26 |   3.41 |
| ukmo_seamless                                                                 | 13769 |  2.84 |   0.90 |   3.47 |
| ecmwf_aifs025_single                                                          | 13769 |  2.93 |   1.64 |   3.65 |
| meteofrance_seamless                                                          | 13769 |  3.08 |  -0.64 |   3.92 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13769 |  3.10 |   2.12 |   3.83 |
| ecmwf_ifs025                                                                  | 13769 |  3.37 |   2.60 |   4.17 |

## Regional MAE by season (temperature)

| candidate                                                                     |   fall |   spring |   summer |   winter |
|:------------------------------------------------------------------------------|-------:|---------:|---------:|---------:|
| best_match                                                                    |   3.49 |     3.05 |     3.51 |     3.54 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       |   4.56 |     3.67 |     4.34 |     4.74 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          |   4.16 |     3.34 |     3.95 |     4.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    |   3.73 |     3.02 |     3.61 |     3.75 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         |   3.33 |     2.85 |     3.28 |     3.16 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   |   3.31 |     2.72 |     3.21 |     3.18 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                |   3.29 |     2.87 |     3.16 |     3.17 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   |   3.30 |     3.02 |     3.11 |     3.38 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               |   3.45 |     3.04 |     3.25 |     3.68 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              |   3.43 |     2.85 |     3.19 |     3.26 |
| blend:gem_seamless+ncep_nbm_conus                                             |   3.52 |     3.04 |     3.17 |     3.32 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       |   3.24 |     2.70 |     3.23 |     3.06 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    |   3.19 |     2.88 |     3.22 |     3.10 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 |   3.19 |     2.87 |     3.14 |     2.98 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless |   3.46 |     2.93 |     3.36 |     3.44 |
| blend:icon_seamless+ncep_nbm_conus                                            |   3.42 |     3.17 |     3.21 |     3.71 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              |   3.50 |     3.15 |     3.33 |     3.52 |
| blend:ncep_nbm_conus+ukmo_seamless                                            |   3.58 |     3.13 |     3.33 |     3.11 |
| ecmwf_aifs025_single                                                          |   4.98 |     4.07 |     4.94 |     5.14 |
| ecmwf_ifs025                                                                  |   4.39 |     3.54 |     3.96 |     4.56 |
| gem_seamless                                                                  |   3.87 |     3.44 |     3.64 |     4.06 |
| gfs_hrrr                                                                      |   3.49 |     3.05 |     3.51 |     3.54 |
| gfs_seamless                                                                  |   3.49 |     3.05 |     3.51 |     3.54 |
| icon_seamless                                                                 |   4.03 |     3.90 |     3.85 |     5.16 |
| jma_seamless                                                                  |   3.32 |     3.92 |     3.28 |     4.02 |
| knmi_seamless                                                                 |   3.61 |     2.88 |     3.55 |     3.57 |
| meteofrance_seamless                                                          |   6.86 |     5.21 |     6.08 |     7.95 |
| metno_seamless                                                                |   3.61 |     2.88 |     3.55 |     3.57 |
| ncep_nbm_conus                                                                |   3.54 |     3.12 |     3.09 |     3.07 |
| ukmo_seamless                                                                 |   4.08 |     3.46 |     3.92 |     3.49 |

## MAE by lead time, days 1-7 (previous-runs, site)

### gust_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 7.27 |   3.71 |   4.23 |   4.42 |   4.65 |   4.98 |   4.48 |
| gem_seamless         | 4.26 |   3.85 |   4.22 |   4.28 |   4.61 |   4.78 |   5.32 |
| gfs_hrrr             | 7.27 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 7.27 |   3.71 |   4.23 |   4.42 |   4.65 |   4.98 |   4.48 |
| icon_seamless        | 5.47 |   5.58 |   5.70 |   6.09 |   6.34 |   7.17 | nan    |
| meteofrance_seamless | 5.53 |   5.39 |   5.63 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.76 |   3.99 |   4.23 |   4.31 |   4.32 |   4.27 |   4.14 |
| ukmo_seamless        | 4.94 |   5.10 |   5.07 |   5.27 |   5.08 |   5.95 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           |  8.09 |  11.74 |  12.05 |  12.22 |  12.96 |  14.43 |  16.62 |
| ecmwf_aifs025_single |  7.30 |   8.19 |   9.59 |   9.82 |   9.91 |  10.49 |  11.78 |
| ecmwf_ifs025         |  8.74 |  10.04 |  10.83 |  10.91 |  11.89 |  14.35 |  14.28 |
| gem_seamless         |  9.31 |  12.51 |  11.19 |  11.90 |  12.22 |  12.62 |  14.27 |
| gfs_hrrr             |  8.09 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         |  8.09 |  11.74 |  12.05 |  12.22 |  12.96 |  14.43 |  16.62 |
| icon_seamless        | 10.34 |  10.64 |  11.02 |  12.02 |  13.66 |  13.16 | nan    |
| jma_seamless         | 15.24 |  15.46 |  15.89 |  16.64 |  16.63 |  16.78 |  15.17 |
| knmi_seamless        |  9.04 |  10.18 |  10.99 |  11.31 |  12.69 |  15.03 |  14.89 |
| meteofrance_seamless |  9.87 |  10.61 |  11.45 | nan    | nan    | nan    | nan    |
| metno_seamless       |  9.04 |  10.18 |  10.99 |  11.31 |  12.69 |  15.03 |  14.89 |
| ncep_nbm_conus       | 12.34 |  12.66 |  13.44 |  13.86 |  14.52 |  15.92 |  16.88 |
| ukmo_seamless        | 14.56 |  15.44 |  16.70 |  18.33 |  17.62 |  19.00 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 3.12 |   3.90 |   4.21 |   4.35 |   5.12 |   5.81 |   6.33 |
| ecmwf_aifs025_single | 2.94 |   3.00 |   3.40 |   3.55 |   3.76 |   4.01 |   4.12 |
| ecmwf_ifs025         | 2.74 |   2.97 |   3.17 |   3.69 |   4.04 |   5.18 |   4.89 |
| gem_seamless         | 3.82 |   5.73 |   4.06 |   4.32 |   4.95 |   5.39 |   6.25 |
| gfs_hrrr             | 3.12 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 3.12 |   3.90 |   4.21 |   4.35 |   5.12 |   5.81 |   6.33 |
| icon_seamless        | 4.86 |   4.99 |   5.01 |   5.16 |   5.37 |   6.43 | nan    |
| jma_seamless         | 4.62 |   4.99 |   5.12 |   5.21 |   6.03 |   7.15 |   8.07 |
| knmi_seamless        | 2.98 |   3.20 |   3.28 |   3.79 |   4.29 |   5.47 |   5.20 |
| meteofrance_seamless | 2.86 |   3.18 |   3.51 | nan    | nan    | nan    | nan    |
| metno_seamless       | 2.98 |   3.20 |   3.28 |   3.79 |   4.29 |   5.47 |   5.20 |
| ncep_nbm_conus       | 3.95 |   4.14 |   4.52 |   4.85 |   5.30 |   5.61 |   6.22 |
| ukmo_seamless        | 4.61 |   4.65 |   4.73 |   4.76 |   5.21 |   5.38 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.40 |   2.58 |   2.62 |   2.72 |   2.75 |   2.64 |   2.37 |
| ecmwf_aifs025_single | 3.46 |   3.47 |   3.42 |   3.40 |   3.44 |   3.58 |   3.56 |
| ecmwf_ifs025         | 3.74 |   3.78 |   3.63 |   3.84 |   3.87 |   3.85 |   3.66 |
| gem_seamless         | 2.63 |   2.16 |   2.04 |   2.03 |   2.04 |   2.02 |   2.15 |
| gfs_hrrr             | 4.40 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.40 |   2.58 |   2.62 |   2.72 |   2.75 |   2.64 |   2.37 |
| icon_seamless        | 2.73 |   2.82 |   2.83 |   2.92 |   2.92 |   3.32 | nan    |
| jma_seamless         | 2.24 |   2.31 |   2.40 |   2.42 |   2.50 |   2.37 |   2.24 |
| knmi_seamless        | 3.36 |   3.40 |   3.34 |   3.53 |   3.62 |   3.59 |   3.47 |
| meteofrance_seamless | 1.60 |   1.56 |   1.64 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.36 |   3.40 |   3.34 |   3.53 |   3.62 |   3.59 |   3.47 |
| ncep_nbm_conus       | 2.87 |   2.97 |   3.06 |   3.09 |   2.89 |   2.78 |   2.54 |
| ukmo_seamless        | 3.00 |   3.09 |   3.00 |   3.03 |   2.95 |   3.33 | nan    |
