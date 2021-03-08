
CREATE TABLE google_activity_by_lb (
id serial PRIMARY KEY,
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

COPY google_activity_by_lb (date,area_name,area_code,retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline) 
FROM '/opt/filedata/google_activity_by_London_Borough.csv' delimiter ',' csv header;