from flask import Flask
from app import app
from models import User

@app.route('/signup/')
def signup():
    return User().signup()