CREATE TABLE IF NOT EXISTS CREATE TABLE IF NOT EXISTS netflix_large_user_data (

    customer_id VARCHAR PRIMARY KEY,

    subscription_length_months INT,
    customer_satisfaction_score INT,
    daily_watch_time_hours NUMERIC,

    engagement_rate INT,
    device_used_most_often VARCHAR,
    genre_preference VARCHAR,
    region VARCHAR,

    payment_history VARCHAR,
    subscription_plan VARCHAR,

    churn BOOLEAN,

    support_queries_logged INT,
    age INT,
    monthly_income NUMERIC,
    promotional_offers_used INT,
    number_of_profiles_created INT

); (

    customer_id VARCHAR PRIMARY KEY,

    subscription_length_months INT,
    customer_satisfaction_score INT,
    daily_watch_time_hours NUMERIC,

    engagement_rate INT,
    device_used_most_often VARCHAR,
    genre_preference VARCHAR,
    region VARCHAR,

    payment_history VARCHAR,
    subscription_plan VARCHAR,

    churn BOOLEAN,

    support_queries_logged INT,
    age INT,
    monthly_income NUMERIC,
    promotional_offers_used INT,
    number_of_profiles_created INT

);