--  some selections written in SQL

-- # bring these selections into a working -- conntected
-- # to a database (even local) --  Python notebook IDE

-- for career-level numbers
SELECT DISTINCT player_name
FROM players;

-- make a careers table
CREATE TABLE careers (VARCHAR(124) ) ;

SELECT DISTINCT player_name
FROM players;

SELECT SUM(points)
FROM careers
WHERE player_name;

