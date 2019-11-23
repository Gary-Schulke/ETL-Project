-- Joins tables
SELECT city.city_id city.city_name, cities.country, tracks.length
FROM cities
JOIN tracks
ON city.city_id = tracks.city_id;

