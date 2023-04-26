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

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the email already exists in the database
        if database.users.find_one({'userEmail': email}):
            return render_template('signup.html', error='Email already exists')
        
        user = {
            'userEmail': email,
            'userDetails': {
                'userName': name,
                'userPassword': password
            }
        }
        database.users.insert_one(user)

        session['user_name'] = name
        session['user_email'] = email

        booking = {
            'userEmail' : email,
            'userFlights' : []
        }

        database.bookings.insert_one(booking)

        return redirect(url_for('homepage.homepage', user_name=name, user_email=email))
    else:
        return render_template('signup.html')
