UPDATE ml_user_month_churn_dataset
SET churn_next_month = 1
WHERE
    inactivity_streak >= 2
    OR watch_decay_ratio < 0.3
    OR sessions_vs_trend_ratio < 0.4;