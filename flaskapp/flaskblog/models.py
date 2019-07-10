#  Prashant Marathay
#  Flask Tutorial Video 5  https://youtu.be/44PvX0Yv368
from datetime import datetime
from flaskblog import db

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
