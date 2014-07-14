""" Class used to stream tweets. """

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv
import time

#ckey = 
#csecret = 
#atoken =
#asecret = 

class listener(StreamListener):

    def on_data(self, data):
        try:
            tweettext = data.split(',"text":"')[1].split('","source')[0]
            if tweettext[0:2]!='RT':# and '#sarcasm' not in tweettext and len(tweettext.split())>5:  #Basic additionnal filters if necessary.
                print tweettext
                saveFile = open('twitDB_sarcasm.csv','a')
                saveFile.write(tweettext)
                saveFile.write('\n')
                saveFile.close()
            return True
        except BaseException, e:
            print 'Failed ondata,', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#NY = [74,40,-73,41]
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#sarcasm"])
#twitterStream.filter(locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41])#locations=[-6.38,49.87,1.77,55.81])