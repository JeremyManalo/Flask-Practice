#  Prashant Marathay
#  Flask Tutorial Video 2  https://www.youtube.com/watch?v=QnDWIZuWYW0

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect     # Import Flask Class and render template
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # app variable set to instance of Flask class with name module where Flask looks for templates and static files
app.config['SECRET_KEY'] = '' # empty for github
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # relative path from the current file
db = SQLAlchemy(app) # sets up tables as classes.  Each class is its own table


# database table definitions
class User(db.Model): # define the table fields for the class below.  Automatically creates a table name of lowercase user
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # backref creates a relationship that allows us to get author attribute.  Lazy is when it loads the data.  Allows for pulling all posts from an author
    # posts is not a column.  It is the relationship table creation that runs as necessary (lazy)
    # Posts is uppercase since we are referencing the actual POST class

    # Reference for object oriented programming in Python
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model): # define the table fields below
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # lowercase u since we are referencing table.column

    def __repr__(self): # magic method.  In this case it is for what we want the output to look like when printed out
        return f"Post('{self.title}', '{self.date_posted}')"

#  from project directory (flask.app), run python and then run from flaskblog import db and then db.create_all() that creates site.db

post_content = [
# a list of dictionaries.  Each dictionary is a single blog post
    {
        'author':       'Prashant Marathay',
        'title':        'Blog Post 1',
        'content':      'First post content',
        'date_posted':  'July 4, 2019'
    },
    {
        'author':       'Sitara Marathay',
        'title':        'Blog Post 2',
        'content':      'Second post content',
        'date_posted':  'July 7, 2019'
    },
]


@app.route("/") # Routes to url/home or url/
@app.route("/home")
def home(): # Function name
    #return "<h1>Home Page</h1>"
    # What to do in the function.  This functionality is moved into html page
    return render_template('home.html', posts=post_content)
    # renders what is in the template folder with .  posts variable = post content.  All this info goes INTO home.html


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST']) # Need to add this for any pages that submit POST or GET requests
def register():
    form = RegistrationForm() #  This is the link.  Pulls Resgistration Form from forms.py
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # python 3 format.
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form) #  This is what happens if the submit is unsuccessful with errors highlighted


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Whoops', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__': # Condition is only true if script is run directly
    app.run(debug=True)
