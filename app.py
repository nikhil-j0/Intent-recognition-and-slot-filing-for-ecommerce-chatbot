from flask import Flask, render_template, request, redirect, url_for, session
from db import db  # Import the db object from db.py
from db import User  # Import the User model from db.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize the SQLAlchemy extension with the Flask app
db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/main')
def main():
    # Check if the user is logged in
    if 'user_id' in session:
        # Render the main page
        return render_template('index.html')
    else:
        # Redirect to the sign-in page if the user is not logged in
        return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username or email already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return 'Username already exists! Please choose a different one.'
        
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return 'Email already exists! Please use a different one.'

        # Create a new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the main page upon successful registration
        return redirect(url_for('main'))  # Fixed route name

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password is correct
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # Store the user's ID in the session
            session['user_id'] = user.id
            # Redirect to the main page upon successful sign-in
            return redirect(url_for('main'))  # Fixed route name
        else:
            return 'Invalid username or password. Please try again.'

    return render_template('signin.html')
# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Product page
@app.route('/product')
def product():
    return render_template('product.html')

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the Services page
@app.route('/Services')
def services():
    return render_template('Services.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
