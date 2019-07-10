from flask import Flask # Import Flask Class
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # app variable set to instance of Flask class with name module where Flask looks for templates and static files
app.config['SECRET_KEY'] = '' # empty for github
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # relative path from the current file
db = SQLAlchemy(app) # sets up tables as classes.  Each class is its own table

from flaskblog import routes
