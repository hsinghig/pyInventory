from flask import Blueprint, render_template, request, redirect, send_file, url_for, jsonify, redirect

home_blueprint = Blueprint("home", __name__, template_folder="templates")

@home_blueprint.route("/")
def home():
    return render_template('home.html')
