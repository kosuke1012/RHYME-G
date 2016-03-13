#-*-coding:utf-8-*-

import twitter
import twitkey
import tweet2me as t2m
import WordConverter as wc


def init():
    CONSUMER_KEY = twitkey.twkey['cons_key']
    CONSUMER_SECRET = twitkey.twkey['cons_sec']
    ACCESS_TOKEN_KEY = twitkey.twkey['accto_key']
    ACCESS_TOKEN_SECRET = twitkey.twkey['accto_sec']

    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)
    return api
    

def get_tweets(api):
    tweets = api.GetReplies(count=5)
    return tweets



def test(fname2me, fname2you):
    api = init()
    tweets = get_tweets(api)
    in_reply_to_status_id_new = []
    for tweet in tweets:
        if tweet.in_reply_to_status_id != None:
            in_reply_to_status_id_new.append(tweet.in_reply_to_status_id)
    in_reply_to_status_id_old = t2m.get_list(fname2you)
    id_old = t2m.get_list(fname2me)
    
    in_reply_to_status_id_notmatch = t2m.notmatch_id(id_old, in_reply_to_status_id_old)
    t2m.set_list(fname2you, in_reply_to_status_id_notmatch)

    in_reply_to_status_id_old = t2m.get_list(fname2you)
    in_reply_to_status_id_notmatch = t2m.notmatch_id(in_reply_to_status_id_new, in_reply_to_status_id_old)
    #t2m.set_list(fname2you, in_reply_to_status_id_notmatch)
    print in_reply_to_status_id_notmatch
    for reply in in_reply_to_status_id_notmatch:
        print reply
    texts =[]
    for tweet in tweets:
        if tweet.in_reply_to_status_id in in_reply_to_status_id_notmatch:
            texts.append(tweet.text.split(" ")[1])
            print tweet.text
    for text in texts:
        print text
        print wc.nihongo_boin(text)

    
    
    
    
if __name__ == '__main__':
    test("2me_list.txt","2you_list.txt")
