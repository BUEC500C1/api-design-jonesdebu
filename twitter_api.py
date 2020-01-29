import tweepy
from flask import Flask, render_template, request
# User passes twitter handle handle
# Function returns text using google vision
# get link of media and save it for the google vision API
# Function hadling for twitter api and google vision api need to be in a Function
# function must be called from a different functions
app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


# User input needs to be from function call and not html page
# Just pass whatever twitter handle to this function because
# this is supposed to be a library that you can import so the
# user of this library should be entering the twitter handle
@app.route("/", methods=['POST'])
def get_user_input():
    # user_name = input("Enter twitter handle:")
    variable = request.form['variable']
    return variable

if __name__ == "__main__":
    app.run(debug=True)
