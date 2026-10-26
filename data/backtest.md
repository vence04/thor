# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=904, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 4.823 |
| bias | 3.741 |

## humidity_pct  (n=904, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 12.578 |
| bias | 9.263 |

## dewpoint_f  (n=904, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 2.412 |
| bias | 2.243 |

## wind_mph  (n=10748, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.822 |
| bias | 1.975 |
| ridge | 0.920 |

## gust_mph  (n=10748, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.739 |
| bias | 3.599 |
| ridge | 2.924 |

## pressure_abs_hpa  (n=8432, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.965 |
| bias | 0.789 |
| ridge | 0.411 |
| lgbm | 0.469 |
