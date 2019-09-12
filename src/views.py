from flask import render_template
from src import app

@app.route("/")
def index():
    return render_template("index.html")