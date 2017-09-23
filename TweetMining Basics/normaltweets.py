import tweepy
import csv
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('abinew.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("hello")
        return True
 
    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    consumer_key = 'ZigWT7qNkVmpW3kn8xqSOkzAp'
    consumer_secret = '1YjkieEWJHrlhNI6UUbwBW9kdUDficunTjZuFdyUD50Wl5cP8g'
    access_token = '779885459929337856-3cGzaP2TvhaQRnppWuW5enUNoHYfx2e'
    access_secret = 'm39Fs4H3s0H6fCxrVs79PnsLjkyl28auhWuswjghE5RWw'
 
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    csvFile = open('tweets.csv', 'w')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)


    for tweet in tweepy.Cursor(api.search, q="#iphone7review", lang="tr").items():
        print (tweet)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])