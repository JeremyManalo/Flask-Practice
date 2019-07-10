#  Prashant Marathay
#  Flask Tutorial Video 1  https://www.youtube.com/watch?v=MwZwr5Tvyxo


from flask import Flask # Import Flask Class
app = Flask(__name__) # app variable set to instance of Flask class with name module where Flask looks for templates and static files

@app.route("/") # Routes to go to route decorators add additional functionality to existing functions.  / root page (home page)
@app.route("/home")
def home(): # Function name
    return "<h1>Home Page</h1>" # What to do in the function


@app.route("/about") # Routes to go to route decorators add additional functionality to existing functions.  / root page (home page)
def about():
    return "<h1>About Page!</h1>"

if __name__ == '__main__': # Condition is only true if script is run directly
    app.run(debug=True)
