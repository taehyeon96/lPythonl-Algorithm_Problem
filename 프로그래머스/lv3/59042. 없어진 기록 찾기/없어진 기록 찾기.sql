-- 코드를 입력하세요
SELECT o.animal_id, o.name
FROM animal_outs o left outer join animal_ins i
ON o.animal_id = i.animal_id
WHERE i.datetime IS NULL