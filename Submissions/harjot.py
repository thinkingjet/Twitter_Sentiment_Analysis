"""
2nd PLACE!!!

CONGRATULATIONS TO hashcat.hccapx#8169
"""


import tweepy
import textblob
import pandas as pd
import matplotlib.pyplot as plt
import re

# so gaurav doesn't know who's api's I used
# vault = open('api keys', 'r').read().splitlines()

# api_key = vault[0]
# api_key_secret = vault[1]
# access_token = vault[2]
# access_token_secret = vault[3]

api_key = 'x2XjAlMEW7UzorVmKAviXLYZX'
api_key_secret = 'CSVoUoCwB2W9R2RfhRX1zXZQa7xrW1zzM9naISGJN1v9IeHV7j'
access_token='1007964620164759552-vF2IGdfuXB7Z0FBxGNidx1IKy6ww7K'
access_token_secret='WIivnWduK1dLCWKohGoYrDv5nSqanwRLgGrxMjM6DPucj'


authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

# setting up variables with respective values
topic = 'bitcoin'

start_date = "2021-08-03"
end_date = "2021-08-08"

search = f'#{topic} -filter:retweets'

tweet_limit = tweepy.Cursor(api.search, q=search, lang='en', until=end_date, since=start_date,
                             tweet_mode='extended').items(100)

tweets = [tweet.full_text for tweet in tweet_limit]

tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

# iterating tweets into rows and 'cleaning' for sentiment analysis
for _, row in tweets_df.iterrows():
    row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('#\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('@\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('\\n', '', row['Tweets'])

# using textblob to conduct the sentiment analysis on limited tweets
tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol > 0 else '-')

# assigning the tweets the '+' or'-' result to plot on graph
positive = tweets_df[tweets_df.Result == '+'].count()['Tweets']
negative = tweets_df[tweets_df.Result == '-'].count()['Tweets']

plt.bar([0, 1], [positive, negative], label=['positive', 'negative'], color=['green', 'red'])
plt.legend()

plt.show()
