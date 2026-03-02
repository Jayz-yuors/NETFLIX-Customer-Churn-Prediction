CREATE TABLE ml_user_month_churn_dataset (

    -- =========================
    -- COMPOSITE PRIMARY KEY
    -- =========================
    user_id VARCHAR,
    snapshot_month DATE,

    PRIMARY KEY (user_id, snapshot_month),

    -- =========================
    -- STATIC USER FEATURES
    -- =========================
    age INT,
    gender VARCHAR,
    country VARCHAR,
    subscription_plan VARCHAR,
    subscription_tenure_days INT,
    monthly_spend NUMERIC,
    household_size INT,
    primary_device VARCHAR,

    -- =========================
    -- MONTHLY WATCH FEATURES
    -- =========================
    monthly_sessions INT,
    monthly_watch_hours NUMERIC,
    avg_watch_duration NUMERIC,
    avg_progress_percentage NUMERIC,
    avg_user_rating NUMERIC,
    completed_sessions INT,
    download_sessions INT,

    active_days_in_month INT,

    -- =========================
    -- MONTHLY DEVICE BEHAVIOR
    -- =========================
    distinct_devices_used INT,

    -- =========================
    -- MONTHLY RECOMMENDATION FEATURES
    -- =========================
    monthly_recommendations INT,
    recommendation_click_rate NUMERIC,
    avg_recommendation_score NUMERIC,
    avg_rank_position NUMERIC,

    -- =========================
    -- MONTHLY SEARCH FEATURES
    -- =========================
    monthly_searches INT,
    search_success_rate NUMERIC,
    avg_search_duration NUMERIC,

    -- =========================
    -- MONTHLY REVIEW FEATURES
    -- =========================
    monthly_reviews INT,
    avg_sentiment_score NUMERIC,
    avg_review_rating NUMERIC,
    avg_review_length NUMERIC,

    -- =========================
    -- MONTHLY MOVIE INTELLIGENCE
    -- =========================
    genre_diversity INT,
    avg_movie_imdb_rating NUMERIC,
    netflix_original_ratio NUMERIC,
    content_warning_ratio NUMERIC,

    -- =========================
    -- RECENCY FEATURES
    -- =========================
    days_since_last_watch INT,
    account_age_days INT,

    -- =========================
    -- TARGET
    -- =========================
    churn_next_month INT
);