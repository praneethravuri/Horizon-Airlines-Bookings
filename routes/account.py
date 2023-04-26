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

account_bp = Blueprint('account', __name__)

@account_bp.route("/account")
def account():

    user_email = session.get("user_email")

    find_user_details = database.users.find({'userEmail': user_email})
    user_name = ""
    # Iterate through the cursor
    for user_details in find_user_details:
        user_name = user_details['userDetails']['userName']
        break

    

    return render_template("account.html", user_email = user_email, user_name = user_name)
