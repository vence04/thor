# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=6200, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.299 |
| bias | 3.678 |
| ridge | 3.177 |

## humidity_pct  (n=6200, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 11.484 |
| bias | 10.206 |
| ridge | 8.333 |

## dewpoint_f  (n=775, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 2.328 |
| bias | 1.881 |

## wind_mph  (n=6200, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.768 |
| bias | 2.583 |
| ridge | 0.849 |

## gust_mph  (n=6200, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.393 |
| bias | 4.254 |
| ridge | 2.761 |

## pressure_abs_hpa  (n=7566, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.688 |
| bias | 1.664 |
| ridge | 0.868 |
| lgbm | 1.080 |
