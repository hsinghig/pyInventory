from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify, redirect
import pandas as pd

from app.utility.csvFileWriter import updater, writer

app = Flask(__name__)
app.config['SECRET_KEY']='IMPACTGUARD'

@app.route("/")
@app.route("/home")
def home():
    filename = 'app//data//test.csv'
    header = ('Rank', 'Rating', 'Title')
    data = [
        (1, 8, 'The Matrix'), (1, 7, 'The Matrix Reloaded'), (1, 5, 'The Matrix Revolutions'), (1, 6, 'The Matrix Resurrections')
    ]
    writer(header, data, filename, "write")
    updater(filename=filename)
    return render_template('index.html')

@app.route("/index")
def index():   
 
    return render_template("index.html")

@app.route("/api/data")
def getExtruderData():

    filepath = 'app//data//extruderData.json'    
    df = pd.read_json(filepath)
    json_data = df.to_json(orient='records')
    return json_data

from app.crossply.views import crossply_blueprint
app.register_blueprint(crossply_blueprint, url_prefix='/crossply')

from app.dashboard.views import dashboard_blueprint
app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

from app.extruder.views import extruder_blueprint
app.register_blueprint(extruder_blueprint, url_prefix='/extruder')