from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

account_bp = Blueprint('account', __name__)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

@account_bp.route("/account")
def account():
    return render_template("account.html")