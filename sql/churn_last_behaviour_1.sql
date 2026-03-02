UPDATE ml_user_month_churn_dataset
SET churn_next_month = 1
WHERE
    monthly_watch_hours < 0.3
    AND active_days_in_month < 3
    AND monthly_sessions < 3
    AND (
        previous_month_watch_hours IS NULL
        OR monthly_watch_hours < previous_month_watch_hours * 0.5
    );