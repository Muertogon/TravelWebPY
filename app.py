from flask import Flask, redirect, url_for, render_template
from apifunc import whatCity
from geoloc import getLoc
import requests
import geocoder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", result = whatCity("New York"))

#in NAVBAR
@app.route('/nature')
def nature():
    return render_template("nature.html")

@app.route('/cities')
def cities():
    return render_template("cities.html")

@app.route('/monuments')
def monuments():
    return render_template("monuments.html")

@app.route('/recommendations', methods=["POST", "GET"])
def recc():
    if request.method == "POST":
        gotCity = request.form["nm"]
    return render_template("recommendations.html", gotten = gotCity)

print(getLoc("Jonava"))

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)

