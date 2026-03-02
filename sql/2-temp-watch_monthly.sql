-- -> MONTHLY WATCH AGGREGATION
CREATE TEMP TABLE watch_monthly AS
SELECT
    user_id,
    date_trunc('month', watch_date)::date AS snapshot_month,

    COUNT(session_id) AS monthly_sessions,
    SUM(watch_duration_minutes)/60.0 AS monthly_watch_hours,
    AVG(watch_duration_minutes) AS avg_watch_duration,
    AVG(progress_percentage) AS avg_progress_percentage,
    AVG(user_rating) AS avg_user_rating,
    SUM(CASE WHEN action = 'completed' THEN 1 ELSE 0 END) AS completed_sessions,
    SUM(CASE WHEN is_download THEN 1 ELSE 0 END) AS download_sessions,
    COUNT(DISTINCT watch_date::date) AS active_days_in_month,
    COUNT(DISTINCT device_type) AS distinct_devices_used,
    MAX(watch_date) AS last_watch_timestamp

FROM watch_history
GROUP BY user_id, date_trunc('month', watch_date);