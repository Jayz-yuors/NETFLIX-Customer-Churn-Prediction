UPDATE ml_user_month_churn_dataset m
SET churn_next_month = CASE
    WHEN lead_watch = 0 OR lead_watch IS NULL THEN 1
    ELSE 0
END
FROM (
    SELECT
        user_id,
        snapshot_month,
        LEAD(monthly_watch_hours)
        OVER (PARTITION BY user_id ORDER BY snapshot_month) AS lead_watch
    FROM ml_user_month_churn_dataset
) sub
WHERE m.user_id = sub.user_id
AND m.snapshot_month = sub.snapshot_month;