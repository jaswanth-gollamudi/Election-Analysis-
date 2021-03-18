# Election Analysis

# Data:-

1)From twitter

2)From various new articles like hindu,timesofindia etc...



# phase-1:-



Done sentiment analysis on candidates let's say x&Y and found the results using data from twitter.
sent_ana file in the repo helps you to do that.
Result something like this pos:- 0.08 neg:-0.01 neu:-0.01 for all the tweets.



# phase-2:-



By using web crawler got the data and stored them in data base and founf the analaysis.
1.web crawling is done using beautifulsoup.

2.connected sqlite database to python to store data from crawlers.

3.Data pre-processing is done using Nltk, where we have these following techniques to find keywords.




# TOKENIZATION

# STOPWORD EXTRACTION

# STEMMING

# POS TAGGING

# CHUNKING&CHINNING

# ENTITY EXTRACTION


After getting key woards found out sentiment analysis using sentiment intensity analizer by using - 

# VADAR:
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically used to sentiments expressed in social media. VADER uses a combination of A sentiment lexicon is a list of lexical features (e.g., words) which are generally labelled according to their semantic orientation as either positive or negative.





After using VADAR we get sentiment for every word we get something like this:

{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

{'neg': 1.0, 'neu': 0.0, 'pos': 0.0, 'compound': -0.296}

{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}




when we calculate average for all the words from data, we found difference between the candidates.
And when we avgerage the analysis from phase-2 and phase-1 ,we will find the overall sentiment analysis.


# All the files are given above with the PPT.







