# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:30:04 2016

@author: navrajnarula

Code for final project

COMP 150 NLP @ Tufts
"""

import random

# inspiration for algorithm: CS111 @ Boston University

# filename: a string representing the name of a text file
# returns a dictionary of key-value pairs in which each key is a word
# ecnountered in the .txt file passed in

def create_dictionary(filename):
    
    file = open(filename, "r")
    text = file.read()
    file.close()

    words = text.split()
    d = {}
    
    current_word = "$"

    for next_word in words:
        
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
            
        if "." in next_word or "!" in next_word or "?" in next_word:
            current_word = "$"
        else:
            current_word = next_word
        
    return d
    
# dictionary: word transitions (i.e. create_dictionary)
# num: positive integer
# generates text of length n from dictionary

def generate_text(dictt, num):
    
    current_token = "$"

    for n in range(num):

        if "." in current_token or "!" in current_token or "?" in current_token:
            next_word = "$"

        else:
            next_word = random.choice(dictt[current_token])
        current_token = next_word

        if next_word == "$":
           print
        else:
            print next_word, 
    print

        