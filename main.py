# Sentiment Analysis performed on twitter tweets.

topic = 'Doge'
tweet_limit = 100
start_date = "2021-06-01"
end_date = "2021-06-07"


import tweepy
import textblob
import pandas as pd
import matplotlib.pyplot as plt
import re
from tkinter import *

api_key = "aPkDQtdtw3UynEDBoxQY4DXL8"
api_key_secret = "m68ktwWnrFVxIyHwOiAr1Fl3Bze3g1XRBqMeOpwynzOSXFtxFt"
access_token = "1007964620164759552-cqJ6IQ3zO0wBCEjiNwwmpkwFN9SHrR"
access_token_secret = "ZMb1eP2pMukZcgdttCWV8qoFzxayaXmN5PFDYysbxJIpL"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator,wait_on_rate_limit=True)

search = f'#{topic} -filter:retweets'

tweet_cursor = tweepy.Cursor(api.search, q=search, lang='en', until=end_date, since=start_date, tweet_mode='extended').items(tweet_limit)

tweets = [tweet.full_text for tweet in tweet_cursor]

tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

for x in range(10):
    print(tweets[x])

for _, row in tweets_df.iterrows():
    row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('#\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('@\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('\\n', '', row['Tweets'])

tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol > 0 else '-')

positive = tweets_df[tweets_df.Result == '+'].count()['Tweets']
negative = tweets_df[tweets_df.Result == '-'].count()['Tweets']

plt.bar([0,1], [positive, negative], label=['Positive', 'Negative'], color=['green', 'red'])
plt.legend()
plt.show()