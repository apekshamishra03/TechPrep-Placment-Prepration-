from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "techprepsecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///techprep.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aptitude')
@login_required
def aptitude():
    username = User.query.get(session['user_id']).username
    return render_template('aptitude.html', username=username)

@app.route('/technical')
@login_required
def technical():
    username = User.query.get(session['user_id']).username
    return render_template('technical.html', username=username)

@app.route('/interview')
@login_required
def interview():
    username = User.query.get(session['user_id']).username
    return render_template('interview.html', username=username)

@app.route('/resources')
@login_required
def resources():
    username = User.query.get(session['user_id']).username
    return render_template('resources.html', username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login Successful!', 'success')
            return redirect(url_for('aptitude'))
        else:
            flash('Invalid Credentials', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'warning')
            return redirect(url_for('signup'))
        else:
            # Hash the password before storing
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created! Login now', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))


import os

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)