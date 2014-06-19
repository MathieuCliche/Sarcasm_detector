import nltk
import numpy as np
import pickle

fileObject1 = open('vecdict.pkl','r')
fileObject2= open('classif.pkl','r') 
vec = pickle.load(fileObject1)
classifier = pickle.load(fileObject2)
fileObject1.close()
fileObject2.close()

def dialogue_act_features(sentence):
    """
        Extracts a set of features from a message.
    """
    features = {}
    tokens = nltk.word_tokenize(sentence)
    for t in tokens:
        features['contains(%s)' % t.lower()] = True
    return features

def tweetscore(sentence):
    
    features = dialogue_act_features(sentence)
    features_vec = vec.transform(features)
    score = classifier.decision_function(features_vec)[0]
    percentage = int(round(1.0/(1.0+np.exp(-score))*100.0))
    
    return percentage
    
#basic_test=['I just love when you make me feel like shit','Life is odd','Just got back to the US !', "Isn'it great when your girlfriend dumps you ?", "I love my job !", 'I love my son !']
#feature_basictest=[]
#for tweet in basic_test: 
#    feature_basictest.append(dialogue_act_features(tweet))
#feature_basictest=np.array(feature_basictest) 
#feature_basictestvec = vec.transform(feature_basictest)


#print classifier.decision_function(feature_basictestvec)