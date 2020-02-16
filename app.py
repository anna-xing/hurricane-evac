import json, os, db
import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify, request, redirect
from pymongo import MongoClient, DESCENDING
from shapely.geometry import LineString, Point
from geopy.distance import geodesic

app = Flask(__name__)
client = MongoClient()

# Both miles
RADIUS = 150
MIN_WINDSPEED = 96

# Landing page
@app.route('/')
def main():
    return render_template('home.html')

@app.route('/map.html')
def map():
    return render_template('map.html')

# Adding evac route entries into MongoDB
@app.route('/add_routes')
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
    return redirect('/')

# Checking if evacuation is feasible given user location
@app.route('/check_evac', methods=['GET', 'POST'])
def check_evac():
    user_location = {
        'lat': request.json['lat'],
        'lng': request.json['lng']
    }

    # Reading in hurricane data points
    import hurr_data_reader

    windspeeds = hurr_data_reader.df1['Wind'].tolist()
    lats = hurr_data_reader.df1['Lat'].tolist()
    lngs = hurr_data_reader.df1['Lon'].tolist()

    for i in range(1, len(windspeeds)):
        # Getting distance from hurricane path to user
        x1 = lats[i-1]
        y1 = lngs[i-1]

        x2 = lats[i]
        y2 = lngs[i]

        user_x = user_location.get('lat')
        user_y = user_location.get('lng')

        hurr_line = {
            'm': (y2-y1) / (x2-x1) if (x2-x1 != 0) else None,
            'b': y1 - ((y2-y1)/(x2-x1)) * x1 if (x2-x1 != 0) else None
        }

        if hurr_line.get('m') == 0:
            perp_line = {
                'm': None,
                'b': None
            }
        else:
            perp_line = {
                'm': -1 / hurr_line.get('m') if hurr_line.get('m') != None else 0,
                'b': user_y - ((x1-x2)/(y2-y1)) * user_x if (y2-y1 != 0) else user_y
            }

        if perp_line.get('m') == None:
            inter_x = user_x
            inter_y = y1
        elif hurr_line.get('m') == None:
            inter_x = x1
            inter_y = user_y
        else:
            inter_x = (perp_line.get('b') - hurr_line.get('b')) / (hurr_line.get('m') - perp_line.get('m'))
            inter_y = hurr_line.get('m') * inter_x + hurr_line.get('b')

        dist = geodesic((inter_x, inter_y), (user_x, user_y)).miles
        
        if windspeeds[i] >= MIN_WINDSPEED and dist <= RADIUS:
            return redirect('/display_evac.html')

    return redirect('/map.html')

# Getting evac routes from MongoDB
# @app.route('/display_evac')
# def display_evac():


if __name__ == "__main__":
    app.run(port=5000)