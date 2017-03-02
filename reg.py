from flask import Flask, render_template, redirect, request, flash
import re, codecs
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
DATE_REGEX = re.compile(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def result():

    submit = True

    email = str(request.form['email'])
    if len(email) < 1:
        flash('Email cannot be blank!')
        submit = False
    elif not EMAIL_REGEX.match(email):
        flash('Invalid email, try again')
        submit = False

    first_name = str(request.form['first_name'])
    if len(first_name) < 1:
        flash('First name cannot be blank')
        submit = False
    elif len(first_name) > 1:
        if not str.isalpha(first_name):
            flash("First name can only contain alphabetic characters!")
            submit = False

    last_name = str(request.form['last_name'])
    if len(last_name) < 1:
        flash("Last name cannot be blank!")
        submit = False
    elif len(last_name) > 1:
        if not str.isalpha(last_name):
            flash("Last name can only contain alphabetic characters!")
            submit = False

    password = str(request.form['password'])
    c_password = str(request.form['c_password'])

    if len(password) < 1:
        flash("Password cannot be blank!")
        submit = False
    elif len(password) < 8:
        flash('Password cannot be less than 8 characters')
        submit = False
    elif password != c_password:
        flash("Password does not match your confirmed password")
        submit = False
    elif not str.isalnum(password):
        flash("Password needs to be alphanumeric!")
        submit = False
    elif str.islower(password):
        flash("Password needs to have at least one uppercase letter!")
        submit = False

    if len(c_password) < 1:
        flash("Confirm password cannot be blank!")
        submit = False
    elif len(c_password) < 8:
        flash("Confirm password cannot be less than 8 characters ")
        submit = False

    if len(request.form['date_of_birth']) < 1:
        flash("Date of birth cannot be blank!")
        submit = False
    elif not DATE_REGEX.match(request.form['date_of_birth']):
        flash("Date of birth format not correct")
        submit = False


    if (submit == True):
        flash("Thanks for submitting your information!")

    return redirect('/')
app.run(debug=True)
