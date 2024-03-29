from flask import Blueprint, render_template, request, redirect, url_for, jsonify, redirect, g
from app.blueprints.extruder.extruderForm import ExtruderForm, ExtruderFilterForm
from app.models.extruderDataHelper import get_extruder_df, get_extruder_history_df, insert_extruder_data, isUpdateorInsert, update_extruder_data
from app.models.referenceTableHelper import get_color_name_for_id, get_colors_from_database, get_extruder_location_from_database, get_result_query, get_width_from_database, get_users_from_database, get_width_name_for_id
from app.utility.query_helper import get_colors, get_extruder_data, get_locations, get_users, get_widths, insert_extruder
from app.utility.db_helper import get_db
from app.utility.flash_utility import flash_message
from datetime import datetime, timezone
import pytz
import pandas as pd

extruder_blueprint = Blueprint("extruder", __name__, template_folder="templates")

# This is one default page 
@extruder_blueprint.route("/", methods=['GET', 'POST'])
def new():
    df = get_extruder_df()
    print(df.head(5))
    return render_template('extrudernew.html', column_names=df.columns.values, data=df)


# This is the history page
@extruder_blueprint.route("/exthist/<int:extID>", methods=['GET', 'POST'])
def hist(extID):
    df = get_extruder_df()
    filterDF = df[df['ID'] == extID]   
    dfHist = get_extruder_history_df(extID)
    return render_template('extruderhist.html', extruderData=filterDF, extruderHist = dfHist)

# This is the add extruder page
@extruder_blueprint.route("/add", methods=["GET", "POST"])
def addExtruder():
    colors = get_colors_from_database()
    width = get_width_from_database()
    location = get_extruder_location_from_database()
    users = get_users_from_database()
    form = ExtruderForm()
    form.locationID.choices = location
    form.colorID.choices = colors
    form.widthID.choices = width 
    form.users.choices = users

    if request.method == "POST":
        locationID = request.form.get('locationID')
        colorID = request.form.get('colorID')
        widthID = request.form.get('widthID')
        length = int(request.form.get('length'))
        weight = float(request.form.get('weight'))
        userID = request.form.get('users')
        comment = request.form.get('comment')
        utc_time = datetime.utcnow()
        # Make it aware of the UTC timezone
        utc_time = utc_time.replace(tzinfo=pytz.utc)
        # Convert it to EST timezone
        est_time = utc_time.astimezone(pytz.timezone("US/Eastern"))
        returnValue = get_result_query(color_id=colorID, width_id=widthID)
        if returnValue == 0:
            insert_extruder_data(
                locationID, colorID, widthID, length, utc_time, utc_time, 
                    userID, userID, weight)
        else:
            id = returnValue
            update_extruder_data(id, locationID, length, modifiedDate=utc_time, modifiedById=userID, weight=weight)

        colorname = get_color_name_for_id(colorID, colors)
        widthname = get_width_name_for_id(widthID, width)

        flash_message(f'form submitted for color : {colorname} with width: {widthname} of length: {length}', 'success')  
        return redirect("/")      

    return render_template('extruderadd.html', form=form)

@extruder_blueprint.route("/new", methods=['GET', 'POST'])
def home():
    data = get_extruder_data()
    print(len(data))
    if request.method == "POST":
        # process form page
        print('hello world!', request.form.get("location"))
        print(request.form.get("rollNumber"), request.form.get("color"), request.form.get("size"), request.form.get("length"), request.form.get("weight"))

   # pdb.set_trace()
    return render_template('extruder.html', data = data)

@extruder_blueprint.route("/filter/<criteria>", methods=['GET', 'POST'])
def filterCriteria12(criteria):
    pass
    

def get_data(numberOfDays):
    if numberOfDays is None:
        print('all the results')
    
    dt = datetime.date.today()
    if (numberOfDays == 7):        
        newDate = dt + dt.timedelta(days = -7)

    if (numberOfDays == 31):
        newDate = dt + dt.timedelta(days = -31)
        
@extruder_blueprint.route("/filter", methods=['GET', 'POST'])
def filterCriteria():
    colorExtruder, colorCrossPly = get_colors()
    widths = get_widths()
    form = ExtruderFilterForm()
    form.colorFilterForm.choices = colorExtruder
    form.widthFilterForm.choices = widths
    if request.method == "POST":
        colorList = request.form.getlist('colorFilterForm')
        widthList = request.form.getlist('widthList')
        return render_template('home.html')
    return render_template('extruderFilter.html', form= form)


@extruder_blueprint.route("/test", methods=['GET', 'POST'])
def test():
    colorExtruder, colorCrossPly = get_colors()
    locationExtruder, locationCrossply = get_locations()
    widths = get_widths()
    users = get_users()
    

    form = ExtruderForm()
    form.locationID.choices = locationExtruder
    form.colorID.choices = colorExtruder
    form.widthID.choices = widths
    form.users.choices = users
    if request.method== "POST":
        locationID = request.form.get('locationID')
        colorID = request.form.get('colorID')
        widthID = request.form.get('widthID')
        length = request.form.get('length')
        weight = request.form.get('weight')
        userID = request.form.get('users')
        comment = request.form.get('comment')
        utc_time = datetime.utcnow()
        # Make it aware of the UTC timezone
        utc_time = utc_time.replace(tzinfo=pytz.utc)
        # Convert it to EST timezone
        est_time = utc_time.astimezone(pytz.timezone("US/Eastern"))
        extruderData = [(locationID, colorID, widthID, length, weight, est_time, userID, utc_time, comment )]
        insert_extruder(extruderData)
        flash_message(f'form submitted for {locationID} of color : {colorID} with width: {widthID} of length: {length}', 'success')        
        return render_template('home.html')

    return render_template('test.html', form=form)
