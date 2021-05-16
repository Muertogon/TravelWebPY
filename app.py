from flask import Flask, redirect, url_for, render_template
from apifunc import whatCityWeather
from geoloc import getLoc
from flask import request
import geocoder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", result = whatCityWeather("New York"))

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

@app.route('/recommendations')
def recommendations():
    return render_template("recommendations.html")

@app.route('/getrecc', methods=["POST", "GET"])
def recc():
    if request.method == "POST":
        gotCity = request.form["nm"]
        city = getLoc(gotCity)

        return render_template("recommendations.html", gotten=city)
    else:
        return render_template("getrecc.html")
        



if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)
