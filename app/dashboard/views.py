from flask import Blueprint, render_template, request, redirect, send_file, url_for, jsonify, redirect
from app import app
from app.dataLoader import loadInventoryData
dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates")

@dashboard_blueprint.route("/")
def home():
    extruderDF, crossPlyDF = loadInventoryData()
    return render_template('dashboard.html', extruderDF=extruderDF, crossPlyDF=crossPlyDF)

@dashboard_blueprint.route("/processextruder")
def processextruder():

    return send_file('../extruderData.csv', as_attachment=True)

@dashboard_blueprint.route("/process-crossply")
def processCrossply():
    return send_file('crossplyData.csv', as_attachment=True)