# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-10-26.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Source in use, per variable

| variable | source |
|---|---|
| dewpoint_f | blend of gem_seamless, gfs_seamless, ncep_nbm_conus |
| gust_mph | blend of gem_seamless, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| humidity_pct | blend of gfs_hrrr, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |
| precip_in | best_match |
| pressure_abs_hpa | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |
| temp_f | knmi_seamless |
| wind_mph | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |

The coming season is **fall**, and the Bear Paw station has not lived through enough of it to judge, so candidates the Whitefield record shows are clearly poor in fall are not eligible. This switches itself off per variable as the station accumulates its own fall hours.

| variable | fall hours on site | candidates ruled out |
|---|---|---|
| dewpoint_f | 113 | 16 |
| humidity_pct | 113 | 14 |
| temp_f | 113 | 7 |

## Site skill, shortlisted candidates (lower MAE = better)

### dewpoint_f

| candidate                                                                                                                                                             |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 113 |  1.56 |  -0.88 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 113 |  1.57 |  -0.64 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 113 |  1.68 |  -0.62 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 113 |  1.70 |   0.12 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                        | 113 |  1.77 |   0.92 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 113 |  1.94 |  -0.75 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                 | 113 |  2.02 |  -1.16 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 113 |  2.04 |  -0.98 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                      | 113 |  2.16 |  -0.51 |    nan |                nan |             nan |         nan |                    nan |
| stack:gem_seamless=0.154+gfs_hrrr=0.028+gfs_seamless=0.028+icon_seamless=0.04+knmi_seamless=0.045+meteofrance_seamless=0.128+metno_seamless=0.045+ukmo_seamless=0.13  | 113 |  2.18 |  -1.10 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 113 |  2.19 |  -1.57 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                          | 113 |  2.28 |  -0.69 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.014+gfs_seamless=0.014+icon_seamless=0.228+jma_seamless=0.068+knmi_seamless=0.019+metno_seamless=0.019                                               | 113 |  2.34 |  -1.72 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 113 |  2.46 |  -1.82 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                    | 113 |  2.49 |   0.33 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 113 |  2.50 |  -1.34 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                         | 113 |  2.58 |  -2.17 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 113 |  2.60 |  -2.01 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 113 |  2.63 |  -1.61 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                          | 113 |  2.95 |   0.77 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                  | 113 |  3.41 |  -0.25 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                         | 113 |  3.63 |  -2.60 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                                                                                                        | 113 |  3.63 |  -2.60 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                         | 113 |  3.70 |  -0.27 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                          | 113 |  3.97 |  -3.26 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                            | 113 |  4.08 |  -2.88 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                              | 113 |  4.08 |  -2.88 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                          | 113 |  4.08 |  -2.88 |    nan |                nan |             nan |         nan |                    nan |

### gust_mph

| candidate                                                                                                                                                             |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 1917 |  4.40 |   3.92 |   0.86 | ridge              |            1.84 |      575.00 |                   1.91 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 1917 |  4.88 |   4.60 |   0.86 | ridge              |            1.85 |      575.00 |                   1.90 |
| stack:gem_seamless=0.154+gfs_hrrr=0.028+gfs_seamless=0.028+icon_seamless=0.04+knmi_seamless=0.045+meteofrance_seamless=0.128+metno_seamless=0.045+ukmo_seamless=0.13  | 1917 |  4.22 |   3.80 |   0.86 | ridge              |            1.89 |      575.00 |                   1.92 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 1917 |  4.26 |   3.76 |   0.86 | ridge              |            1.89 |      575.00 |                   1.95 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 1917 |  4.75 |   4.43 |   0.85 | ridge              |            1.92 |      575.00 |                   2.01 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 1917 |  4.79 |   4.34 |   0.84 | ridge              |            1.93 |      575.00 |                   1.97 |
| metno_seamless                                                                                                                                                        | 1917 |  6.02 |   5.82 |   0.84 | ridge              |            1.94 |      575.00 |                   1.96 |
| knmi_seamless                                                                                                                                                         | 1917 |  6.02 |   5.82 |   0.84 | ridge              |            1.94 |      575.00 |                   1.96 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 1917 |  3.85 |   3.07 |   0.86 | ridge              |            1.96 |      575.00 |                   1.98 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 1917 |  3.71 |   2.65 |   0.84 | ridge              |            1.97 |      575.00 |                   1.97 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                 | 1917 |  3.87 |   2.95 |   0.83 | ridge              |            1.97 |      575.00 |                   1.97 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 1917 |  3.34 |   2.08 |   0.85 | ridge              |            1.99 |      575.00 |                   1.98 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 1917 |  4.30 |   3.75 |   0.84 | ridge              |            2.01 |      575.00 |                   2.02 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                      | 1917 |  4.09 |   3.50 |   0.84 | ridge              |            2.01 |      575.00 |                   2.08 |
| ecmwf_ifs025                                                                                                                                                          | 1917 |  7.25 |   7.13 |   0.84 | ridge              |            2.03 |      575.00 |                   1.95 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                    | 1917 |  3.61 |   2.72 |   0.83 | ridge              |            2.04 |      575.00 |                   2.13 |
| stack:gfs_hrrr=0.014+gfs_seamless=0.014+icon_seamless=0.228+jma_seamless=0.068+knmi_seamless=0.019+metno_seamless=0.019                                               | 1917 |  5.35 |   5.03 |   0.83 | ridge              |            2.05 |      575.00 |                   1.97 |
| ncep_nbm_conus                                                                                                                                                        | 1917 |  3.58 |   2.45 |   0.82 | ridge              |            2.10 |      575.00 |                   2.20 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 1917 |  4.10 |   3.12 |   0.80 | ridge              |            2.11 |      575.00 |                   2.10 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 1917 |  4.35 |   3.34 |   0.79 | ridge              |            2.16 |      575.00 |                   2.08 |
| icon_seamless                                                                                                                                                         | 1917 |  5.47 |   5.05 |   0.82 | ridge              |            2.17 |      575.00 |                   1.99 |
| gem_seamless                                                                                                                                                          | 1917 |  3.77 |   1.71 |   0.81 | ridge              |            2.24 |      575.00 |                   2.06 |
| best_match                                                                                                                                                            | 1917 |  4.91 |   3.79 |   0.75 | ridge              |            2.28 |      575.00 |                   2.08 |
| gfs_hrrr                                                                                                                                                              | 1917 |  4.91 |   3.79 |   0.75 | ridge              |            2.28 |      575.00 |                   2.08 |
| gfs_seamless                                                                                                                                                          | 1917 |  4.91 |   3.79 |   0.75 | ridge              |            2.28 |      575.00 |                   2.08 |
| ukmo_seamless                                                                                                                                                         | 1917 |  4.01 |   2.99 |   0.79 | ridge              |            2.29 |      575.00 |                   2.24 |
| meteofrance_seamless                                                                                                                                                  | 1917 |  5.67 |   5.33 |   0.72 | ridge              |            2.42 |      575.00 |                   2.34 |

### humidity_pct

| candidate                                                                                                                                                             |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 113 |  7.66 |   7.09 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 113 |  7.89 |   7.66 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                         | 113 |  7.95 |   3.64 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                                                                                                        | 113 |  7.95 |   3.64 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 113 |  8.70 |   8.39 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                          | 113 |  8.76 |   1.34 |    nan |                nan |             nan |         nan |                    nan |
| stack:gem_seamless=0.154+gfs_hrrr=0.028+gfs_seamless=0.028+icon_seamless=0.04+knmi_seamless=0.045+meteofrance_seamless=0.128+metno_seamless=0.045+ukmo_seamless=0.13  | 113 |  8.99 |   8.77 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 113 |  9.99 |   9.39 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 113 | 10.06 |   9.80 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 113 | 10.47 |  10.35 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                 | 113 | 10.59 |  10.41 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                          | 113 | 10.77 |   9.65 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 113 | 10.83 |  10.69 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                            | 113 | 10.83 |   6.79 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                              | 113 | 10.83 |   6.79 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                          | 113 | 10.83 |   6.79 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                  | 113 | 10.94 |   5.37 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 113 | 12.19 |  12.12 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 113 | 12.46 |  12.39 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 113 | 13.19 |  12.95 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                         | 113 | 13.44 |  12.91 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.014+gfs_seamless=0.014+icon_seamless=0.228+jma_seamless=0.068+knmi_seamless=0.019+metno_seamless=0.019                                               | 113 | 13.79 |  13.54 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 113 | 13.81 |  13.75 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                      | 113 | 13.92 |  13.91 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                         | 113 | 14.34 |  14.22 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                    | 113 | 14.41 |  14.41 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                        | 113 | 14.59 |  14.59 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                          | 113 | 24.69 |  23.96 |    nan |                nan |             nan |         nan |                    nan |

### precip_in

| candidate                                                                                                                                                             |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                                                                                                            | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                              | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                          | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:gem_seamless=0.154+gfs_hrrr=0.028+gfs_seamless=0.028+icon_seamless=0.04+knmi_seamless=0.045+meteofrance_seamless=0.128+metno_seamless=0.045+ukmo_seamless=0.13  | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                 | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 2331 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.014+gfs_seamless=0.014+icon_seamless=0.228+jma_seamless=0.068+knmi_seamless=0.019+metno_seamless=0.019                                               | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                         | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                      | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                  | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 2331 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                    | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                         | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                          | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                          | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                        | 2331 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                                                                                                        | 2331 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                         | 2331 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                          | 2331 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                                                                                                             |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 9502 |  1.48 |  -0.62 |   0.93 | bias               |            1.04 |     2851.00 |                   0.50 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 9502 |  1.51 |  -0.66 |   0.93 | bias               |            1.04 |     2851.00 |                   0.54 |
| stack:gem_seamless=0.154+gfs_hrrr=0.028+gfs_seamless=0.028+icon_seamless=0.04+knmi_seamless=0.045+meteofrance_seamless=0.128+metno_seamless=0.045+ukmo_seamless=0.13  | 9502 |  1.47 |  -0.60 |   0.93 | bias               |            1.05 |     2851.00 |                   0.55 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                      | 9502 |  1.59 |  -0.75 |   0.93 | bias               |            1.05 |     2851.00 |                   0.53 |
| ecmwf_ifs025                                                                                                                                                          | 9502 |  1.38 |  -0.48 |   0.93 | bias               |            1.06 |     2851.00 |                   0.50 |
| metno_seamless                                                                                                                                                        | 9502 |  1.39 |  -0.49 |   0.93 | bias               |            1.06 |     2851.00 |                   0.49 |
| knmi_seamless                                                                                                                                                         | 9502 |  1.39 |  -0.49 |   0.93 | bias               |            1.06 |     2851.00 |                   0.49 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 9502 |  1.50 |  -0.64 |   0.93 | bias               |            1.06 |     2851.00 |                   0.58 |
| stack:gfs_hrrr=0.014+gfs_seamless=0.014+icon_seamless=0.228+jma_seamless=0.068+knmi_seamless=0.019+metno_seamless=0.019                                               | 9502 |  1.37 |  -0.49 |   0.94 | bias               |            1.08 |     2851.00 |                   0.58 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 9502 |  1.31 |  -0.43 |   0.94 | bias               |            1.08 |     2851.00 |                   0.51 |
| meteofrance_seamless                                                                                                                                                  | 9502 |  1.31 |  -0.30 |   0.93 | bias               |            1.10 |     2851.00 |                   0.64 |
| icon_seamless                                                                                                                                                         | 9502 |  1.30 |  -0.35 |   0.94 | bias               |            1.15 |     2851.00 |                   0.67 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 9502 |  1.30 |  -0.35 |   0.94 | bias               |            1.15 |     2851.00 |                   0.67 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 9502 |  1.25 |  -0.31 |   0.94 | bias               |            1.15 |     2851.00 |                   0.64 |
| jma_seamless                                                                                                                                                          | 9502 |  1.50 |  -0.62 |   0.94 | bias               |            1.15 |     2851.00 |                   0.55 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                    | 9502 |  1.95 |  -1.15 |   0.93 | bias               |            1.16 |     2851.00 |                   0.57 |
| ukmo_seamless                                                                                                                                                         | 9502 |  1.95 |  -1.15 |   0.93 | bias               |            1.16 |     2851.00 |                   0.57 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 9502 |  1.74 |  -0.90 |   0.93 | bias               |            1.17 |     2851.00 |                   0.65 |
| gem_seamless                                                                                                                                                          | 9502 |  1.24 |  -0.27 |   0.94 | bias               |            1.19 |     2851.00 |                   0.66 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 9502 |  1.24 |  -0.27 |   0.94 | bias               |            1.19 |     2851.00 |                   0.66 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 9502 |  1.64 |  -0.79 |   0.93 | raw                |            1.55 |     2851.00 |                   1.55 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                 | 9502 |  1.83 |  -1.01 |   0.93 | raw                |            1.71 |     2851.00 |                   1.84 |
| best_match                                                                                                                                                            | 9502 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2851.00 |                   2.52 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 9502 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2851.00 |                   2.52 |
| gfs_hrrr                                                                                                                                                              | 9502 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2851.00 |                   2.52 |
| gfs_seamless                                                                                                                                                          | 9502 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2851.00 |                   2.52 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 9502 |  2.14 |  -1.31 |   0.92 | raw                |            1.93 |     2851.00 |                   2.52 |

### temp_f

| candidate                                                                                                                                                             |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| meteofrance_seamless                                                                                                                                                  | 113 |  3.79 |  -3.06 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                          | 113 |  4.39 |  -4.04 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                         | 113 |  4.60 |  -4.40 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                                                                                                        | 113 |  4.60 |  -4.40 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                          | 113 |  4.74 |  -4.45 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 113 |  5.01 |  -4.93 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 113 |  5.07 |  -5.03 |    nan |                nan |             nan |         nan |                    nan |
| stack:gem_seamless=0.154+gfs_hrrr=0.028+gfs_seamless=0.028+icon_seamless=0.04+knmi_seamless=0.045+meteofrance_seamless=0.128+metno_seamless=0.045+ukmo_seamless=0.13  | 113 |  5.07 |  -5.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                        | 113 |  5.43 |  -5.42 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 113 |  5.45 |  -5.43 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 113 |  5.49 |  -5.45 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 113 |  5.51 |  -5.48 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 113 |  5.69 |  -5.62 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 113 |  5.79 |  -5.70 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                 | 113 |  5.93 |  -5.90 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 113 |  5.95 |  -5.95 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 113 |  5.98 |  -5.94 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                    | 113 |  6.06 |  -6.05 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 113 |  6.13 |  -6.12 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 113 |  6.41 |  -6.32 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                      | 113 |  6.46 |  -6.44 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                            | 113 |  6.53 |  -6.48 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                              | 113 |  6.53 |  -6.48 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                          | 113 |  6.53 |  -6.48 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                         | 113 |  6.76 |  -6.69 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.014+gfs_seamless=0.014+icon_seamless=0.228+jma_seamless=0.068+knmi_seamless=0.019+metno_seamless=0.019                                               | 113 |  7.15 |  -7.05 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                         | 113 |  7.47 |  -7.22 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                          | 113 |  8.27 |  -8.20 |    nan |                nan |             nan |         nan |                    nan |

### wind_mph

| candidate                                                                                                                                                             |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 1917 |  2.74 |   2.69 |   0.75 | ridge              |            0.73 |      575.00 |                   0.68 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 1917 |  2.89 |   2.83 |   0.74 | ridge              |            0.74 |      575.00 |                   0.70 |
| knmi_seamless                                                                                                                                                         | 1917 |  3.11 |   3.02 |   0.74 | ridge              |            0.74 |      575.00 |                   0.68 |
| metno_seamless                                                                                                                                                        | 1917 |  3.11 |   3.02 |   0.74 | ridge              |            0.74 |      575.00 |                   0.68 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 1917 |  3.08 |   3.03 |   0.74 | ridge              |            0.74 |      575.00 |                   0.68 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 1917 |  2.79 |   2.72 |   0.73 | ridge              |            0.74 |      575.00 |                   0.72 |
| stack:gem_seamless=0.154+gfs_hrrr=0.028+gfs_seamless=0.028+icon_seamless=0.04+knmi_seamless=0.045+meteofrance_seamless=0.128+metno_seamless=0.045+ukmo_seamless=0.13  | 1917 |  2.39 |   2.32 |   0.72 | ridge              |            0.75 |      575.00 |                   0.69 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 1917 |  2.57 |   2.51 |   0.72 | ridge              |            0.75 |      575.00 |                   0.72 |
| ecmwf_ifs025                                                                                                                                                          | 1917 |  3.45 |   3.40 |   0.75 | ridge              |            0.75 |      575.00 |                   0.63 |
| stack:gfs_hrrr=0.014+gfs_seamless=0.014+icon_seamless=0.228+jma_seamless=0.068+knmi_seamless=0.019+metno_seamless=0.019                                               | 1917 |  2.64 |   2.59 |   0.73 | ridge              |            0.77 |      575.00 |                   0.73 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 1917 |  2.55 |   2.47 |   0.70 | ridge              |            0.77 |      575.00 |                   0.73 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 1917 |  2.78 |   2.70 |   0.70 | ridge              |            0.77 |      575.00 |                   0.70 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 1917 |  2.64 |   2.57 |   0.69 | ridge              |            0.78 |      575.00 |                   0.76 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                 | 1917 |  2.83 |   2.76 |   0.70 | ridge              |            0.78 |      575.00 |                   0.69 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 1917 |  2.99 |   2.92 |   0.69 | ridge              |            0.78 |      575.00 |                   0.70 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 1917 |  2.53 |   2.42 |   0.67 | ridge              |            0.78 |      575.00 |                   0.72 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                      | 1917 |  2.60 |   2.52 |   0.69 | ridge              |            0.78 |      575.00 |                   0.75 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 1917 |  3.10 |   3.04 |   0.69 | ridge              |            0.79 |      575.00 |                   0.68 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                    | 1917 |  2.61 |   2.50 |   0.67 | ridge              |            0.80 |      575.00 |                   0.76 |
| ncep_nbm_conus                                                                                                                                                        | 1917 |  2.73 |   2.56 |   0.64 | ridge              |            0.80 |      575.00 |                   0.77 |
| icon_seamless                                                                                                                                                         | 1917 |  2.65 |   2.58 |   0.70 | ridge              |            0.81 |      575.00 |                   0.75 |
| gem_seamless                                                                                                                                                          | 1917 |  2.42 |   2.27 |   0.66 | ridge              |            0.82 |      575.00 |                   0.69 |
| jma_seamless                                                                                                                                                          | 1917 |  2.24 |   2.12 |   0.63 | ridge              |            0.83 |      575.00 |                   0.77 |
| best_match                                                                                                                                                            | 1917 |  3.35 |   3.27 |   0.66 | ridge              |            0.83 |      575.00 |                   0.67 |
| gfs_hrrr                                                                                                                                                              | 1917 |  3.35 |   3.27 |   0.66 | ridge              |            0.83 |      575.00 |                   0.67 |
| gfs_seamless                                                                                                                                                          | 1917 |  3.35 |   3.27 |   0.66 | ridge              |            0.83 |      575.00 |                   0.67 |
| meteofrance_seamless                                                                                                                                                  | 1917 |  1.59 |   1.28 |   0.55 | ridge              |            0.84 |      575.00 |                   0.72 |
| ukmo_seamless                                                                                                                                                         | 1917 |  2.62 |   2.43 |   0.63 | ridge              |            0.86 |      575.00 |                   0.75 |

## Regional skill — KHIE, Whitefield NH, every season

Ranks models with 13k hours and two winters; the site record above decides. KHIE is 16 km east and is not this hollow: over the hours both stations recorded, temperature correlates 0.88 and dew point 0.92, but wind only 0.57.

### dewpoint_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13401 |  1.97 |   0.81 |   2.64 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13401 |  2.00 |   0.48 |   2.64 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13401 |  2.01 |   0.62 |   2.71 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13401 |  2.04 |   0.92 |   2.69 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13401 |  2.06 |   0.28 |   2.77 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13401 |  2.09 |   1.01 |   2.75 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13401 |  2.10 |   0.55 |   2.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13401 |  2.10 |   0.93 |   2.89 |
| ncep_nbm_conus                                                                | 13264 |  2.15 |   0.23 |   2.81 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13401 |  2.16 |   1.21 |   2.95 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13401 |  2.25 |   0.66 |   2.94 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13401 |  2.27 |   1.24 |   3.13 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13401 |  2.35 |   1.56 |   3.21 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13401 |  2.40 |   1.68 |   3.07 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13401 |  2.47 |   1.74 |   3.38 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13401 |  2.53 |   1.50 |   3.39 |
| gem_seamless                                                                  | 13401 |  2.53 |   0.33 |   3.44 |
| knmi_seamless                                                                 | 13401 |  2.53 |   1.31 |   3.39 |
| metno_seamless                                                                | 13401 |  2.53 |   1.31 |   3.39 |
| best_match                                                                    | 13401 |  2.77 |   0.87 |   3.59 |
| gfs_hrrr                                                                      | 13401 |  2.77 |   0.87 |   3.59 |
| gfs_seamless                                                                  | 13401 |  2.77 |   0.87 |   3.59 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13401 |  2.81 |   2.21 |   3.65 |
| icon_seamless                                                                 | 13401 |  3.07 |   2.22 |   4.18 |
| jma_seamless                                                                  | 13401 |  3.27 |   1.93 |   4.33 |
| ecmwf_ifs025                                                                  | 13401 |  3.29 |   2.72 |   4.21 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13401 |  3.56 |   3.15 |   4.51 |
| ukmo_seamless                                                                 | 13401 |  3.69 |   2.72 |   4.86 |
| ecmwf_aifs025_single                                                          | 13401 |  3.95 |   3.58 |   4.95 |
| meteofrance_seamless                                                          | 13401 |  7.29 |   7.09 |   8.37 |

### gust_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| gem_seamless                                                                  | 13292 |  4.59 |   3.01 |   6.56 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13292 |  4.76 |   3.42 |   6.21 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13292 |  5.22 |   4.22 |   6.59 |
| ncep_nbm_conus                                                                | 13158 |  5.30 |   3.84 |   6.71 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13292 |  5.77 |   4.83 |   7.10 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13292 |  5.82 |   4.83 |   7.27 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13292 |  5.83 |   5.04 |   7.17 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13292 |  5.98 |   5.11 |   7.30 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13292 |  6.06 |   5.16 |   7.64 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13292 |  6.25 |   5.27 |   7.55 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13292 |  6.49 |   5.75 |   7.77 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13292 |  6.56 |   5.93 |   7.86 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13292 |  6.60 |   5.75 |   7.92 |
| best_match                                                                    | 13292 |  6.62 |   5.83 |   8.57 |
| gfs_seamless                                                                  | 13292 |  6.62 |   5.83 |   8.57 |
| gfs_hrrr                                                                      | 13292 |  6.62 |   5.83 |   8.57 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13292 |  6.84 |   6.06 |   8.09 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13292 |  7.04 |   6.49 |   8.40 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13292 |  7.46 |   7.08 |   8.93 |
| ukmo_seamless                                                                 | 13292 |  7.48 |   6.68 |   8.90 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13292 |  7.63 |   7.03 |   8.87 |
| icon_seamless                                                                 | 13292 |  8.23 |   7.64 |   9.73 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13292 |  8.67 |   8.33 |  10.11 |
| metno_seamless                                                                | 13292 |  8.92 |   8.48 |  10.34 |
| knmi_seamless                                                                 | 13292 |  8.92 |   8.48 |  10.34 |
| meteofrance_seamless                                                          | 13292 | 10.08 |   9.62 |  12.01 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13292 | 13.72 |  13.64 |  15.42 |
| ecmwf_ifs025                                                                  | 13292 | 13.72 |  13.64 |  15.42 |

### humidity_pct

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13401 |  6.98 |  -0.04 |   9.01 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13401 |  7.04 |   1.54 |   9.19 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13401 |  7.24 |  -0.77 |   9.42 |
| ncep_nbm_conus                                                                | 13264 |  7.49 |  -1.13 |   9.88 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13401 |  7.49 |  -1.53 |   9.73 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13401 |  7.54 |  -2.14 |   9.92 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13401 |  8.14 |  -2.97 |  10.75 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13401 |  8.17 |  -2.53 |  10.74 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13401 |  8.35 |  -2.65 |  10.89 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13401 |  8.54 |  -2.50 |  11.01 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13401 |  8.56 |  -2.89 |  11.27 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13401 |  8.59 |  -1.86 |  10.87 |
| ukmo_seamless                                                                 | 13401 |  8.69 |   4.10 |  11.60 |
| icon_seamless                                                                 | 13401 |  8.73 |  -3.15 |  11.68 |
| metno_seamless                                                                | 13401 |  8.77 |  -1.85 |  11.58 |
| knmi_seamless                                                                 | 13401 |  8.77 |  -1.85 |  11.58 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13401 |  8.80 |  -2.49 |  11.20 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13401 |  9.00 |  -3.20 |  11.63 |
| jma_seamless                                                                  | 13401 |  9.10 |   3.05 |  11.90 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13401 |  9.56 |  -1.74 |  12.51 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13401 |  9.63 |  -2.94 |  12.24 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13401 |  9.67 |  -2.58 |  12.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13401 |  9.75 |  -0.31 |  12.52 |
| ecmwf_aifs025_single                                                          | 13401 |  9.77 |  -1.18 |  12.64 |
| ecmwf_ifs025                                                                  | 13401 | 10.19 |   0.57 |  13.02 |
| gem_seamless                                                                  | 13401 | 10.90 |  -4.60 |  14.89 |
| gfs_hrrr                                                                      | 13401 | 11.74 |  -3.84 |  14.91 |
| gfs_seamless                                                                  | 13401 | 11.74 |  -3.84 |  14.91 |
| best_match                                                                    | 13401 | 11.74 |  -3.84 |  14.91 |
| meteofrance_seamless                                                          | 13401 | 11.91 |   2.58 |  14.84 |

### temp_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13401 |  3.06 |   1.13 |   4.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13401 |  3.07 |   1.54 |   4.13 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13401 |  3.11 |   1.36 |   4.13 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13401 |  3.11 |   1.55 |   4.25 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13401 |  3.13 |   1.39 |   4.22 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13401 |  3.17 |   1.40 |   4.27 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13401 |  3.18 |   1.38 |   4.30 |
| ncep_nbm_conus                                                                | 13264 |  3.19 |   0.42 |   4.02 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13401 |  3.19 |   1.58 |   4.33 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13401 |  3.26 |   1.18 |   4.36 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13401 |  3.29 |   1.65 |   4.42 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13401 |  3.32 |   0.70 |   4.25 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13401 |  3.32 |   1.86 |   4.56 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13401 |  3.33 |   1.84 |   4.45 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13401 |  3.37 |   1.55 |   4.45 |
| gfs_hrrr                                                                      | 13401 |  3.39 |   1.83 |   4.51 |
| gfs_seamless                                                                  | 13401 |  3.39 |   1.83 |   4.51 |
| best_match                                                                    | 13401 |  3.39 |   1.83 |   4.51 |
| metno_seamless                                                                | 13401 |  3.40 |   1.80 |   4.65 |
| knmi_seamless                                                                 | 13401 |  3.40 |   1.80 |   4.65 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13401 |  3.51 |   2.33 |   4.93 |
| jma_seamless                                                                  | 13401 |  3.59 |   0.53 |   4.75 |
| gem_seamless                                                                  | 13401 |  3.74 |   1.91 |   5.37 |
| ukmo_seamless                                                                 | 13401 |  3.79 |   0.98 |   4.95 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13401 |  3.91 |   2.67 |   5.63 |
| ecmwf_ifs025                                                                  | 13401 |  4.06 |   2.31 |   5.68 |
| icon_seamless                                                                 | 13401 |  4.15 |   3.23 |   5.73 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13401 |  4.29 |   3.05 |   6.07 |
| ecmwf_aifs025_single                                                          | 13401 |  4.75 |   3.79 |   6.63 |
| meteofrance_seamless                                                          | 13401 |  6.35 |   5.98 |   8.23 |

### wind_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| ncep_nbm_conus                                                                | 13158 |  2.13 |   0.08 |   3.18 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13292 |  2.29 |   0.15 |   3.02 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13292 |  2.32 |   0.50 |   2.99 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13292 |  2.35 |   0.66 |   2.98 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13292 |  2.36 |   0.41 |   2.99 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13292 |  2.38 |   0.52 |   2.96 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13292 |  2.39 |   0.59 |   3.03 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13292 |  2.42 |   0.48 |   3.10 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13292 |  2.44 |   0.59 |   3.03 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13292 |  2.45 |   0.63 |   3.05 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13292 |  2.47 |   0.85 |   3.06 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13292 |  2.48 |   0.90 |   3.04 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13292 |  2.50 |   0.73 |   3.03 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13292 |  2.53 |   1.10 |   3.08 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13292 |  2.53 |   0.96 |   3.11 |
| icon_seamless                                                                 | 13292 |  2.61 |   0.92 |   3.19 |
| gem_seamless                                                                  | 13292 |  2.63 |   0.23 |   3.32 |
| jma_seamless                                                                  | 13292 |  2.68 |   0.27 |   3.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13292 |  2.70 |   1.38 |   3.23 |
| metno_seamless                                                                | 13292 |  2.78 |   1.47 |   3.44 |
| knmi_seamless                                                                 | 13292 |  2.78 |   1.47 |   3.44 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13292 |  2.79 |   1.48 |   3.41 |
| gfs_hrrr                                                                      | 13292 |  2.79 |   1.24 |   3.42 |
| best_match                                                                    | 13292 |  2.79 |   1.24 |   3.42 |
| gfs_seamless                                                                  | 13292 |  2.79 |   1.24 |   3.42 |
| ukmo_seamless                                                                 | 13292 |  2.85 |   0.88 |   3.48 |
| ecmwf_aifs025_single                                                          | 13292 |  2.94 |   1.62 |   3.65 |
| meteofrance_seamless                                                          | 13292 |  3.09 |  -0.66 |   3.94 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13292 |  3.10 |   2.10 |   3.83 |
| ecmwf_ifs025                                                                  | 13292 |  3.36 |   2.59 |   4.17 |

## Regional MAE by season (temperature)

| candidate                                                                     |   fall |   spring |   summer |   winter |
|:------------------------------------------------------------------------------|-------:|---------:|---------:|---------:|
| best_match                                                                    |   3.53 |     3.05 |     3.51 |     3.54 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       |   4.59 |     3.67 |     4.34 |     4.74 |
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
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    |   3.23 |     2.88 |     3.22 |     3.10 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 |   3.21 |     2.87 |     3.14 |     2.98 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless |   3.51 |     2.93 |     3.36 |     3.44 |
| blend:icon_seamless+ncep_nbm_conus                                            |   3.43 |     3.17 |     3.21 |     3.71 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              |   3.55 |     3.15 |     3.33 |     3.52 |
| blend:ncep_nbm_conus+ukmo_seamless                                            |   3.62 |     3.13 |     3.33 |     3.11 |
| ecmwf_aifs025_single                                                          |   4.98 |     4.07 |     4.94 |     5.14 |
| ecmwf_ifs025                                                                  |   4.42 |     3.54 |     3.96 |     4.56 |
| gem_seamless                                                                  |   3.96 |     3.44 |     3.64 |     4.06 |
| gfs_hrrr                                                                      |   3.53 |     3.05 |     3.51 |     3.54 |
| gfs_seamless                                                                  |   3.53 |     3.05 |     3.51 |     3.54 |
| icon_seamless                                                                 |   4.13 |     3.90 |     3.85 |     5.16 |
| jma_seamless                                                                  |   3.34 |     3.92 |     3.28 |     4.02 |
| knmi_seamless                                                                 |   3.64 |     2.88 |     3.55 |     3.57 |
| meteofrance_seamless                                                          |   6.89 |     5.21 |     6.08 |     7.95 |
| metno_seamless                                                                |   3.64 |     2.88 |     3.55 |     3.57 |
| ncep_nbm_conus                                                                |   3.46 |     3.12 |     3.09 |     3.07 |
| ukmo_seamless                                                                 |   4.17 |     3.46 |     3.92 |     3.49 |

## MAE by lead time, days 1-7 (previous-runs, site)

### gust_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 7.01 |   3.60 |   3.83 |   4.14 |   4.39 |   4.89 |   4.57 |
| gem_seamless         | 4.14 |   3.92 |   4.21 |   3.97 |   4.39 |   4.68 |   5.43 |
| gfs_hrrr             | 7.01 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 7.01 |   3.60 |   3.83 |   4.14 |   4.39 |   4.89 |   4.57 |
| icon_seamless        | 5.52 |   5.58 |   5.66 |   6.20 |   6.29 |   6.58 | nan    |
| meteofrance_seamless | 5.85 |   5.77 |   5.93 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.60 |   3.74 |   3.95 |   4.12 |   4.03 |   4.13 |   4.03 |
| ukmo_seamless        | 4.58 |   4.93 |   4.62 |   5.01 |   5.06 |   5.40 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 11.16 |  14.06 |  14.47 |  14.26 |  14.41 |  13.08 |  16.38 |
| ecmwf_aifs025_single |  9.29 |  11.05 |  11.26 |  10.35 |  11.15 |  12.18 |  11.50 |
| ecmwf_ifs025         | 10.48 |  11.75 |  10.32 |  13.07 |  11.06 |  16.10 |  10.32 |
| gem_seamless         |  8.16 |  18.23 |  11.08 |  13.61 |  14.02 |  17.24 |  17.10 |
| gfs_hrrr             | 11.16 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 11.16 |  14.06 |  14.47 |  14.26 |  14.41 |  13.08 |  16.38 |
| icon_seamless        | 13.32 |  13.49 |  14.51 |  13.76 |  14.76 |  11.33 | nan    |
| jma_seamless         | 24.28 |  23.87 |  21.81 |  22.26 |  23.23 |  18.79 |  14.32 |
| knmi_seamless        | 11.02 |  11.79 |  10.90 |  12.94 |  10.63 |  15.89 |  10.58 |
| meteofrance_seamless | 11.96 |  12.31 |  11.83 | nan    | nan    | nan    | nan    |
| metno_seamless       | 11.02 |  11.79 |  10.90 |  12.94 |  10.63 |  15.89 |  10.58 |
| ncep_nbm_conus       | 16.65 |  17.52 |  18.81 |  18.34 |  19.90 |  20.69 |  22.42 |
| ukmo_seamless        | 16.42 |  18.51 |  24.05 |  21.23 |  18.56 |  20.63 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.09 |   5.40 |   5.84 |   5.18 |   5.34 |   5.77 |   5.71 |
| ecmwf_aifs025_single | 5.02 |   5.18 |   5.35 |   5.05 |   4.63 |   4.43 |   3.75 |
| ecmwf_ifs025         | 4.29 |   4.61 |   4.85 |   5.56 |   5.02 |   5.01 |   4.44 |
| gem_seamless         | 4.49 |  10.04 |   6.62 |   6.48 |   6.07 |   7.04 |   6.46 |
| gfs_hrrr             | 4.09 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.09 |   5.40 |   5.84 |   5.18 |   5.34 |   5.77 |   5.71 |
| icon_seamless        | 7.73 |   8.07 |   7.94 |   7.15 |   5.93 |   6.13 | nan    |
| jma_seamless         | 8.14 |   8.66 |   8.60 |   8.07 |   8.01 |   8.13 |   7.65 |
| knmi_seamless        | 4.37 |   4.60 |   4.72 |   5.44 |   5.02 |   4.98 |   4.85 |
| meteofrance_seamless | 4.30 |   4.60 |   4.83 | nan    | nan    | nan    | nan    |
| metno_seamless       | 4.37 |   4.60 |   4.72 |   5.44 |   5.02 |   4.98 |   4.85 |
| ncep_nbm_conus       | 5.79 |   6.43 |   6.47 |   5.76 |   5.10 |   4.81 |   5.03 |
| ukmo_seamless        | 6.22 |   6.13 |   6.92 |   6.16 |   5.97 |   6.08 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.51 |   2.60 |   2.50 |   2.70 |   2.67 |   2.64 |   2.41 |
| ecmwf_aifs025_single | 3.19 |   3.19 |   3.23 |   3.32 |   3.38 |   3.47 |   3.36 |
| ecmwf_ifs025         | 3.44 |   3.53 |   3.39 |   3.63 |   3.78 |   3.51 |   3.29 |
| gem_seamless         | 2.57 |   2.12 |   1.96 |   1.89 |   1.95 |   1.91 |   2.12 |
| gfs_hrrr             | 4.51 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.51 |   2.60 |   2.50 |   2.70 |   2.67 |   2.64 |   2.41 |
| icon_seamless        | 2.68 |   2.72 |   2.74 |   2.86 |   2.85 |   2.98 | nan    |
| jma_seamless         | 2.14 |   2.25 |   2.29 |   2.34 |   2.49 |   2.33 |   2.12 |
| knmi_seamless        | 3.08 |   3.21 |   3.10 |   3.36 |   3.56 |   3.30 |   3.13 |
| meteofrance_seamless | 1.62 |   1.62 |   1.66 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.08 |   3.21 |   3.10 |   3.36 |   3.56 |   3.30 |   3.13 |
| ncep_nbm_conus       | 2.67 |   2.68 |   2.73 |   2.79 |   2.57 |   2.51 |   2.33 |
| ukmo_seamless        | 2.82 |   2.95 |   2.72 |   2.92 |   2.88 |   3.01 | nan    |
