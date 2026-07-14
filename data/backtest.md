# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=128, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 5.589 |

## humidity_pct  (n=128, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 13.005 |

## dewpoint_f  (n=16, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.845 |

## wind_mph  (n=128, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.463 |

## gust_mph  (n=128, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 4.059 |

## pressure_abs_hpa  (n=7186, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.190 |
| bias | 2.177 |
| ridge | 2.185 |
| lgbm | 3.258 |
