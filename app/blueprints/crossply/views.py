from flask import Blueprint, render_template, request, redirect, url_for, jsonify, redirect


crossply_blueprint = Blueprint("crossply", __name__, template_folder="templates")

@crossply_blueprint.route("/")
def home():
    return render_template('xply.html')