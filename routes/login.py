from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

login_bp = Blueprint('login', __name__)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

@login_bp.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = users.find_one({'userEmail': email, 'userDetails.userPassword': password})

    if user:
        user_name = user["userDetails"]["userName"]
        booking = bookings.find_one({"userEmail" : email})
        session["user_email"] = email
        if booking:
            user_flights = booking["userFlights"]
            session["user_flights"] = user_flights
            return redirect(url_for("homepage.homepage", user_name = user_name, user_email = email))
        else:
            return render_template("homepage.html", error = "No Bookings")
        
    else:
        return render_template("login.html", error = "Invalid Credentials")