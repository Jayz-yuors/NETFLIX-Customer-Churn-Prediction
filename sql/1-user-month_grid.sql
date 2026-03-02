/*CREATE TEMP TABLE months AS -> temporary month list
SELECT generate_series(
    '2024-01-01'::date,
    '2025-12-01'::date,
    interval '1 month'
)::date AS snapshot_month;*/
CREATE TEMP TABLE user_month_base AS  
SELECT
    u.user_id,
    m.snapshot_month
FROM users1 u
CROSS JOIN months m; 
