# first you need to create your own Twitter API account
consumer_key = 'INSERT consumer key'
consumer_key_secret = 'INSERT consumer key secret'
access_token = 'INSERT access token'
access_token_secret = 'INSERT access token secret'

# this code will link your python to Twitter
aut = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
aut.set_access_token(access_token, access_token_secret)
api = tweepy.API(aut)

# run this to confirm if the API you used is in fact your own Twitter handle
username = api.me()
print(username.name)

# choose a Twitter handle that you'd like pull tweets from
tweets = api.search('INSERT A TWITTER HANDLE')

# create an empty list so that you may fill in this list with each tweet while you loop through them

temp = []

 # use textblob and the sentiment function to come up with your sentiment analysis from the tweets
 
    for i in tweets:
        temp.append(i.text)
        analysis = TextBlob(i.text)
        temp.append(analysis.sentiment)
        if analysis.sentiment[0]>=0:
           temp.append('Positive')
        else:
           temp.append('Negative')

df = pd.DataFrame(temp)

# view your dataframe results
print(df)

# export your data and sentiment score into a csv file
df.to_csv("out.csv")
