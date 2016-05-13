# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:14:22 2016

@author: navrajnarula

Code for final project

COMP 150 NLP @ Tufts
"""

# import libraries
import re
import nltk
from nltk.tag import pos_tag, map_tag
import random 
from nltk.corpus import cmudict
from collections import Counter

# initialize CMU pronounciation dictionary
d = cmudict.dict()

# relegate text files

rWright = "rWright.txt"
rWrightTagged = "rWrightTagged.txt"
generatedHaikus = "generatedHaikus.txt"

# tokenize each word in a file
def tokenize(filename):

    filename = open(filename, "r")
    # tokenize each work in .txt file
    text = []
    for line in filename:
        # to avoid issues with ASCII characters
        line = line.decode("utf-8")
        # avoid appending blank lines
        if len(line) > 1:
            line.rstrip('\n').split()
            text.append(nltk.word_tokenize(line))
    return text

# make tokens out of Wright's haikus
makeTokens = tokenize(rWright)

def tagTokens(makeTokens):
    tagged = []
    for item in makeTokens:
        tagged.append([(word, map_tag('en-ptb', 'universal', tag)) for word, tag in pos_tag(item)])
    return tagged
    
taggedWords = tagTokens(makeTokens)


def writeToFile():
    with open(rWrightTagged, "w") as fp:
        count = 0
        for line in taggedWords:
            for word in taggedWords:
                for item in word:
                    fp.write(str(item))
                    count += 1
        print "There are", count, "lines in your file."
        
        
outputFile = open(rWrightTagged, "r")

def createTuplesfromFile(outputFile):
    
   outputFile = open(rWrightTagged, "r")
   strings = ""
   for i in outputFile:
       strings += i       
   rx = re.compile(r"\(u'(.*?)'\,\su'(.*?)'\)")
   #Find all the matches
   matches = rx.findall(strings)
   tuples = []
   for match in matches:
       tuples.append(match)
   return tuples
    
wordTagPair = createTuplesfromFile(outputFile)

def countTags(wordTagPair):
   countTagList = []
   for item in wordTagPair:
       if item[1] not in countTagList and item[1] != ".":
           countTagList.append(item[1])
   return countTagList
   
def matchNOUN(wordTagPair):
    
   nouns = [x[0] for x in wordTagPair if "NOUN" in x]
   return nouns
   
def matchVERB(wordTagPair):
    
   verbs = [x[0] for x in wordTagPair if "VERB" in x]
   return verbs
    
def matchPRON(wordTagPair):
    
   pronouns = [x[0] for x in wordTagPair if "PRON" in x]
   return pronouns

def matchDET(wordTagPair):
    
   determiners = [x[0] for x in wordTagPair if "DET" in x]
   return determiners 

def matchADJ(wordTagPair):
    
   adjectives = [x[0] for x in wordTagPair if "ADJ" in x]
   return adjectives

def matchADV(wordTagPair):
    
   adverbs = [x[0] for x in wordTagPair if "ADV" in x]
   return adverbs  

def matchPRT(wordTagPair):
    
   particles = [x[0] for x in wordTagPair if "PRT" in x]
   return particles
   
def matchADP(wordTagPair):
    
   prepositions_postpositions = [x[0] for x in wordTagPair if "ADP" in x]
   return prepositions_postpositions
   
def matchCONJ(wordTagPair):
    
   conjunctions = [x[0] for x in wordTagPair if "CONJ" in x]
   return conjunctions
   
def matchNUM(wordTagPair):
    
   numerals = [x[0] for x in wordTagPair if "NUM" in x]
   return numerals

# counts the number of times the first comes before the latter
def patternRec(wordTagPair):
    return Counter((f, s) for (_, f), (_, s) in zip(wordTagPair, wordTagPair[1:]))
    
commonCounts = patternRec(wordTagPair)
    
def sortCommonCounts(commonCounts):
    x = sorted(commonCounts.items(), key=lambda i: i[1], reverse=True)
    #x = sorted(x)
    return x
   
def numSyllables(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
 
def generateHaiku(wordTagPair):
    
    haikuList = []    
    for i in range(100):
    
        lineOne = random.choice(matchDET(wordTagPair)).title()  \
        + " " + random.choice(matchNOUN(wordTagPair)).lower() + " " + random.choice(matchNOUN(wordTagPair)).lower() \
        + " " + random.choice(matchNOUN(wordTagPair)).lower()
    
        lineTwo = random.choice(matchPRT(wordTagPair)).title() + " " + random.choice(matchNOUN(wordTagPair)).lower()  \
        + " " + random.choice(matchNOUN(wordTagPair)).lower() + " " + random.choice(matchADP(wordTagPair)).lower() \
        + " " + random.choice(matchNOUN(wordTagPair)).lower()
    
        lineThree = random.choice(matchVERB(wordTagPair)).title()  \
        + " " + random.choice(matchNOUN(wordTagPair)).lower() + " " + random.choice(matchNOUN(wordTagPair)).lower() \
        + " " + random.choice(matchVERB(wordTagPair)).lower()
        
        haikuList.append([lineOne, lineTwo, lineThree])
    return haikuList
    
haikuList = generateHaiku(wordTagPair)
    
def writeHaikus(haikuList):
    with open(generatedHaikus, "w") as fp:
        fp.write('{}\n'.format('\n\n'.join(['\n'.join(haiku) for haiku in haikuList])))
        print "There are {} lines in your file.".format(len(haikuList)*3 + len(haikuList)-1)
    


