#-*-coding:utf-8-*-

import re

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

        self.api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET)
        

    def get_tweets2you_TL(self):
        #bot -> someone 
        tweets2you = self.api.GetReplies(count=5)
        #count=5 means last 5 tweets to you
        return tweet2you

    def get_tweets2me_TL(self):
        #someone -> bot
        tweet2me = self.api.GetReplies(count=5)
        #count=5 means last 5 tweets to me
        return tweet2me

    def get_id_tweets2you_TL(self):
        id_tweets2you = []
        tweets2you = self.get_tweets2you_TL()
        for tweet in tweets2you:
            id_tweets2you.append(tweet.in_reply_to_status_id)
            #api:in_reply_to_status_id
        return id_tweets2you

    def get_id_tweets2me_TL(self):
        id_tweets2me = []
        tweet2me = self.get_tweets2me_TL()
        for tweet in tweets2me:
            id_tweets2me.append(tweet.id)
            #api:id
        return id_tweets2me

    def get_id_tweet2you_DB(self):
        #record from db
        id_tweet2you_DB = []
        print ""
        return id_tweet2you_DB

    def get_id_tweet2me_DB(self):
        #record from db
        id_tweet2me_DB = []
        print ""
        return id_tweet2me_DB
    
    def notmatch_id(self, id_new, id_old):
        if len(id_old) < 0:
            return id_new
        else:
            id_notmatch = []
            for i in id_new:
                if i not in id_old:
                    id_not_match.append(i)
            return id_notmatch

    def set_id_tweet2you(self):
        #record to DB
        id_new = self.get_id_tweets2you_TL()
        id_old = self.get_id_tweet2you_DB()
        id_notmatch = self.notmatch_id(id_new, id_old)
        print ""

    def set_id_tweet2me(self):
        #record to DB
        id_new = self.get_id_tweets2me_TL()
        id_old = self.get_id_tweet2me_DB()
        id_notmatch = self.notmatch_id(id_new, id_old)
        print ""

    def set_text2you(self):
        #record to DB
        print ""

    def set_text2me(self):
        #record to DB
        print ""
    
    def trim_text(self,text):
        at_in_text = re.findall('@.*\s', text)
        print at_in_text
        if len(at_in_text) > 0:
            for at_ in at_in_text:
                trim_text = text.strip(at_)
        return trim_text

    def tweet(self):
        print ""
    
    def run(self):
        #get tweet
        tweets2me = self.get_tweets2me_TL()
        id_tweets2me = self.get_id_tweets2me_TL()
        #compare tweet with DB
        id_tweet2me_DB = self,get_id_tweet2me_DB()
        id_notmatch = self.notmatch_id(id_tweet2me, id_tweet2me_DB)
        
        #text2me -> text2you (Word Converter)
        
        #tweet2you

        #Record to DB

        print ""
    
def test():
    t2b = Tweet2bot()
    print t2b.trim_text('@Tweet2bot @ Tweet3bot ラップデータベース')

if __name__ == '__main__':
    test()

    
    

    
