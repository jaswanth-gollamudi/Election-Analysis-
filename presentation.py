# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:39:56 2019

@author: Jaswanth_Bot
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:38:22 2019

@author: Jaswanth_Bot
"""

import sqlite3
from bs4 import BeautifulSoup
import urllib
import re
import urllib.request
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import copy
#nltk.download()

connection = sqlite3.connect("kumarrr.db")
cursor = connection.cursor()
result = cursor.execute("SELECT url from links_html;")



def get_p(url):
    with urllib.request.urlopen(url) as link:
        html = link.read()
        #print(html)
        soup = BeautifulSoup(html , 'html.parser')
        x = soup.find_all('p', string = True)
        #print(x)
        #final_text = re.sub(r'<.*?>', "", str(x))
        #print(final_text)
        single_link_array = []
        for i in x:
           #print(i)
           #print('\n')
           text = re.sub(r'<.*?>', "", str(i))
           #print(text)
           single_link_array.append(text)
    return single_link_array

final_array = []    
for i in result:
    single_link_array = get_p(i[0])
    for i in single_link_array:
        final_array.append(i)

print(final_array)

print(len(final_array))

    
#def new_tokenize(final_array):
    #final_tokens = []
    #for i in final_array:
        #token = word_tokenize(i)
        #for j in token:
            #final_tokens.append(j)
   # return final_tokens
'''
tokenized_text=[]   
def tokenizing(text):
     tokenized_text=word_tokenize(text)
     for i in word_tokenize(text):      
      print(tokenized_text)   '''   
      
      
def n_tokenizing(final_array):
    tokens = []
    for i in final_array:
        tokenized_text = word_tokenize(str(i))
        for j in tokenized_text:
            tokens.append(j)
    return(tokens)
            
        
        
print(n_tokenizing(final_array))
tokens = n_tokenizing(final_array)




'''
def stoppy(text): 
     stop_words = set(stopwords.words("english"))
     words=word_tokenize(text)
     filtered_sentence=[]
     for w in words:
         if w not in stop_words:
             filtered_sentence.append(w)
     print(filtered_sentence)
     '''
     
def new_stoppy(tokens):
    stop_words = set(stopwords.words("english"))
    filtered_tokens = []
    for word in tokens:
        if word not in stop_words:
            filtered_tokens.append(word)
    return filtered_tokens

print(new_stoppy(tokens))
filtered_tokens = new_stoppy(tokens)
print(filtered_tokens)

'''
def stemming(text):
      ps = PorterStemmer()
      words = word_tokenize(text)
      for w in words:
        print(ps.stem(w))'''
        

def new_stemming(filtered_tokens):
    ps = PorterStemmer()
    stemmed_tokens = []
    for word in filtered_tokens:
        stemmed_tokens.append(ps.stem(word))
    return stemmed_tokens

print(new_stemming(filtered_tokens))
stemmed = new_stemming(filtered_tokens)
print(stemmed)

'''
def pos_(text):
    
    stop_words = set(stopwords.words("english"))   
    for i in tokenized_text: 
      wordsList = nltk.word_tokenize(i) 
      wordsList = [w for w in wordsList if not w in stop_words]  
      tagged = nltk.pos_tag(wordsList) 
      print( tagged)
 '''     
      
      
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#tokenized = custom_sent_tokenizer.tokenize(sample_text)

def n_pos(stemmed):
    return nltk.pos_tag(stemmed)
    
tagged_words = n_pos(stemmed)
print(tagged_words)

'''
def chunk_it(sentence):
    
    for i in tokenized_text:
      words = nltk.word_tokenize(i)
      tagged = nltk.pos_tag(words)
      
      chunkParser = nltk.RegexpParser(grammar)
      tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
      tree = chunkParser.parse(tagged)
      for subtree in tree.subtrees():
        print(subtree)
    '''
    
def new_chunk_it(tagged_words):
    grammar = ('''
           NP: {<DT>?<JJ>*<NN>} # NP
          ''')
    chunkParser = nltk.RegexpParser(grammar)
    tree = chunkParser.parse(tagged_words)
    chunked = []
    for subtree in tree.subtrees():
        chunked.append(subtree)
    return chunked
        
        
chunked = new_chunk_it(tagged_words)
print(chunked)
def extract_NN(sent):
     grammar = r"""
      NBAR:
        {<NN.*>*<NN.*>}

      NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}
    """
     chunker = nltk.RegexpParser(grammar)
     ne = set()
     chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
     for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
        ne.add(' '.join([child[0] for child in tree.leaves()]))
     print(ne)
     
extract_NN(str(final_array))





