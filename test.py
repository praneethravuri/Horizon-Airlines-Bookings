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

query = db.discount.find()

with open('db_data/discount.json', 'w') as f:
    for _ in query:
        json.dump(_, f, default=json_util.default)
        f.write('\n')