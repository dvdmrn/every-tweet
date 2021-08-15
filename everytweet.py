#!/usr/bin/env python3

import itertools
import json
import tweepy
import time 
import os

'''
    save progress vars...
    charLen := the current character length 
    i := current index of the generator
'''

_apiKey = os.getenv("API_KEY")
_apiSecretKey = os.getenv("API_SECRET_KEY")
_accessToken = os.getenv("ACCESS_TOKEN")
_accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(_apiKey,_apiSecretKey)
auth.set_access_token(_accessToken, _accessTokenSecret)
api = tweepy.API(auth)

progress = {"i": 0, "charLen": 1}
maxChars = 280 # 250 chars is max tweet length
chars = "abcdefghijklmnopqrstuvwxyz 0123456789!,?.$'~+&*():/#"
# 2809 hours

def sanitizeMeDaddy(s):
    '''
    passes leading and trailing whitespace
    so that api calls don't go boom boom
    s := a String
    ''' 
    if(s[0] == " " or s[len(s)-1] == " "):
        return(" ")
    else:
        return(s)

def getCombos():        
    for i in range(progress['charLen'],maxChars-1):
        if(i==maxChars): # reached max
            exit()
        else:
            print(f"loop: {i}; charLen: {progress['charLen']}; ")
            combos = itertools.product(chars,repeat=progress["charLen"])
            slicedCombos = itertools.islice(combos,progress["i"], None)
            for subset in slicedCombos:
                progress["i"] += 1
                with open('progress.json','w') as outfile:
                    json.dump(progress,outfile)
                msg = "".join(subset)
                print(f'iterator step: {progress["i"]}; output {msg}')
                msg = sanitizeMeDaddy(msg)
                if(msg == " "):
                    pass
                else:
                    tweet(msg)
                    time.sleep(3600) # sleep for 1 hour
            progress["charLen"] += 1
            progress["i"] = 0

def tweet(theTweet):
    print(f'tweeting: {theTweet}')
    api.update_status(theTweet)

def loadProgress():
    global progress
    print("loading progress...")
    with open("progress.json") as jsonFile:
        progress = json.load(jsonFile)
    print("last progress: ")
    print(progress)


print("initialized")
loadProgress()
getCombos()
exit()


