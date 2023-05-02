from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import random
import string
import json
from bson import json_util

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]
discount = db["discount"]

for document in flights.find():
    # Set price to a random float between 500 and 2000 rounded to 2 decimal places
    price = round(random.uniform(500, 2000), 2)
    
    # Update the document in the collection
    flights.update_one({'_id': document['_id']}, {'$set': {"flight_details.price": price}})