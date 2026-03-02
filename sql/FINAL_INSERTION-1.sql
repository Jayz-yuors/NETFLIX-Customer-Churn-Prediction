INSERT INTO ml_user_month_churn_dataset
SELECT
    umb.user_id,
    umb.snapshot_month,

    -- Static
    u.age,
    u.gender,
    u.country,
    u.subscription_plan,
    (CURRENT_DATE - u.subscription_start_date) AS subscription_tenure_days,
    u.monthly_spend,
    u.household_size,
    u.primary_device,

    -- Watch
    w.monthly_sessions,
    w.monthly_watch_hours,
    w.avg_watch_duration,
    w.avg_progress_percentage,
    w.avg_user_rating,
    w.completed_sessions,
    w.download_sessions,
    w.active_days_in_month,
    w.distinct_devices_used,

    -- Recommendation
    r.monthly_recommendations,
    r.recommendation_click_rate,
    r.avg_recommendation_score,
    r.avg_rank_position,

    -- Search
    s.monthly_searches,
    s.search_success_rate,
    s.avg_search_duration,

    -- Review
    rm.monthly_reviews,
    rm.avg_sentiment_score,
    rm.avg_review_rating,
    rm.avg_review_length,
    rm.genre_diversity,
    rm.avg_movie_imdb_rating,
    rm.netflix_original_ratio,
    rm.content_warning_ratio,

    -- Recency
    (umb.snapshot_month - w.last_watch_timestamp::date) AS days_since_last_watch,
    (umb.snapshot_month - u.created_at::date) AS account_age_days,

    -- Placeholder churn (we compute next)
    0 AS churn_next_month

FROM user_month_base umb
LEFT JOIN users1 u ON umb.user_id = u.user_id
LEFT JOIN watch_monthly w ON umb.user_id = w.user_id AND umb.snapshot_month = w.snapshot_month
LEFT JOIN rec_monthly r ON umb.user_id = r.user_id AND umb.snapshot_month = r.snapshot_month
LEFT JOIN search_monthly s ON umb.user_id = s.user_id AND umb.snapshot_month = s.snapshot_month
LEFT JOIN review_movie_monthly rm ON umb.user_id = rm.user_id AND umb.snapshot_month = rm.snapshot_month

WHERE w.monthly_sessions IS NOT NULL;