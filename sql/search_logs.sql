CREATE TABLE IF NOT EXISTS search_logs (
    search_id SERIAL PRIMARY KEY,
    user_id VARCHAR REFERENCES users1(user_id),
    search_query TEXT,
    search_timestamp TIMESTAMP,
    clicked_result BOOLEAN,
    results_count INT,
    device_type VARCHAR,
    search_category VARCHAR,
    location_country VARCHAR,
    search_duration_seconds NUMERIC,
    was_successful BOOLEAN
);
