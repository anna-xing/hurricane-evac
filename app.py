import requests, json, os
import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)

@app.route('/')
def render():
    return render_template('map.html')

# @app.route('/check_evac', methods=['GET', 'POST'])
# def check_evac():
#     import hurr_data_reader
#     results = lambda : for row in hurr_data_reader.df1.iterrows():
#         print("latitude: " + str(row['Lat']) + ", longitude: " + str(row['Lon']))
#     return results
