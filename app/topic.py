""" This class is a wrapper around the gensim LDA topic modeler. """

from gensim import corpora, models, similarities
import numpy as np
import nltk
import exp_replace
from nltk.corpus import stopwords

class topic(object):
    
    def __init__(self,nbtopic=100,alpha=1,model=None,dicttp=None):
        
        self.nbtopic = nbtopic
        self.porter = nltk.PorterStemmer()
        self.alpha = alpha
        self.stop = stopwords.words('english')+['.','!','?','"','...','\\',"''",'[',']','~',"'m","'s",';',':','..','$']
        if model!=None and dicttp!=None:
            self.lda = models.ldamodel.LdaModel.load(model)
            self.dictionary =  corpora.Dictionary.load(dicttp)

    def fit(self,documents):
        
        documents_mod = [exp_replace.replace_reg(sentence) for sentence in documents]
        tokens = [nltk.word_tokenize(sentence) for sentence in documents_mod]
        tokens = [[self.porter.stem(t.lower()) for t in sentence if t.lower() not in self.stop] for sentence in tokens]        
            
        self.dictionary = corpora.Dictionary(tokens)
        corpus = [self.dictionary.doc2bow(text) for text in tokens]
        self.lda = models.ldamodel.LdaModel(corpus,id2word=self.dictionary, num_topics=self.nbtopic,alpha=self.alpha)
        
        self.lda.save('topics.tp')
        self.dictionary.save('topics_dict.tp')
        
    def get_topic(self,topic_number):
        
        return self.lda.print_topic(topic_number)
    
    def transform(self,sentence):
        
        sentence_mod = exp_replace.replace_reg(sentence)
        tokens = nltk.word_tokenize(sentence_mod)
        tokens = [self.porter.stem(t.lower()) for t in tokens if t.lower() not in self.stop] 
        corpus_sentence = self.dictionary.doc2bow(tokens)
        
        return self.lda[corpus_sentence]  


