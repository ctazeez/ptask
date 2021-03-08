from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test12345@db/postgres'
app.debug=True

db=SQLAlchemy(app)

class google_activity(db.Model):

    __tablename__ = 'google_activity_by_lb'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    area_name = db.Column(db.String(), nullable=True)
    area_code = db.Column(db.String(), nullable=True)
    retail_and_recreation_percent_change_from_baseline = db.Column(db.String(), nullable=True)
    grocery_and_pharmacy_percent_change_from_baseline = db.Column(db.String(), nullable=True)
    parks_percent_change_from_baseline = db.Column(db.String(), nullable=True)
    transit_stations_percent_change_from_baseline = db.Column(db.String(), nullable=True)
    workplaces_percent_change_from_baseline = db.Column(db.String(), nullable=True)
    residential_percent_change_from_baseline = db.Column(db.String(), nullable=True)


    def __init__(self,id,date,area_name,area_code,retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline):
        self.id = id
        self.date = date
        self.area_name = area_name
        self.area_code = area_code
        self.retail_and_recreation_percent_change_from_baseline = retail_and_recreation_percent_change_from_baseline
        self.grocery_and_pharmacy_percent_change_from_baseline = grocery_and_pharmacy_percent_change_from_baseline
        self.parks_percent_change_from_baseline = parks_percent_change_from_baseline
        self.transit_stations_percent_change_from_baseline = transit_stations_percent_change_from_baseline
        self.workplaces_percent_change_from_baseline = workplaces_percent_change_from_baseline
        self.residential_percent_change_from_baseline = residential_percent_change_from_baseline

@app.route('/healthcheck', methods=['GET'])
def healthCheck():
    return {
        'Status':'Healthy'
    }

@app.route('/api/area', methods=['GET'])
def getArea():
    name = request.args.get('name')
    # allarea = area.query.all()
    #getarea = google_activity()
    result=[]
    allarea = google_activity.query.all()
    #filtered = [a for a in allarea if a['area_name']==name]
    for area in allarea:
        curActivity ={}
        curActivity['area_name'] = area.area_name
        curActivity['area_code'] = area.area_code
        
        result.append(curActivity)
    return jsonify(result), 200
    
@app.route('/google_activity', methods=['GET'])
def getGoogleActivity():
    output=[]
    allactivity = google_activity.query.all()

    for acitivity in allactivity:
        curActivity ={}
        curActivity['Date'] = acitivity.date
        curActivity['area_name'] = acitivity.area_name
        curActivity['area_code'] = acitivity.area_code
        curActivity['retail_and_recreation_percent_change_from_baseline'] = acitivity.retail_and_recreation_percent_change_from_baseline
        curActivity['grocery_and_pharmacy_percent_change_from_baseline'] = acitivity.grocery_and_pharmacy_percent_change_from_baseline
        curActivity['parks_percent_change_from_baseline'] = acitivity.parks_percent_change_from_baseline
        curActivity['transit_stations_percent_change_from_baseline'] = acitivity.transit_stations_percent_change_from_baseline
        curActivity['workplaces_percent_change_from_baseline'] = acitivity.workplaces_percent_change_from_baseline
        curActivity['residential_percent_change_from_baseline'] = acitivity.residential_percent_change_from_baseline

        output.append(curActivity)

    return jsonify(output)

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
