CREATE VIEW view_requests_per_day AS 
SELECT time::date AS day, COUNT(time) AS num 
FROM log 
GROUP BY day;


CREATE VIEW view_requests_per_day_with_error AS SELECT time::date AS day, COUNT(time) AS num 
FROM log 
WHERE status LIKE '404%' 
GROUP BY day;