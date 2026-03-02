WITH future_activity AS (
    SELECT
        user_id,
        snapshot_month,
        LEAD(monthly_sessions) OVER (
            PARTITION BY user_id
            ORDER BY snapshot_month
        ) AS next_month_sessions
    FROM ml_user_month_churn_dataset
)

UPDATE ml_user_month_churn_dataset t
SET churn_next_month = CASE
    WHEN f.next_month_sessions IS NULL 
         OR f.next_month_sessions = 0
    THEN 1
    ELSE 0
END
FROM future_activity f
WHERE t.user_id = f.user_id
AND t.snapshot_month = f.snapshot_month;