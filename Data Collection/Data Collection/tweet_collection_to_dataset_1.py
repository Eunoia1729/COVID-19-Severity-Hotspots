import tweepy

# Step 1 - Authenticate
consumer_key= 'SMVEA3MypMkgOeAGjn75N0gHJ'
consumer_secret= 'skaKGnyqPpzGO9PHubYaEVygai6fQB95ZkZQJrFFYaJfXZvI8J'

access_token='715755192994643968-NgdBmvMLFm7QotE1sZezym6daI0WyOD'
access_token_secret='d9B1xOXUzlgNyGa8Zyex09V6sTz4RUS5a4yPVqwCyiNRV'

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
    if(tweet.user.location == None or tweet.user.location == "" ):
        continue
    tweet_text = tweet.full_text
    location = tweet.user.location
    tweet_text = (emoji.demojize(tweet_text))
    tweet_text = re.sub("\s:"," ", tweet_text)
    tweet_text = re.sub(":"," ", tweet_text)
    clean_text = re.sub(r"""
               [,.;@#?!&$"']+
               \ *  
               """,
               " ", 
               tweet_text, flags=re.VERBOSE)
    location = re.sub(r"""
               [,.;@#?!&$"']+
               \ *  
               """,
               " ", 
               location, flags=re.VERBOSE)
    #clean_text = "\"" + clean_text + "\""
    #location = "\"" + location + "\""
    msg = [clean_text, location] 
    msg = tuple(msg)                    
    msgs.append(msg)

df = pd.DataFrame(msgs)

print(len(msgs))

df = pd.DataFrame(msgs, columns = ['Text', 'Location']) 

df.to_csv (r'C:\\Users\\HP\Desktop\\Machine Learning\\tweet_data.csv', index = False, header=True)