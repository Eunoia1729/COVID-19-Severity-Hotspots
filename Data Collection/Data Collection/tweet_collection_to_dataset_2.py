import tweepy

# Step 1 - Authenticate
consumer_key= '***REMOVED***'
consumer_secret= '***REMOVED***'

access_token='***REMOVED***'
access_token_secret='***REMOVED***'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Step2 - Call the API
api = tweepy.API(auth)

# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

import pandas
import re
import emoji

msgs = []
msg =[]
count = 0
number_of_tweets = 1000

for tweet in tweepy.Cursor(api.search, q='#corona', rpp=100, lang="en", tweet_mode='extended').items(number_of_tweets):
    tweet_text = tweet.full_text
    geo = tweet.coordinates
    if(geo == None):
        continue
    longitude = geo['coordinates'][0]
    latitude = geo['coordinates'][1]
    tweet_text = (emoji.demojize(tweet_text))
    tweet_text = re.sub("\s:"," ", tweet_text)
    tweet_text = re.sub(":"," ", tweet_text)
    clean_text = re.sub(r"""
               [,.;@#?!&$"']+
               \ *  
               """,
               " ", 
               tweet_text, flags=re.VERBOSE)
    #clean_text = "\"" + clean_text + "\""
    #location = "\"" + location + "\""
    msg = [clean_text, longitude, latitude, 0] 
    msg = tuple(msg)                    
    msgs.append(msg)

df = pd.DataFrame(msgs)

df = pd.DataFrame(msgs, columns = ['Text', 'Longitude', 'Latitude', 'Sentiment']) 

df.to_csv (r'/content/gdrive/My Drive/dmw_project/tweet_data.csv', index = False, header=True)