from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import random
import string

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]
discount = db["discount"]

def generate_promo_code():
    letters = string.ascii_uppercase
    digits = string.digits
    return (''.join(random.choice(letters) for i in range(3)) + '-' +
            ''.join(random.choice(digits) for i in range(3)) + '-' +
            ''.join(random.choice(letters) for i in range(3)))


# Insert 10 documents with randomly generated promo codes and discount values
# Insert 10 documents with randomly generated promo codes and discount values
for i in range(20):
    promo_code = generate_promo_code()
    discount_value = random.randint(10, 70)
    document = {
        "promoCode" : promo_code,
        "discount" : discount_value
    }

    discount.insert_one(document)
