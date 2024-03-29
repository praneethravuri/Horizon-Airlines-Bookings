# INFS 740 Project (Spring 2023) - Horizon Airlines Bookings

## George Mason University - MSCS


### Project Installation (Docker)

1. Pulling the Docker Image

`docker pull praneeth2510/horizon-airlines-bookings`

2. Running the application

```docker run -p 8080:8080 praneeth2510/horizon-airlines-bookings```

### Project Description

Horizon Airlines Bookings is a web application built with Flask and MongoDB, enabling users to easily book and manage flights. Users can view available flights, apply promo codes, and update their personal information, including email, name, and password. The site features a login authentication system and allows users to delete their account. The efficient booking system streamlines the process by only requiring payment information. In summary, Horizon Airlines Bookings offers a comprehensive airline management system with all essential features for an efficient booking experience.

#### Technologies

-   Frontend - Html, CSS, Javascript, JQuery
-   Backend - Flask, Javascript, Jquery
-   Database - MongoDB

#### Collections

-   Users
-   Flights
-   Bookings
-   Discount

#### Basic Queries (CRUD Operations)

-   Create a new account
-   Update name, email, and password of the user
-   Cancel flights
-   Check duplicate flight booking
-   Check pre-existing users in the database
-   Delete account of the user

#### Complex Queries

1. Collections used - Users, Flights, Bookings

<div>
<img src="./documentation_images/complex_query_1.png" alt="">
<p>
In the login.html form, users enter their email and password which are checked against the corresponding records in the MongoDB users collection. If the credentials are correct, the bookings for that email are retrieved. If the user_flights list is empty, "No bookings found" is displayed on the homepage.html. Otherwise, for each flight in the user_flights list, the flight ID is used to search the flights collection in MongoDB and all information about that flight is displayed on the homepage.html.
</p>
</div>

|                   User Authentication                    |                        Login.py                        |
| :------------------------------------------------------: | :----------------------------------------------------: |
| <img src="./documentation_images/login_html.png" alt=""> | <img src="./documentation_images/login_py.png" alt=""> |

|                    Display User Bookings                    |                        Homepage.py                        |
| :---------------------------------------------------------: | :-------------------------------------------------------: |
| <img src="./documentation_images/homepage_html.png" alt=""> | <img src="./documentation_images/homepage_py.png" alt=""> |

<br>
<br>
<br>
<br>

2. Collections used - Users, Bookings, Flights

<div>
<img src="./documentation_images/complex_query_2.png" alt="">
<p>
When the user selects the origin and destination locations, all available flights are displayed in flight.html. After selecting a flight, the user is directed to the payment page. Upon clicking the "confirm" button, if the user already has a booking with the same flight ID, an error is displayed. Otherwise, the flight ID is added to the user's booking list.
</p>
</div>

|                   User Authentication                    |                        Homepage.py                        |
| :------------------------------------------------------: | :-------------------------------------------------------: |
| <img src="./documentation_images/login_html.png" alt=""> | <img src="./documentation_images/homepage_py.png" alt=""> |

|                   Display Searched Flights                    |                            Flights.py                            |
| :-----------------------------------------------------------: | :--------------------------------------------------------------: |
| <img src="./documentation_images/display_flights.png" alt=""> | <img src="./documentation_images/display_flights_py.png" alt=""> |

|                    Confirm Flight Booking                    |                           Payment.py                            |
| :----------------------------------------------------------: | :-------------------------------------------------------------: |
| <img src="./documentation_images/confirm_flight.png" alt=""> | <img src="./documentation_images/confirm_flight_py.png" alt=""> |

<br>
<br>
<br>
<br>

3. Collections used - Users, Bookings, Flights, discount (Bonus Complex Query)

<div>
<img src="./documentation_images/complex_query_3.png" alt="">
<p>
After selecting the origin and destination locations, all available flights are displayed in flight.html. Upon selecting a flight, the user is redirected to the payment page where, upon clicking "confirm," the system checks if the user has already booked the same flight. If yes, an error message is displayed. Otherwise, the flight ID is added to the user's booking list. Additionally, if the user enters a valid promo code, the price of the flight ticket is reduced based on the code entered. However, if an invalid promo code is entered, an error message is displayed.
</p>
</div>

|                   User Authentication                    |                        Homepage.py                        |
| :------------------------------------------------------: | :-------------------------------------------------------: |
| <img src="./documentation_images/login_html.png" alt=""> | <img src="./documentation_images/homepage_py.png" alt=""> |

|                   Display Searched Flights                    |                            Flights.py                            |
| :-----------------------------------------------------------: | :--------------------------------------------------------------: |
| <img src="./documentation_images/display_flights.png" alt=""> | <img src="./documentation_images/display_flights_py.png" alt=""> |

|                    Validate Promo Code                    |                          Payment.py                          |
| :-------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="./documentation_images/valid_promo.png" alt=""> | <img src="./documentation_images/valid_promo_py.png" alt=""> |

<br>
<br>

#### Visualization

1. A bar graph is created using the list of cities from where flights are departing, which shows the most busiest cities.
   <img src="./static/images/fromLocation.png" alt="">

2. A bar graph is generated using the list of cities to which flights are arriving, highlighting the most frequently visited cities.
   <img src="./static/images/toLocation.png" alt="">

3. A node graph is created to represent the flight paths originating from various cities, which also displays the interconnected flights between two destinations.
   <img src="./static/images/connected_flights.png" alt="">

All the visualizations are generated dynamically by `visualization.py`

#### Conslusion

In conclusion, this project is a fully functional web-based flight booking system that provides users with a convenient way to search and book flights. The system is designed with a user-friendly interface and includes features such as flight search, booking, and payment.

Overall, this project serves as a practical example of how web-based applications can be designed to provide a seamless and personalized user experience, making the booking process easier and more efficient for users.

<hr>

### Project Setup

#### 1. Create virtual environment (Windows)

Delete `env` folder if it is already present in the project folder

`python -m venv env`

Navigate to `env/Scripts`

Run the command `activate` and go to the main project folder

#### 2. Install necessary libraries

`pip install flask pymongo matplotlib networkx`

#### 3. Go to services and check if MongoDB is running

#### 4. Initialize the MongoDB in Command Prompt

`mongod`

#### 5. In the virtual environment, run app.py

`python app.py`

#### 6. Credentials, locations, promo codes

Credentials, locations, and promo codes can be found in the `db_data` folder. One can access them in the form of json or text files
