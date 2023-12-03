from flask import Blueprint, render_template, request, redirect, send_file, url_for, jsonify, redirect

from app.dataLoader import loadInventoryData
from app.models import tblwidth

from app.extensions import db
from sqlalchemy import text

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

@dashboard_blueprint.route('/user/<name>')
def create_tablewidth(name):
    width = tblwidth(name=name, isActive=True, comment='Added now')
    db.session.add(width)
    db.session.commit()
    return 'created width'

@dashboard_blueprint.route('/color/<name>')
def select_tblcolor(name):
    stmt = text('select id, name, isactive from [ip].[tblextruderlocation]')
    with db.engine.connect() as conn:
        result = conn.execute(stmt)
    #result = db.engine.execute(stmt)
    print(result)
    return 'result came from tblcolor'