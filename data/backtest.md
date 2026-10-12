# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=10948, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 4.347 |
| bias | 3.905 |
| ridge | 4.358 |

## humidity_pct  (n=10940, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 10.786 |
| bias | 10.057 |
| ridge | 9.155 |

## dewpoint_f  (n=1372, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.381 |
| bias | 1.950 |
| ridge | 1.934 |

## wind_mph  (n=10948, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.875 |
| bias | 2.148 |
| ridge | 1.002 |

## gust_mph  (n=10948, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.489 |
| bias | 4.079 |
| ridge | 3.274 |

## pressure_abs_hpa  (n=8163, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.685 |
| bias | 1.613 |
| ridge | 0.804 |
| lgbm | 0.919 |
