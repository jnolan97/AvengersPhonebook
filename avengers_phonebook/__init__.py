from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Import for Flask Mail
from flask_mail import Mail, Message

#Import for flask login
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

login = LoginManager(app)
login.login_view = 'login'

from avengers_phonebook import routes,models