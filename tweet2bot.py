#-*-coding:utf-8-*-

import twitter
import twitkey
import tweet2me as t2m
import WordConverter as wc

class Tweet2bot:
    
    def init(self):
        CONSUMER_KEY = twitkey.twkey['cons_key']
        CONSUMER_SECRET = twitkey.twkey['cons_sec']
        ACCESS_TOKEN_KEY = twitkey.twkey['accto_key']
        ACCESS_TOKEN_SECRET = twitkey.twkey['accto_sec']

        api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET)
        return api

    def get_id_tweets2you_TL(self):
        id_tweets2you = api.GetReplies(count=5)
        #count=5 means last 5 tweets to you
        
        return id_tweets2you

    def get_id_tweets2me_TL(self):
        id_tweets2me = api.GetReplies(count=5)
        #count=5 means last 5 tweets to me
        
        return id_tweets2me

    def notmatch_id(self, id_new, id_old):
        if len(id_old) < 0:
            return id_new
        else:
            id_notmatch = []
            for i in id_new:
                if i not in id_old:
                    id_not_match.append(i)
            return id_notmatch

    def set_id_tweet2me(self):
        #record to DB
        print ""

    def set_id_tweet2you(self):
        #record to DB
        print ""
        
    def set_text2me(self):
        #record to DB
        print ""

    def set_text2you(self):
        #record to DB
        print ""

    
    

    
