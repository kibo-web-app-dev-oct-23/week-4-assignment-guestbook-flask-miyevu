from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

DATABASE = 'guestbook.db'

#don't touch, just for the tests to run
app.secret_key = 'secret'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    # If we send POST request to create user
    # add logic
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

    if request.method == 'GET':
        return
    # If we send GET request to get all users
    # add logic

    return render_template('index.html')