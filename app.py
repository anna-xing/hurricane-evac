import requests, json, os, db
import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify
from pymongo import MongoClient, DESCENDING

app = Flask(__name__)
client = MongoClient()

# Landing page
@app.route('/')
def main():
    return render_template('map.html')

# Adding evac route entries into MongoDB
@app.route("/add_routes")
def add_route():
    db.db.collection.insert_one({"_id": "testRoute1", "distance": 5, "feasible": True})
    db.db.collection.insert_one({"_id": "testRoute2", "distance": 3, "feasible": False})
    return render_template('map.html')

# Checking if evacuation is feasible given user location
@app.route('/check_evac', methods=['GET', 'POST'])
def check_evac():
    import hurr_data_reader
    # processing here

if __name__ == "__main__":
    app.run(port=5000)
