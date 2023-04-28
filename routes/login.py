from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient('mongodb://localhost:27017/')
            cls._instance.db = cls._instance.client['airportDB']
            cls._instance.users = cls._instance.db['users']
            cls._instance.flights = cls._instance.db['flights']
            cls._instance.bookings = cls._instance.db['bookings']
        return cls._instance

database = Database()

login_bp = Blueprint('login', __name__)

@login_bp.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    print(f"\n\nEntered email : {email} \nEntered password : {password} \n\n")

    user = database.users.find_one({'userEmail': email, 'userDetails.userPassword': password})

    if user:
        print("\nFound user in the database")
        user_name = user["userDetails"]["userName"]
        booking = database.bookings.find_one({"userEmail" : email})
        session["user_email"] = email
        if booking:
            user_flights = booking["userFlights"]
            session["user_flights"] = user_flights
            return redirect(url_for("homepage.homepage", user_name = user_name, user_email = email))
        else:
            return render_template("homepage.html", error = "No Bookings")
        
    else:
        return render_template("login.html", error = "Invalid Credentials")
    
@login_bp.route("/login", methods=['GET'])
def logout():
    return render_template("login.html", status = "Logged Out Successfully")