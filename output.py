# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:41:02 2019

@author: Jaswanth_Bot
"""

   
    
import nltk
import pandas as pd
nltk.download('vader_lexicon')
dataset = ['issues', 'complaint', 'months', 'parents', 'night', 'morning', 'days', 'information', 'Please', 'response', 'home', 'article recommendations', 'police complaint', 'day', 'Adblocker', 'flutter', 'Suresh', 'Kuppam mandal', 'Kuppam police', 'incident', 'years', 'police station', 'letter',  'family members', 'Tanjamma Kotalu village', 'terms', 'child', 'Saturday', 'hours', 'April', 'village', 'woman', 'neighbours', 'subscriber community', 'website', 'site', 'house', 'husband', 'couple']
def nltk_sentiment(sentence):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    nltk_sentiment = SentimentIntensityAnalyzer()
    score = nltk_sentiment.polarity_scores(sentence)
    print(score)

nltk_results = [nltk_sentiment(row) for row in dataset]
results_df = pd.DataFrame(nltk_results)
text_df = pd.DataFrame(dataset, columns = ['text'])
nltk_df = text_df.join(results_df) 