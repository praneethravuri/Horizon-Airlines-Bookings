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

account_bp = Blueprint('account', __name__)

@account_bp.route("/account")
def account():

    user_email = session.get("user_email")

    find_user_details = database.users.find({'userEmail': user_email})
    user_name = ""
    user_password = ""
    for user_details in find_user_details:
        user_name = user_details['userDetails']['userName']
        break

    for user_details in find_user_details:
        user_password = user_details['userDetails']['userPassword']
        break

    return render_template("account.html", user_email = user_email, user_name = user_name, user_password = user_password)

@account_bp.route("/delete-account", methods=['POST'])
def delete_account():
    user_email = session.get("user_email")
    print(user_email)
    print("here")
    result = database.users.delete_one({"userEmail": user_email})
    print("Account deleted")
    print(result.deleted_count)
    return render_template("login.html")


@account_bp.route("/update-account", methods=['POST'])
def update_account():
    user_email = session.get("user_email")

    # Get the new user details from the submitted form
    new_user_name = request.form.get("user_name")
    new_user_password = request.form.get("user_password")
    new_user_email = request.form.get("user_new_email")

    query = {'userEmail': user_email}
    new_values = { "$set": { 'userDetails.userName': new_user_name, 'userDetails.userPassword': new_user_password, 'userEmail': new_user_email } }

    database.users.update_one(query, new_values)

    print("user details updated")

    return redirect(url_for("account.account"))
