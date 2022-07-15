SELECT animal_type, count(*)
FROM animal_ins
Group BY animal_type
ORDER BY animal_type asc