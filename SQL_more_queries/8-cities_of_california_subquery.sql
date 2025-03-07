--  lists all the cities of California that can be found
USE hbtn_0d_usa;
SET @california_id = (SELECT id FROM states WHERE name = 'California');
SELECT id, name FROM cities WHERE state_id = @california_id ORDER BY id ASC;
