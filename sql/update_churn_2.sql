UPDATE ml_user_month_churn_dataset t
SET churn_next_month = CASE
    WHEN next_activity.next_month_watch IS NULL
         AND next_activity.next_2_month_watch IS NULL
    THEN 1
    ELSE 0
END
FROM (
    SELECT
        user_id,
        snapshot_month,
        LEAD(monthly_sessions, 1) OVER (
            PARTITION BY user_id
            ORDER BY snapshot_month
        ) AS next_month_watch,
        LEAD(monthly_sessions, 2) OVER (
            PARTITION BY user_id
            ORDER BY snapshot_month
        ) AS next_2_month_watch
    FROM ml_user_month_churn_dataset
) next_activity
WHERE t.user_id = next_activity.user_id
AND t.snapshot_month = next_activity.snapshot_month;