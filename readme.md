# INFS 740 Project

### Team Members:
* Praneeth Ravuri (G01369627)
* Arishith Pakalapati (G01374702)


### Project Description

Horizon Airlines is a web application built with Flask and MongoDB, enabling users to easily book and manage flights. Users can view available flights, apply promo codes, and update their personal information, including email, name, and password. The site features a login authentication system and allows users to delete their account. The efficient booking system streamlines the process by only requiring payment information. In summary, Horizon Airlines offers a comprehensive airline management system with all essential features for an efficient booking experience.

#### Technologies
* Frontend - Html, CSS, Javascript
* Backend - Flask
* Database - MongoDB

#### Collections
* Users
* Flights
* Bookings
* Discount

#### Basic Queries (CRUD Operations)
* Create a new account
* Update name, email, and password of the user
* Cancel flights
* Check duplicate flight booking
* Check pre-existing users in the database
* Delete account of the user

#### Complex Queries
1. Collections used - Users, Flights, Bookings


<p style="align-items: center;">
    <img src="./documentation_images/complex_query_1.png" alt="">
</p>

<hr>

### 1. Create virtual environment

Delete ```env``` folder if it is already present in the project folder

```python -m venv env```

### 2. Install necessary libraries

```pip install flask pymongo jupyter matplotlib```

### 3. Go to services and check if MongoDB is running

### 4. Initialize the MongoDB in Command Prompt

```mongod```

### 5. In the virtual environment, run app.py

```python app.py```


### Database users and passwords
```
1) Email: emma.williams@gmail.com
Password: p@ssw0rd123


2) Email: jacob.harris@yahoo.com    
Password: qwerty321


3) Email: lisa.rodriguez@hotmail.com
Password: secretp@ss


4) Email: peter.nguyen@outlook.com  
Password: myP@ssw0rd


5) Email: kate.brown@gmail.com      
Password: letmein123


6) Email: john.doe@gmail.com
Password: mySecretPassword123


7) Email: sarah.smith@yahoo.com
Password: ilovecookies


8) Email: michael.nguyen@hotmail.com
Password: S3cretP@ss


9) Email: jessica.johnson@outlook.com
Password: mypassword1234


10) Email: adam.garcia@gmail.com
Password: P@ssw0rd!


11) Email: ryan.jackson@yahoo.com
Password: g1vem3access!


12) Email: alexandra.chen@hotmail.com
Password: il0ve2dance


13) Email: jason.hernandez@outlook.com
Password: m1ndth3gap


14) Email: emma.miller@gmail.com
Password: th1nkpositive


15) Email: hannah.wilson@gmail.com
Password: p@ssw0rd456


16) Email: david.kim@yahoo.com
Password: myP@ssword

17) Email: olivia.li@hotmail.com
Password: letmein12


18) Email: joshua.young@outlook.com
Password: p@ssword123


19) Email: grace.davis@gmail.com
Password: m0t1vat3d!
```

### Source and Final Destination

```
Abu Dhabi --> New Delhi
Abu Dhabi --> New York
Abu Dhabi --> Toronto
Amsterdam --> Mexico City
Amsterdam --> New Delhi
Amsterdam --> Rio de Janeiro
Amsterdam --> São Paulo
Atlanta --> Amsterdam
Atlanta --> Dubai
Atlanta --> San Francisco
Atlanta --> Dubai
Atlanta --> Dubai
Atlanta --> Dubai
Berlin --> Dubai
Chicago --> London
Chicago --> Sydney
Chicago --> London
Chicago --> Shanghai
Chicago --> London
Chicago --> Shanghai
Dallas --> London
Dallas --> Seattle
Delhi --> Beijing
Dubai --> Los Angeles
Dubai --> New Delhi
Dubai --> New York
Dubai --> San Francisco
Dublin --> Barcelona
Dublin --> Barcelona
Doha --> Sydney
Doha --> Miami
Doha --> Los Angeles
Doha --> Melbourne
Frankfurt --> Chicago
Frankfurt --> Tokyo
Frankfurt --> Mexico City
Frankfurt --> Rio de Janeiro
Hong Kong --> Los Angeles
Hong Kong --> Sydney
Hong Kong --> New York
Istanbul --> New Delhi
Istanbul --> Chicago
Istanbul --> San Francisco
Istanbul --> Los Angeles
Johannesburg --> London
London --> New York
London --> Sydney
London --> New York
London --> Cape Town
London --> Tokyo
London --> Tokyo
Melbourne --> Auckland
Miami --> London
Moscow --> Bangkok
Moscow --> Beijing
Mumbai --> London
Mumbai --> Sydney
New York --> Shanghai
New York --> Los Angeles
New York --> Dubai
Paris --> Tokyo
Paris --> Tokyo
Paris --> New York
Paris --> Buenos Aires
Paris --> Singapore
Rome --> Mexico City
Rome --> Miami
Seoul --> Paris
Sydney --> New York
Sydney --> Vancouver
Sydney --> Auckland
Sydney --> Tokyo
Tokyo --> Honolulu
Tokyo --> Los Angeles
Tokyo --> San Francisco
Tokyo --> London
Tokyo --> Melbourne
Toronto --> Mexico City
Toronto --> Rio de Janeiro
Zurich --> Rio de Janeiro

```

### Discount Codes

```
{'promoCode': 'DTO-036-PDW', 'discount': 20}
{'promoCode': 'ZKY-992-VHK', 'discount': 47}
{'promoCode': 'OZG-298-JAK', 'discount': 51}
{'promoCode': 'FOS-611-QXN', 'discount': 23}
{'promoCode': 'RAV-655-HJY', 'discount': 25}
{'promoCode': 'QRK-023-FRT', 'discount': 45}
{'promoCode': 'JMV-410-TKK', 'discount': 46}
{'promoCode': 'OWE-389-FBU', 'discount': 45}
{'promoCode': 'ZKO-635-QCV', 'discount': 44}
{'promoCode': 'SBT-073-NQS', 'discount': 38}
{'promoCode': 'TUW-670-MAJ', 'discount': 52}
{'promoCode': 'SYI-541-ZRA', 'discount': 60}
{'promoCode': 'KLX-651-LYM', 'discount': 66}
{'promoCode': 'KPZ-289-NWC', 'discount': 20}
{'promoCode': 'WNX-038-TTG', 'discount': 10}
{'promoCode': 'LQN-986-HSK', 'discount': 57}
{'promoCode': 'PUX-017-BVO', 'discount': 30}
{'promoCode': 'MDO-656-RGL', 'discount': 47}
{'promoCode': 'JUN-747-DRS', 'discount': 45}
{'promoCode': 'FFC-779-XXD', 'discount': 50}
```