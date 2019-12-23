"""
Created on Thu Sep 05 09:56:48 2019

@author: matheuswagner
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

class FrequencyList:
    def __init__(self):
        self.stopwords=list()
        self.stopwords.extend(list(stopwords.words('english')))
        self.stopwords.extend(list(punctuation))
        self.documentList=list()
        self.vocabulary=set()

    #Adds a new document and tokenizes it  
    def addDocument(self,document):
        file=open(document,'r')
        sentence=file.read()
        sentence=sentence.lower()
        docX=word_tokenize(sentence)
        self.buildVocabulary(docX)
        file.close()

    #Removes all stopwords of the tokenized document
    def buildVocabulary(self,docX):
        docX=[word for word in docX if word not in self.stopwords]
        self.documentList.append(docX)
        self.vocabulary=self.vocabulary|set(docX)

    #Builds the frequency vector of each document and puts it in a list
    def buildFrequenciesList(self):
        fr_vector=[]
        frequencyList=[]
        for document in self.documentList:
            for term in self.vocabulary:
                fr_vector.append(document.count(term))
            frequencyList.append(fr_vector)
            fr_vector=[]
        return frequencyList
