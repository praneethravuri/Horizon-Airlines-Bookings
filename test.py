from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]

i = 1
for user in users.find({}, {'userEmail': 1, 'userDetails.userPassword': 1}):
    print(str(i) + ") Email: " + user["userEmail"] + "\n" + "Password: " + user["userDetails"]["userPassword"] + "\n\n")
    i+=1