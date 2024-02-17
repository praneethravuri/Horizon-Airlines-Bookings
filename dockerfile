# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Set the working directory in the Docker container
WORKDIR /python-docker

# Copy the requirements file and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of your Flask application's code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Run the Flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
