UPDATE ml_user_month_churn_dataset m
SET churn_next_month = CASE
    WHEN (
        sub.next_watch IS NOT NULL
        AND (
            sub.next_watch < m.monthly_watch_hours * 0.3
            OR sub.next_sessions < m.monthly_sessions * 0.4
        )
    )
    THEN 1
    ELSE 0
END
FROM (
    SELECT
        user_id,
        snapshot_month,
        LEAD(monthly_watch_hours)
            OVER (PARTITION BY user_id ORDER BY snapshot_month) AS next_watch,
        LEAD(monthly_sessions)
            OVER (PARTITION BY user_id ORDER BY snapshot_month) AS next_sessions
    FROM ml_user_month_churn_dataset
) sub
WHERE m.user_id = sub.user_id
AND m.snapshot_month = sub.snapshot_month;