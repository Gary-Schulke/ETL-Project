-- Database: ETL_Project

-- DROP DATABASE "ETL_Project";

CREATE DATABASE "city_transit_db"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Create tables for raw data to be loaded into
CREATE TABLE cities (
city_id INT PRIMARY KEY,
city_name VARCHAR,
country VARCHAR
);

CREATE TABLE tracks (
city_id INT PRIMARY KEY,
length INTx
);



