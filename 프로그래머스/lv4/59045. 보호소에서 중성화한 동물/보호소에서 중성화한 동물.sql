SELECT i.animal_id, i.animal_type, i.name
FROM animal_ins i JOIN animal_outs o
ON i.animal_id = o.animal_id
WHERE i.sex_upon_intake like 'Intact%'
AND o.sex_upon_outcome not like 'Intact%'
ORDER BY i.animal_id