from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PhoneNumberInfo(FlaskForm):
    phone_number = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField()
