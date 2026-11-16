# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=2180, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.954 |
| bias | 3.185 |
| ridge | 2.611 |

## humidity_pct  (n=4360, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 10.645 |
| bias | 12.940 |
| ridge | 10.327 |

## dewpoint_f  (n=4360, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 2.890 |
| bias | 3.107 |
| ridge | 3.272 |

## wind_mph  (n=11159, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.725 |
| bias | 2.683 |
| ridge | 0.906 |

## gust_mph  (n=11159, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 3.984 |
| bias | 4.085 |
| ridge | 2.615 |

## pressure_abs_hpa  (n=8864, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 0.960 |
| bias | 0.775 |
| ridge | 0.411 |
| lgbm | 0.468 |
