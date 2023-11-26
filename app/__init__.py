import dateutil
from flask import Flask, send_from_directory, Blueprint, render_template, request, redirect, url_for, jsonify, g
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
from werkzeug.utils import secure_filename, escape
import pdb
import sqlite3
import datetime
from flask_sqlalchemy import SQLAlchemy
from secrets import token_hex
import pandas as pd
import os
from app.utility.csvFileWriter import updater, writer
import config
from app.dataLoader import get_table_DUMMY_DATA

basedir = os.path.abspath(os.path.dirname(__file__))

server = 'dbpyinventory.database.windows.net'
database = 'pyInventoryDB'
username = 'sqladmin'
pwd = 'Harsha77!'

#connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server='+server+';Database='+database+';Uid='+username+';Pwd='+pwd+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
  

app = Flask(__name__)
app.config["SECRET_KEY"] = "IMPACT_GUARD"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mssql+pyodbc://'+username+':' + pwd + '@'+ server + '/' + database + '?driver=ODBC+Driver+17+for+SQL+Server'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://NEW-OFFICE\\user:password@localhost/testdb?driver=ODBC+Driver+17+for+SQL+Server"
db = SQLAlchemy(app)
print(app)
print(app.config)

widths = db.Table('tblwidth', db.metadata, schema="ip", autoload=True, autoload_with=db.engine)

@app.template_filter('strftime')
def _jinja2_filter_datetime(strDate, fmt=None):
    date = dateutil.parser.parse(strDate)
    native = date.replace(tzinfo=None)
    format='%b %d, %Y %H:%M:%S'
    format2 = '%Y-%m-%d %H:%M:%S'
    return native.strftime(format) 

# app.config['SECRET_KEY']='IMPACTGUARD'
# app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["jpeg", "jpg", "png"]
# app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
# app.config["IMAGE_UPLOADS"] = os.path.join(basedir, "uploads")
# app.config["RECAPTCHA_PUBLIC_KEY"] = "6Lfty"
# app.config["RECAPTCHA_PRIVATE_KEY"]="6LFSDFFDY"
# for key in app.config:
#     print(key, app.config[key])
# print(app.config)
# print(os.environ)

@app.route("/table")
def displayTable():
    results = db.session.query(widths).all()
    for r in results:
        print(r.name)
    heading, data = get_table_DUMMY_DATA()
    return render_template('table.html', heading=heading, data=data)

@app.route("/chart")
def get_chart():
    return render_template('chart.html')

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

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()