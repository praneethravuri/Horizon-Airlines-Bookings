from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

from_locations = list(flights.distinct("flight_details.fromLocation"))
to_locations = list(flights.distinct("flight_details.toLocation"))
from_location_code = list(flights.distinct("flight_details.fromLocationAirportCode"))
to_location_code = list(flights.distinct("flight_details.toLocationAirportCode"))

print(from_locations)
print("\n")
print(to_locations)
print("\n")
print(from_location_code)
print("\n")
print(to_location_code)