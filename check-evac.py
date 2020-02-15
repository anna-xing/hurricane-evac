import requests
import json
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/database"
# mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return "hello world"