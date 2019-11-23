-- Create tables for raw data to be loaded into
CREATE TABLE cities (
city_id INT PRIMARY KEY,
city_name VARCHAR,
country VARCHAR
);

CREATE TABLE tracks (
city_id INT PRIMARY KEY,
length INT
);



