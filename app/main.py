import sys
import json
import psycopg2
import datetime
from flask import Flask,Response


connection = psycopg2.connect(database="postgres", user="postgres", password="test12345", host="db", port="5432")

app = Flask(__name__)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@app.route("/")
def hello():
   return_list = []

   try:
      cursor = connection.cursor()
      postgreSQL_select_Query = "select * from google_activity_by_lb"
      cursor.execute(postgreSQL_select_Query)      
      all_records = cursor.fetchall()
      
      for row in all_records:
         return_list.append(row)
    
   except (Exception, psycopg2.Error) as error:
      print("Error while fetching data from PostgreSQL", error)
   finally:
      cursor.close()

   return Response(json.dumps(return_list,default = myconverter),  mimetype='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)