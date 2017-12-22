from TweeterStreamListener import *

class ListenerRunner():
    
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_key = access_key
        self.access_seret = access_secret
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.auth = auth
        self.api = tweepy.API(auth)

# make this a class and get a tweepy.Stream object on call
# also allow the class to return specific tweets? This class should collect data
