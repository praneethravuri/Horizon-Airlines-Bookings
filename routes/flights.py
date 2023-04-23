from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

flights_bp = Blueprint('flights', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

@flights_bp.route("/search-flights")
def search_flights():
    user_email = session.get("user_email")
    print(user_email)
    return render_template("flights.html")