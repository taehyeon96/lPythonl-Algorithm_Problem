SET @HOUR = -1;                        -- @HOUR라는 변수 선언(시간은 0부터이므로)

SELECT (@HOUR := @HOUR+1) as 'HOUR',
        (SELECT COUNT(HOUR(datetime)) 
         FROM animal_outs
         WHERE HOUR(datetime) = @HOUR) as 'COUNT'
FROM animal_outs
WHERE @HOUR <= 22;