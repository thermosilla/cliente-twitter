import config as conf

from twitter import *

t = Twitter(auth=OAuth(conf.TOKEN, conf.TOKEN_KEY, conf.CON_SECRET,
    conf.CON_SECRET_KEY))

def search(query):
    return t.search.tweets(q=query)
