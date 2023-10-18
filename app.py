from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.get("/")
def home():
    return "Welcome to Flask Home Page!"