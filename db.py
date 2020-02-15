from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://annaxing:xinga4546@hurricane-evac-heu3f.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')