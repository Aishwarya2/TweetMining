import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
consumer_key = 'ZigWT7qNkVmpW3kn8xqSOkzAp'
consumer_secret = '1YjkieEWJHrlhNI6UUbwBW9kdUDficunTjZuFdyUD50Wl5cP8g'
access_token = '779885459929337856-3cGzaP2TvhaQRnppWuW5enUNoHYfx2e'
access_secret = 'm39Fs4H3s0H6fCxrVs79PnsLjkyl28auhWuswjghE5RWw'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#    twitter_stream = Stream(auth, MyListener())
#    twitter_stream.filter(track=['#iphone7reviews','#iPhone7review','#iphone7plusreviews','#iPhone7plusreview'], languages = ['en'])
for tweet in tweepy.Cursor(api.search, q="#iphone7", lang="en").items():
    try:
        with open('ash.json','a') as f1:
            f1.write(tweet)
    except BaseException as e:
        print('hello')
    
