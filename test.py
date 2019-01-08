import tweepy
import pprint
consumer_key = "8D5DEXkFuTNgGYLsXFrekZGWB"
consumer_secret = "XV8rZzHfg57vjG7HI3k50e2v94XMRRnjYgZ5TO8xDvxeZfwicb"
access_token= "4514204717-v3rf4py2sKwr4fT1r48GE2pqrAB7TZ6OZlLhhab"
access_token_secret = "WgA55zkTlY7CXCtRjD6bjV76fOFQxXSbvAdG2exznvYcT"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'pydelhi', count = 10, include_rts = True)

for status in stuff:
    print(status._json['text'])
