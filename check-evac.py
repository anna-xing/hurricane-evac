import requests, json, os, pandas, numpy, hurr_data_reader
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)

FIND_USER_ENDPOINT = ""
API_KEY = "AIzaSyANV5fMhen4qk84sPxZyuQ4QypR3t1pz0I"

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/check_evac', methods=['GET', 'POST'])
def check_evac(user_location):
    for hurr_point in range(len(df1.index)):
        