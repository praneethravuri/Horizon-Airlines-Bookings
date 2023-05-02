from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

# Create a singleton class to handle the MongoDB database connection
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

homepage_bp = Blueprint('homepage', __name__)

def split_time(time_):
    time_ = time_.split("T")
    return time_[0] + " | " + time_[1][0:-1]

@homepage_bp.route('/homepage')
def homepage():
    user_name = request.args.get("user_name")
    user_email = request.args.get("user_email")
    user_flights = session.get("user_flights") or []
    user_flights_dict = {}
    has_bookings = False
    if user_flights:
        flight_details = database.flights.find({"flight_id": {"$in": user_flights}})
        for flight in flight_details:
            user_flights_dict[flight["flight_id"]] = [
                flight["flight_details"]["airlineName"],
                flight["flight_details"]["fromLocation"],
                flight["flight_details"]["fromLocationAirportCode"],
                flight["flight_details"]["toLocation"],
                flight["flight_details"]["toLocationAirportCode"],
                split_time(flight["flight_details"]["departureTime"]),
                split_time(flight["flight_details"]["arrivalTime"]),
                flight["flight_details"]["duration"],
                flight["flight_details"]["price"]
            ]
        has_bookings = True

    return render_template("homepage.html", user_name=user_name, user_flights_dict=user_flights_dict, has_bookings=has_bookings, user_email = user_email)

@homepage_bp.route('/delete-flight', methods=['POST'])
def delete_flight():
    to_be_deleted_flight = request.form['flight_id']
    user_name = request.args.get("user_name")
    user_email = session.get("user_email")
    user = database.bookings.find_one({"userEmail": user_email})
    user_flights = user["userFlights"]
    updated_flights = [f for f in user_flights if f != to_be_deleted_flight]
    database.bookings.update_one({'userEmail': user_email}, {'$set': {'userFlights': updated_flights}})
    
    return redirect(url_for('homepage.homepage', user_name = user_name, user_email = user_email))
