import requests, json, os
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)

@app.route('/')
def render():
    return render_template('index.html')
