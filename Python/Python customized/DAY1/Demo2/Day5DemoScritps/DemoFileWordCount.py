'''
Created on 20-Feb-2017

@author: mohan.chinnaiah
'''

def countWords(filePath):

    file=open(filePath,'r');

    numberOfWords=0;
    words=[]

    for line in file:
        for word in line.split():
            numberOfWords+=1
            words+=word
     
    
    print(numberOfWords)
    #print(words)





countWords('c:/sfdclab/file.txt')