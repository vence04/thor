# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)

Site actuals: Ecowitt hourly means, 2025-08-18 to 2026-11-23.
Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).

## Source in use, per variable

| variable | source |
|---|---|
| dewpoint_f | ncep_nbm_conus |
| gust_mph | blend of knmi_seamless, metno_seamless, ncep_nbm_conus |
| humidity_pct | blend of ecmwf_aifs025_single, ecmwf_ifs025, gem_seamless, gfs_hrrr, gfs_seamless, icon_seamless, jma_seamless, knmi_seamless, meteofrance_seamless, metno_seamless, ukmo_seamless |
| precip_in | best_match |
| pressure_abs_hpa | blend of icon_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus, ukmo_seamless |
| temp_f | knmi_seamless |
| wind_mph | blend of gfs_hrrr, gfs_seamless, knmi_seamless, metno_seamless, ncep_nbm_conus |

The coming season is **winter**, and the Bear Paw station has not lived through enough of it to judge, so candidates the Whitefield record shows are clearly poor in winter are not eligible. This switches itself off per variable as the station accumulates its own winter hours.

| variable | winter hours on site | candidates ruled out |
|---|---|---|
| dewpoint_f | 0 | 14 |
| gust_mph | 0 | 23 |
| humidity_pct | 0 | 22 |
| temp_f | 0 | 9 |
| wind_mph | 0 | 12 |

## Site skill, shortlisted candidates (lower MAE = better)

### dewpoint_f

| candidate                                                                                                                                                             |   n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| meteofrance_seamless                                                                                                                                                  | 713 |  2.44 |   0.80 |   0.92 | ridge              |            1.45 |      214.00 |                   1.45 |
| ncep_nbm_conus                                                                                                                                                        | 713 |  1.46 |   0.07 |   0.94 | raw                |            1.49 |      214.00 |                   1.49 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 713 |  1.57 |  -0.89 |   0.90 | bias               |            1.58 |      214.00 |                   1.58 |
| stack:knmi_seamless=0.09+metno_seamless=0.09+ncep_nbm_conus=0.808                                                                                                     | 713 |  1.46 |  -0.09 |   0.93 | raw                |            1.59 |      214.00 |                   1.59 |
| stack:gem_seamless=0.002+icon_seamless=0.266+jma_seamless=0.068+ncep_nbm_conus=0.049                                                                                  | 713 |  1.89 |  -1.23 |   0.85 | bias               |            1.73 |      214.00 |                   1.73 |
| blend:knmi_seamless+ncep_nbm_conus                                                                                                                                    | 713 |  1.66 |  -0.39 |   0.92 | ridge              |            1.80 |      214.00 |                   1.80 |
| stack:gfs_hrrr=0.027+gfs_seamless=0.027+knmi_seamless=0.245+metno_seamless=0.245+ncep_nbm_conus=0.521                                                                 | 713 |  1.63 |  -0.49 |   0.92 | ridge              |            1.82 |      214.00 |                   1.82 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 713 |  1.94 |  -0.95 |   0.87 | bias               |            1.83 |      214.00 |                   1.83 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                     | 713 |  1.83 |  -0.54 |   0.91 | ridge              |            1.87 |      214.00 |                   1.87 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 713 |  1.64 |  -1.12 |   0.89 | ridge              |            1.96 |      214.00 |                   1.96 |
| icon_seamless                                                                                                                                                         | 713 |  2.35 |  -1.86 |   0.76 | ridge              |            2.09 |      214.00 |                   2.09 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 713 |  1.61 |  -0.75 |   0.90 | ridge              |            2.17 |      214.00 |                   2.17 |
| jma_seamless                                                                                                                                                          | 713 |  2.43 |   0.32 |   0.81 | raw                |            2.27 |      214.00 |                   2.27 |
| knmi_seamless                                                                                                                                                         | 713 |  2.27 |  -0.85 |   0.88 | raw                |            2.42 |      214.00 |                   2.42 |
| metno_seamless                                                                                                                                                        | 713 |  2.27 |  -0.85 |   0.88 | raw                |            2.42 |      214.00 |                   2.42 |
| ecmwf_ifs025                                                                                                                                                          | 713 |  2.28 |  -1.09 |   0.93 | raw                |            2.47 |      214.00 |                   2.47 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 713 |  1.82 |  -1.20 |   0.90 | raw                |            2.49 |      214.00 |                   2.49 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 713 |  1.80 |  -1.19 |   0.88 | raw                |            2.59 |      214.00 |                   2.59 |
| gem_seamless                                                                                                                                                          | 713 |  2.34 |  -1.57 |   0.80 | ridge              |            2.78 |      214.00 |                   2.78 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 713 |  2.04 |  -1.42 |   0.87 | raw                |            2.95 |      214.00 |                   2.95 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 713 |  1.79 |  -1.41 |   0.86 | raw                |            2.97 |      214.00 |                   2.97 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 713 |  1.91 |  -1.34 |   0.86 | raw                |            3.01 |      214.00 |                   3.01 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 713 |  2.37 |  -1.81 |   0.82 | raw                |            3.70 |      214.00 |                   3.70 |
| best_match                                                                                                                                                            | 713 |  3.42 |  -2.75 |   0.73 | raw                |            5.10 |      214.00 |                   5.10 |
| gfs_hrrr                                                                                                                                                              | 713 |  3.42 |  -2.75 |   0.73 | raw                |            5.10 |      214.00 |                   5.10 |
| gfs_seamless                                                                                                                                                          | 713 |  3.42 |  -2.75 |   0.73 | raw                |            5.10 |      214.00 |                   5.10 |

### gust_mph

| candidate                                                                                                                                                             |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                     | 2517 |  4.85 |   4.56 |   0.79 | ridge              |            1.77 |      755.00 |                   1.69 |
| blend:knmi_seamless+ncep_nbm_conus                                                                                                                                    | 2517 |  4.39 |   4.00 |   0.78 | ridge              |            1.78 |      755.00 |                   1.68 |
| stack:gfs_hrrr=0.027+gfs_seamless=0.027+knmi_seamless=0.245+metno_seamless=0.245+ncep_nbm_conus=0.521                                                                 | 2517 |  4.35 |   3.95 |   0.78 | ridge              |            1.78 |      755.00 |                   1.68 |
| knmi_seamless                                                                                                                                                         | 2517 |  5.87 |   5.68 |   0.78 | ridge              |            1.78 |      755.00 |                   1.76 |
| metno_seamless                                                                                                                                                        | 2517 |  5.87 |   5.68 |   0.78 | ridge              |            1.78 |      755.00 |                   1.76 |
| ecmwf_ifs025                                                                                                                                                          | 2517 |  7.13 |   7.03 |   0.78 | ridge              |            1.80 |      755.00 |                   1.82 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 2517 |  4.28 |   3.82 |   0.77 | ridge              |            1.81 |      755.00 |                   1.73 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 2517 |  4.72 |   4.31 |   0.76 | ridge              |            1.82 |      755.00 |                   1.80 |
| stack:knmi_seamless=0.09+metno_seamless=0.09+ncep_nbm_conus=0.808                                                                                                     | 2517 |  3.67 |   2.93 |   0.75 | ridge              |            1.84 |      755.00 |                   1.70 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 2517 |  4.73 |   4.45 |   0.77 | ridge              |            1.85 |      755.00 |                   1.75 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 2517 |  4.05 |   3.48 |   0.77 | ridge              |            1.88 |      755.00 |                   1.69 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 2517 |  4.56 |   4.22 |   0.77 | ridge              |            1.89 |      755.00 |                   1.77 |
| meteofrance_seamless                                                                                                                                                  | 2517 |  5.29 |   4.89 |   0.69 | ridge              |            1.91 |      755.00 |                   1.80 |
| ncep_nbm_conus                                                                                                                                                        | 2517 |  3.41 |   2.32 |   0.72 | ridge              |            1.91 |      755.00 |                   1.75 |
| stack:gem_seamless=0.002+icon_seamless=0.266+jma_seamless=0.068+ncep_nbm_conus=0.049                                                                                  | 2517 |  4.75 |   4.26 |   0.77 | ridge              |            1.92 |      755.00 |                   1.75 |
| icon_seamless                                                                                                                                                         | 2517 |  5.13 |   4.64 |   0.76 | ridge              |            1.94 |      755.00 |                   1.78 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 2517 |  3.65 |   2.82 |   0.75 | ridge              |            1.95 |      755.00 |                   1.76 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 2517 |  3.62 |   2.59 |   0.72 | ridge              |            1.97 |      755.00 |                   1.87 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 2517 |  4.03 |   3.12 |   0.70 | ridge              |            1.98 |      755.00 |                   1.94 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 2517 |  3.21 |   1.91 |   0.73 | ridge              |            2.00 |      755.00 |                   1.85 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 2517 |  4.31 |   3.39 |   0.68 | ridge              |            2.04 |      755.00 |                   2.04 |
| gfs_seamless                                                                                                                                                          | 2517 |  4.95 |   3.93 |   0.64 | ridge              |            2.16 |      755.00 |                   2.21 |
| best_match                                                                                                                                                            | 2517 |  4.95 |   3.93 |   0.64 | ridge              |            2.16 |      755.00 |                   2.21 |
| gfs_hrrr                                                                                                                                                              | 2517 |  4.95 |   3.93 |   0.64 | ridge              |            2.16 |      755.00 |                   2.21 |
| gem_seamless                                                                                                                                                          | 2517 |  3.72 |   1.51 |   0.68 | ridge              |            2.20 |      755.00 |                   2.06 |

### humidity_pct

| candidate                                                                                                                                                             |   n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 713 |  6.56 |   4.03 |   0.89 | raw                |            6.57 |      214.00 |                   6.57 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 713 |  7.17 |   4.13 |   0.86 | raw                |            6.95 |      214.00 |                   6.95 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 713 |  7.71 |   5.59 |   0.88 | raw                |            7.23 |      214.00 |                   7.23 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 713 |  7.16 |   4.81 |   0.88 | raw                |            7.27 |      214.00 |                   7.27 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 713 |  7.62 |   5.43 |   0.87 | raw                |            7.48 |      214.00 |                   7.48 |
| ecmwf_ifs025                                                                                                                                                          | 713 |  7.62 |   3.69 |   0.86 | bias               |            7.58 |      214.00 |                   7.58 |
| metno_seamless                                                                                                                                                        | 713 |  7.92 |   3.87 |   0.81 | raw                |            8.04 |      214.00 |                   8.04 |
| knmi_seamless                                                                                                                                                         | 713 |  7.92 |   3.87 |   0.81 | raw                |            8.04 |      214.00 |                   8.04 |
| best_match                                                                                                                                                            | 713 |  7.70 |   1.21 |   0.77 | raw                |            8.10 |      214.00 |                   8.10 |
| gfs_seamless                                                                                                                                                          | 713 |  7.70 |   1.21 |   0.77 | raw                |            8.10 |      214.00 |                   8.10 |
| gfs_hrrr                                                                                                                                                              | 713 |  7.70 |   1.21 |   0.77 | raw                |            8.10 |      214.00 |                   8.10 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 713 |  7.56 |   5.39 |   0.87 | raw                |            8.24 |      214.00 |                   8.24 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                     | 713 |  8.38 |   5.90 |   0.84 | raw                |            8.37 |      214.00 |                   8.37 |
| stack:gfs_hrrr=0.027+gfs_seamless=0.027+knmi_seamless=0.245+metno_seamless=0.245+ncep_nbm_conus=0.521                                                                 | 713 |  8.67 |   6.72 |   0.86 | raw                |            8.60 |      214.00 |                   8.60 |
| blend:knmi_seamless+ncep_nbm_conus                                                                                                                                    | 713 |  8.95 |   6.92 |   0.85 | raw                |            8.90 |      214.00 |                   8.90 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 713 |  9.47 |   7.45 |   0.84 | raw                |            9.23 |      214.00 |                   9.23 |
| gem_seamless                                                                                                                                                          | 713 |  9.60 |   5.12 |   0.75 | raw                |            9.40 |      214.00 |                   9.40 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 713 |  9.60 |   7.54 |   0.83 | raw                |            9.43 |      214.00 |                   9.43 |
| icon_seamless                                                                                                                                                         | 713 | 10.25 |   7.25 |   0.79 | raw                |           10.02 |      214.00 |                  10.02 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 713 | 10.31 |   8.61 |   0.85 | raw                |           10.17 |      214.00 |                  10.17 |
| stack:knmi_seamless=0.09+metno_seamless=0.09+ncep_nbm_conus=0.808                                                                                                     | 713 | 10.41 |   8.86 |   0.85 | raw                |           10.22 |      214.00 |                  10.22 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 713 |  9.30 |   6.93 |   0.80 | raw                |           10.32 |      214.00 |                  10.32 |
| stack:gem_seamless=0.002+icon_seamless=0.266+jma_seamless=0.068+ncep_nbm_conus=0.049                                                                                  | 713 | 10.91 |   8.56 |   0.81 | raw                |           10.67 |      214.00 |                  10.67 |
| ncep_nbm_conus                                                                                                                                                        | 713 | 11.45 |   9.97 |   0.84 | raw                |           11.14 |      214.00 |                  11.14 |
| meteofrance_seamless                                                                                                                                                  | 713 |  9.85 |   5.53 |   0.83 | raw                |           11.15 |      214.00 |                  11.15 |
| jma_seamless                                                                                                                                                          | 713 | 15.65 |  12.77 |   0.64 | raw                |           14.91 |      214.00 |                  14.91 |

### precip_in

| candidate                                                                                                                                                             |    n |   mae |   bias |   corr |   corrected_method |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|-------------------:|----------------:|------------:|-----------------------:|
| best_match                                                                                                                                                            | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_hrrr                                                                                                                                                              | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gfs_seamless                                                                                                                                                          | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 2930 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| meteofrance_seamless                                                                                                                                                  | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:gem_seamless=0.002+icon_seamless=0.266+jma_seamless=0.068+ncep_nbm_conus=0.049                                                                                  | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| gem_seamless                                                                                                                                                          | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:gfs_hrrr=0.027+gfs_seamless=0.027+knmi_seamless=0.245+metno_seamless=0.245+ncep_nbm_conus=0.521                                                                 | 2930 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| icon_seamless                                                                                                                                                         | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+ncep_nbm_conus                                                                                                                                    | 2930 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| stack:knmi_seamless=0.09+metno_seamless=0.09+ncep_nbm_conus=0.808                                                                                                     | 2930 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| jma_seamless                                                                                                                                                          | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                     | 2930 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ncep_nbm_conus                                                                                                                                                        | 2930 |  0.00 |  -0.00 |    nan |                nan |             nan |         nan |                    nan |
| metno_seamless                                                                                                                                                        | 2930 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| knmi_seamless                                                                                                                                                         | 2930 |  0.00 |   0.00 |    nan |                nan |             nan |         nan |                    nan |
| ecmwf_ifs025                                                                                                                                                          | 2930 |  0.01 |   0.00 |    nan |                nan |             nan |         nan |                    nan |

### pressure_abs_hpa

| candidate                                                                                                                                                             |     n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 10102 |  1.45 |  -0.64 |   0.95 | bias               |            0.96 |     3031.00 |                   0.49 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 10102 |  1.48 |  -0.68 |   0.96 | bias               |            0.97 |     3031.00 |                   0.51 |
| ecmwf_ifs025                                                                                                                                                          | 10102 |  1.35 |  -0.50 |   0.95 | bias               |            0.97 |     3031.00 |                   0.44 |
| stack:gfs_hrrr=0.027+gfs_seamless=0.027+knmi_seamless=0.245+metno_seamless=0.245+ncep_nbm_conus=0.521                                                                 | 10102 |  1.42 |  -0.58 |   0.95 | bias               |            0.98 |     3031.00 |                   0.48 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                     | 10102 |  1.35 |  -0.50 |   0.95 | bias               |            0.98 |     3031.00 |                   0.47 |
| blend:knmi_seamless+ncep_nbm_conus                                                                                                                                    | 10102 |  1.35 |  -0.50 |   0.95 | bias               |            0.98 |     3031.00 |                   0.47 |
| knmi_seamless                                                                                                                                                         | 10102 |  1.35 |  -0.50 |   0.95 | bias               |            0.98 |     3031.00 |                   0.47 |
| metno_seamless                                                                                                                                                        | 10102 |  1.35 |  -0.50 |   0.95 | bias               |            0.98 |     3031.00 |                   0.47 |
| stack:knmi_seamless=0.09+metno_seamless=0.09+ncep_nbm_conus=0.808                                                                                                     | 10102 |  1.35 |  -0.50 |   0.95 | bias               |            0.98 |     3031.00 |                   0.47 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 10102 |  1.47 |  -0.66 |   0.95 | bias               |            0.99 |     3031.00 |                   0.54 |
| jma_seamless                                                                                                                                                          | 10102 |  1.46 |  -0.63 |   0.96 | bias               |            1.02 |     3031.00 |                   0.46 |
| meteofrance_seamless                                                                                                                                                  | 10102 |  1.27 |  -0.32 |   0.96 | bias               |            1.04 |     3031.00 |                   0.60 |
| stack:gem_seamless=0.002+icon_seamless=0.266+jma_seamless=0.068+ncep_nbm_conus=0.049                                                                                  | 10102 |  1.28 |  -0.42 |   0.96 | bias               |            1.04 |     3031.00 |                   0.52 |
| icon_seamless                                                                                                                                                         | 10102 |  1.27 |  -0.37 |   0.96 | bias               |            1.08 |     3031.00 |                   0.55 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 10102 |  1.27 |  -0.37 |   0.96 | bias               |            1.08 |     3031.00 |                   0.55 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 10102 |  1.22 |  -0.33 |   0.96 | bias               |            1.08 |     3031.00 |                   0.60 |
| gem_seamless                                                                                                                                                          | 10102 |  1.21 |  -0.29 |   0.96 | bias               |            1.12 |     3031.00 |                   0.67 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 10102 |  1.21 |  -0.29 |   0.96 | bias               |            1.12 |     3031.00 |                   0.67 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 10102 |  1.62 |  -0.82 |   0.95 | raw                |            1.57 |     3031.00 |                   1.34 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 10102 |  1.72 |  -0.92 |   0.95 | raw                |            1.63 |     3031.00 |                   1.38 |
| gfs_seamless                                                                                                                                                          | 10102 |  2.13 |  -1.35 |   0.95 | raw                |            2.04 |     3031.00 |                   2.02 |
| gfs_hrrr                                                                                                                                                              | 10102 |  2.13 |  -1.35 |   0.95 | raw                |            2.04 |     3031.00 |                   2.02 |
| best_match                                                                                                                                                            | 10102 |  2.13 |  -1.35 |   0.95 | raw                |            2.04 |     3031.00 |                   2.02 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 10102 |  2.13 |  -1.35 |   0.95 | raw                |            2.04 |     3031.00 |                   2.02 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 10102 |  2.13 |  -1.35 |   0.95 | raw                |            2.04 |     3031.00 |                   2.02 |

### temp_f

| candidate                                                                                                                                                             |   n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| meteofrance_seamless                                                                                                                                                  | 713 |  2.83 |  -1.31 |   0.93 | raw                |            3.42 |      214.00 |                   3.42 |
| ecmwf_ifs025                                                                                                                                                          | 713 |  3.05 |  -2.54 |   0.93 | raw                |            3.56 |      214.00 |                   3.56 |
| knmi_seamless                                                                                                                                                         | 713 |  3.36 |  -2.42 |   0.88 | raw                |            4.13 |      214.00 |                   4.13 |
| metno_seamless                                                                                                                                                        | 713 |  3.36 |  -2.42 |   0.88 | raw                |            4.13 |      214.00 |                   4.13 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                     | 713 |  3.48 |  -2.89 |   0.90 | raw                |            4.27 |      214.00 |                   4.27 |
| blend:knmi_seamless+ncep_nbm_conus                                                                                                                                    | 713 |  3.62 |  -3.12 |   0.91 | raw                |            4.36 |      214.00 |                   4.36 |
| stack:gfs_hrrr=0.027+gfs_seamless=0.027+knmi_seamless=0.245+metno_seamless=0.245+ncep_nbm_conus=0.521                                                                 | 713 |  3.64 |  -3.17 |   0.91 | raw                |            4.41 |      214.00 |                   4.41 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 713 |  3.69 |  -3.22 |   0.90 | raw                |            4.62 |      214.00 |                   4.62 |
| stack:knmi_seamless=0.09+metno_seamless=0.09+ncep_nbm_conus=0.808                                                                                                     | 713 |  3.97 |  -3.56 |   0.92 | raw                |            4.64 |      214.00 |                   4.64 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 713 |  3.68 |  -3.18 |   0.90 | raw                |            4.67 |      214.00 |                   4.67 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 713 |  3.76 |  -3.39 |   0.90 | raw                |            4.76 |      214.00 |                   4.76 |
| ncep_nbm_conus                                                                                                                                                        | 713 |  4.20 |  -3.81 |   0.92 | raw                |            4.81 |      214.00 |                   4.81 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 713 |  4.07 |  -3.76 |   0.90 | raw                |            4.96 |      214.00 |                   4.96 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 713 |  4.07 |  -3.75 |   0.89 | raw                |            5.03 |      214.00 |                   5.03 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 713 |  4.09 |  -3.71 |   0.89 | raw                |            5.13 |      214.00 |                   5.13 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 713 |  4.08 |  -3.68 |   0.88 | raw                |            5.15 |      214.00 |                   5.15 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 713 |  4.05 |  -3.69 |   0.88 | raw                |            5.15 |      214.00 |                   5.15 |
| jma_seamless                                                                                                                                                          | 713 |  4.79 |  -4.43 |   0.88 | raw                |            5.21 |      214.00 |                   5.21 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 713 |  4.53 |  -4.23 |   0.90 | raw                |            5.25 |      214.00 |                   5.25 |
| gfs_hrrr                                                                                                                                                              | 713 |  4.23 |  -3.72 |   0.86 | raw                |            5.27 |      214.00 |                   5.27 |
| best_match                                                                                                                                                            | 713 |  4.23 |  -3.72 |   0.86 | raw                |            5.27 |      214.00 |                   5.27 |
| gfs_seamless                                                                                                                                                          | 713 |  4.23 |  -3.72 |   0.86 | raw                |            5.27 |      214.00 |                   5.27 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 713 |  4.35 |  -4.00 |   0.88 | raw                |            5.35 |      214.00 |                   5.35 |
| stack:gem_seamless=0.002+icon_seamless=0.266+jma_seamless=0.068+ncep_nbm_conus=0.049                                                                                  | 713 |  4.79 |  -4.50 |   0.87 | raw                |            5.57 |      214.00 |                   5.57 |
| gem_seamless                                                                                                                                                          | 713 |  4.34 |  -3.55 |   0.81 | raw                |            5.66 |      214.00 |                   5.66 |
| icon_seamless                                                                                                                                                         | 713 |  5.03 |  -4.65 |   0.83 | raw                |            5.94 |      214.00 |                   5.94 |

### wind_mph

| candidate                                                                                                                                                             |    n |   mae |   bias |   corr | corrected_method   |   corrected_mae |   holdout_n |   corrected_recent_mae |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----:|------:|-------:|-------:|:-------------------|----------------:|------------:|-----------------------:|
| ecmwf_ifs025                                                                                                                                                          | 2517 |  3.41 |   3.36 |   0.59 | ridge              |            0.70 |      755.00 |                   0.68 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                               | 2517 |  3.01 |   2.96 |   0.59 | ridge              |            0.71 |      755.00 |                   0.66 |
| metno_seamless                                                                                                                                                        | 2517 |  3.10 |   3.01 |   0.61 | ridge              |            0.71 |      755.00 |                   0.69 |
| knmi_seamless                                                                                                                                                         | 2517 |  3.10 |   3.01 |   0.61 | ridge              |            0.71 |      755.00 |                   0.69 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless+icon_seamless+jma_seamless+knmi_seamless+meteofrance_seamless+metno_seamless+ukmo_seamless | 2517 |  2.67 |   2.62 |   0.59 | ridge              |            0.72 |      755.00 |                   0.67 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                           | 2517 |  2.82 |   2.76 |   0.58 | ridge              |            0.72 |      755.00 |                   0.68 |
| blend:knmi_seamless+metno_seamless+ncep_nbm_conus                                                                                                                     | 2517 |  2.91 |   2.83 |   0.58 | ridge              |            0.73 |      755.00 |                   0.69 |
| jma_seamless                                                                                                                                                          | 2517 |  2.17 |   2.05 |   0.54 | ridge              |            0.73 |      755.00 |                   0.69 |
| stack:gfs_hrrr=0.027+gfs_seamless=0.027+knmi_seamless=0.245+metno_seamless=0.245+ncep_nbm_conus=0.521                                                                 | 2517 |  2.83 |   2.75 |   0.56 | ridge              |            0.74 |      755.00 |                   0.69 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                                                                                                            | 2517 |  2.99 |   2.93 |   0.53 | ridge              |            0.74 |      755.00 |                   0.66 |
| blend:knmi_seamless+ncep_nbm_conus                                                                                                                                    | 2517 |  2.82 |   2.73 |   0.56 | ridge              |            0.74 |      755.00 |                   0.70 |
| gfs_seamless                                                                                                                                                          | 2517 |  3.24 |   3.17 |   0.50 | ridge              |            0.74 |      755.00 |                   0.68 |
| gfs_hrrr                                                                                                                                                              | 2517 |  3.24 |   3.17 |   0.50 | ridge              |            0.74 |      755.00 |                   0.68 |
| best_match                                                                                                                                                            | 2517 |  3.24 |   3.17 |   0.50 | ridge              |            0.74 |      755.00 |                   0.68 |
| blend:gfs_hrrr+ncep_nbm_conus                                                                                                                                         | 2517 |  2.88 |   2.81 |   0.52 | ridge              |            0.75 |      755.00 |                   0.67 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless                                                                                         | 2517 |  2.72 |   2.65 |   0.56 | ridge              |            0.76 |      755.00 |                   0.71 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                                                                                                        | 2517 |  2.67 |   2.60 |   0.51 | ridge              |            0.76 |      755.00 |                   0.69 |
| stack:gem_seamless=0.002+icon_seamless=0.266+jma_seamless=0.068+ncep_nbm_conus=0.049                                                                                  | 2517 |  2.45 |   2.38 |   0.58 | ridge              |            0.76 |      755.00 |                   0.66 |
| icon_seamless                                                                                                                                                         | 2517 |  2.54 |   2.45 |   0.58 | ridge              |            0.77 |      755.00 |                   0.66 |
| blend:icon_seamless+ncep_nbm_conus                                                                                                                                    | 2517 |  2.53 |   2.45 |   0.53 | ridge              |            0.78 |      755.00 |                   0.69 |
| stack:knmi_seamless=0.09+metno_seamless=0.09+ncep_nbm_conus=0.808                                                                                                     | 2517 |  2.69 |   2.56 |   0.49 | ridge              |            0.78 |      755.00 |                   0.72 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                                                                                                                       | 2517 |  2.45 |   2.36 |   0.52 | ridge              |            0.79 |      755.00 |                   0.72 |
| meteofrance_seamless                                                                                                                                                  | 2517 |  1.55 |   1.21 |   0.32 | ridge              |            0.79 |      755.00 |                   0.72 |
| ncep_nbm_conus                                                                                                                                                        | 2517 |  2.63 |   2.46 |   0.45 | ridge              |            0.80 |      755.00 |                   0.74 |
| blend:gem_seamless+ncep_nbm_conus                                                                                                                                     | 2517 |  2.44 |   2.31 |   0.47 | ridge              |            0.81 |      755.00 |                   0.76 |
| gem_seamless                                                                                                                                                          | 2517 |  2.33 |   2.17 |   0.44 | ridge              |            0.82 |      755.00 |                   0.79 |

## Regional skill — KHIE, Whitefield NH, every season

Ranks models with 13k hours and two winters; the site record above decides. KHIE is 16 km east and is not this hollow: over the hours both stations recorded, temperature correlates 0.88 and dew point 0.92, but wind only 0.57.

### dewpoint_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 14069 |  1.97 |   0.82 |   2.64 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 14069 |  1.99 |   0.46 |   2.63 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 14069 |  2.01 |   0.64 |   2.72 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 14069 |  2.04 |   0.91 |   2.70 |
| blend:gem_seamless+ncep_nbm_conus                                             | 14069 |  2.06 |   0.28 |   2.77 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 14069 |  2.08 |   0.98 |   2.74 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 14069 |  2.10 |   0.53 |   2.74 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 14069 |  2.10 |   0.94 |   2.89 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 14069 |  2.17 |   1.23 |   2.98 |
| ncep_nbm_conus                                                                | 13932 |  2.18 |   0.24 |   2.85 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 14069 |  2.24 |   0.62 |   2.93 |
| blend:icon_seamless+ncep_nbm_conus                                            | 14069 |  2.29 |   1.25 |   3.16 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 14069 |  2.36 |   1.58 |   3.24 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 14069 |  2.39 |   1.67 |   3.07 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 14069 |  2.48 |   1.74 |   3.40 |
| gem_seamless                                                                  | 14069 |  2.51 |   0.32 |   3.42 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 14069 |  2.55 |   1.49 |   3.42 |
| knmi_seamless                                                                 | 14069 |  2.55 |   1.35 |   3.42 |
| metno_seamless                                                                | 14069 |  2.55 |   1.35 |   3.42 |
| best_match                                                                    | 14069 |  2.75 |   0.81 |   3.57 |
| gfs_hrrr                                                                      | 14069 |  2.75 |   0.81 |   3.57 |
| gfs_seamless                                                                  | 14069 |  2.75 |   0.81 |   3.57 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 14069 |  2.83 |   2.24 |   3.68 |
| icon_seamless                                                                 | 14069 |  3.08 |   2.25 |   4.19 |
| jma_seamless                                                                  | 14069 |  3.30 |   1.98 |   4.37 |
| ecmwf_ifs025                                                                  | 14069 |  3.33 |   2.78 |   4.26 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 14069 |  3.60 |   3.20 |   4.56 |
| ukmo_seamless                                                                 | 14069 |  3.69 |   2.71 |   4.87 |
| ecmwf_aifs025_single                                                          | 14069 |  3.99 |   3.63 |   5.00 |
| meteofrance_seamless                                                          | 14069 |  7.33 |   7.14 |   8.41 |

### gust_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| gem_seamless                                                                  | 13959 |  4.57 |   3.04 |   6.53 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13959 |  4.75 |   3.46 |   6.20 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13959 |  5.23 |   4.27 |   6.60 |
| ncep_nbm_conus                                                                | 13825 |  5.30 |   3.89 |   6.70 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13959 |  5.77 |   4.87 |   7.10 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13959 |  5.84 |   5.07 |   7.17 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13959 |  5.84 |   4.88 |   7.29 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13959 |  5.97 |   5.14 |   7.28 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13959 |  6.08 |   5.22 |   7.65 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13959 |  6.23 |   5.28 |   7.52 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13959 |  6.49 |   5.78 |   7.76 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13959 |  6.57 |   5.96 |   7.85 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13959 |  6.61 |   5.80 |   7.92 |
| best_match                                                                    | 13959 |  6.65 |   5.88 |   8.59 |
| gfs_seamless                                                                  | 13959 |  6.65 |   5.88 |   8.59 |
| gfs_hrrr                                                                      | 13959 |  6.65 |   5.88 |   8.59 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13959 |  6.83 |   6.08 |   8.08 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13959 |  7.05 |   6.53 |   8.41 |
| ukmo_seamless                                                                 | 13959 |  7.44 |   6.67 |   8.86 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13959 |  7.49 |   7.12 |   8.96 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13959 |  7.62 |   7.05 |   8.85 |
| icon_seamless                                                                 | 13959 |  8.25 |   7.68 |   9.73 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13959 |  8.69 |   8.36 |  10.12 |
| metno_seamless                                                                | 13959 |  8.91 |   8.48 |  10.31 |
| knmi_seamless                                                                 | 13959 |  8.91 |   8.48 |  10.31 |
| meteofrance_seamless                                                          | 13959 | 10.10 |   9.65 |  12.02 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13959 | 13.75 |  13.67 |  15.44 |
| ecmwf_ifs025                                                                  | 13959 | 13.75 |  13.67 |  15.44 |

### humidity_pct

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 14069 |  7.05 |  -0.07 |   9.10 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 14069 |  7.10 |   1.47 |   9.27 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 14069 |  7.32 |  -0.80 |   9.51 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 14069 |  7.57 |  -1.58 |   9.83 |
| ncep_nbm_conus                                                                | 13932 |  7.63 |  -1.11 |  10.06 |
| blend:icon_seamless+ncep_nbm_conus                                            | 14069 |  7.65 |  -2.11 |  10.07 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 14069 |  8.25 |  -3.01 |  10.88 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 14069 |  8.29 |  -2.60 |  10.88 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 14069 |  8.45 |  -2.76 |  11.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 14069 |  8.64 |  -2.63 |  11.14 |
| blend:gem_seamless+ncep_nbm_conus                                             | 14069 |  8.68 |  -2.97 |  11.41 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 14069 |  8.68 |  -2.03 |  11.00 |
| ukmo_seamless                                                                 | 14069 |  8.73 |   3.95 |  11.68 |
| icon_seamless                                                                 | 14069 |  8.82 |  -3.11 |  11.80 |
| metno_seamless                                                                | 14069 |  8.85 |  -1.89 |  11.68 |
| knmi_seamless                                                                 | 14069 |  8.85 |  -1.89 |  11.68 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 14069 |  8.89 |  -2.62 |  11.34 |
| jma_seamless                                                                  | 14069 |  9.02 |   2.97 |  11.81 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 14069 |  9.10 |  -3.35 |  11.77 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 14069 |  9.66 |  -1.85 |  12.63 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 14069 |  9.72 |  -3.12 |  12.38 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 14069 |  9.76 |  -2.76 |  12.57 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 14069 |  9.84 |  -0.39 |  12.64 |
| ecmwf_aifs025_single                                                          | 14069 |  9.86 |  -1.28 |  12.76 |
| ecmwf_ifs025                                                                  | 14069 | 10.28 |   0.49 |  13.13 |
| gem_seamless                                                                  | 14069 | 11.00 |  -4.78 |  15.03 |
| gfs_hrrr                                                                      | 14069 | 11.84 |  -4.12 |  15.07 |
| gfs_seamless                                                                  | 14069 | 11.84 |  -4.12 |  15.07 |
| best_match                                                                    | 14069 | 11.84 |  -4.12 |  15.07 |
| meteofrance_seamless                                                          | 14069 | 11.88 |   2.53 |  14.83 |

### temp_f

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 14069 |  3.09 |   1.16 |   4.06 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 14069 |  3.10 |   1.58 |   4.18 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 14069 |  3.13 |   1.40 |   4.17 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 14069 |  3.15 |   1.60 |   4.30 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 14069 |  3.16 |   1.43 |   4.27 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 14069 |  3.19 |   1.44 |   4.31 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 14069 |  3.22 |   1.43 |   4.37 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 14069 |  3.23 |   1.63 |   4.40 |
| ncep_nbm_conus                                                                | 13932 |  3.25 |   0.44 |   4.11 |
| blend:gem_seamless+ncep_nbm_conus                                             | 14069 |  3.29 |   1.22 |   4.42 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 14069 |  3.33 |   1.69 |   4.48 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 14069 |  3.34 |   0.73 |   4.29 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 14069 |  3.36 |   1.89 |   4.62 |
| blend:icon_seamless+ncep_nbm_conus                                            | 14069 |  3.38 |   1.85 |   4.52 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 14069 |  3.40 |   1.57 |   4.50 |
| gfs_hrrr                                                                      | 14069 |  3.41 |   1.88 |   4.55 |
| gfs_seamless                                                                  | 14069 |  3.41 |   1.88 |   4.55 |
| best_match                                                                    | 14069 |  3.41 |   1.88 |   4.55 |
| metno_seamless                                                                | 14069 |  3.44 |   1.86 |   4.72 |
| knmi_seamless                                                                 | 14069 |  3.44 |   1.86 |   4.72 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 14069 |  3.55 |   2.40 |   4.99 |
| jma_seamless                                                                  | 14069 |  3.61 |   0.62 |   4.80 |
| gem_seamless                                                                  | 14069 |  3.76 |   1.97 |   5.40 |
| ukmo_seamless                                                                 | 14069 |  3.80 |   1.01 |   4.97 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 14069 |  3.96 |   2.75 |   5.71 |
| ecmwf_ifs025                                                                  | 14069 |  4.12 |   2.40 |   5.78 |
| icon_seamless                                                                 | 14069 |  4.17 |   3.25 |   5.78 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 14069 |  4.35 |   3.14 |   6.16 |
| ecmwf_aifs025_single                                                          | 14069 |  4.82 |   3.88 |   6.72 |
| meteofrance_seamless                                                          | 14069 |  6.42 |   6.06 |   8.31 |

### wind_mph

| candidate                                                                     |     n |   mae |   bias |   rmse |
|:------------------------------------------------------------------------------|------:|------:|-------:|-------:|
| ncep_nbm_conus                                                                | 13825 |  2.10 |   0.09 |   3.16 |
| blend:gem_seamless+ncep_nbm_conus                                             | 13959 |  2.27 |   0.18 |   3.00 |
| blend:icon_seamless+ncep_nbm_conus                                            | 13959 |  2.30 |   0.52 |   2.97 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 | 13959 |  2.34 |   0.68 |   2.97 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               | 13959 |  2.35 |   0.44 |   2.97 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                | 13959 |  2.37 |   0.54 |   2.94 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              | 13959 |  2.38 |   0.62 |   3.01 |
| blend:ncep_nbm_conus+ukmo_seamless                                            | 13959 |  2.41 |   0.50 |   3.08 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   | 13959 |  2.43 |   0.62 |   3.01 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              | 13959 |  2.44 |   0.65 |   3.04 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    | 13959 |  2.46 |   0.88 |   3.05 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   | 13959 |  2.47 |   0.93 |   3.02 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         | 13959 |  2.49 |   0.76 |   3.02 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       | 13959 |  2.52 |   1.13 |   3.06 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless | 13959 |  2.52 |   0.99 |   3.10 |
| icon_seamless                                                                 | 13959 |  2.61 |   0.95 |   3.18 |
| gem_seamless                                                                  | 13959 |  2.62 |   0.26 |   3.30 |
| jma_seamless                                                                  | 13959 |  2.67 |   0.31 |   3.30 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    | 13959 |  2.70 |   1.42 |   3.23 |
| metno_seamless                                                                | 13959 |  2.78 |   1.50 |   3.43 |
| knmi_seamless                                                                 | 13959 |  2.78 |   1.50 |   3.43 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          | 13959 |  2.79 |   1.51 |   3.41 |
| gfs_hrrr                                                                      | 13959 |  2.79 |   1.28 |   3.42 |
| best_match                                                                    | 13959 |  2.79 |   1.28 |   3.42 |
| gfs_seamless                                                                  | 13959 |  2.79 |   1.28 |   3.42 |
| ukmo_seamless                                                                 | 13959 |  2.84 |   0.92 |   3.47 |
| ecmwf_aifs025_single                                                          | 13959 |  2.93 |   1.65 |   3.64 |
| meteofrance_seamless                                                          | 13959 |  3.07 |  -0.61 |   3.90 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       | 13959 |  3.10 |   2.13 |   3.83 |
| ecmwf_ifs025                                                                  | 13959 |  3.37 |   2.61 |   4.16 |

## Regional MAE by season (temperature)

| candidate                                                                     |   fall |   spring |   summer |   winter |
|:------------------------------------------------------------------------------|-------:|---------:|---------:|---------:|
| best_match                                                                    |   3.57 |     3.05 |     3.51 |     3.54 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025                                       |   4.75 |     3.67 |     4.34 |     4.74 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless                          |   4.33 |     3.34 |     3.95 |     4.32 |
| blend:ecmwf_aifs025_single+ecmwf_ifs025+gem_seamless+gfs_hrrr+gfs_seamless    |   3.86 |     3.02 |     3.61 |     3.75 |
| blend:gem_seamless+gfs_hrrr+gfs_seamless+ncep_nbm_conus+ukmo_seamless         |   3.43 |     2.85 |     3.28 |     3.16 |
| blend:gem_seamless+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus   |   3.43 |     2.72 |     3.21 |     3.18 |
| blend:gem_seamless+gfs_seamless+ncep_nbm_conus                                |   3.40 |     2.87 |     3.16 |     3.17 |
| blend:gem_seamless+icon_seamless+jma_seamless+metno_seamless+ncep_nbm_conus   |   3.45 |     3.02 |     3.11 |     3.38 |
| blend:gem_seamless+icon_seamless+ncep_nbm_conus                               |   3.60 |     3.04 |     3.25 |     3.68 |
| blend:gem_seamless+metno_seamless+ncep_nbm_conus                              |   3.55 |     2.85 |     3.19 |     3.26 |
| blend:gem_seamless+ncep_nbm_conus                                             |   3.63 |     3.04 |     3.17 |     3.32 |
| blend:gfs_hrrr+gfs_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus       |   3.35 |     2.70 |     3.23 |     3.06 |
| blend:gfs_hrrr+gfs_seamless+ncep_nbm_conus                                    |   3.28 |     2.88 |     3.22 |     3.10 |
| blend:gfs_hrrr+ncep_nbm_conus                                                 |   3.29 |     2.87 |     3.14 |     2.98 |
| blend:icon_seamless+knmi_seamless+metno_seamless+ncep_nbm_conus+ukmo_seamless |   3.59 |     2.93 |     3.36 |     3.44 |
| blend:icon_seamless+ncep_nbm_conus                                            |   3.58 |     3.17 |     3.21 |     3.71 |
| blend:icon_seamless+ncep_nbm_conus+ukmo_seamless                              |   3.62 |     3.15 |     3.33 |     3.52 |
| blend:ncep_nbm_conus+ukmo_seamless                                            |   3.67 |     3.13 |     3.33 |     3.11 |
| ecmwf_aifs025_single                                                          |   5.17 |     4.07 |     4.94 |     5.14 |
| ecmwf_ifs025                                                                  |   4.57 |     3.54 |     3.96 |     4.56 |
| gem_seamless                                                                  |   3.99 |     3.44 |     3.64 |     4.06 |
| gfs_hrrr                                                                      |   3.57 |     3.05 |     3.51 |     3.54 |
| gfs_seamless                                                                  |   3.57 |     3.05 |     3.51 |     3.54 |
| icon_seamless                                                                 |   4.22 |     3.90 |     3.85 |     5.16 |
| jma_seamless                                                                  |   3.47 |     3.92 |     3.28 |     4.02 |
| knmi_seamless                                                                 |   3.74 |     2.88 |     3.55 |     3.57 |
| meteofrance_seamless                                                          |   7.03 |     5.21 |     6.08 |     7.95 |
| metno_seamless                                                                |   3.74 |     2.88 |     3.55 |     3.57 |
| ncep_nbm_conus                                                                |   3.65 |     3.12 |     3.09 |     3.07 |
| ukmo_seamless                                                                 |   4.14 |     3.46 |     3.92 |     3.49 |

## MAE by lead time, days 1-7 (previous-runs, site)

### gust_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 6.78 |   3.54 |   4.06 |   4.18 |   4.40 |   4.71 |   4.53 |
| gem_seamless         | 3.98 |   3.62 |   3.91 |   3.98 |   4.39 |   4.49 |   4.84 |
| gfs_hrrr             | 6.78 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 6.78 |   3.54 |   4.06 |   4.18 |   4.40 |   4.71 |   4.53 |
| icon_seamless        | 4.91 |   5.18 |   5.28 |   5.56 |   5.73 |   6.79 | nan    |
| meteofrance_seamless | 4.88 |   4.78 |   5.14 | nan    | nan    | nan    | nan    |
| ncep_nbm_conus       | 3.39 |   3.64 |   3.89 |   3.93 |   3.93 |   3.99 |   3.91 |
| ukmo_seamless        | 4.44 |   4.63 |   4.72 |   4.82 |   4.54 |   5.58 | nan    |

### humidity_pct

| model                |     1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|------:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           |  7.99 |  11.79 |  12.06 |  12.38 |  13.09 |  15.02 |  16.58 |
| ecmwf_aifs025_single |  7.04 |   8.09 |   9.40 |   9.60 |   9.62 |  10.50 |  11.56 |
| ecmwf_ifs025         |  9.16 |  10.29 |  11.31 |  11.00 |  11.86 |  13.54 |  13.72 |
| gem_seamless         |  9.68 |  13.79 |  11.88 |  12.28 |  12.76 |  12.66 |  14.06 |
| gfs_hrrr             |  7.99 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         |  7.99 |  11.79 |  12.06 |  12.38 |  13.09 |  15.02 |  16.58 |
| icon_seamless        | 10.66 |  11.39 |  11.47 |  12.18 |  12.90 |  13.12 | nan    |
| jma_seamless         | 15.57 |  15.68 |  16.09 |  16.54 |  16.37 |  16.26 |  16.06 |
| knmi_seamless        |  9.50 |  10.65 |  11.40 |  11.36 |  12.52 |  14.16 |  14.38 |
| meteofrance_seamless | 10.92 |  11.52 |  12.33 | nan    | nan    | nan    | nan    |
| metno_seamless       |  9.50 |  10.65 |  11.40 |  11.36 |  12.52 |  14.16 |  14.38 |
| ncep_nbm_conus       | 12.64 |  13.18 |  13.90 |  14.07 |  14.60 |  15.83 |  16.58 |
| ukmo_seamless        | 15.88 |  16.93 |  17.45 |  18.29 |  18.66 |  19.80 | nan    |

### temp_f

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 3.17 |   4.08 |   4.39 |   4.62 |   5.30 |   5.92 |   6.79 |
| ecmwf_aifs025_single | 3.14 |   3.18 |   3.51 |   3.69 |   3.82 |   4.01 |   4.16 |
| ecmwf_ifs025         | 3.05 |   3.31 |   3.61 |   3.98 |   4.36 |   5.13 |   4.99 |
| gem_seamless         | 4.47 |   6.55 |   4.45 |   4.84 |   5.35 |   5.79 |   6.49 |
| gfs_hrrr             | 3.17 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 3.17 |   4.08 |   4.39 |   4.62 |   5.30 |   5.92 |   6.79 |
| icon_seamless        | 5.18 |   5.21 |   5.11 |   5.25 |   5.30 |   6.30 | nan    |
| jma_seamless         | 5.02 |   5.28 |   5.46 |   5.50 |   5.96 |   6.93 |   8.06 |
| knmi_seamless        | 3.35 |   3.56 |   3.75 |   4.25 |   4.62 |   5.44 |   5.29 |
| meteofrance_seamless | 3.24 |   3.67 |   3.99 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.35 |   3.56 |   3.75 |   4.25 |   4.62 |   5.44 |   5.29 |
| ncep_nbm_conus       | 4.33 |   4.50 |   4.79 |   5.09 |   5.45 |   5.94 |   6.69 |
| ukmo_seamless        | 5.46 |   5.47 |   5.21 |   5.30 |   5.84 |   5.82 | nan    |

### wind_mph

| model                |    1 |      2 |      3 |      4 |      5 |      6 |      7 |
|:---------------------|-----:|-------:|-------:|-------:|-------:|-------:|-------:|
| best_match           | 4.20 |   2.44 |   2.47 |   2.55 |   2.50 |   2.45 |   2.27 |
| ecmwf_aifs025_single | 3.40 |   3.42 |   3.36 |   3.35 |   3.35 |   3.44 |   3.47 |
| ecmwf_ifs025         | 3.61 |   3.68 |   3.52 |   3.75 |   3.82 |   3.73 |   3.67 |
| gem_seamless         | 2.46 |   2.01 |   1.94 |   1.93 |   1.95 |   1.94 |   1.98 |
| gfs_hrrr             | 4.20 | nan    | nan    | nan    | nan    | nan    | nan    |
| gfs_seamless         | 4.20 |   2.44 |   2.47 |   2.55 |   2.50 |   2.45 |   2.27 |
| icon_seamless        | 2.58 |   2.71 |   2.71 |   2.79 |   2.72 |   3.22 | nan    |
| jma_seamless         | 2.18 |   2.25 |   2.34 |   2.33 |   2.38 |   2.32 |   2.20 |
| knmi_seamless        | 3.25 |   3.35 |   3.27 |   3.47 |   3.59 |   3.43 |   3.45 |
| meteofrance_seamless | 1.52 |   1.51 |   1.61 | nan    | nan    | nan    | nan    |
| metno_seamless       | 3.25 |   3.35 |   3.27 |   3.47 |   3.59 |   3.43 |   3.45 |
| ncep_nbm_conus       | 2.73 |   2.84 |   2.95 |   2.94 |   2.73 |   2.68 |   2.46 |
| ukmo_seamless        | 2.82 |   2.94 |   2.91 |   2.90 |   2.74 |   3.21 | nan    |
