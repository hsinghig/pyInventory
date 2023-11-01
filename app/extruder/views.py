from flask import Blueprint, render_template, request, redirect, url_for, jsonify, redirect

from app import app

extruder_blueprint = Blueprint("extruder", __name__, template_folder="templates")

@extruder_blueprint.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        # process form page
        print('hello world!', request.form.get("location"))
        print(request.form.get("rollNumber"), request.form.get("color"), request.form.get("size"), request.form.get("length"), request.form.get("weight"))

   # pdb.set_trace()
    return render_template('extruder.html')