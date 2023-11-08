from flask import Flask, send_from_directory, Blueprint, render_template, request, redirect, url_for, jsonify, g
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
from werkzeug.utils import secure_filename, escape
import pdb
import sqlite3
import datetime
from secrets import token_hex
import pandas as pd
import os
from app.utility.csvFileWriter import updater, writer

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY']='IMPACTGUARD'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["jpeg", "jpg", "png"]
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
app.config["IMAGE_UPLOADS"] = os.path.join(basedir, "uploads")
app.config["RECAPTCHA_PUBLIC_KEY"] = "6Lfty"
app.config["RECAPTCHA_PRIVATE_KEY"]="6LFSDFFDY"

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