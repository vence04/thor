# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-11-16.
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

| candidate                                                                                                                                                                                                     |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                                | 545 |  1.27 |  -0.84 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                               | 545 |  1.30 |  -0.68 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                             | 545 |  1.31 |  -0.30 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                            | 545 |  1.34 |  -0.56 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                               | 545 |  1.38 |  -0.36 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                                | 545 |  1.42 |   0.32 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 545 |  1.43 |  -0.45 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                 | 545 |  1.44 |  -0.79 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 545 |  1.44 |  -0.70 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 545 |  1.44 |  -0.70 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                         | 545 |  1.52 |  -0.80 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.02+gem_seamless=0.163+gfs_hrrr=0.033+gfs_seamless=0.033+icon_seamless=0.021+knmi_seamless=0.062+meteofrance_seamless=0.098+metno_seamless=0.062+ncep_nbm_conus=0.006+ukmo_seamless=0.113 | 545 |  1.54 |  -0.68 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                         | 545 |  1.59 |  -1.09 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 545 |  1.63 |  -0.89 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.011+gfs_seamless=0.011+icon_seamless=0.202+jma_seamless=0.019+knmi_seamless=0.047+metno_seamless=0.047+ncep_nbm_conus=0.034                                                                  | 545 |  1.66 |  -0.98 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                 | 545 |  1.73 |  -0.62 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                              | 545 |  1.76 |  -0.71 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                    | 545 |  1.77 |  -1.16 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                  | 545 |  1.86 |  -0.92 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                 | 545 |  2.02 |  -1.44 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                            | 545 |  2.03 |  -0.35 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                 | 545 |  2.15 |  -0.49 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                  | 545 |  2.17 |  -0.76 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                  | 545 |  2.48 |   0.27 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                                                          | 545 |  2.59 |   0.83 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                                                                    | 545 |  2.62 |  -1.91 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                  | 545 |  2.62 |  -1.91 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                      | 545 |  2.62 |  -1.91 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                 | 545 |  3.21 |  -1.02 |    nan |                nan |             nan |         nan |                    nan |

### gust_mph

| candidate                                                                                                                                                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ecmwf_ifs025                                                                                                                                                                                                  | 2349 |  7.30 |   7.20 |   0.79 | ridge              |            1.94 |      705.00 |                   1.90 |
| knmi_seamless                                                                                                                                                                                                 | 2349 |  6.02 |   5.83 |   0.77 | ridge              |            1.96 |      705.00 |                   1.98 |
| stack:gfs_hrrr=0.011+gfs_seamless=0.011+icon_seamless=0.202+jma_seamless=0.019+knmi_seamless=0.047+metno_seamless=0.047+ncep_nbm_conus=0.034                                                                  | 2349 |  5.12 |   4.83 |   0.78 | ridge              |            1.98 |      705.00 |                   1.91 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                         | 2349 |  4.91 |   4.65 |   0.78 | ridge              |            1.98 |      705.00 |                   1.93 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 2349 |  4.44 |   3.99 |   0.77 | ridge              |            1.99 |      705.00 |                   1.98 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 2349 |  4.44 |   3.99 |   0.77 | ridge              |            1.99 |      705.00 |                   1.98 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 2349 |  4.21 |   3.72 |   0.78 | ridge              |            2.01 |      705.00 |                   1.96 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                               | 2349 |  3.94 |   3.34 |   0.78 | ridge              |            2.01 |      705.00 |                   1.99 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                            | 2349 |  4.21 |   3.66 |   0.77 | ridge              |            2.03 |      705.00 |                   1.94 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                 | 2349 |  4.73 |   4.41 |   0.77 | ridge              |            2.03 |      705.00 |                   2.01 |
| stack:ecmwf_ifs025=0.02+gem_seamless=0.163+gfs_hrrr=0.033+gfs_seamless=0.033+icon_seamless=0.021+knmi_seamless=0.062+meteofrance_seamless=0.098+metno_seamless=0.062+ncep_nbm_conus=0.006+ukmo_seamless=0.113 | 2349 |  4.31 |   3.90 |   0.77 | ridge              |            2.05 |      705.00 |                   2.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 2349 |  4.89 |   4.48 |   0.75 | ridge              |            2.05 |      705.00 |                   2.09 |
| icon_seamless                                                                                                                                                                                                 | 2349 |  5.31 |   4.84 |   0.76 | ridge              |            2.07 |      705.00 |                   2.04 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                               | 2349 |  3.80 |   3.01 |   0.76 | ridge              |            2.09 |      705.00 |                   2.02 |
| ncep_nbm_conus                                                                                                                                                                                                | 2349 |  3.55 |   2.48 |   0.73 | ridge              |            2.14 |      705.00 |                   2.01 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                             | 2349 |  3.33 |   2.09 |   0.74 | ridge              |            2.15 |      705.00 |                   2.11 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                                | 2349 |  3.77 |   2.77 |   0.73 | ridge              |            2.16 |      705.00 |                   2.15 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                              | 2349 |  4.08 |   3.46 |   0.75 | ridge              |            2.17 |      705.00 |                   2.13 |
| meteofrance_seamless                                                                                                                                                                                          | 2349 |  5.49 |   5.13 |   0.67 | ridge              |            2.22 |      705.00 |                   1.95 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                         | 2349 |  3.98 |   3.09 |   0.72 | ridge              |            2.22 |      705.00 |                   2.29 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                 | 2349 |  4.20 |   3.30 |   0.70 | ridge              |            2.23 |      705.00 |                   2.25 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                    | 2349 |  4.49 |   3.57 |   0.68 | ridge              |            2.28 |      705.00 |                   2.37 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                            | 2349 |  3.68 |   2.77 |   0.71 | ridge              |            2.28 |      705.00 |                   2.31 |
| gem_seamless                                                                                                                                                                                                  | 2349 |  3.84 |   1.70 |   0.69 | ridge              |            2.37 |      705.00 |                   2.37 |
| best_match                                                                                                                                                                                                    | 2349 |  5.14 |   4.12 |   0.64 | ridge              |            2.39 |      705.00 |                   2.57 |
| gfs_hrrr                                                                                                                                                                                                      | 2349 |  5.14 |   4.12 |   0.64 | ridge              |            2.39 |      705.00 |                   2.57 |
| gfs_seamless                                                                                                                                                                                                  | 2349 |  5.14 |   4.12 |   0.64 | ridge              |            2.39 |      705.00 |                   2.57 |
| ukmo_seamless                                                                                                                                                                                                 | 2349 |  4.15 |   3.05 |   0.64 | ridge              |            2.50 |      705.00 |                   2.65 |

### humidity_pct

| candidate                                                                                                                                                                                                     |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 545 |  6.36 |   3.74 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 545 |  6.86 |   4.33 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 545 |  6.86 |   4.33 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                    | 545 |  7.01 |   4.02 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                         | 545 |  7.02 |   4.57 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.02+gem_seamless=0.163+gfs_hrrr=0.033+gfs_seamless=0.033+icon_seamless=0.021+knmi_seamless=0.062+meteofrance_seamless=0.098+metno_seamless=0.062+ncep_nbm_conus=0.006+ukmo_seamless=0.113 | 545 |  7.31 |   4.19 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                                | 545 |  7.33 |   5.00 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                                                                    | 545 |  7.42 |   1.34 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                      | 545 |  7.42 |   1.34 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                  | 545 |  7.42 |   1.34 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                 | 545 |  7.56 |   5.36 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                         | 545 |  7.62 |   4.58 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                  | 545 |  7.68 |   3.75 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                 | 545 |  7.71 |   3.32 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                               | 545 |  8.15 |   5.66 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.011+gfs_seamless=0.011+icon_seamless=0.202+jma_seamless=0.019+knmi_seamless=0.047+metno_seamless=0.047+ncep_nbm_conus=0.034                                                                  | 545 |  8.42 |   5.80 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                 | 545 |  8.48 |   5.78 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                                                          | 545 |  8.95 |   3.66 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                               | 545 |  9.05 |   6.65 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                             | 545 |  9.19 |   6.82 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                  | 545 |  9.25 |   4.26 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 545 |  9.48 |   6.96 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                            | 545 |  9.82 |   7.84 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                 | 545 |  9.82 |   6.30 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                              | 545 | 10.00 |   7.42 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                            | 545 | 10.60 |   7.98 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                                | 545 | 11.03 |   9.39 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                 | 545 | 12.86 |   6.57 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                  | 545 | 15.08 |  11.52 |    nan |                nan |             nan |         nan |                    nan |

### precip_in

| candidate                                                                                                                                                                                                     |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                                                                                                                                                    | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                      | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                  | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                         | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                    | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.02+gem_seamless=0.163+gfs_hrrr=0.033+gfs_seamless=0.033+icon_seamless=0.021+knmi_seamless=0.062+meteofrance_seamless=0.098+metno_seamless=0.062+ncep_nbm_conus=0.006+ukmo_seamless=0.113 | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                         | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                 | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                                | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                 | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.011+gfs_seamless=0.011+icon_seamless=0.202+jma_seamless=0.019+knmi_seamless=0.047+metno_seamless=0.047+ncep_nbm_conus=0.034                                                                  | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                              | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                               | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                 | 2762 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                               | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                            | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                                                          | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                             | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                  | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                            | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                 | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                  | 2762 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                                | 2762 |  0.01 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                 | 2762 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                  | 2762 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                                                                                                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                 | 9934 |  1.45 |  -0.63 |   0.95 | bias               |            1.02 |     2980.00 |                   0.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                         | 9934 |  1.48 |  -0.67 |   0.95 | bias               |            1.02 |     2980.00 |                   0.29 |
| stack:ecmwf_ifs025=0.02+gem_seamless=0.163+gfs_hrrr=0.033+gfs_seamless=0.033+icon_seamless=0.021+knmi_seamless=0.062+meteofrance_seamless=0.098+metno_seamless=0.062+ncep_nbm_conus=0.006+ukmo_seamless=0.113 | 9934 |  1.44 |  -0.62 |   0.95 | bias               |            1.03 |     2980.00 |                   0.29 |
| ecmwf_ifs025                                                                                                                                                                                                  | 9934 |  1.36 |  -0.49 |   0.95 | bias               |            1.03 |     2980.00 |                   0.30 |
| knmi_seamless                                                                                                                                                                                                 | 9934 |  1.36 |  -0.49 |   0.95 | bias               |            1.04 |     2980.00 |                   0.34 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                              | 9934 |  1.57 |  -0.76 |   0.95 | bias               |            1.04 |     2980.00 |                   0.35 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 9934 |  1.47 |  -0.65 |   0.95 | bias               |            1.04 |     2980.00 |                   0.31 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 9934 |  1.47 |  -0.65 |   0.95 | bias               |            1.04 |     2980.00 |                   0.31 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 9934 |  1.29 |  -0.44 |   0.95 | bias               |            1.05 |     2980.00 |                   0.36 |
| stack:gfs_hrrr=0.011+gfs_seamless=0.011+icon_seamless=0.202+jma_seamless=0.019+knmi_seamless=0.047+metno_seamless=0.047+ncep_nbm_conus=0.034                                                                  | 9934 |  1.33 |  -0.48 |   0.95 | bias               |            1.06 |     2980.00 |                   0.35 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                               | 9934 |  1.26 |  -0.38 |   0.95 | bias               |            1.06 |     2980.00 |                   0.35 |
| meteofrance_seamless                                                                                                                                                                                          | 9934 |  1.28 |  -0.31 |   0.95 | bias               |            1.08 |     2980.00 |                   0.31 |
| jma_seamless                                                                                                                                                                                                  | 9934 |  1.47 |  -0.63 |   0.95 | bias               |            1.10 |     2980.00 |                   0.42 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                               | 9934 |  1.23 |  -0.32 |   0.95 | bias               |            1.12 |     2980.00 |                   0.41 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                            | 9934 |  1.28 |  -0.36 |   0.95 | bias               |            1.13 |     2980.00 |                   0.43 |
| icon_seamless                                                                                                                                                                                                 | 9934 |  1.28 |  -0.36 |   0.95 | bias               |            1.13 |     2980.00 |                   0.43 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                             | 9934 |  1.21 |  -0.28 |   0.95 | bias               |            1.16 |     2980.00 |                   0.42 |
| gem_seamless                                                                                                                                                                                                  | 9934 |  1.21 |  -0.28 |   0.95 | bias               |            1.16 |     2980.00 |                   0.42 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                                | 9934 |  1.61 |  -0.80 |   0.94 | raw                |            1.57 |     2980.00 |                   0.81 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 9934 |  1.71 |  -0.91 |   0.94 | raw                |            1.63 |     2980.00 |                   0.90 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                         | 9934 |  1.81 |  -1.02 |   0.94 | raw                |            1.74 |     2980.00 |                   0.98 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                            | 9934 |  1.92 |  -1.16 |   0.94 | raw                |            1.86 |     2980.00 |                   1.12 |
| ukmo_seamless                                                                                                                                                                                                 | 9934 |  1.92 |  -1.16 |   0.94 | raw                |            1.86 |     2980.00 |                   1.12 |
| best_match                                                                                                                                                                                                    | 9934 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2980.00 |                   1.21 |
| gfs_seamless                                                                                                                                                                                                  | 9934 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2980.00 |                   1.21 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                 | 9934 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2980.00 |                   1.21 |
| gfs_hrrr                                                                                                                                                                                                      | 9934 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2980.00 |                   1.21 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                    | 9934 |  2.11 |  -1.32 |   0.94 | raw                |            2.00 |     2980.00 |                   1.21 |

### temp_f

| candidate                                                                                                                                                                                                     |   n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| meteofrance_seamless                                                                                                                                                                                          | 545 |  2.42 |  -0.59 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                                                                  | 545 |  2.75 |  -2.20 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                                                                 | 545 |  2.94 |  -1.84 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 545 |  3.08 |  -2.49 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 545 |  3.08 |  -2.49 |    nan |                nan |             nan |         nan |                    nan |
| stack:ecmwf_ifs025=0.02+gem_seamless=0.163+gfs_hrrr=0.033+gfs_seamless=0.033+icon_seamless=0.021+knmi_seamless=0.062+meteofrance_seamless=0.098+metno_seamless=0.062+ncep_nbm_conus=0.006+ukmo_seamless=0.113 | 545 |  3.11 |  -2.42 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 545 |  3.11 |  -2.56 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                         | 545 |  3.13 |  -2.67 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                               | 545 |  3.14 |  -2.56 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                                | 545 |  3.34 |  -2.92 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                             | 545 |  3.41 |  -2.93 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                    | 545 |  3.42 |  -3.04 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                 | 545 |  3.44 |  -2.97 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                 | 545 |  3.46 |  -3.12 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                                                                  | 545 |  3.51 |  -2.52 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 545 |  3.53 |  -3.12 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                         | 545 |  3.53 |  -3.12 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                                                                      | 545 |  3.54 |  -2.90 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                                                                  | 545 |  3.54 |  -2.90 |    nan |                nan |             nan |         nan |                    nan |
| best_match                                                                                                                                                                                                    | 545 |  3.54 |  -2.90 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                               | 545 |  3.67 |  -3.24 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.011+gfs_seamless=0.011+icon_seamless=0.202+jma_seamless=0.019+knmi_seamless=0.047+metno_seamless=0.047+ncep_nbm_conus=0.034                                                                  | 545 |  3.72 |  -3.26 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                                                                | 545 |  3.76 |  -3.34 |    nan |                nan |             nan |         nan |                    nan |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                            | 545 |  3.92 |  -3.64 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                            | 545 |  3.96 |  -3.60 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                              | 545 |  3.99 |  -3.72 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                                                                 | 545 |  4.32 |  -3.87 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                                                                  | 545 |  4.34 |  -4.02 |    nan |                nan |             nan |         nan |                    nan |
| ukmo_seamless                                                                                                                                                                                                 | 545 |  4.52 |  -3.94 |    nan |                nan |             nan |         nan |                    nan |

### wind_mph

| candidate                                                                                                                                                                                                     |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ecmwf_ifs025                                                                                                                                                                                                  | 2349 |  3.50 |   3.45 |   0.64 | ridge              |            0.72 |      705.00 |                   0.74 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 2349 |  3.09 |   3.04 |   0.61 | ridge              |            0.73 |      705.00 |                   0.71 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless                                         | 2349 |  2.74 |   2.70 |   0.62 | ridge              |            0.74 |      705.00 |                   0.73 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 2349 |  2.90 |   2.85 |   0.60 | ridge              |            0.75 |      705.00 |                   0.74 |
| blend:gem_seamless+gfs_hrrr+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                       | 2349 |  2.90 |   2.85 |   0.60 | ridge              |            0.75 |      705.00 |                   0.74 |
| knmi_seamless                                                                                                                                                                                                 | 2349 |  3.17 |   3.09 |   0.63 | ridge              |            0.75 |      705.00 |                   0.78 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                                                                    | 2349 |  3.07 |   3.02 |   0.55 | ridge              |            0.75 |      705.00 |                   0.71 |
| best_match                                                                                                                                                                                                    | 2349 |  3.30 |   3.23 |   0.53 | ridge              |            0.76 |      705.00 |                   0.74 |
| gfs_hrrr                                                                                                                                                                                                      | 2349 |  3.30 |   3.23 |   0.53 | ridge              |            0.76 |      705.00 |                   0.74 |
| gfs_seamless                                                                                                                                                                                                  | 2349 |  3.30 |   3.23 |   0.53 | ridge              |            0.76 |      705.00 |                   0.74 |
| stack:ecmwf_ifs025=0.02+gem_seamless=0.163+gfs_hrrr=0.033+gfs_seamless=0.033+icon_seamless=0.021+knmi_seamless=0.062+meteofrance_seamless=0.098+metno_seamless=0.062+ncep_nbm_conus=0.006+ukmo_seamless=0.113 | 2349 |  2.53 |   2.46 |   0.58 | ridge              |            0.77 |      705.00 |                   0.77 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                                                                 | 2349 |  2.97 |   2.91 |   0.54 | ridge              |            0.77 |      705.00 |                   0.73 |
| stack:gfs_hrrr=0.011+gfs_seamless=0.011+icon_seamless=0.202+jma_seamless=0.019+knmi_seamless=0.047+metno_seamless=0.047+ncep_nbm_conus=0.034                                                                  | 2349 |  2.75 |   2.70 |   0.61 | ridge              |            0.77 |      705.00 |                   0.75 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                                                                | 2349 |  2.76 |   2.69 |   0.54 | ridge              |            0.77 |      705.00 |                   0.74 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                         | 2349 |  2.82 |   2.75 |   0.54 | ridge              |            0.78 |      705.00 |                   0.76 |
| meteofrance_seamless                                                                                                                                                                                          | 2349 |  1.56 |   1.23 |   0.44 | ridge              |            0.79 |      705.00 |                   0.73 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus                                                                                                                                   | 2349 |  2.57 |   2.51 |   0.58 | ridge              |            0.79 |      705.00 |                   0.78 |
| blend:gem_seamless+knmi_seamless+ncep_nbm_conus                                                                                                                                                               | 2349 |  2.72 |   2.64 |   0.56 | ridge              |            0.79 |      705.00 |                   0.78 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                 | 2349 |  2.82 |   2.75 |   0.58 | ridge              |            0.80 |      705.00 |                   0.81 |
| icon_seamless                                                                                                                                                                                                 | 2349 |  2.62 |   2.54 |   0.58 | ridge              |            0.82 |      705.00 |                   0.78 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                                                               | 2349 |  2.53 |   2.46 |   0.54 | ridge              |            0.82 |      705.00 |                   0.80 |
| gem_seamless                                                                                                                                                                                                  | 2349 |  2.40 |   2.25 |   0.49 | ridge              |            0.82 |      705.00 |                   0.83 |
| jma_seamless                                                                                                                                                                                                  | 2349 |  2.22 |   2.10 |   0.50 | ridge              |            0.82 |      705.00 |                   0.82 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                                                            | 2349 |  2.63 |   2.56 |   0.54 | ridge              |            0.83 |      705.00 |                   0.79 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                                                             | 2349 |  2.53 |   2.42 |   0.49 | ridge              |            0.83 |      705.00 |                   0.81 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                                                                                                                                                              | 2349 |  2.61 |   2.53 |   0.51 | ridge              |            0.85 |      705.00 |                   0.85 |
| ncep_nbm_conus                                                                                                                                                                                                | 2349 |  2.74 |   2.59 |   0.46 | ridge              |            0.86 |      705.00 |                   0.82 |
| blend:ncep_nbm_conus+ukmo_seamless                                                                                                                                                                            | 2349 |  2.65 |   2.53 |   0.46 | ridge              |            0.88 |      705.00 |                   0.89 |
| ukmo_seamless                                                                                                                                                                                                 | 2349 |  2.70 |   2.47 |   0.41 | ridge              |            0.91 |      705.00 |                   0.97 |

## Regional skill — KHIE, Whitefield NH, every season

Ranks models with 13k hours and two winters; the site record above decides. KHIE is 16 km east and is not this hollow: over the hours both stations recorded, temperature correlates 0.88 and dew point 0.92, but wind only 0.57.

### dewpoint_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13903 |  1.96 |   0.80 |   2.64 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13903 |  1.99 |   0.46 |   2.63 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13903 |  2.00 |   0.62 |   2.72 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13903 |  2.04 |   0.91 |   2.69 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13903 |  2.06 |   0.27 |   2.76 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13903 |  2.08 |   0.98 |   2.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13903 |  2.09 |   0.92 |   2.88 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13903 |  2.10 |   0.52 |   2.74 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13903 |  2.16 |   1.21 |   2.96 |
| ncep_nbm_conus                                                                | 13766 |  2.16 |   0.21 |   2.83 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13903 |  2.24 |   0.63 |   2.93 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13903 |  2.27 |   1.23 |   3.13 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13903 |  2.34 |   1.56 |   3.22 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13903 |  2.39 |   1.67 |   3.07 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13903 |  2.46 |   1.72 |   3.38 |
| gem_seamless                                                                  | 13903 |  2.52 |   0.32 |   3.43 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13903 |  2.53 |   1.47 |   3.39 |
| knmi_seamless                                                                 | 13903 |  2.54 |   1.32 |   3.41 |
| metno_seamless                                                                | 13903 |  2.54 |   1.32 |   3.41 |
| best_match                                                                    | 13903 |  2.75 |   0.83 |   3.57 |
| gfs_hrrr                                                                      | 13903 |  2.75 |   0.83 |   3.57 |
| gfs_seamless                                                                  | 13903 |  2.75 |   0.83 |   3.57 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13903 |  2.82 |   2.23 |   3.66 |
| icon_seamless                                                                 | 13903 |  3.06 |   2.22 |   4.17 |
| jma_seamless                                                                  | 13903 |  3.26 |   1.94 |   4.33 |
| ecmwf_ifs025                                                                  | 13903 |  3.31 |   2.75 |   4.24 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13903 |  3.58 |   3.18 |   4.53 |
| ukmo_seamless                                                                 | 13903 |  3.67 |   2.69 |   4.84 |
| ecmwf_aifs025_single                                                          | 13903 |  3.97 |   3.60 |   4.97 |
| meteofrance_seamless                                                          | 13903 |  7.30 |   7.11 |   8.38 |

### gust_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| gem_seamless                                                                  | 13792 |  4.58 |   3.04 |   6.55 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13792 |  4.76 |   3.46 |   6.22 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13792 |  5.24 |   4.27 |   6.61 |
| ncep_nbm_conus                                                                | 13658 |  5.31 |   3.89 |   6.72 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13792 |  5.78 |   4.87 |   7.11 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13792 |  5.85 |   4.89 |   7.30 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13792 |  5.85 |   5.08 |   7.19 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13792 |  5.98 |   5.14 |   7.30 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13792 |  6.09 |   5.22 |   7.67 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13792 |  6.25 |   5.29 |   7.55 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13792 |  6.50 |   5.78 |   7.78 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13792 |  6.58 |   5.96 |   7.87 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13792 |  6.62 |   5.79 |   7.94 |
| best_match                                                                    | 13792 |  6.66 |   5.88 |   8.61 |
| gfs_seamless                                                                  | 13792 |  6.66 |   5.88 |   8.61 |
| gfs_hrrr                                                                      | 13792 |  6.66 |   5.88 |   8.61 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13792 |  6.85 |   6.09 |   8.10 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13792 |  7.06 |   6.53 |   8.42 |
| ukmo_seamless                                                                 | 13792 |  7.47 |   6.68 |   8.89 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13792 |  7.50 |   7.12 |   8.97 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13792 |  7.63 |   7.05 |   8.87 |
| icon_seamless                                                                 | 13792 |  8.25 |   7.68 |   9.75 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13792 |  8.69 |   8.36 |  10.13 |
| metno_seamless                                                                | 13792 |  8.92 |   8.49 |  10.33 |
| knmi_seamless                                                                 | 13792 |  8.92 |   8.49 |  10.33 |
| meteofrance_seamless                                                          | 13792 | 10.12 |   9.67 |  12.04 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13792 | 13.75 |  13.68 |  15.45 |
| ecmwf_ifs025                                                                  | 13792 | 13.75 |  13.68 |  15.45 |

### humidity_pct

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13903 |  7.01 |   0.01 |   9.04 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13903 |  7.07 |   1.54 |   9.22 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13903 |  7.28 |  -0.71 |   9.45 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13903 |  7.51 |  -1.48 |   9.74 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13903 |  7.59 |  -2.02 |   9.97 |
| ncep_nbm_conus                                                                | 13766 |  7.59 |  -1.03 |  10.00 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13903 |  8.17 |  -2.90 |  10.76 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13903 |  8.21 |  -2.49 |  10.77 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13903 |  8.38 |  -2.64 |  10.91 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13903 |  8.57 |  -2.51 |  11.03 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13903 |  8.59 |  -2.85 |  11.29 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13903 |  8.59 |  -1.91 |  10.87 |
| ukmo_seamless                                                                 | 13903 |  8.72 |   4.01 |  11.63 |
| icon_seamless                                                                 | 13903 |  8.75 |  -3.01 |  11.68 |
| metno_seamless                                                                | 13903 |  8.81 |  -1.78 |  11.61 |
| knmi_seamless                                                                 | 13903 |  8.81 |  -1.78 |  11.61 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13903 |  8.81 |  -2.51 |  11.22 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13903 |  9.01 |  -3.22 |  11.63 |
| jma_seamless                                                                  | 13903 |  9.04 |   3.01 |  11.82 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13903 |  9.58 |  -1.71 |  12.51 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13903 |  9.63 |  -2.99 |  12.25 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13903 |  9.67 |  -2.61 |  12.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13903 |  9.79 |  -0.25 |  12.56 |
| ecmwf_aifs025_single                                                          | 13903 |  9.81 |  -1.14 |  12.67 |
| ecmwf_ifs025                                                                  | 13903 | 10.23 |   0.64 |  13.06 |
| gem_seamless                                                                  | 13903 | 10.88 |  -4.62 |  14.86 |
| gfs_hrrr                                                                      | 13903 | 11.73 |  -3.96 |  14.91 |
| gfs_seamless                                                                  | 13903 | 11.73 |  -3.96 |  14.91 |
| best_match                                                                    | 13903 | 11.73 |  -3.96 |  14.91 |
| meteofrance_seamless                                                          | 13903 | 11.89 |   2.64 |  14.81 |

### temp_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13903 |  3.06 |   1.12 |   4.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13903 |  3.06 |   1.54 |   4.13 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13903 |  3.10 |   1.36 |   4.12 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13903 |  3.11 |   1.55 |   4.25 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13903 |  3.12 |   1.39 |   4.22 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13903 |  3.16 |   1.40 |   4.26 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13903 |  3.18 |   1.37 |   4.30 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13903 |  3.18 |   1.57 |   4.33 |
| ncep_nbm_conus                                                                | 13766 |  3.22 |   0.38 |   4.06 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13903 |  3.26 |   1.16 |   4.36 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13903 |  3.29 |   1.63 |   4.42 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13903 |  3.31 |   0.68 |   4.25 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13903 |  3.32 |   1.84 |   4.55 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13903 |  3.33 |   1.80 |   4.45 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13903 |  3.36 |   1.52 |   4.44 |
| gfs_hrrr                                                                      | 13903 |  3.38 |   1.85 |   4.50 |
| gfs_seamless                                                                  | 13903 |  3.38 |   1.85 |   4.50 |
| best_match                                                                    | 13903 |  3.38 |   1.85 |   4.50 |
| metno_seamless                                                                | 13903 |  3.39 |   1.80 |   4.66 |
| knmi_seamless                                                                 | 13903 |  3.39 |   1.80 |   4.66 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13903 |  3.50 |   2.35 |   4.93 |
| jma_seamless                                                                  | 13903 |  3.57 |   0.56 |   4.74 |
| gem_seamless                                                                  | 13903 |  3.72 |   1.92 |   5.34 |
| ukmo_seamless                                                                 | 13903 |  3.77 |   0.98 |   4.94 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13903 |  3.90 |   2.68 |   5.63 |
| ecmwf_ifs025                                                                  | 13903 |  4.06 |   2.33 |   5.70 |
| icon_seamless                                                                 | 13903 |  4.11 |   3.19 |   5.69 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13903 |  4.28 |   3.07 |   6.08 |
| ecmwf_aifs025_single                                                          | 13903 |  4.75 |   3.81 |   6.64 |
| meteofrance_seamless                                                          | 13903 |  6.35 |   5.99 |   8.23 |

### wind_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| ncep_nbm_conus                                                                | 13658 |  2.12 |   0.09 |   3.17 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13792 |  2.28 |   0.17 |   3.01 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13792 |  2.31 |   0.52 |   2.99 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13792 |  2.34 |   0.67 |   2.97 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13792 |  2.36 |   0.42 |   2.98 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13792 |  2.37 |   0.53 |   2.95 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13792 |  2.38 |   0.61 |   3.02 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13792 |  2.42 |   0.50 |   3.09 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13792 |  2.44 |   0.61 |   3.01 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13792 |  2.45 |   0.64 |   3.04 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13792 |  2.46 |   0.87 |   3.06 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13792 |  2.47 |   0.91 |   3.03 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13792 |  2.49 |   0.75 |   3.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13792 |  2.52 |   1.12 |   3.07 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13792 |  2.53 |   0.98 |   3.10 |
| icon_seamless                                                                 | 13792 |  2.61 |   0.94 |   3.18 |
| gem_seamless                                                                  | 13792 |  2.62 |   0.24 |   3.30 |
| jma_seamless                                                                  | 13792 |  2.67 |   0.29 |   3.31 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13792 |  2.70 |   1.40 |   3.23 |
| metno_seamless                                                                | 13792 |  2.78 |   1.48 |   3.43 |
| knmi_seamless                                                                 | 13792 |  2.78 |   1.48 |   3.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13792 |  2.79 |   1.50 |   3.41 |
| gfs_hrrr                                                                      | 13792 |  2.79 |   1.26 |   3.41 |
| best_match                                                                    | 13792 |  2.79 |   1.26 |   3.41 |
| gfs_seamless                                                                  | 13792 |  2.79 |   1.26 |   3.41 |
| ukmo_seamless                                                                 | 13792 |  2.84 |   0.90 |   3.47 |
| ecmwf_aifs025_single                                                          | 13792 |  2.93 |   1.64 |   3.65 |
| meteofrance_seamless                                                          | 13792 |  3.08 |  -0.64 |   3.92 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13792 |  3.10 |   2.12 |   3.83 |
| ecmwf_ifs025                                                                  | 13792 |  3.37 |   2.60 |   4.17 |

## Regional MAE by season (temperature)

| candidate                                                                     |   fall |   spring |   summer |   winter |
|:------------------------------------------------------------------------------|-------:|---------:|---------:|---------:|
| best_match                                                                    |   3.47 |     3.05 |     3.51 |     3.54 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       |   4.54 |     3.67 |     4.34 |     4.74 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          |   4.15 |     3.34 |     3.95 |     4.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    |   3.71 |     3.02 |     3.61 |     3.75 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         |   3.32 |     2.85 |     3.28 |     3.16 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   |   3.30 |     2.72 |     3.21 |     3.18 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                |   3.28 |     2.87 |     3.16 |     3.17 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   |   3.30 |     3.02 |     3.11 |     3.38 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               |   3.44 |     3.04 |     3.25 |     3.68 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              |   3.42 |     2.85 |     3.19 |     3.26 |
| blend:gem_seamless+ncep_nbm_conus                                             |   3.51 |     3.04 |     3.17 |     3.32 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       |   3.23 |     2.70 |     3.23 |     3.06 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    |   3.18 |     2.88 |     3.22 |     3.10 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 |   3.18 |     2.87 |     3.14 |     2.98 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless |   3.45 |     2.93 |     3.36 |     3.44 |
| blend:icon_seamless+ncep_nbm_conus                                            |   3.42 |     3.17 |     3.21 |     3.71 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              |   3.49 |     3.15 |     3.33 |     3.52 |
| blend:ncep_nbm_conus+ukmo_seamless                                            |   3.57 |     3.13 |     3.33 |     3.11 |
| ecmwf_aifs025_single                                                          |   4.96 |     4.07 |     4.94 |     5.14 |
| ecmwf_ifs025                                                                  |   4.38 |     3.54 |     3.96 |     4.56 |
| gem_seamless                                                                  |   3.85 |     3.44 |     3.64 |     4.06 |
| gfs_hrrr                                                                      |   3.47 |     3.05 |     3.51 |     3.54 |
| gfs_seamless                                                                  |   3.47 |     3.05 |     3.51 |     3.54 |
| icon_seamless                                                                 |   4.02 |     3.90 |     3.85 |     5.16 |
| jma_seamless                                                                  |   3.31 |     3.92 |     3.28 |     4.02 |
| knmi_seamless                                                                 |   3.60 |     2.88 |     3.55 |     3.57 |
| meteofrance_seamless                                                          |   6.83 |     5.21 |     6.08 |     7.95 |
| metno_seamless                                                                |   3.60 |     2.88 |     3.55 |     3.57 |
| ncep_nbm_conus                                                                |   3.54 |     3.12 |     3.09 |     3.07 |
| ukmo_seamless                                                                 |   4.06 |     3.46 |     3.92 |     3.49 |

## MAE by lead time, days 1-7 (previous-runs, site)

### gust_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 7.24 |   3.72 |   4.25 |   4.41 |   4.58 |   4.97 |   4.57 |
| gem_seamless         | 4.24 |   3.81 |   4.22 |   4.25 |   4.64 |   4.78 |   5.23 |
| gfs_hrrr             | 7.24 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 7.24 |   3.72 |   4.25 |   4.41 |   4.58 |   4.97 |   4.57 |
| icon_seamless        | 5.42 |   5.56 |   5.66 |   6.05 |   6.23 |   7.16 | nan    |
| meteofrance_seamless | 5.40 |   5.24 |   5.51 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.70 |   3.95 |   4.22 |   4.28 |   4.29 |   4.28 |   4.17 |
| ukmo_seamless        | 4.87 |   5.09 |   5.10 |   5.29 |   4.96 |   5.92 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           |  7.90 |  11.64 |  11.96 |  12.09 |  12.87 |  14.24 |  16.48 |
| ecmwf_aifs025_single |  7.13 |   7.99 |   9.34 |   9.60 |   9.70 |  10.27 |  11.56 |
| ecmwf_ifs025         |  8.73 |   9.88 |  10.64 |  10.70 |  11.77 |  14.06 |  14.19 |
| gem_seamless         |  9.11 |  12.22 |  10.89 |  11.63 |  11.84 |  12.44 |  13.89 |
| gfs_hrrr             |  7.90 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         |  7.90 |  11.64 |  11.96 |  12.09 |  12.87 |  14.24 |  16.48 |
| icon_seamless        | 10.03 |  10.32 |  10.70 |  11.67 |  13.19 |  12.76 | nan    |
| jma_seamless         | 14.83 |  15.10 |  15.52 |  16.15 |  16.21 |  16.34 |  14.96 |
| knmi_seamless        |  8.96 |  10.04 |  10.75 |  11.01 |  12.54 |  14.69 |  14.74 |
| meteofrance_seamless |  9.94 |  10.55 |  11.38 | nan    | nan    | nan    | nan    |
| metno_seamless       |  8.96 |  10.04 |  10.75 |  11.01 |  12.54 |  14.69 |  14.74 |
| ncep_nbm_conus       | 12.15 |  12.43 |  13.26 |  13.68 |  14.32 |  15.73 |  16.62 |
| ukmo_seamless        | 14.48 |  15.42 |  16.57 |  18.30 |  17.52 |  19.05 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 3.05 |   3.86 |   4.17 |   4.37 |   5.16 |   5.73 |   6.26 |
| ecmwf_aifs025_single | 2.89 |   2.95 |   3.35 |   3.49 |   3.66 |   3.94 |   4.07 |
| ecmwf_ifs025         | 2.70 |   2.93 |   3.14 |   3.62 |   3.95 |   5.02 |   4.73 |
| gem_seamless         | 3.72 |   5.58 |   3.99 |   4.27 |   4.86 |   5.25 |   6.14 |
| gfs_hrrr             | 3.05 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 3.05 |   3.86 |   4.17 |   4.37 |   5.16 |   5.73 |   6.26 |
| icon_seamless        | 4.71 |   4.82 |   4.84 |   4.99 |   5.22 |   6.28 | nan    |
| jma_seamless         | 4.54 |   4.91 |   5.04 |   5.10 |   5.87 |   6.96 |   7.89 |
| knmi_seamless        | 2.90 |   3.10 |   3.20 |   3.67 |   4.16 |   5.28 |   5.01 |
| meteofrance_seamless | 2.82 |   3.13 |   3.44 | nan    | nan    | nan    | nan    |
| metno_seamless       | 2.90 |   3.10 |   3.20 |   3.67 |   4.16 |   5.28 |   5.01 |
| ncep_nbm_conus       | 3.90 |   4.09 |   4.49 |   4.80 |   5.25 |   5.57 |   6.15 |
| ukmo_seamless        | 4.46 |   4.48 |   4.58 |   4.61 |   5.04 |   5.22 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.37 |   2.58 |   2.63 |   2.72 |   2.69 |   2.62 |   2.39 |
| ecmwf_aifs025_single | 3.46 |   3.48 |   3.43 |   3.41 |   3.44 |   3.58 |   3.56 |
| ecmwf_ifs025         | 3.71 |   3.74 |   3.60 |   3.85 |   3.87 |   3.86 |   3.69 |
| gem_seamless         | 2.62 |   2.16 |   2.05 |   2.03 |   2.04 |   2.02 |   2.14 |
| gfs_hrrr             | 4.37 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.37 |   2.58 |   2.63 |   2.72 |   2.69 |   2.62 |   2.39 |
| icon_seamless        | 2.72 |   2.82 |   2.83 |   2.93 |   2.89 |   3.34 | nan    |
| jma_seamless         | 2.23 |   2.31 |   2.42 |   2.43 |   2.50 |   2.36 |   2.25 |
| knmi_seamless        | 3.35 |   3.39 |   3.34 |   3.56 |   3.65 |   3.60 |   3.50 |
| meteofrance_seamless | 1.57 |   1.53 |   1.62 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.35 |   3.39 |   3.34 |   3.56 |   3.65 |   3.60 |   3.50 |
| ncep_nbm_conus       | 2.86 |   2.97 |   3.07 |   3.09 |   2.89 |   2.82 |   2.58 |
| ukmo_seamless        | 2.99 |   3.10 |   3.03 |   3.05 |   2.92 |   3.33 | nan    |
