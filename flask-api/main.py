from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test12345@db/postgres'
app.debug=True

db=SQLAlchemy(app)

class Activity(db.Model):

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


@app.route('/api/v1/healthcheck', methods=['GET'])
def healthCheck():
    try:
        count = Activity.query.count()
        return{
            'Status':'Healthy'
        }, 200
    except exceptions.SQLAlchemyError:
        print("Error while fetching data from PostgreSQL")
        return{
            'Status':'Not Healthy'
        }, 404


@app.route('/api/v1/activities', methods=['GET'])
def activities():
    output= []
    
    try:
      
        allactivity = Activity.query.all()

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
    except exceptions.SQLAlchemyError:
        print("Error while fetching data from PostgreSQL")
        return{
            'message':'Error while fetching data from PostgreSQL'
        }, 404

    return jsonify(output), 200

@app.route('/api/v1/activities/area_by_code/<code>', methods=['GET'])
def get_area_by_code(code):

    try:
        output = []
        allactivity = Activity.query.filter(area_code==code).one()

        for acitivity in allactivity:
            curActivity ={}
            curActivity['area_name'] = acitivity.area_name
            curActivity['area_code'] = acitivity.area_code

            output.append(curActivity)
        
    except exceptions.SQLAlchemyError:
        print("Error while fetching data from PostgreSQL")
        return{
            'message':'Error while fetching data from PostgreSQL'
        }, 404

    return jsonify(output), 200


@app.route('/api/v1/activities/pointers',methods=['GET'])
def getSearchData(): 
    allarea = Activity.query.all()
    keys = [k for k in allarea[0].__dict__]
    del keys[0]
    return jsonify(keys), 200


@app.route('/api/v1/activities/pointers/<string:areacode>/<string:coloumn>/<string:pvalue>', methods=['GET'])
def get_data_by_area_code_and_coloumn(areacode: str, coloumn: str, pvalue: str):
    
    result = []
    
    all_data = Activity.query.filter(getattr(Activity,coloumn).like("%" + pvalue + "%")).filter_by(area_code=areacode).all()

    if len(all_data) <=0:
        return{
            "Message":"No result.. check the data passed."
        }, 400

    for data in all_data:
        curData ={}
        curData['area_name'] = data.area_name
        curData['area_code'] = data.area_code
        curData['date'] = data.date
        curData['retail_and_recreation_percent_change_from_baseline'] = data.retail_and_recreation_percent_change_from_baseline
        curData['grocery_and_pharmacy_percent_change_from_baseline'] = data.grocery_and_pharmacy_percent_change_from_baseline
        curData['parks_percent_change_from_baseline'] = data.parks_percent_change_from_baseline
        curData['transit_stations_percent_change_from_baseline'] = data.transit_stations_percent_change_from_baseline
        curData['workplaces_percent_change_from_baseline'] = data.workplaces_percent_change_from_baseline
        curData['residential_percent_change_from_baseline'] = data.residential_percent_change_from_baseline
        
        result.append(curData)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
