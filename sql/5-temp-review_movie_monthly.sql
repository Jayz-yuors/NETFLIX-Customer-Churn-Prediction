CREATE TEMP TABLE review_movie_monthly AS
SELECT
    r.user_id,
    date_trunc('month', r.review_timestamp)::date AS snapshot_month,

    COUNT(*) AS monthly_reviews,
    AVG(r.sentiment_score) AS avg_sentiment_score,
    AVG(r.rating) AS avg_review_rating,
    AVG(r.review_length) AS avg_review_length,

    COUNT(DISTINCT m.genre_primary) AS genre_diversity,
    AVG(m.imdb_rating) AS avg_movie_imdb_rating,
    AVG(CASE WHEN m.is_netflix_original THEN 1 ELSE 0 END) AS netflix_original_ratio,
    AVG(CASE WHEN m.content_warning THEN 1 ELSE 0 END) AS content_warning_ratio

FROM reviews r
LEFT JOIN movies m ON r.movie_id = m.movie_id
GROUP BY r.user_id, date_trunc('month', r.review_timestamp);