import json, os, db, geopy.geocoders
import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient, DESCENDING
from shapely.geometry import LineString, Point

app = Flask(__name__)
client = MongoClient()

# Both miles
RADIUS = 150
MIN_WINDSPEED = 96

# Landing page
@app.route('/')
def main():
    return render_template('map.html')

# Adding evac route entries into MongoDB
@app.route("/add_routes")
def add_route():
    db.db.collection.insert_one({"start": [26.317770, -81.745250], "end": [26.167890, -81.113650]})
    db.db.collection.insert_one({"start": [26.157330, -81.345170], "end": [25.840650, -81.383470]})
    db.db.collection.insert_one({"start": [26.323280, -81.810040], "end": [26.157330, -81.345170]})
    db.db.collection.insert_one({"start": [26.499590, -81.489690], "end": [26.466190, -81.436340]})
    db.db.collection.insert_one({"start": [26.321970, -81.810180], "end": [25.813330, -80.883550]})
    db.db.collection.insert_one({"start": [26.418500, -81.407150], "end": [26.292980, -81.579290]})
    db.db.collection.insert_one({"start": [26.333730, -81.545900], "end": [26.233970, -81.544540]})
    db.db.collection.insert_one({"start": [26.229860, -81.543380], "end": [26.211830, -81.723030]})
    db.db.collection.insert_one({"start": [26.272970, -81.790520], "end": [26.153120, -81.538400]})
    return render_template('map.html')

# Checking if evacuation is feasible given user location
@app.route('/check_evac', methods=['GET', 'POST'])
def check_evac():
    user_location = request.get_json()

    # Reading in hurricane data points
    import hurr_data_reader

    windspeeds = hurr_data_reader.df1['Wind'].tolist()
    lats = hurr_data_reader.df1['Lat'].tolist()
    lngs = hurr_data_reader.df1['Lon'].tolist()

    for i in range(1, len(windspeeds)):
        # Getting distance from hurricane path to user
        line = LineString([ (lats[i-1], lngs[i-1]), (lats[i], lngs[i])])
        pt = Point(user_location.get('lat'), user_location.get('lng'))
        dist = pt.distance(line)
        nearest_pt = line.interpolate(dist).wkt.coords
        dist_miles = geodesic(nearest_pt, (user_location.get('lat'), user_location.get('lng'))).miles

        if windspeeds[i] >= MIN_WINDSPEED and dist_miles <= RADIUS:
            return "evac needed!" #render_template('/display_evac.html')
    
    return "evac not recommended!" #render_template('/no_evac.html')

if __name__ == "__main__":
    app.run(port=5000)