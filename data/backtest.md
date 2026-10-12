# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=10956, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 3.251 |
| bias | 3.293 |
| ridge | 3.467 |

## humidity_pct  (n=10948, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 8.727 |
| bias | 8.319 |
| ridge | 8.461 |

## dewpoint_f  (n=1373, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 1.752 |
| bias | 1.667 |
| ridge | 1.564 |

## wind_mph  (n=10956, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.964 |
| bias | 1.357 |
| ridge | 1.002 |

## gust_mph  (n=10956, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.319 |
| bias | 3.208 |
| ridge | 3.006 |

## pressure_abs_hpa  (n=8164, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.691 |
| bias | 0.582 |
| ridge | 0.435 |
| lgbm | 0.470 |
