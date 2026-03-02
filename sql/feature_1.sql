UPDATE ml_user_month_churn_dataset m
SET
    previous_month_watch_hours = sub.prev_watch,
    previous_month_sessions = sub.prev_sessions
FROM (
    SELECT
        user_id,
        snapshot_month,
        LAG(monthly_watch_hours)
            OVER (PARTITION BY user_id ORDER BY snapshot_month) AS prev_watch,
        LAG(monthly_sessions)
            OVER (PARTITION BY user_id ORDER BY snapshot_month) AS prev_sessions
    FROM ml_user_month_churn_dataset
) sub
WHERE m.user_id = sub.user_id
AND m.snapshot_month = sub.snapshot_month;