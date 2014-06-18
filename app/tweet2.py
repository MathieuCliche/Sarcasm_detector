import tweepy
from tweepy import OAuthHandler
import csv
import time

ckey = 'jXYP0oLxe3pHpgmSB0svgvD6Y'
csecret = '3usxAeZnvEsIRgsDXUgiGf4yk9MR9XM1my3cHiqqcOegOfBung'
atoken = '281777900-ckj8pV8ngvCz0c2XolQxbBNBluyxorXGocDDjoKG'
asecret = 'KQqzeDaqn0LDu3y3BWDrTqlU6EOuVsVsmRNKyGD4gnIaO'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)
test=[]
for data in tweepy.Cursor(api.search,
                           q="#sarcastic",
                           result_type="recent",
                           #since="2014-06-14",
                           #until="2014-06-15",
                           include_entities=True,
                           lang="en").items():
    try:
        tweettext = data.text#data.split(',"text":"')[1].split('","source')[0]
        if tweettext[0:2]!='RT':
            print tweettext
            saveFile = open('twitDB_sarcasm.csv','a')
            saveFile.write(tweettext)
            saveFile.write('\n')
            saveFile.close()
    except BaseException, e:
        print 'Failed ondata,', str(e)
        #time.sleep(5)