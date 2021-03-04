
CREATE USER myuser;
CREATE DATABASE IF NOT EXISTS mydb;
GRANT ALL PRIVILEGES ON DATABASE mydb TO ptask_user;

CREATE TABLE IF NOT EXISTS google_activity_by_lb (
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

COPY google_activity_by_lb FROM '/opt/filedata/google_activity_by_London_Borough.csv' delimiter ',' csv header;