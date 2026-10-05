# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=9632, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 4.344 |
| bias | 3.869 |
| ridge | 4.084 |

## humidity_pct  (n=9624, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 10.790 |
| bias | 10.077 |
| ridge | 9.206 |

## dewpoint_f  (n=1204, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.422 |
| bias | 1.946 |
| ridge | 1.782 |

## wind_mph  (n=9632, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.802 |
| bias | 2.273 |
| ridge | 0.943 |

## gust_mph  (n=9632, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.404 |
| bias | 4.078 |
| ridge | 3.107 |

## pressure_abs_hpa  (n=7995, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.686 |
| bias | 1.605 |
| ridge | 0.781 |
| lgbm | 0.958 |
