# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=5704, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.203 |
| bias | 4.334 |
| ridge | 3.582 |

## humidity_pct  (n=5704, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 10.766 |
| bias | 11.651 |
| ridge | 9.546 |

## dewpoint_f  (n=5704, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.959 |
| bias | 3.713 |
| ridge | 3.251 |

## wind_mph  (n=12503, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.980 |
| bias | 2.585 |
| ridge | 0.854 |

## gust_mph  (n=12503, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.909 |
| bias | 4.220 |
| ridge | 2.552 |

## pressure_abs_hpa  (n=9032, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.966 |
| bias | 0.761 |
| ridge | 0.409 |
| lgbm | 0.449 |
