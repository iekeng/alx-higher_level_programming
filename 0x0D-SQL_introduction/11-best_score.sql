-- List all records with score greater than or equal to ten in second_table
SELECT score, name 
FROM second_table 
WHERE `score` >= 10 
ORDER BY `score` DESC;
