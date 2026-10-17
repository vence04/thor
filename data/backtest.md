# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=11068, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 3.315 |
| bias | 3.646 |
| ridge | 3.511 |

## humidity_pct  (n=11060, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 7.385 |
| bias | 7.996 |
| ridge | 7.835 |

## dewpoint_f  (n=1492, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.752 |
| bias | 1.682 |
| ridge | 1.555 |

## wind_mph  (n=11068, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.745 |
| bias | 1.729 |
| ridge | 0.978 |

## gust_mph  (n=11068, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.671 |
| bias | 3.673 |
| ridge | 3.120 |

## pressure_abs_hpa  (n=8283, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.962 |
| bias | 0.791 |
| ridge | 0.405 |
| lgbm | 0.490 |
