from avengers_phonebook import app, db, login

#Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Date Time Module
from datetime import datetime
from flask_login import UserMixin

#Create the current user_manager using the user_login function
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usernamephone_number = db.Column(db.String(150), nullable = False, unique = True,default="")
    username = db.Column(db.String(150), nullable = False, unique = True,default="")
    email = db.Column(db.String(150), nullable = False, unique = True,default="")
    password = db.Column(db.String(256),nullable = False,default="")
    def __init__(self,usernamephone_number,username,email,password):
        self.usernamephone_number = usernamephone_number
        self.username = username
        self.email = email
        self.password = self.set_password(password)
    
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.phone_number} has been created.'

class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    phone_numb = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,name,phone_numb,user_id):
        self.name = name
        self.phone_numb = phone_numb
        self.user_id = user_id
    
    def __repr__(self):
        return f"The Avenger is {self.name} \n and the phone number is {self.phone_numb}"