UPDATE ml_user_month_churn_dataset m
SET
    rolling_3m_watch_avg = sub.roll_watch,
    rolling_3m_sessions_avg = sub.roll_sessions,
    watch_volatility_3m = sub.std_watch,
    session_volatility_3m = sub.std_sessions
FROM (
    SELECT
        user_id,
        snapshot_month,

        AVG(monthly_watch_hours)
            OVER (PARTITION BY user_id
                  ORDER BY snapshot_month
                  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS roll_watch,

        AVG(monthly_sessions)
            OVER (PARTITION BY user_id
                  ORDER BY snapshot_month
                  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS roll_sessions,

        STDDEV(monthly_watch_hours)
            OVER (PARTITION BY user_id
                  ORDER BY snapshot_month
                  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS std_watch,

        STDDEV(monthly_sessions)
            OVER (PARTITION BY user_id
                  ORDER BY snapshot_month
                  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS std_sessions

    FROM ml_user_month_churn_dataset
) sub
WHERE m.user_id = sub.user_id
AND m.snapshot_month = sub.snapshot_month;