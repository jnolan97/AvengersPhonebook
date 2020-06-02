from avengers_phonebook import app
from flask import render_template, request
from avengers_phonebook.forms import PhoneNumberInfo

#Home Route
@app.route('/')
def home():
    return render_template("home.html")
#Register route
@app.route('/phonebook', methods=['GET','POST'])
def phonebook():
    form = PhoneNumberInfo()
    if request.method == 'POST' and form.validate():
        # Get info
        phone_number = form.phone_number.data
        print(phone_number)
    return render_template('phonebook.html',form = form)