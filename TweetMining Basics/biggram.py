#import regex
import re
import json
from collections import Counter 
from nltk.stem import RegexpStemmer
from nltk import bigrams
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
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
st = open('stopwords.txt', 'r')
st = RegexpStemmer('ing$|s$|able$|ly$', min=4)
stopWords = getStopWordList('stopwords.txt')
tweets_write = open('abiwrite.csv', "w")
tweets_feature = open('tweet.csv',"w")
l = open('sriram.txt', 'w')
with open('file.json', 'r') as f:
    count_all = Counter()
    count1 =Counter()
    count2 =Counter()
    for line in f:
        try:
            tweet = json.loads(line)
            tokens = preprocess(tweet['text'])
            pro = getFeatureVector(tokens)
            terms_all = [term for term in pro]
            #x = [st.stem(term) for term in pro]
            #for y in x:
             #   l.write(y)
              #  l.write('\n')
            count_all.update(terms_all)
            terms_bigram = bigrams(terms_all)
            terms_stopbigram = bigrams(stopWords)
            count1.update(terms_bigram)
            count2.update(terms_stopbigram)
            coded = tokens.encode('utf-8')
            s = str(coded)
            tweets_write.write(s[2:-1])
            tweets_write.write('\n')
            tweets_feature.write(pro)
            tweets_feature.write('\n')
        except:
            continue
    print(count_all.most_common(200))
    print(count1.most_common(100))
    print (count2.most_common(5))
    print (pro)



