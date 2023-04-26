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

i = 0
for air in airline_names:
    print("db.discount.insertOne({" + '"' + air + '"' + ":" + "{government: " + str(random.randint(0, 70)) + ",student: " + str(random.randint(0, 70)) +",privateSector: " + str(random.randint(0, 70)) +",unemployed: " + str(random.randint(0, 70)) +",business: " + str(random.randint(0, 70))  + "}})")
    print("\n")

result = discount.find_one({'Qantas Airways.privateSector': 1})

# print the value of privateSector
print(result['Qantas Airways']['privateSector'])