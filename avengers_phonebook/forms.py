from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email

class PhoneNumberInfo(FlaskForm):
    usernamephone_number = StringField('Phone', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField()

class PhoneNumForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    phone_numb = StringField('Phone',validators=[DataRequired()])
    submit = SubmitField()