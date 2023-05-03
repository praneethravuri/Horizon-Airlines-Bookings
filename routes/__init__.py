from flask import Flask
from pymongo import MongoClient
import secrets

app = Flask(__name__, template_folder='templates')
app.secret_key = secrets.token_hex(16)

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


# Register the homepage blueprint
from routes.homepage import homepage_bp
app.register_blueprint(homepage_bp)

from routes.flights import flights_bp
app.register_blueprint(flights_bp)

from routes.login import login_bp
app.register_blueprint(login_bp)

from routes.account import account_bp
app.register_blueprint(account_bp)

from routes.payment import payment_bp
app.register_blueprint(payment_bp)

from routes.signup import signup_bp
app.register_blueprint(signup_bp)

from routes.visualization import visualization_bp
app.register_blueprint(visualization_bp)

#from routes.login import 

# Import and register other blueprints here

if __name__ == '__main__':
    app.run(debug=True)
