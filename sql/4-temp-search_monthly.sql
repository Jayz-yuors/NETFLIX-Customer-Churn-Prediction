-- -> SEARCH AGGREGATION
CREATE TEMP TABLE search_monthly AS
SELECT
    user_id,
    date_trunc('month', search_timestamp)::date AS snapshot_month,

    COUNT(*) AS monthly_searches,
    AVG(CASE WHEN was_successful THEN 1 ELSE 0 END) AS search_success_rate,
    AVG(search_duration_seconds) AS avg_search_duration

FROM search_logs
GROUP BY user_id, date_trunc('month', search_timestamp);