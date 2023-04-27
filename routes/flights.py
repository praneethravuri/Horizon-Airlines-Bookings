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

flights_bp = Blueprint('flights', __name__)

@flights_bp.route("/search-flights", methods=["GET", "POST"])
def search_flights():
    user_name = request.args.get("user_name")
    user_email = request.args.get("user_email")

    from_locations = list(database.flights.distinct("flight_details.fromLocation"))
    to_locations = list(database.flights.distinct("flight_details.toLocation"))

    from_location_user = ""
    to_location_user = ""

    submit_clicked = False

    if request.method == "POST":
        from_location_user = request.form.get("from_location")
        to_location_user = request.form.get("to_location")
        submit_clicked = True

    searched_flights = ""
    search_message = ""

    if from_location_user == "":
        searched_flights = database.flights.find({"flight_details.toLocation" : to_location_user})
        search_message = f"Showing flights to {to_location_user}"
    elif to_location_user == "":
        searched_flights = database.flights.find({"flight_details.fromLocation" : from_location_user})
        search_message = f"Showing flights from {from_location_user}"
    elif from_location_user != "" and to_location_user != "":
        searched_flights = database.flights.find({"flight_details.fromLocation" : from_location_user, "flight_details.toLocation" : to_location_user})
        search_message = f"Showing flights from {from_location_user} to {to_location_user}"
    elif from_location_user == "" and to_location_user == "":
        search_message = ""

    all_flights = []

    for f in searched_flights:
        flight_details = {"flight_id": f["flight_id"]}
        flight_details.update(f["flight_details"])
        all_flights.append(flight_details)

    return render_template("flights.html", from_locations = from_locations, to_locations = to_locations, submit_clicked = submit_clicked, all_flights = all_flights, search_message = search_message, user_name = user_name, user_email = user_email)

@flights_bp.route("/add-flight", methods=['POST'])
def add_flight():
    to_be_added_flight = request.form['flight_id']
    user_name = request.args.get("user_name")
    user_email = request.args.get("user_email")
    user = database.bookings.find_one({"userEmail" : user_email})
    user_flights = user["userFlights"]
    error = "not_possible"
    if to_be_added_flight in user_flights:
        error = "Flight already booked!"
        print(error)
        return {"error": "booked"}
    else:
        #user_flights.append(to_be_added_flight)
        #database.bookings.update_one({'userEmail': user_email}, {'$set': {'userFlights': user_flights}})
        #print("Added flight details to the user's bookings")
        print('comes here ')
        return redirect("/payment.html", user_name = user_name, user_email = user_email)
        # return {"flight_id" : to_be_added_flight}


    return redirect(url_for('flights.search_flights'))
