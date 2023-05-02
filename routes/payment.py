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
            cls._instance.discount = cls._instance.db['discount']
        return cls._instance

database = Database()

payment_bp = Blueprint('payment', __name__)

def split_time(time_):
    time_ = time_.split("T")
    return time_[0] + " | " + time_[1][0:-1]

@payment_bp.route("/payment", methods = ["GET"])
def payment():
    to_be_added_flight = request.args.get('flight_id')


    price = request.args.get("price")
    tax = float(price) / 2
    total_price = round(float(price) + float(tax), 2)

    session["price"] = price
    session["tax"] = tax
    session["total_price"] = total_price

    session["to_be_added_flight"] = to_be_added_flight
    print(f"Flight id payment {to_be_added_flight}")
    user_email = session.get("user_email")
    user = database.bookings.find_one({"userEmail" : user_email})
    user_flights = user["userFlights"]
    status = ""
    user_flights_dict = {}
    flight_details = database.flights.find({"flight_id": to_be_added_flight})
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
        
    session["user_flights_dict"] = user_flights_dict

    return render_template("payment.html", status = status, user_flights_dict=user_flights_dict, price = price, tax = tax, total_price = total_price, discount = "")

@payment_bp.route("/confirm-payment", methods = ["POST"])
def confirm_payment():
    print("here confirm payment")
    status = ""
    user_flights_dict = {}
    to_be_added_flight = session.get("to_be_added_flight")
    price = session.get("price")
    print(price)
    print(f"\n\n{to_be_added_flight}")
    user_email = session.get("user_email")
    print(user_email)
    user = database.bookings.find_one({"userEmail" : user_email})
    user_flights = user["userFlights"]
    print(user_flights)
    error = "not_possible"
    if to_be_added_flight in user_flights:
        error = "Flight already booked!"
        print(error)
        return {"status" : "error-dup"}
    else:
        user_flights.append(to_be_added_flight)
        database.bookings.update_one({'userEmail': user_email}, {'$set': {'userFlights': user_flights}})
        print("Added flight details to the user's bookings\n\n")
        return {"status" : "booked"}

@payment_bp.route("/cancel-transaction", methods = ["POST"])
def cancel_transaction():
    print("clicked cancel")
    return render_template("flights.html", status = "Cancelled Transaction")


@payment_bp.route("/validate-promo-code", methods=["POST"])
def validate_promo_code():
    user_flights_dict = session.get("user_flights_dict")
    promo_code = request.form["promocode"]
    print(f"Promo code {promo_code}")
    print(type(promo_code))
    price = float(session.get("price"))
    status = ""
    tax = float(session.get("tax"))
    total_price = float(session.get("total_price"))

    result = database.discount.find_one({"promoCode": promo_code})
    print(result)

    if result:
        discount = float(result["discount"])
        price = round(price - ((discount / 100) * price), 2)
        print(f"discounted price: {price}")
        total_price = round(float(price) + float(tax), 2)
        status = "success"
        return render_template(
            "payment.html",
            status=status,
            user_flights_dict=user_flights_dict,
            price=price,
            tax=tax,
            total_price=total_price,
            discount=discount,
        )
    else:
        status = "error"
        return render_template(
            "payment.html",
            status=status,
            user_flights_dict=user_flights_dict,
            price=price,
            tax=tax,
            total_price=total_price,
            discount="",
        )
