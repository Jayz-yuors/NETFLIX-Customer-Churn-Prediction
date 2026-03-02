CREATE TABLE recommendation_logs (
    recommendation_id SERIAL PRIMARY KEY,
    user_id VARCHAR REFERENCES users1(user_id),
    movie_id VARCHAR REFERENCES movies(movie_id),
    recommendation_timestamp TIMESTAMP,
    clicked BOOLEAN,
    watch_after_recommendation BOOLEAN,
    recommendation_type VARCHAR,
    device_type VARCHAR,
    rank_position INT,
    recommendation_score NUMERIC,
    location_country VARCHAR
);