CREATE TABLE IF NOT EXISTS watch_history (
    session_id VARCHAR PRIMARY KEY,
    user_id VARCHAR REFERENCES users1(user_id),
    movie_id VARCHAR REFERENCES movies(movie_id),
    watch_date TIMESTAMP,
    device_type VARCHAR,
    watch_duration_minutes NUMERIC,
    progress_percentage NUMERIC,
    action VARCHAR,
    quality VARCHAR,
    location_country VARCHAR,
    is_download BOOLEAN,
    user_rating NUMERIC
);