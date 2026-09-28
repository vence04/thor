# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=8288, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 4.519 |
| bias | 3.654 |
| ridge | 3.883 |

## humidity_pct  (n=8280, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 11.216 |
| bias | 10.190 |
| ridge | 8.719 |

## dewpoint_f  (n=1036, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 2.419 |
| bias | 1.970 |

## wind_mph  (n=8288, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.862 |
| bias | 2.354 |
| ridge | 0.876 |

## gust_mph  (n=8288, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.468 |
| bias | 4.155 |
| ridge | 3.037 |

## pressure_abs_hpa  (n=7827, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.688 |
| bias | 1.623 |
| ridge | 0.794 |
| lgbm | 1.021 |
