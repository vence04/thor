# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=6384, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.308 |
| bias | 3.723 |
| ridge | 3.386 |

## humidity_pct  (n=6376, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 11.436 |
| bias | 10.221 |
| ridge | 8.533 |

## dewpoint_f  (n=798, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 2.338 |
| bias | 1.882 |

## wind_mph  (n=6384, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.761 |
| bias | 2.569 |
| ridge | 0.851 |

## gust_mph  (n=6384, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.374 |
| bias | 4.221 |
| ridge | 2.751 |

## pressure_abs_hpa  (n=7589, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.688 |
| bias | 1.660 |
| ridge | 0.860 |
| lgbm | 1.113 |
