#-*-coding:utf-8-*-

import twitter
import twitkey

import inspect


""" init """  
CONSUMER_KEY = twitkey.twkey['cons_key']
CONSUMER_SECRET = twitkey.twkey['cons_sec']
ACCESS_TOKEN_KEY = twitkey.twkey['accto_key']
ACCESS_TOKEN_SECRET = twitkey.twkey['accto_sec']

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)
#tweets = api.GetSearch(term=u"#今日")
tweets_from = api.GetMentions()
tweets_to = api.GetReplies()

ins = inspect.getargspec(api.GetMentions)
#print ins

print "from"
for i in range(3):
    print tweets_from[i].text
    print tweets_from[i].in_reply_to_status_id
    print tweets_from[i].id

print "to"
for i in range(3):
    print tweets_to[i].text
    print tweets_to[i].in_reply_to_status_id 
    print tweets_to[i].id 

