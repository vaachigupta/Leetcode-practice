# Write your MySQL query statement below
SELECT id 
FROM (SELECT id, recordDate, temperature AS today_temp, 
LAG(recordDate) OVER (ORDER BY recordDATE) AS prev_date,
LAG(temperature) OVER (ORDER BY recordDATE) AS yesterday_temp 
FROM Weather
) AS wea
WHERE DATEDIFF(recordDate, prev_date)=1 
AND yesterday_temp<today_temp;