from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = users.find_one({'user_email': email, 'user_details.user_password': password})

    if user:
        return 'Login successful!'
    else:
        return 'Invalid credentials'

if __name__ == '__main__':
    app.run(debug=True)
