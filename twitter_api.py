import tweepy
from flask import Flask, render_template, request
# User passes twitter handle handle
# Function returns text using google vision
#get link of media and save it for the google vision API
app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/", methods=['POST'])
def get_user_input():
    variable = request.form['variable']
    return variable

if __name__ == "__main__":
    app.run(debug=True)
