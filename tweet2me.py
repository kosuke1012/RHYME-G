#-*-coding:utf-8-*-

import twitter
import twitkey

""" init """  
CONSUMER_KEY = twitkey.twkey['cons_key']
CONSUMER_SECRET = twitkey.twkey['cons_sec']
ACCESS_TOKEN_KEY = twitkey.twkey['accto_key']
ACCESS_TOKEN_SECRET = twitkey.twkey['accto_sec']

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def get_tweets():
    tweets = api.GetMentions()
    return tweets

def get_list(filename):
    f = open(filename, "r")
    keys = f.readline().strip("\t")
    id_list = []
    for i in f:
        id_list.append(int(i))
    f.close()
    return id_list

def notmatch_id(id_new, id_old):
    if len(id_old) < 0:
        return id_new
    else:
        id_notmatch = []
        for i in id_new:
            if i not in id_old:
                id_notmatch.append(i)
        return id_notmatch

def set_list(filename,id_list):
    f = open(filename, "a")
    for i in id_list:
        f.write(str(i))
        f.write("\n")
    f.close()

def test(filename):
    tweets = get_tweets()
    id_new = []
    for tweet in tweets:
        id_new.append(tweet.id)

    id_old = get_list(filename)
    id_notmatch = notmatch_id(id_new, id_old)
    set_list(filename, id_notmatch)
    
if __name__ == '__main__':
    test("2me_list.txt")
