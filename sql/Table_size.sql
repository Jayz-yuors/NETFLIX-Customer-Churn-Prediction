SELECT 
(SELECT COUNT(*) FROM users1) AS users,
(SELECT COUNT(*) FROM movies) AS movies,
(SELECT COUNT(*) FROM watch_history) AS watch,
(SELECT COUNT(*) FROM recommendation_logs) AS recommend,
(SELECT COUNT(*) FROM search_logs) AS search,
(SELECT COUNT(*) FROM reviews) AS reviews;