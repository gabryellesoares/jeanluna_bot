import tweepy

print('jean luna')

CONSUMER_KEY = 'WI1KD0sAnBQGVptHeBEMvxRqs'
CONSUMER_SECRET = 'lg4kHPMrcRLKkzKAazQ8gFAz3myWPUXKFf6aCJ6EC8ZTreNIQK'
ACCESS_KEY = '1289979324930686981-I7BdzsM2CzrSvaFSiAk9NdgEdGhplP'
ACCESS_SECRET = 'kaBjgEZQvTO1nSqJg3wCABF6ilntYZVIOgrKGJANnFMKC'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


tweets = api.search('jean luna')
for tweet in tweets:
    if 'jean luna' in tweet.text.lower():
        print ('found jean luna!')
        print ('it works!!!')
    print(str(tweet.id) + ' - ' + tweet.text)