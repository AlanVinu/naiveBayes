from numpy import *

#Word list to vector function
def loadDataSet() :
    postingList = [['my','dog','has','flea','problems','help','please'],
                   ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute','I','love','him'],
                   ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0,1,0,1,0,1]  #1 implies abusive, 0 not
    return postingList, classVec

def createVocabList(dataSet) :
    vocabSet = set([])
    for document in dataSet :
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet) :
    returnVec = [0]*len(vocabList)
    for word in inputSet :
        if word in vocabList :
            returnVec[vocabList.index(word)] = 1
        else : print("The word: %s is not in my Vocabulary!" % word)
    return returnVec

#Naive Bayes classifier training function
def trainNB0(trainMatrix, trainCategory) :
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs) :
        if trainCategory[i] == 1 :
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else :
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)      #change to log()
    p0Vect = log(p0Num/p0Denom)      #change to log()
    return p0Vect, p1Vect, pAbusive

