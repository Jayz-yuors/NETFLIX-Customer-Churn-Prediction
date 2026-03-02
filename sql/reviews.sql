CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    user_id VARCHAR REFERENCES users1(user_id),
    movie_id VARCHAR REFERENCES movies(movie_id),
    review_text TEXT,
    sentiment_score NUMERIC,
    rating NUMERIC,
    review_timestamp TIMESTAMP,
    device_type VARCHAR,
    contains_spoilers BOOLEAN,
    review_length INT,
    location_country VARCHAR,
    helpful_votes NUMERIC
);