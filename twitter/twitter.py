import os
import tweepy
import requests

from tweepy import Stream
from dotenv import load_dotenv
from tweepy import OAuthHandler
from tweepy.streaming import Stream


class Twitter():
    def __init__(self, *args, **kwargs):
        self.CONSUMER_KEY = os.getenv('CONSUMER_KEY')
        self.CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
        self.ACCESS_KEY = os.getenv('ACCESS_KEY')
        self.ACCESS_SECRET = os.getenv('ACCESS_SECRET')
        self.CURRENT_USER = os.getenv('CURRENT_USER')
        self.API = self.auth()
        self.get_data()
        self.friends = self.get_current_user_friends()
        self.get_friends_tweets()
    
    def auth(self):
        """ API Authentication """
        au = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        au.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        return tweepy.API(au)
    
    
    def get_data(self):
        """ Get timeline tweets from API"""
        public_tweets = self.API.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)
            
    def get_current_user_friends(self):
        """Get a list of current user's friends.'"""
        user = self.API.get_user(screen_name=self.CURRENT_USER)
        
        friends = []
        for friend in user.friends():
            friends.append(friend.screen_name)
        friends.append(self.CURRENT_USER)
        #print(friends)
        return friends
    
    def get_friends_tweets(self):
        """Returns each friend's tweets' """
        tweets = []
        for friend in self.friends:
            for tweet in tweepy.Cursor(self.API.user_timeline).items():
                tweets.append(tweet._json)
        print(tweets,"\n")
        
        return tweets
if __name__ == "__main__":
    load_dotenv()
    Twitter()