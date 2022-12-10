import tweepy

# Replace with your Twitter API keys
consumer_key = "<your-consumer-key>"
consumer_secret = "<your-consumer-secret>"
access_key = "<your-access-key>"
access_secret = "<your-access-secret>"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# The topic you want to search for
TOPIC = "machine learning"

# The maximum number of results to return
MAX_RESULTS = 10

# Fetch the most recent tweets on the topic
tweets = tweepy.Cursor(api.search, q=TOPIC, lang="en", tweet_mode="extended").items(MAX_RESULTS)

# Print the tweets and their comments
for tweet in tweets:
    print(tweet.full_text)
    comments = tweet.comments()
    for comment in comments:
        print(comment.text)
    print()
