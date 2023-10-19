from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Home Page!"

@app.route("/home")
def index():   
    return render_template("index.html")

@app.route("/api/data")
def getExtruderData():
    filepath = 'app//data//extruderData.json'    
    df = pd.read_json(filepath)
    json_data = df.to_json(orient='records')
    return json_data