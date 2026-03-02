UPDATE ml_user_month_churn_dataset m
SET inactivity_streak = sub.streak
FROM (
    SELECT
        user_id,
        snapshot_month,

        SUM(
            CASE
                WHEN monthly_watch_hours < 0.3 THEN 1
                ELSE 0
            END
        ) OVER (
            PARTITION BY user_id
            ORDER BY snapshot_month
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS streak

    FROM ml_user_month_churn_dataset
) sub
WHERE m.user_id = sub.user_id
AND m.snapshot_month = sub.snapshot_month;