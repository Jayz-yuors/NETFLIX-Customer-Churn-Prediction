UPDATE ml_user_month_churn_dataset t
SET churn_next_month = 1
WHERE NOT EXISTS (
    SELECT 1
    FROM watch_history w
    WHERE w.user_id = t.user_id
      AND w.watch_date >= t.snapshot_month + interval '1 month'
      AND w.watch_date <  t.snapshot_month + interval '3 month'
);