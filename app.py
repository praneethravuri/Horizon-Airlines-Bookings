from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import secrets

app = Flask(__name__, template_folder='templates')
app.secret_key = secrets.token_hex(16)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = users.find_one({'userEmail': email, 'userDetails.userPassword': password})

    if user:
        user_name = user["userDetails"]["userName"]
        booking = bookings.find_one({"userEmail" : email})
        if booking:
            user_flights = booking["userFlights"]
            session["user_flights"] = user_flights
        return redirect(url_for("homepage", user_name = user_name))
        
    else:
        return 'Invalid credentials'
    
@app.route("/homepage")
def homepage():
    user_name = request.args.get("user_name")
    user_flights = session.get("user_flights")

    user_flights_dict = {}

    for flight in user_flights:
        find_flight = flights.find_one({"flight_id" : flight})
        user_flights_dict[find_flight["flight_id"]] = [find_flight["flight_details"]["airlineName"], find_flight["flight_details"]["fromLocation"], find_flight["flight_details"]["fromLocationAirportCode"],find_flight["flight_details"]["toLocation"], find_flight["flight_details"]["toLocationAirportCode"],find_flight["flight_details"]["departureTime"], find_flight["flight_details"]["arrivalTime"], find_flight["flight_details"]["duration"], find_flight["flight_details"]["totalSeats"] ]
    return render_template("homepage.html", user_name = user_name, user_flights_dict = user_flights_dict)

if __name__ == '__main__':
    app.run(debug=True)
