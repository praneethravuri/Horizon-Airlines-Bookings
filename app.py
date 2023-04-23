from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import secrets
from routes.homepage import homepage_bp

app = Flask(__name__, template_folder='templates')
app.secret_key = secrets.token_hex(16)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

# Register the homepage blueprint
app.register_blueprint(homepage_bp)

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
            return redirect(url_for("homepage.homepage", user_name = user_name))
        else:
            return render_template("homepage.html", error = "No Bookings")
        
    else:
        return render_template("login.html", error = "Invalid Credentials")
    
@app.route("/search-flights")
def search_flights():
    return render_template("flights.html")

@app.route("/search-hotels")
def search_hotels():
    pass
    
if __name__ == '__main__':
    app.run(debug=True)
