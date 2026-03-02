CREATE TABLE ml_user_churn_dataset (

    -- =========================
    -- PRIMARY KEY
    -- =========================
    user_id VARCHAR PRIMARY KEY,

    -- =========================
    -- STATIC USER FEATURES
    -- =========================
    age INT,
    gender VARCHAR,
    country VARCHAR,
    subscription_plan VARCHAR,
    subscription_tenure_days INT,
    is_active BOOLEAN,
    monthly_spend NUMERIC,
    household_size INT,
    primary_device VARCHAR,

    -- =========================
    -- WATCH BEHAVIOR FEATURES
    -- =========================
    total_sessions INT,
    total_watch_hours NUMERIC,
    avg_watch_duration NUMERIC,
    avg_progress_percentage NUMERIC,
    avg_user_rating NUMERIC,
    completed_sessions INT,
    download_sessions INT,

    days_since_last_watch INT,
    active_days_count INT,
    binge_sessions_ratio NUMERIC,

    -- =========================
    -- DEVICE BEHAVIOR
    -- =========================
    distinct_devices_used INT,
    dominant_device VARCHAR,

    -- =========================
    -- RECOMMENDATION FEATURES
    -- =========================
    total_recommendations INT,
    recommendation_click_rate NUMERIC,
    avg_recommendation_score NUMERIC,
    avg_rank_position NUMERIC,

    -- =========================
    -- SEARCH FEATURES
    -- =========================
    total_searches INT,
    search_success_rate NUMERIC,
    avg_search_duration NUMERIC,

    -- =========================
    -- REVIEW FEATURES
    -- =========================
    total_reviews INT,
    avg_sentiment_score NUMERIC,
    avg_review_rating NUMERIC,
    avg_review_length NUMERIC,
    total_helpful_votes NUMERIC,

    -- =========================
    -- MOVIE INTELLIGENCE FEATURES
    -- =========================
    genre_diversity INT,
    most_watched_genre VARCHAR,
    avg_movie_imdb_rating NUMERIC,
    avg_movie_release_year NUMERIC,
    netflix_original_ratio NUMERIC,
    content_warning_ratio NUMERIC,

    -- =========================
    -- TIME FEATURES
    -- =========================
    account_age_days INT,
    last_activity_timestamp TIMESTAMP,

    -- =========================
    -- TARGET LABEL
    -- =========================
    churn_label INT
);