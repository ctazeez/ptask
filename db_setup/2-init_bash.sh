#!/bin/bash

host="$1"

cmd="$@"
  
until [ -f /opt/filedata/google_activity_by_London_Borough.csv ]; do
  >&2 echo "Backup not available sleeping"
  sleep 1
done
  
>&2 echo "Backup file exists"
exec $cmd