import tweepy
from google.cloud import vision
# User passes twitter handle handle
# Function returns text using google vision
# get link of media and save it for the google vision API
# Function hadling for twitter api and google vision api need to be in a Function
# function must be called from a different functions

#consumer_key is a string from twitter API
#consumer_secret is a string from twitter API
#key is a string from twitter API
#secret is a string from twitter API
#userid is the id of the twitter user whos feed you would like to retrieve

#HOW TO: Enter your consumer key, consumer secret, key, secret, and the user id
# of the user whose timeline you would like to retrieve. The function will print out
# a lsit of what labels a photo contains and will print out the photo's media url

#IMPORTANT - In the requirements.txt i added the google cloud related libraries
# however it is recommended to use a independent environment (using venv as source)
# when using the google cloud libraries so as to not interfere with other projects.

def read_image(consumer_key, consumer_secret, key, secret, userid):
    #twitter API OAuth 2 Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth)


    #get user timeline for tweets to convert
    user = api.get_user(userid)
    tweets = api.user_timeline(id=userid)

    #setup google vision API
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()

    #get media urls and print label descriptions
    for status in tweepy.Cursor(api.user_timeline, id="userid").items():
        if 'media' in status.entities:
            for images in status.entities['media']:
                image.source.image_uri = images['media_url']
                response = client.label_detection(image=image)
                print(f"image at {images['media_url']} contains:")
                for label in response.label_annotations:
                    print(label.description)


con_key = 
con_secret = 
key = 
secret = 
userid = 'Donovan01060515'
read_image(con_key, con_secret, key, secret, userid)
