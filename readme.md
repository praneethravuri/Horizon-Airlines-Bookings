### 1. Create virtual environment

Delete ```env``` folder if it is already present in the project folder

```python -m venv env```

### 2. Install necessary libraries

```pip install flask pymongo```

### 3. Go to services and check if MongoDB is running

### 4. Initialize the MongoDB in Command Prompt

```mongod```

### 5. In the virtual environment, run app.py

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