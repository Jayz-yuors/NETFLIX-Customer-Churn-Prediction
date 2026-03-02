DROP TABLE movies CASCADE;

CREATE TABLE movies (
    movie_id VARCHAR PRIMARY KEY,
    title VARCHAR,
    content_type VARCHAR,
    genre_primary VARCHAR,
    genre_secondary VARCHAR,
    release_year NUMERIC,
    duration_minutes NUMERIC,
    rating VARCHAR,
    language VARCHAR,
    country_of_origin VARCHAR,
    imdb_rating NUMERIC,
    production_budget NUMERIC,
    box_office_revenue NUMERIC,
    number_of_seasons NUMERIC,
    number_of_episodes NUMERIC,
    is_netflix_original BOOLEAN,
    added_to_platform DATE,
    content_warning BOOLEAN
);