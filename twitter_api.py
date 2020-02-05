import tweepy
from google.cloud import vision
# User passes twitter handle handle
# Function returns text using google vision
# get link of media and save it for the google vision API
# Function hadling for twitter api and google vision api need to be in a Function
# function must be called from a different functions



#twitter API OAuth 2 Authentication
auth = tweepy.OAuthHandler("4IVCCtuSQ3eLb8i2kH70lVawI", "7erpsGo0gNJTPnTEYc73PFkB6iCvJZrK8HIb7vVm45ywKfZ04d")
auth.set_access_token("1222366331825090560-pTDch0qvoCkSvFVdgUoybz8OMQy5c8", "7b5LVDnfykKS5Xi5YYH4uiPAZNovzG2HnrpLE2OXV0whZ")

api = tweepy.API(auth)


#get user timeline for tweets to convert
user = api.get_user('Donovan01060515')
tweets = api.user_timeline(user.screen_name)

#setup google vision API
client = vision.ImageAnnotatorClient()
image = vision.types.Image()

#get media url and print label descriptions
image.source.image_uri = 'gs://cloud-samples-data/vision/using_curl/shanghai.jpeg'
response = client.label_detection(image=image)
for label in response.label_annotations:
    print(label.description)

#added for further testing:
for tweet in tweets:
    print(tweet.text)

#TODO:
#   1. Generalize tweepy.OAuthHandler, auth.set_access.token and api.get_user to be arguments that are entered into the function
#   2. Create a more oherent description of the media recieved from the twitter feed
