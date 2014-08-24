""" This is the function which gets called by the button 'Test',
it takes a sentence and returns a percentage which describes how sarcastic
the input sentence is. """

import numpy as np
import pickle
import os
import feature_extract
import topic

fileObject1 = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vecdict.p'), 'r')
fileObject2= open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'classif.p'), 'r')

vec = pickle.load(fileObject1)
classifier = pickle.load(fileObject2)

fileObject1.close()
fileObject2.close()

topic_mod = topic.topic(model=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'topics.tp'),\
                        dicttp=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'topics_dict.tp'))

def tweetscore(sentence):
    
    features = feature_extract.dialogue_act_features(sentence,topic_mod)
    features_vec = vec.transform(features)
    score = classifier.decision_function(features_vec)[0]
    percentage = int(round(2.0*(1.0/(1.0+np.exp(-score))-0.5)*100.0))
    
    return percentage

    