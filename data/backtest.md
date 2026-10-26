# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=10716, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 3.478 |
| bias | 3.773 |
| ridge | 3.620 |

## humidity_pct  (n=10708, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 7.602 |
| bias | 8.319 |
| ridge | 8.534 |

## dewpoint_f  (n=10716, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.651 |
| bias | 2.840 |
| ridge | 2.845 |

## wind_mph  (n=10716, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.826 |
| bias | 1.967 |
| ridge | 0.922 |

## gust_mph  (n=10716, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.746 |
| bias | 3.594 |
| ridge | 2.925 |

## pressure_abs_hpa  (n=8428, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.965 |
| bias | 0.789 |
| ridge | 0.411 |
| lgbm | 0.468 |
