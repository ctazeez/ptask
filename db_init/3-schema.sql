CREATE USER myuser;
CREATE DATABASE mydb;
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

CREATE TABLE google_activity_by_london_borough (
date DATE,
area_name VARCHAR ( 50 ) ,
area_code VARCHAR ( 50 ) ,
retail_and_recreation_percent_change_from_baseline VARCHAR ( 255 ) ,
grocery_and_pharmacy_percent_change_from_baseline VARCHAR ( 255 ) ,
parks_percent_change_from_baseline VARCHAR ( 255 ) ,
transit_stations_percent_change_from_baseline VARCHAR ( 255 ) ,
workplaces_percent_change_from_baseline VARCHAR ( 255 ) ,
residential_percent_change_from_baseline VARCHAR ( 255 )
);