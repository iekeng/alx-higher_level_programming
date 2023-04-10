-- Lists all cities of California in the db
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name='California')
ORDER BY id ASC;
