UPDATE ml_user_month_churn_dataset
SET
    delta_watch_hours = monthly_watch_hours - previous_month_watch_hours,
    delta_sessions = monthly_sessions - previous_month_sessions,

    watch_decay_ratio =
        CASE
            WHEN previous_month_watch_hours > 0
            THEN monthly_watch_hours / previous_month_watch_hours
            ELSE NULL
        END,

    session_decay_ratio =
        CASE
            WHEN previous_month_sessions > 0
            THEN monthly_sessions::NUMERIC / previous_month_sessions
            ELSE NULL
        END,

    completion_ratio =
        CASE
            WHEN monthly_sessions > 0
            THEN completed_sessions::NUMERIC / monthly_sessions
            ELSE 0
        END,

    engagement_score =
        (0.4 * monthly_watch_hours)
        + (0.3 * monthly_sessions)
        + (0.3 * active_days_in_month);