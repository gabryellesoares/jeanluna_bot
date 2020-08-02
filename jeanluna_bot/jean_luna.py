import tweepy
import time

CONSUMER_KEY = 'WI1KD0sAnBQGVptHeBEMvxRqs'
CONSUMER_SECRET = 'lg4kHPMrcRLKkzKAazQ8gFAz3myWPUXKFf6aCJ6EC8ZTreNIQK'
ACCESS_KEY = '1289979324930686981-I7BdzsM2CzrSvaFSiAk9NdgEdGhplP'
ACCESS_SECRET = 'kaBjgEZQvTO1nSqJg3wCABF6ilntYZVIOgrKGJANnFMKC'
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
tweets = api.search(q='jean luna', since_id=last_tweet_id, tweet_mode='extended')

def reply_and_retweet():
    print ('testing')
    
    # the tweets are going to be retweeted/responded in chronologic order
    # 1289993816586326018 id for testing
    for tweet in reversed(tweets): 
        print(str(tweet.id) + ' - ' + tweet.full_text)
        last_tweet_id = tweet.id
        store_last_tweet_id(last_tweet_id, FILE_NAME)
        if 'jean luna' in tweet.full_text.lower():
            print ('found jean luna!')
            print ('it works!!!')
            api.retweet(tweet.id)
            api.update_status('@' + tweet.user.screen_name + ' jean luna', tweet.id)

while True:
    reply_and_retweet()
    time.sleep(15)