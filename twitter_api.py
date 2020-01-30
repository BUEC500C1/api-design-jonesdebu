import tweepy
from flask import Flask, render_template, request
# User passes twitter handle handle
# Function returns text using google vision
# get link of media and save it for the google vision API
# Function hadling for twitter api and google vision api need to be in a Function
# function must be called from a different functions

#twitter API OAuth 2 AUthentication
auth = tweepy.OAuthHandler("4IVCCtuSQ3eLb8i2kH70lVawI", "7erpsGo0gNJTPnTEYc73PFkB6iCvJZrK8HIb7vVm45ywKfZ04d")
auth.set_access_token("1222366331825090560-pTDch0qvoCkSvFVdgUoybz8OMQy5c8", "7b5LVDnfykKS5Xi5YYH4uiPAZNovzG2HnrpLE2OXV0whZ")

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

print("Before Flask start")

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
def get_user_input():#(twitter_handle)
    # user_name = input("Enter twitter handle:")
    variable = request.form['variable']
    return variable

#@app.route("/")
#def get_feed(twitter_handle):
#    user =

if __name__ == "__main__":
    app.run(debug=True)
