from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Home Page!"

@app.route("/home")
def index():
    return render_template("index.html")