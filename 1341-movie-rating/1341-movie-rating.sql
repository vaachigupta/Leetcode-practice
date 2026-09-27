# Write your MySQL query statement below
(SELECT u.name AS results
FROM Users u JOIN MovieRating m
ON u.user_id=m.user_id
GROUP BY u.user_id, u.name
ORDER BY COUNT(*) DESC, u.name
LIMIT 1 )

UNION ALL

( SELECT t.title AS results
FROM Movies t JOIN MovieRating m 
ON t.movie_id=m.movie_id
WHERE m.created_at>='2020-02-01'
    AND m.created_at<'2020-03-01'
GROUP BY t.movie_id, t.title
ORDER BY AVG(m.rating) DESC, t.title
LIMIT 1);