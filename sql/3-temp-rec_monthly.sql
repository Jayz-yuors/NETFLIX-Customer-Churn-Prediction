-- -> RECOMMENDATION AGGREGATION
CREATE TEMP TABLE rec_monthly AS
SELECT
    user_id,
    date_trunc('month', recommendation_timestamp)::date AS snapshot_month,

    COUNT(*) AS monthly_recommendations,
    AVG(CASE WHEN clicked THEN 1 ELSE 0 END) AS recommendation_click_rate,
    AVG(recommendation_score) AS avg_recommendation_score,
    AVG(rank_position) AS avg_rank_position

FROM recommendation_logs
GROUP BY user_id, date_trunc('month', recommendation_timestamp);