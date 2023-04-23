from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient

login_bp = Blueprint('login', __name__)