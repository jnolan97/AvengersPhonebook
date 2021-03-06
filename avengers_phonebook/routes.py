from avengers_phonebook import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from avengers_phonebook.forms import PhoneNumberInfo, LoginForm,PhoneNumForm
from avengers_phonebook.models import User, PhoneNumber, check_password_hash
from flask_login import login_required,login_user,current_user,logout_user

#Home Route
@app.route('/')
def home():
    return render_template("home.html")
#Register route
@app.route('/phonebook', methods=['GET','POST'])
#@login_required
def phonebook():
    form = PhoneNumberInfo()
    if request.method == 'POST' and form.validate():
        # Get info
        usernamephone_number = form.usernamephone_number.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",usernamephone_number,username,password,email)
        #create instance of user
        user = User(username,usernamephone_number,email,password)
        # open and insert into db and then save info
        db.session.add(user)
        db.session.commit()
        #Flask Email Sender
        msg = Message(f'Thanks for Signing up! {email}', recipients=[email])
        msg.body =('Congrats on signing up! Looking forward to your posts!')
        msg.html = ('<h1> Welcome to May_Blog! </h1>' '<p> This will be fun! </p>')
        mail.send(msg)
    return render_template('phonebook.html',form = form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html',form=form)

@app.route('/phonenumber/update',methods = ['GET','POST'])
@login_required
def phone_update():
    # user = User.query.get_or_404(current_user.id)
    update_form = PhoneNumForm()

    if request.method == 'POST' and update_form.validate():
        name = update_form.name.data
        phone_numb = update_form.phone_numb.data
        user_id = current_user.id 
        # print(name,phone_numb,current_user.id)
        #update_form = PhoneNumForm(name,phone_numb,user_id)
        phone = PhoneNumber(name,phone_numb,user_id)
        db.session.add(phone)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('phone_update.html',update_form = update_form)

@app.route('/numbers.html')
def numbers():
    nums = PhoneNumber.query.all()
    return render_template('numbers.html',nums = nums)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/phonenumber')
@login_required
def phonenumber():
    phone_numbers = {'Hulk':1234567789,'IronMan':4445556666,'Hawkeye':1123584444}
    return render_template("phonenumber.html",phone_numbers = phone_numbers)