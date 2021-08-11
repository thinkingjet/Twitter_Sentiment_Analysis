"""
1st PLACE!!!

CONGRATULATIONS TO AK26#5915
"""


import tweepy
import pandas as pd
import textblob
import matplotlib.pyplot as  plt
import regex as re

consumer_key = 'x2XjAlMEW7UzorVmKAviXLYZX'
consumer_secret = 'CSVoUoCwB2W9R2RfhRX1zXZQa7xrW1zzM9naISGJN1v9IeHV7j'
access_token='1007964620164759552-vF2IGdfuXB7Z0FBxGNidx1IKy6ww7K'
access_token_secret='WIivnWduK1dLCWKohGoYrDv5nSqanwRLgGrxMjM6DPucj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
tweets = tweepy.Cursor(api.search,q="bitcoin -filter:retweets",until = '2021-08-04',count =100,lang='en',since_id=1).items(100)

# create tweet list
tweets_list = [[tweet.created_at,tweet.id,tweet.text] for tweet in tweets]

#get the only text data in list
only_text = [data[2] for data in tweets_list]

# regex to grab only words from the text
only_words = re.compile(r'[A-Za-z\'0-9]+',re.VERBOSE)

#loop through the text list for data scrap
for i in range(0,len(only_text)):
    only_text[i] = re.sub(r'@[A-Za-z0-9_:]*|(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%|)*\b|[\n]*', '', only_text[i], flags=re.MULTILINE)
    only_text[i] = ' '.join(only_words.findall(only_text[i]))


#analyse sentiment polarity for each tweet and save the data in a list
data_sentiment = map(lambda tweet : textblob.TextBlob(tweet).sentiment.polarity,only_text)


#create the dataframe from fetched data through API call
tweets_df = pd.DataFrame(tweets_list,columns=["created_at","id","text"])

sentiment = []

#classify negative or positive on the basis of sentiment analysis data 
for item in data_sentiment:
	if item <=0:
		sentiment.append('negative')
	else:
		sentiment.append('positive')

for data in only_text:
	print('-->'+data)
    

#merge the sentiment analysis result with the tweets_df 
tweets_df['sentiment'] = sentiment
print(tweets_df.head(10))

#visualisation in graph 
tweets_df.groupby('sentiment')['id'].nunique().plot(kind='bar')
plt.show()

