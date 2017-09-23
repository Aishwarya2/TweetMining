import json
import operator
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import pandas as pd
tweets_data2 = []
tweets_file = open('new.json', "r")
tweets_write = open('write.csv', "w")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        texts = tweet['text']
        coded = texts.encode('utf-8')
        s = str(coded)
        tweets_write.write(s[2:-1])
        tweets_write.write('\n')
        tweets_data2.append(tweet)
    except:
	    continue


