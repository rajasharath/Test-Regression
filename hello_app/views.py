from datetime import datetime
from flask import Flask, render_template
from pd import pandas
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/api/readcsvcolumns")
def readcsvcolumns():
xlsx = pd.ExcelFile('Asinex_2D_K-means_50 Clustering.xlsx',sheetname='Asinex_2D_K-means Clustering')
return xlsx.columns
