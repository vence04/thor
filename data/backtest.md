# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=10116, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 3.204 |
| bias | 3.491 |
| ridge | 3.359 |

## humidity_pct  (n=10108, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 7.465 |
| bias | 8.166 |
| ridge | 7.922 |

## dewpoint_f  (n=1373, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 1.699 |
| bias | 1.624 |
| ridge | 1.491 |

## wind_mph  (n=10116, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.591 |
| bias | 1.568 |
| ridge | 0.911 |

## gust_mph  (n=10116, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.746 |
| bias | 2.983 |
| ridge | 2.852 |

## pressure_abs_hpa  (n=8164, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.963 |
| bias | 0.795 |
| ridge | 0.405 |
| lgbm | 0.461 |
