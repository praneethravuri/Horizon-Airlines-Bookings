### Create virtual environment

Delete ```env``` folder if it is already present in the project folder

```python -m venv env```

### Install necessary libraries

```pip install flask pymongo```

### Go to services and check if MongoDB is running

### Initialize the MongoDB in Command Prompt

```mongod```

### In the virtual environment, run app.py

```python app.py```

### Project Structure

```
.
|--data
|--db_data
|--ENV
|--static
|  |--CSS
|  |  |--homepage.css
|  |  |--login.css
|  |  |--navbar.css
|  |--JS
|  |  |--invalidCredentials.js
|  |--images
|--templates
|  |--homepage.html
|  |--login.html
|--app.py
|--README.MD

```