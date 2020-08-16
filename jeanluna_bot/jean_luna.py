import tweepy
import time
from os import environ

# yes i've regenerated the keys
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
FILE_NAME = 'last_tweet_id.txt'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def retrieve_last_tweet_id(file_name):
    read_file = open(file_name, 'r')
    last_tweet_id = int(read_file.read().strip())
    read_file.close()
    return last_tweet_id

def store_last_tweet_id(last_tweet_id, file_name):
    write_file = open(file_name, 'w')
    write_file.write(str(last_tweet_id))
    write_file.close()
    return

last_tweet_id = retrieve_last_tweet_id(FILE_NAME)

def reply_and_retweet():
    # the tweets are going to be retweeted/responded in chronologic order
    for tweet in reversed(tweets): 
        print(str(tweet.id) + ' - ' + tweet.full_text)
        last_tweet_id = tweet.id
        user = tweet.user.screen_name
        store_last_tweet_id(last_tweet_id, FILE_NAME)
        not_rt = bool(tweet.retweeted) == False
        not_jl = not(user == 'jeanluna_bot')
        try:
            if 'jean luna' in tweet.full_text.lower() and not_rt and not_jl:
                print ('found jean luna!')
                print ('it works!!!')
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
                api.update_status('@' + tweet.user.screen_name + ' jean luna', tweet.id)
        except tweepy.error.TweepError as e:
            next


# each 15 seconds it will run again
while True:
    tweets = api.search(q='jean luna', since_id=last_tweet_id, tweet_mode='extended')
    reply_and_retweet()
    time.sleep(15)