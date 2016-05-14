# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:30:04 2016

@author: navrajnarula

Code for final project

COMP 150 NLP @ Tufts
"""

# inspiration for algorithm: CS111 @ Boston University

# This is the baseline algorithm for generating a Markov
# chains/text based off of Wright's poetry.

import random

# filename: a string representing the name of a text file
# returns a dictionary of key-value pairs in which each key is a word
# ecnountered in the .txt file passed in

def create_dictionary(filename):
    
    file = open(filename, "r")
    text = file.read()
    file.close()

    words = text.split()
    d = {}
    
    # $ indicates the starting word
    current_word = "$"

    for next_word in words:
        
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
         
        # exclude ending words from starting sentences 
        if "." in next_word or "!" in next_word or "?" in next_word:
            current_word = "$"
        else:
            current_word = next_word
        
    return d
    
# dictionary: word transitions (i.e. create_dictionary)
# num: positive integer
# generates text of length n from dictionary

def generate_text(dictt, num):
    
    text = ""
    
    current_token = "$"

    for n in range(num):

        if "." in current_token or "!" in current_token or "?" in current_token:
            next_word = "$"

        else:
            # select random token to continue word sequence
            next_word = random.choice(dictt[current_token])
        current_token = next_word

        if next_word == "$":
           text += "" 
        else:
            text += (str(next_word,)+" ")
    
    return text
    
# intialize dictionary with filename
dictt = create_dictionary("rwright.txt")

# create 100 haikus by calling on generate_text function
def createHaikus():
    haikus = []
    for i in range(100):
        newHaiku = generate_text(dictt, 15)
        haikus.append(newHaiku)
    return haikus

# create list of haikus
    
haikuList = createHaikus()
               
# iterate over each haiku in the list and 
# write to the file specified in the function
def writeHaikus(haikuList):
    with open("genHaikusBaseline.txt", "w") as fp:
        count = 0
        for item in haikuList:
            fp.write("%s\n" % item)
            fp.write("\n")
            count += 1
        print "There are", count, "lines in your file."
      
# The main function will write the haikus out to a file titled: genHaikusBaseline.txt
# Please note that all haikus are on one line in this file
      
def main():
    
    # write haikus to file
    writeHaikus(haikuList)