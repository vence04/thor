# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=2092, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 3.010 |
| bias | 3.476 |
| ridge | 2.542 |

## humidity_pct  (n=4184, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 10.802 |
| bias | 12.995 |
| ridge | 10.155 |

## dewpoint_f  (n=4184, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.935 |
| bias | 3.174 |
| ridge | 3.401 |

## wind_mph  (n=10983, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.711 |
| bias | 2.690 |
| ridge | 0.908 |

## gust_mph  (n=10983, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.957 |
| bias | 4.088 |
| ridge | 2.608 |

## pressure_abs_hpa  (n=8842, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.959 |
| bias | 0.776 |
| ridge | 0.411 |
| lgbm | 0.449 |
