from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

DATABASE = 'guestbook.db'

#don't touch, just for the tests to run
app.secret_key = 'secret'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                message TEXT NOT NULL
            )
        ''')

@app.route('/', methods=['GET', 'POST'])
def index():
    # If we send POST request to create user
    # add logic
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
    
        if not name or not email or not message:
            flash('All fields must be filled.', 'error')
        else:
            # Insert data into the database
            db = get_db()
            cursor = db.cursor()
            cursor.execute('''
                INSERT INTO guests (name, email, message) VALUES (?, ?, ?)
            ''', (name, email, message))
            db.commit()
            flash('Entry submitted successfully!', 'success')
            return redirect(url_for('index'))

    if request.method == 'GET':
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT name, email, message FROM guests")
        entries = cursor.fetchall()
        db.close()
        return render_template('view_guestbook.html', entries=entries)  
    # If we send GET request to get all users
    # add logic

    return render_template('index.html')

@app.route('/view_guestbook')
def view_guestbook():
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    # Retrieve all guestbook entries from the database
    cursor.execute("SELECT name, email, message FROM guests")
    entries = cursor.fetchall()

    # Close the database connection
    conn.close()

    return render_template('view_guestbook.html', entries=entries)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)