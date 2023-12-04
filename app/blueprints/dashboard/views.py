from flask import Blueprint, render_template, request, redirect, send_file, url_for, jsonify, redirect, g

from app.dataLoader import loadInventoryData
from app.models import tblwidth
import os
from app.extensions import db
from sqlalchemy import text
import pandas as pd
from datetime import datetime

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates")

def get_df():
    columns = ['id', 'location', 'color', 'width', 'length', 'date_created', 'created_by', 'modified_date']
    result = get_result()
    print(result)   
    df = pd.DataFrame(result, columns=columns)
    return df

@dashboard_blueprint.route("/")
def home():
    extruderDF, crossPlyDF = loadInventoryData()
    df = get_df()
    return render_template('dashboard.html', extruderDF=df, crossPlyDF=crossPlyDF)

@dashboard_blueprint.route("/processextruder")
def processextruder():
    basedir = os.path.abspath(os.path.dirname(__file__))
    fullFolderPath = basedir + "\\fileresult"
    empty_folder(fullFolderPath)
    
    df = get_df()
    basedir = os.path.abspath(os.path.dirname(__file__))
    print(basedir + "\\fileresult\\")
    filename = fullFolderPath + "\\" + str(datetime.now().microsecond) + '_extruder.csv'
    df.to_csv(filename)
    return send_file(filename, as_attachment=True)

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
    #stmt = text('select id, name, isactive from [ip].[tblextruderlocation]')
    selectstmt = get_select_stmt()
    stmt = text(selectstmt)

    with db.engine.connect() as conn:
        result = conn.execute(stmt)
        for i in result:
            print(i[0], i[1], i[2], i[3])
    #result = db.engine.execute(stmt)
    print(result)
    return 'result came from tblcolor'

def get_result():
    selectstmt = get_select_stmt()
    stmt = text(selectstmt)
    values = []
    with db.engine.connect() as conn:
        result = conn.execute(stmt)
        for i in result:
            
            data = {
                'id': i[0], 
                'location': i[10],
                'color': i[9],
                'width': i[14],
                'length': i[4],
                'date_created': i[5],
                'created_by': i[13],
                'modified_date': i[6]                
            }
            values.append(data)        
        return values
    
    print(values)
    return None


def get_select_stmt():
    stmt= '''
SELECT ip.tblextruder.id, ip.tblextruder.location_id, ip.tblextruder.color_id, ip.tblextruder.width_id, ip.tblextruder.length,
ip.tblextruder.CreatedDate, ip.tblextruder.ModifiedDate, ip.tblextruder.CreatedBy_id, ip.tblextruder.ModifiedBy_id, 
ip.tblcolor.name as colorname, ip.tblextruderlocation.name AS locationname, 
             ip.tbluser.firstname, ip.tbluser.lastname, ip.tbluser.email, ip.tblwidth.name AS widthname, ip.tbluser.isactive as useractive
FROM   ip.tblextruder INNER JOIN
             ip.tblcolor ON ip.tblextruder.color_id = ip.tblcolor.id INNER JOIN
             ip.tblextruderlocation ON ip.tblextruder.location_id = ip.tblextruderlocation.id INNER JOIN
             ip.tbluser ON ip.tblextruder.id = ip.tbluser.id INNER JOIN
             ip.tblwidth ON ip.tblextruder.width_id = ip.tblwidth.id
    '''
    return stmt

def empty_folder(mydir):
    filelist = [ f for f in os.listdir(mydir)]
    for f in filelist:
        os.remove(os.path.join(mydir, f))