"""
Created on Thu Sep 05 09:56:48 2019

@author: matheuswagner
"""

class SimilarityMeasures:
    def __init__(self, vector1, vector2):
        self.d1 = vector1
        self.d2 = vector2
        self.difference = []
        self.minimos=0
        self.maximos=0

    def differenceList(self):
        for i in range(len(self.d1)):
            self.difference.append(abs(self.d1[i] - self.d2[i]))
        
    def minMax(self):
        for i in range(len(self.d1)):
            self.minimos += min(self.d1[i],self.d2[i])
            self.maximos += max(self.d1[i],self.d2[i])
    
    '''Method created by Oghbaie and Mohammadi Zanjireh avaliable on 
    https://journalofbigdata.springeropen.com/track/pdf/10.1186/s40537-018-0163-2 
    '''
    def pdsm(self):
        pf=0.0
        af=0.0
        if self.minimos==0 and self.maximos==0:
            self.minMax()
        for i in range(0, len(self.d1)):
            if self.d1[i]!=0 and self.d2[i]!=0:
                pf+=1
            if self.d1[i]==0 and self.d2[i]==0:
                af+=1
        if self.maximos==0:
            self.maximos+=1
            self.minimos+=1
        a = (float(self.minimos)/float(self.maximos))
        b = ((pf+1)/((len(self.d1)-af)+1))
        return a*b

    def euclidianDistance(self):
        soma = 0
        for i in range(len(self.d1)):
            soma += (self.d1[i]-self.d2[i]) ** 2
        euclidian = soma ** (1/2)
        return euclidian

    def cosineSimilarity(self):
        top = 0
        bot = 0
        qd1 = 0
        qd2 = 0
        for i in range(len(self.d1)):
            top += (self.d1[i] * self.d2[i])
            qd1 += self.d1[i] ** 2
            qd2 += self.d2[i] ** 2
        qd1 = qd1 ** (1/2)
        qd2 = qd2 ** (1/2)
        bot = qd1 * qd2
        return (top/bot)

    def manhattanDistance(self):
        if not self.difference:
            self.differenceList()
        return sum(self.difference)

    def chebyshevDistance(self):
        if not self.difference:
            self.differenceList()
        return max(self.difference)

    def jaccardCoeficient(self):
        if self.minimos==0 and self.maximos==0:
            self.minMax()
        return (self.minimos/self.maximos)

    def extendedJaccardCoeficient(self):
        top = 0
        bot = 0
        a = 0
        b = 0
        for i in range(len(self.d1)):
            top += self.d1[i]*self.d2[i]
            a += self.d1[i]*self.d1[i]
            b += self.d2[i]*self.d2[i]
        bot = a + b - top
        return (top/bot)