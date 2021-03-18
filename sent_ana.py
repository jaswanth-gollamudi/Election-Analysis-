import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
 
class TwitterClient(object):
    
    def __init__(self):
        
        consumer_key = 'IIfpERdYbMJXo9p7rCaocukh1'
        consumer_secret = 'PNv4ERiRCpqgFqxt54RIS2CikKA6ofQALkSZSJCGvCrgSKw3Sa'
        access_token = '856162682025775104-7bOImv2nFyz3xlIVyPFJ71OYn3Nk2hv'
        access_token_secret = 'DGea0jqtsThEt91Fs00H3SKMRoXxowuWe4fHPMDqXf9OY'
 
        
        try:
            
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            
            self.auth.set_access_token(access_token, access_token_secret)
            
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
       
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
       
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 10):
        
        tweets = []
 
        try:
           
            fetched_tweets = self.api.search(q = query, count = count)
 
           
            for tweet in fetched_tweets:
                
                parsed_tweet = {}
 
               
                parsed_tweet['text'] = tweet.text
               
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                
                if tweet.retweet_count > 0:
                    
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            
            return tweets
 
        except tweepy.TweepError as e:
           
            print("Error : " + str(e))
 
def main():
   
    api = TwitterClient()
    
    tweets = api.get_tweets(query = 'Narendra modi', count = 2000)
 
   
    ptweets = [t for t in tweets if t['sentiment'] == 'positive']
    
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
   
    ntweets = [t for t in tweets if t['sentiment'] == 'negative']
    
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
   
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
 
    
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
 
   
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
 
if __name__ == "__main__":
   
    main()
