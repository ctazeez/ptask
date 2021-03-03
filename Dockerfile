FROM postgres:latest
#for postgres
RUN  apt-get update -y && apt-get install wget -y
CMD cd /tmp/ && wget https://data.london.gov.uk/download/google-mobility-by-borough/26d5821b-fcb6-4aae-af73-ee0596942d16/google_activity_by_London_Borough.csv"
