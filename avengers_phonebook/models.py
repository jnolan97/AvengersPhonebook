from avengers_phonebook import app, db

#Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Date Time Module
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usernamephone_number = db.Column(db.String(150), nullable = False, unique = True)

    def __init__(self,phone_number):
        self.phone_number = phone_number

    def __repr__(self):
        return f'{self.phone_number} has been created.'
