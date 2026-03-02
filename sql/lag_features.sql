UPDATE ml_user_month_churn_dataset t
SET
    previous_month_watch_hours = lag_watch.prev_watch_hours,
    delta_watch_hours = t.monthly_watch_hours - lag_watch.prev_watch_hours,
    previous_month_sessions = lag_watch.prev_sessions,
    delta_sessions = t.monthly_sessions - lag_watch.prev_sessions,
    rolling_3m_watch_avg = lag_watch.rolling_avg,
    watch_momentum_ratio = 
        CASE 
            WHEN lag_watch.prev_watch_hours IS NULL OR lag_watch.prev_watch_hours = 0
            THEN NULL
            ELSE t.monthly_watch_hours / lag_watch.prev_watch_hours
        END
FROM (
    SELECT
        user_id,
        snapshot_month,
        LAG(monthly_watch_hours) OVER (
            PARTITION BY user_id
            ORDER BY snapshot_month
        ) AS prev_watch_hours,
        LAG(monthly_sessions) OVER (
            PARTITION BY user_id
            ORDER BY snapshot_month
        ) AS prev_sessions,
        AVG(monthly_watch_hours) OVER (
            PARTITION BY user_id
            ORDER BY snapshot_month
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS rolling_avg
    FROM ml_user_month_churn_dataset
) lag_watch
WHERE t.user_id = lag_watch.user_id
AND t.snapshot_month = lag_watch.snapshot_month;