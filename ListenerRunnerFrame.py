from TweeterStreamListener import *

consumer_key= # 'key'
consumer_secret= # 'key'
access_key= # 'key'
access_secret= # 'key'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

