""" The main function in this file, i.e. 'dialogue_act_features', takes a tweet and a topic modeler and returns
a dictionnary of features.  The feature extraction is composed of unigrams and bigrams,
a sentiment analysis, a part of speech counter, a capicalization counter and a topic vector."""

import nltk
import numpy as np
import string
import load_sent
from textblob import TextBlob
import exp_replace

print 'Loading files'
porter = nltk.PorterStemmer()
#sentiments = load_sent.load_sent_word_net()

def dialogue_act_features(sentence,topic_modeler):
        
    features = {}
    
    grams_feature(features,sentence)
    #sent_feature(features,sentence)
    #pos_feature(features,sentence)
    #cap_feature(features,sentence)
    topic_feature(features,sentence,topic_modeler)
    
    return features
    
def grams_feature(features,sentence):
    sentence_reg = exp_replace.replace_reg(sentence)
    
    #Spell check
    #sentence_reg = TextBlob(sentence_reg)
    #sentence_reg = str(sentence_reg.correct())
    
    tokens = nltk.word_tokenize(sentence_reg)
    tokens = [porter.stem(t.lower()) for t in tokens] 
    bigrams = nltk.bigrams(tokens)
    bigrams = [tup[0]+' ' +tup[1] for tup in bigrams]
    grams = tokens + bigrams
    
    for t in grams:
        features['contains(%s)' % t] = 1.0
        
def sent_feature(features,sentence):
   
    sentence_sentiment = exp_replace.replace_emo(sentence)
    tokens = nltk.word_tokenize(sentence_sentiment)
    tokens = [(t.lower()) for t in tokens] 
    
    mean_sentiment = sentiments.score_sentence(tokens)
    features['Positive sentiment'] = mean_sentiment[0]
    features['Negative sentiment'] = mean_sentiment[1]
    
    #TextBlob sentiment analysis
    try:
        blob = TextBlob("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip())
        features['Blob sentiment'] = blob.sentiment.polarity
        features['Blob subjectivity'] = blob.sentiment.subjectivity
    except:
        features['Blob sentiment'] = 0.0
        features['Blob subjectivity'] = 0.0
    
    #Split in 2
    if len(tokens)==1:
        tokens+=['.']
    f_half = tokens[0:len(tokens)/2]
    s_half = tokens[len(tokens)/2:]
    
    
    mean_sentiment_f = sentiments.score_sentence(f_half)
    features['Positive sentiment 1/2'] = mean_sentiment_f[0]
    features['Negative sentiment 1/2'] = mean_sentiment_f[1]
    
    mean_sentiment_s = sentiments.score_sentence(s_half)
    features['Positive sentiment 2/2'] = mean_sentiment_s[0]
    features['Negative sentiment 2/2'] = mean_sentiment_s[1]

     #TextBlob sentiment analysis
    try:
        blob = TextBlob("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in f_half]).strip())
        features['Blob sentiment 1/2'] = blob.sentiment.polarity
        features['Blob subjectivity 1/2'] = blob.sentiment.subjectivity
    except:
        features['Blob sentiment 1/2'] = 0.0
        features['Blob subjectivity 1/2'] = 0.0
    try:
        blob = TextBlob("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in s_half]).strip())
        features['Blob sentiment 2/2'] = blob.sentiment.polarity
        features['Blob subjectivity 2/2'] = blob.sentiment.subjectivity
    except:
        features['Blob sentiment 2/2'] = 0.0
        features['Blob subjectivity 2/2'] = 0.0

    #Split in 3
    if len(tokens)==2:
        tokens+=['.']
    f_half = tokens[0:len(tokens)/3]
    s_half = tokens[len(tokens)/3:2*len(tokens)/3]
    t_half = tokens[2*len(tokens)/3:]
    
    mean_sentiment_f = sentiments.score_sentence(f_half)
    features['Positive sentiment 1/3'] = mean_sentiment_f[0]
    features['Negative sentiment 1/3'] = mean_sentiment_f[1]
    
    mean_sentiment_s = sentiments.score_sentence(s_half)
    features['Positive sentiment 2/3'] = mean_sentiment_s[0]
    features['Negative sentiment 2/3'] = mean_sentiment_s[1]
    
    mean_sentiment_t = sentiments.score_sentence(t_half)
    features['Positive sentiment 3/3'] = mean_sentiment_t[0]
    features['Negative sentiment 3/3'] = mean_sentiment_t[1]
    
    #TextBlob sentiment analysis
    try:
        blob = TextBlob("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in f_half]).strip())
        features['Blob sentiment 1/3'] = blob.sentiment.polarity
        features['Blob subjectivity 1/3'] = blob.sentiment.subjectivity
    except:
        features['Blob sentiment 1/3'] = 0.0
        features['Blob subjectivity 1/3'] = 0.0
    try:
        blob = TextBlob("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in s_half]).strip())
        features['Blob sentiment 2/3'] = blob.sentiment.polarity
        features['Blob subjectivity 2/3'] = blob.sentiment.subjectivity
    except:
        features['Blob sentiment 2/3'] = 0.0
        features['Blob subjectivity 2/3'] = 0.0
    try:
        blob = TextBlob("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in t_half]).strip())
        features['Blob sentiment 3/3'] = blob.sentiment.polarity
        features['Blob subjectivity 3/3'] = blob.sentiment.subjectivity
    except:
        features['Blob sentiment 3/3'] = 0.0
        features['Blob subjectivity 3/3'] = 0.0
    
def pos_feature(features,sentence):
    
    sentence_pos = exp_replace.replace_emo(sentence)
    tokens = nltk.word_tokenize(sentence_pos)
    tokens = [(t.lower()) for t in tokens] 
    pos_vector = sentiments.posvector(tokens)
    for j in range(len(pos_vector)):
        features['POS' + str(j+1)] = pos_vector[j]
        
def cap_feature(features,sentence):
    counter = 0
    treshold = 4
    for j in range(len(sentence)):
        counter+=int(sentence[j].isupper())
    features['Capitalization'] = int(counter>=treshold)
    
def topic_feature(features,sentence,topic_modeler):
    
    topics = topic_modeler.transform(sentence)
    
    for j in range(len(topics)):
        features['Topic :' +str(topics[j][0])] = topics[j][1]
    
    