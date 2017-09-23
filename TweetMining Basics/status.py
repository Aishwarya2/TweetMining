import tweepy
from tweepy import OAuthHandler
consumer_key = 'ZigWT7qNkVmpW3kn8xqSOkzAp'
consumer_secret = '1YjkieEWJHrlhNI6UUbwBW9kdUDficunTjZuFdyUD50Wl5cP8g'
access_token = '779885459929337856-3cGzaP2TvhaQRnppWuW5enUNoHYfx2e'
access_secret = 'm39Fs4H3s0H6fCxrVs79PnsLjkyl28auhWuswjghE5RWw'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)