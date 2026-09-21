# Offset model backtest

Source model: `best_match`. Rolling-origin CV, 4 folds. Winner must beat raw MAE by >2%.

## temp_f  (n=6960, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 4.315 |
| bias | 3.799 |
| ridge | 3.825 |

## humidity_pct  (n=6952, method=**raw**)
| method | CV MAE |
|--------|--------|
| raw | 11.201 |
| bias | 9.960 |
| ridge | 8.860 |

## dewpoint_f  (n=870, method=**bias**)
| method | CV MAE |
|--------|--------|
| raw | 2.331 |
| bias | 1.842 |

## wind_mph  (n=6960, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 2.742 |
| bias | 2.479 |
| ridge | 0.887 |

## gust_mph  (n=6960, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 4.342 |
| bias | 4.159 |
| ridge | 2.952 |

## pressure_abs_hpa  (n=7661, method=**ridge**)
| method | CV MAE |
|--------|--------|
| raw | 1.687 |
| bias | 1.654 |
| ridge | 0.850 |
| lgbm | 1.108 |
