from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

flights_bp = Blueprint('flights', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

@flights_bp.route("/search-flights", methods=["GET", "POST"])
def search_flights():
    user_email = session.get("user_email")

    from_locations = list(flights.distinct("flight_details.fromLocation"))
    to_locations = list(flights.distinct("flight_details.toLocation"))

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
        searched_flights = flights.find({"flight_details.toLocation" : to_location_user})
        search_message = f"Showing flights to {to_location_user}"
    elif to_location_user == "":
        searched_flights = flights.find({"flight_details.fromLocation" : from_location_user})
        search_message = f"Showing flights from {from_location_user}"
    elif from_location_user != "" and to_location_user != "":
        searched_flights = flights.find({"flight_details.fromLocation" : from_location_user, "flight_details.toLocation" : to_location_user})
        search_message = f"Showing flights from {from_location_user} to {to_location_user}"

    all_flights = []

    for f in searched_flights:
        flight_details = {"flight_id": f["flight_id"]}
        flight_details.update(f["flight_details"])
        all_flights.append(flight_details)

    return render_template("flights.html", from_locations = from_locations, to_locations = to_locations, submit_clicked = submit_clicked, all_flights = all_flights, search_message = search_message)