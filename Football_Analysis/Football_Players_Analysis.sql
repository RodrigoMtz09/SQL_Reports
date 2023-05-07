-- 500 most expensive Football players in the world

-- Display the first 5 rows of the dataset 
SELECT *
FROM players 
LIMIT 5;


-- To verify that the changes have been made correctly
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'players' ORDER BY column_name;

-- Determining the total count of rows that contain a missing value
SELECT COUNT(*) 
FROM players 
WHERE market_value IS NULL OR position IS NULL

-- Determining the total count of rows that contain a missing value
SELECT name, market_value, club, position, country 
FROM players 
ORDER BY market_value DESC 
LIMIT 10;

-- Determining the total count of rows that contain a missing value
SELECT position, COUNT(name) as number_of_players 
FROM players 
GROUP BY position 
ORDER BY number_of_players DESC; 

-- Determining the total count of rows that contain a missing value
SELECT club, COUNT(*) AS number_of_players 
FROM players 
GROUP BY club 
ORDER BY number_of_players DESC 
LIMIT 10;

-- Determining the total count of rows that contain a missing value
SELECT rank, name, position, club, matches 
FROM players 
ORDER BY matches DESC 
LIMIT 1;


-- Player with the highest number of assists in the dataset
SELECT rank, name, assists, position, club 
FROM players 
ORDER BY assists DESC 
LIMIT 1;

-- Player with the highest number of yellow cards 
SELECT rank, name, position, club, yellow_cards 
FROM players 
ORDER BY yellow_cards DESC 
LIMIT 1;

-- Determining those players who have score more than 20 goals
SELECT rank, name, club, goals 
FROM players WHERE goals > 20 
ORDER BY goals DESC;

-- Position with the highest number of red cards (SUM red_cards by position)
SELECT position, SUM(red_cards) as total_red_cards 
FROM players 
GROUP BY position 
HAVING SUM(red_cards) > 0 
ORDER BY total_red_cards DESC;

-- Display the countries with the most number of players in the dataset (Top 15)
SELECT country, COUNT(*) AS total_of_expensive_players 
FROM players 
GROUP BY country 
ORDER BY total_of_expensive_players DESC 
LIMIT 15;

-- Count of players by different age groups 
SELECT CASE 
WHEN age < 21 THEN 'under 21' 
WHEN age BETWEEN 21 AND 25 THEN '21 - 25' 
WHEN age BETWEEN 26 AND 30 THEN '26 - 30' 
ELSE '+30' END AS age_group, 
COUNT(*) AS total_of_players 
FROM players 
GROUP BY age_group 
ORDER BY age_group DESC;

-- Determining the highest market value by position (From highest to lowest)
SELECT position, MAX(market_value) AS max_market_value 
FROM players 
GROUP BY position 
ORDER BY max_market_value DESC;

-- Determining the average market value by position (From highest to lowest)
SELECT position, ROUND(AVG(market_value),2) AS avg_market_value 
FROM players 
GROUP BY position 
ORDER BY avg_market_value DESC;

-- Players with the most number of matches as substitutes
SELECT rank, name, matches, number_of_substitute_in 
FROM players WHERE number_of_substitute_in > 0 
ORDER BY number_of_substitute_in DESC 
LIMIT 15;


-- Bonus: The club with the second highest amount of players 

-- First, creating A CTE only with club and number of players by club 
WITH counts AS (
SELECT club, COUNT(*) AS total_players
FROM players
GROUP BY club
),

-- Then, we use the rank function, creating the another CTE 
ranked AS (
SELECT *, RANK() OVER(ORDER BY total_players DESC) AS rank
FROM counts )

-- Now, just select the rank number 2 to get the club with the second highest number of players 
SELECT * 
FROM ranked
WHERE rank = 2;




