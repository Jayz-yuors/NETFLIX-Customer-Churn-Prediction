CREATE TABLE IF NOT EXISTS users1 (
    user_id VARCHAR PRIMARY KEY,
    email VARCHAR UNIQUE,
    first_name VARCHAR,
    last_name VARCHAR,
    age INT,
    gender VARCHAR,
    country VARCHAR,
    state_province VARCHAR,
    city VARCHAR,
    subscription_plan VARCHAR,
    subscription_start_date DATE,
    is_active BOOLEAN,
    monthly_spend NUMERIC,
    primary_device VARCHAR,
    household_size INT,
    created_at TIMESTAMP
);
