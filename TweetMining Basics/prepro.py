import preprocessor as p
import json
import operator
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
tweets_file = open('new.json', "r")
tweets_write = open('write.csv', "w")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        texts = tweet['text']
        p.clean(tweet)
        p.tokenize(tweet)
        parsed_text = p.parse(tweet)
        print (parsed_text)
        coded = parsed_text.encode('utf-8')
        s = str(coded)
        tweets_write.write(s)
        tweets_write.write('\n')
    except:
	    continue