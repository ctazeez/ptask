#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER myuser;
    CREATE DATABASE mydb;
    GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
    CREATE TABLE myTable(ZIP1 char(5),ZIP2 char(5)); 
    COPY myTable FROM '/tmp/google_activity_by_London_Borough.csv' WITH (FORMAT csv);
EOSQL
