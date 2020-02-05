import tweepy
from google.cloud import vision
# User passes twitter handle handle
# Function returns text using google vision
# get link of media and save it for the google vision API
# Function hadling for twitter api and google vision api need to be in a Function
# function must be called from a different functions


#def read_tweets():
#twitter API OAuth 2 AUthentication
auth = tweepy.OAuthHandler("4IVCCtuSQ3eLb8i2kH70lVawI", "7erpsGo0gNJTPnTEYc73PFkB6iCvJZrK8HIb7vVm45ywKfZ04d")
auth.set_access_token("1222366331825090560-pTDch0qvoCkSvFVdgUoybz8OMQy5c8", "7b5LVDnfykKS5Xi5YYH4uiPAZNovzG2HnrpLE2OXV0whZ")

api = tweepy.API(auth)

#tweepy.Cursor(api.search, q="hashtag", count=5, include_entities=True)

#public_tweets = api.home_timeline()

#get user timeline for tweets to convert
user = api.get_user('Donovan01060515')
tweets = api.user_timeline(id="Donovan01060515")

#setup google vision API
client = vision.ImageAnnotatorClient()
image = vision.types.Image()

for status in tweepy.Cursor(api.user_timeline, id="Donovan01060515").items():
    if 'media' in status.entities:
        for images in status.entities['media']:
            image.source.image_uri = images['media_url']
            response = client.label_detection(image=image)
            for label in response.label_annotations:
                print(label.description)

for tweet in tweets:
    print(tweet.text)
