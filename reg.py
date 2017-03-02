from flask import Flask, render_template, redirect, request, flash
import re, codecs
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
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

    if (submit == True):
        flash("Thanks for submitting your information!")

    return redirect('/')
app.run(debug=True)
