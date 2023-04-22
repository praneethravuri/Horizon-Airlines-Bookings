from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')

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
        print(user_name)
        print(email)
        booking = bookings.find_one({"userEmail" : email})
        if booking:
            all_flights = booking["userFlights"]
            print(all_flights)
        user_flight = "tbd"
        airline_name = "tbd"
        return redirect(url_for("homepage", user_name = user_name, user_flight = user_flight, airline_name = airline_name))
        
    else:
        return 'Invalid credentials'
    
@app.route("/homepage")
def homepage():
    user_name = request.args.get("user_name")
    user_flight = request.args.get("user_flight")
    airline_name = request.args.get("airline_name")
    user_bookings = request.args.get("user_bookings")
    return render_template("homepage.html", user_name = user_name, user_flight = user_flight, airline_name = airline_name)

if __name__ == '__main__':
    app.run(debug=True)
