# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=6424, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 4.307 |
| bias | 3.706 |
| ridge | 3.428 |

## humidity_pct  (n=6416, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 11.408 |
| bias | 10.232 |
| ridge | 8.638 |

## dewpoint_f  (n=803, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.340 |
| bias | 1.892 |

## wind_mph  (n=6424, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.758 |
| bias | 2.557 |
| ridge | 0.857 |

## gust_mph  (n=6424, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.370 |
| bias | 4.219 |
| ridge | 2.764 |

## pressure_abs_hpa  (n=7594, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.689 |
| bias | 1.658 |
| ridge | 0.859 |
| lgbm | 1.072 |
