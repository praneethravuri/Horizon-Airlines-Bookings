from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

payment_bp = Blueprint('payment', __name__)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

@payment_bp.route("/login")
def payment():
    return render_template("payment.html")