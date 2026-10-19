# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=10972, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 3.230 |
| bias | 3.375 |
| ridge | 3.041 |

## humidity_pct  (n=10964, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 7.358 |
| bias | 7.967 |
| ridge | 7.853 |

## dewpoint_f  (n=10972, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.657 |
| bias | 2.767 |
| ridge | 2.800 |

## wind_mph  (n=10972, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.782 |
| bias | 1.770 |
| ridge | 1.004 |

## gust_mph  (n=10972, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.728 |
| bias | 3.839 |
| ridge | 3.186 |

## pressure_abs_hpa  (n=8313, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.962 |
| bias | 0.791 |
| ridge | 0.406 |
| lgbm | 0.489 |
