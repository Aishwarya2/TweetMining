#import regex
import re
import json
import operator
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
#start process_tweet
def preprocess(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
tweets_write = open('write.csv', "w")
with open('new.json', 'r') as f:
    for line in f:
        try:
            tweet = json.loads(line)
            tokens = preprocess(tweet['text'])
            coded = tokens.encode('utf-8')
            s = str(coded)
            tweets_write.write(s[2:-1])
            tweets_write.write('\n')
        except:
            continue