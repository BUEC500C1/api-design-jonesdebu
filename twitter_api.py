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
    for status in tweepy.Cursor(api.user_timeline, id="Donovan01060515").items():
        if 'media' in status.entities:
            for images in status.entities['media']:
                image.source.image_uri = images['media_url']
                response = client.label_detection(image=image)
                print(f"image at {images['media_url']} contains:")
                for label in response.label_annotations:
                    print(label.description)


con_key = "4IVCCtuSQ3eLb8i2kH70lVawI"
con_secret = "7erpsGo0gNJTPnTEYc73PFkB6iCvJZrK8HIb7vVm45ywKfZ04d"
key = "1222366331825090560-pTDch0qvoCkSvFVdgUoybz8OMQy5c8"
secret = "7b5LVDnfykKS5Xi5YYH4uiPAZNovzG2HnrpLE2OXV0whZ"
userid = 'Donovan01060515'
read_image(con_key, con_secret, key, secret, userid)
