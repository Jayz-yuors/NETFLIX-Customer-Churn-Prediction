UPDATE ml_user_month_churn_dataset
SET churn_next_month = CASE
    WHEN delta_watch_hours < -0.8
         AND rolling_3m_watch_avg < 1.0
    THEN 1
    ELSE 0
END;