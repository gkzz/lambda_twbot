# coding: UTF-8
try:
    import unzip_requirements
except ImportError:
    pass

import tweepy
import time
import os
import random
import traceback

def _set_token():
    """ set twitter token """

    CK = os.environ['CONSUMER_KEY']
    CS = os.environ['CONSUMER_SECRET']
    AT = os.environ['ACCESS_TOKEN']
    AS = os.environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    return tweepy.API(auth)


def _find_tweet(token):
    found = []

    kws = [
        '#polca 支援',
        '#polca 挑戦',
    ]

    for kw in kws:
        for tweet in tweepy.Cursor(token.search, kw).items(5):
            found.append(tweet)
    
    return found


def rtweet(event, context):
    """ entry point of rtweet """

    counter = 0

    token = _set_token()
    tweets = _find_tweet(token)

    for tweet in tweets:
        try:
            #print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
            tweet.retweet()
            logger.info(tweet.retweet())
            counter+=1
            #print('Retweet published successfully.')
    
            # Where sleep(10), sleep is measured in seconds.
            # Change 10 to amount of seconds you want to have in-between retweets.
            # Read Twitter's rules on automation. Don't spam!
            time.sleep(random.randint(2,5))
            
        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.TweepError as error:
            print('''Retweet not successful. 
            Reason: {r}
            '''.format(r=error.reason))
    
        except StopIteration:
            print(traceback.format_exc())
            break
    
    return "RtweetConts: {num}".format(num=counter)
    

    

def fav(event, context):
    """ entry point of fav """

    counter = 0

    token = _set_token()
    tweets = _find_tweet(token)

    for tweet in tweets:
        try:
            tweet.favorite()
    
            # Where sleep(10), sleep is measured in seconds.
            # Change 10 to amount of seconds you want to have in-between retweets.
            # Read Twitter's rules on automation. Don't spam!
            time.sleep(random.randint(2,5))
            
        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.TweepError as error:
            print('''Fav not successful. 
            Reason: {r}
            '''.format(r=error.reason))
    
        except StopIteration:
            print(traceback.format_exc())
            break
    
    return "FavConts: {num}".format(num=counter)
    


#if __name__ == "__main__":
#    rtweet('', '')
