from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import secrets
from routes.homepage import homepage_bp
from routes.flights import flights_bp
from routes.login import login_bp
from routes.account import account_bp
from routes.payment import payment_bp


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
app.register_blueprint(flights_bp)
app.register_blueprint(login_bp)
app.register_blueprint(account_bp)
app.register_blueprint(payment_bp)

@app.route('/')
def index():
    return render_template('login.html')
    
if __name__ == '__main__':
    app.run(debug=True)
