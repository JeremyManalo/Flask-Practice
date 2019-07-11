from flask import render_template, url_for, flash, redirect # Import Flask Class and routes imports
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
#  Flask Tutorial Video 5  https://youtu.be/44PvX0Yv368

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success') # python 3 format.
        return redirect(url_for('login'))
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
