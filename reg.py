from flask import Flask, render_template, redirect, request, flash
import re, codecs
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process' methods=['POST'])
def result():
    if len(request.form['email'] < 1:
        flash('Email cannot be blank!')


    return redirect('/')
app.run(debug=True)
