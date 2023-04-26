from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]
discount = db["discount"]

airline_names = flights.distinct("flight_details.airlineName")

dic = {}

for i in airline_names:
    dic[i] = {"governmentDiscount" : random.randint(1, 7) * 10, "studentDiscount" : random.randint(1, 7) * 10}

discount.insert_one(dic)