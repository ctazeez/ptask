#!/bin/bash

host="$1"

cmd="$@"
 
until [ -f /opt/filedata/google_activity_by_London_Borough.csv ] ; 
do
  >&2 echo "File not unavailable - sleeping"
  sleep 1
done
 
>&2 echo "File ready - executing command"
exec $cmd