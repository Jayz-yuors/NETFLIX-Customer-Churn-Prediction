UPDATE ml_user_month_churn_dataset
SET
    watch_vs_trend_ratio =
        CASE
            WHEN rolling_3m_watch_avg > 0
            THEN monthly_watch_hours / rolling_3m_watch_avg
            ELSE NULL
        END,

    sessions_vs_trend_ratio =
        CASE
            WHEN rolling_3m_sessions_avg > 0
            THEN monthly_sessions::NUMERIC / rolling_3m_sessions_avg
            ELSE NULL
        END;