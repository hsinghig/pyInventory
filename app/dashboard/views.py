from flask import Blueprint, render_template, request, redirect, url_for, jsonify, redirect
from app import app
from app.dataLoader import loadInventoryData
dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates")

@dashboard_blueprint.route("/")
def home():
    extruderDF, crossPlyDF = loadInventoryData()
    return render_template('dashboard.html', extruderDF=extruderDF, crossPlyDF=crossPlyDF)