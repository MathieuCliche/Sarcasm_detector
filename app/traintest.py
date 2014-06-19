import nltk
import numpy as np
from sklearn.utils import shuffle
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
import pickle


def dialogue_act_features(sentence):
    """
        Extracts a set of features from a message.
    """
    features = {}
    tokens = nltk.word_tokenize(sentence)
    for t in tokens:
        features['contains(%s)' % t.lower()] = True
    return features

print 'Pickling out'
pos_data=np.load('posproc.npy')
neg_data=np.load('negproc.npy')
print 'Number of  sarcastic tweets :', len(pos_data)
print 'Number of  non-sarcastic tweets :', len(neg_data)

print 'Feature eng'
# label set
cls_set = ['Non-Sarcastic','Sarcastic']
featuresets = [] 
alltweets=[]
for tweet in pos_data: 
    featuresets.append((dialogue_act_features(tweet),cls_set[1]))
    alltweets.append(tweet)
 
for tweet in neg_data: 
    featuresets.append((dialogue_act_features(tweet),cls_set[0]))
    alltweets.append(tweet)
alltweets=np.array(alltweets)
featuresets=np.array(featuresets)

targets=(featuresets[0::,1]=='Sarcastic').astype(int)
vec = DictVectorizer()
featurevec = vec.fit_transform(featuresets[0::,0])


#Saving the dictionnary vectorizer
file_Name = "vecdict.pkl"
fileObject = open(file_Name,'wb') 
pickle.dump(vec, fileObject)
fileObject.close()


basic_test=['I just love when you make me feel like shit','Life is odd','Just got back to the US !', "Isn'it great when your girlfriend dumps you ?", "I love my job !", 'I love my son !']
feature_basictest=[]
for tweet in basic_test: 
    feature_basictest.append(dialogue_act_features(tweet))
feature_basictest=np.array(feature_basictest) 
feature_basictestvec = vec.transform(feature_basictest)
 
print 'Feature splitting'
#Shuffling
order=shuffle(range(len(featuresets)))
alltweets=alltweets[order]
targets=targets[order]
featurevec=featurevec[order,0::]

#Spliting
size = int(len(featuresets) * .2) # 30% is used for the test set

tweettest = alltweets[:size]
trainvec = featurevec[size:,0::]
train_targets = targets[size:]
testvec = featurevec[:size,0::]
test_targets = targets[:size]

print 'Training'

classifier = LinearSVC()#
classifier.fit(trainvec,train_targets)

#Saving the classifier
file_Name = "classif.pkl"
fileObject = open(file_Name,'wb') 
pickle.dump(classifier, fileObject)
fileObject.close()

print 'Validating'

output = classifier.predict(testvec)

print classification_report(test_targets, output, target_names=cls_set)

print basic_test
print classifier.predict(feature_basictestvec)
print classifier.decision_function(feature_basictestvec)
