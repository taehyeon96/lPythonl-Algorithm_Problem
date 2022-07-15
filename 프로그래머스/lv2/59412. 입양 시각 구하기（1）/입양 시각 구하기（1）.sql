SELECT HOUR(datetime) as 'HOUR', COUNT(datetime) as 'COUNT'
FROM animal_outs
WHERE HOUR(datetime) BETWEEN '09:00:00' AND '19:59:00'
GROUP BY HOUR(datetime)
ORDER BY HOUR(datetime)