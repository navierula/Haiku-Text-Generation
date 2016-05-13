# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:27:37 2016

@author: navrajnarula

Code for final project

COMP 150 NLP @ Tufts
"""

# import libraries

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# These are the survey questions I encouraged participants to answer.
# Link to survey: https://docs.google.com/forms/d/1gFJoyH5MmeUkHRZTmixFD6SgORdm8JR0FQU0pznc9Hc/viewanalytics?usp=form_confirm


"""
Q1

To beak dawn chattering / A feet house in clang / The peach willow put
(written by program)

Q2

A bloody knife blade / Is being licked by a cat / At hog-killing time.
(written by Wright)

Q3

They smelt like roses / But when I put on the light / They were violets
(written by Wright)

Q4

To cockleburs forge stove / The sinking stones from evening / The sound pine shyly
(written by program)

Q5

To into spring cock / Which year table from rain / The sparrow solemnity trembling
(written by program)

Q6

To violets river crows / The blindman breath of island / The horn point startles
(written by program)

Q7

Spring begins shyly / With one hairpin of green grass / In a flower pot
(written by Wright)

Q8

To limping barn farm / The feel rain of violets / A tomorrow summer straightens
(written by program)

Q9

The Christmas season / A whore is painting her lips / Larger than they are.
(written by Wright)

Q10

Down evening ice becomes / A sawdust wind in rainstorm / The caw boy turning
(written by program)

"""

# read in the survey results
# 74 in total, at time of analysis
df = pd.read_csv("surveyResults.csv")

# isolate each column in the dataframe,
# according to attribute

# Answers to questions
Q1res = df["Q1"]
Q2res = df["Q2"]
Q3res = df["Q3"]
Q4res = df["Q4"]
Q5res = df["Q5"]
Q6res = df["Q6"]
Q7res = df["Q7"]
Q8res = df["Q8"]
Q9res = df["Q9"]
Q10res = df["Q10"]

# Answers to gender and age
gender = df["Gender"]
age = df["Age"]

# calculate the number of answers in which people selected that the haiku
# was written by wright, correct case
def calcCorrectWright(question):
    calcCorrect = sum([1 for item in question if item == "written by Wright"])
    return calcCorrect
    
# calculate the number of answers in which people selected that the haiku
# was written by wright, incorrect case    
def calcIncorrectWright(question):
    calcIncorrect = sum([1 for item in question if item == "written by Wright"])
    return calcIncorrect
  
# calculate the number of answers in which people selected that the haiku
# was written by the program, correct case   
def calcCorrectProgram(question):
    calcCorrect = sum([1 for item in question if item == "written by program"])
    return calcCorrect
    
# calculate the number of answers in which people selected that the haiku
# was written by the program, incorrect case 
def calcIncorrectProgram(question):
    calcIncorrect = sum([1 for item in question if item == "written by program"])
    return calcIncorrect
 

# determine how many people answered correctly
# and incorrectly for each of the 10 questions 
 
Q1correct = calcCorrectProgram(Q1res)
Q1incorrect = calcIncorrectWright(Q1res)

Q2correct = calcCorrectWright(Q2res)
Q2incorrect = calcIncorrectProgram(Q2res)

Q3correct = calcCorrectWright(Q3res)
Q3incorrect = calcIncorrectProgram(Q3res)

Q4correct = calcCorrectProgram(Q4res)
Q4incorrect = calcIncorrectWright(Q4res)

Q5correct = calcCorrectProgram(Q5res)
Q5incorrect = calcIncorrectWright(Q5res)

Q6correct = calcCorrectProgram(Q6res)
Q6incorrect = calcIncorrectWright(Q6res)

Q7correct = calcCorrectWright(Q7res)
Q7incorrect = calcIncorrectProgram(Q7res)

Q8correct = calcCorrectProgram(Q8res)
Q8incorrect = calcIncorrectWright(Q8res)

Q9correct = calcCorrectWright(Q9res)
Q9incorrect = calcIncorrectProgram(Q9res)

Q10correct = calcCorrectProgram(Q10res)
Q10incorrect = calcIncorrectWright(Q10res)

# determine the exact percentage in which overall participants answered 
# questions correctly
correctAns = [Q1correct, Q2correct, Q3correct, Q4correct, Q5correct, Q6correct, Q7correct, Q8correct, Q9correct, Q10correct]

correctAnsPercent = []
for item in correctAns:
    calc = float(item)/float(74)
    correctAnsPercent.append(calc)

avgCorrectAns = sum(correctAnsPercent)/len(correctAnsPercent)

# determine the exact percentage in which overall participants answered 
# questions incorrectly

incorrectAns = [Q1incorrect, Q2incorrect, Q3incorrect, Q4incorrect, Q5incorrect, Q6incorrect, Q7incorrect, Q8incorrect, Q9incorrect, Q10incorrect]

IncorrectAnsPercent = []
for item in incorrectAns:
    calc = float(item)/float(74)
    IncorrectAnsPercent.append(calc)

avgIncorrectAns = sum(IncorrectAnsPercent)/len(IncorrectAnsPercent)

# determine which question was answered the most correctly
def maxCorrect(correctAns):
    return max(correctAns), correctAns.index(max(correctAns)) + 1
    
# determine which question was answered the least correctly
def minCorrect(correctAns):
    return min(correctAns), correctAns.index(min(correctAns)) + 1

# determine which question was answered the most incorrectly   
def maxIncorrect(incorrectAns):
    return max(incorrectAns), incorrectAns.index(max(incorrectAns)) + 1
 
# determine which question was answered the least incorrectly    
def minIncorrect(incorrectAns):
    return min(incorrectAns), incorrectAns.index(min(incorrectAns)) + 1
    
# graph correct vs. incorrect in pie chart for Q10 (answered most incorrectly)
def graphQ10(Q10correct, Q10incorrect):
    labels = "written by Wright", "written by program"
    sizes = [Q10incorrect, Q10correct]
    colors = ["tomato", "sage"]
    explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct="%1.1f%%", shadow=False, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis("equal")
    plt.title("\nDown evening ice becomes / A sawdust wind in rainstorm / The caw boy turning\n")
    fig = plt.figure()
    return fig
 
# graph correct vs. incorrect in pie chart for Q7 (answered most correctly)   
def graphQ7(Q7correct, Q7incorrect):
    labels = "written by Wright", "written by program"
    sizes = [Q7correct, Q7incorrect]
    colors = ["tomato", "sage"]
    explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct="%1.1f%%", shadow=False, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis("equal")
    plt.title("\nSpring begins shyly / With one hairpin of green grass / In a flower pot\n")
    fig = plt.figure()
    return fig
    
# collect statistics in order to make a pie chart
# displaying how many men and women answered 
# Q7 correctly or incorrectly
 
countFemaleCorrect7 = [] 
ageFemaleCorrect7 = []

countMaleCorrect7 = [] 
ageMaleCorrect7 = []

countFemaleInCorrect7 = [] 
ageFemaleIncorrect7 = []


countMaleIncorrect7 = []  
ageMaleIncorrect7 = []

for i, j, k in zip(Q7res, gender, age):
    
    if j == "Female" and i == "written by Wright":
        countFemaleCorrect7.append("1")
        ageFemaleCorrect7.append(k)
          
    if j == "Male" and i == "written by Wright":
        countMaleCorrect7.append("1")
        ageMaleCorrect7.append(k)
        
    if j == "Female" and i == "written by program":
        countFemaleInCorrect7.append("0")
        ageFemaleIncorrect7.append(k)
        
    if j == "Male" and i == "written by program":
        countMaleIncorrect7.append("0")
        ageMaleIncorrect7.append(k)
        
# collect statistics in order to make a pie chart
# displaying how many men and women answered 
# Q10 correctly or incorrectly
        
countFemaleCorrect10 = [] 
ageFemaleCorrect10 = []

countMaleCorrect10 = [] 
ageMaleCorrect10 = []

countFemaleInCorrect10 = [] 
ageFemaleIncorrect10 = []


countMaleIncorrect10 = []  
ageMaleIncorrect10 = []

for i, j, k in zip(Q10res, gender, age):
    
    if j == "Female" and i == "written by Wright":
        countFemaleCorrect10.append("1")
        ageFemaleCorrect10.append(k)
          
    if j == "Male" and i == "written by Wright":
        countMaleCorrect10.append("1")
        ageMaleCorrect10.append(k)
        
    if j == "Female" and i == "written by program":
        countFemaleInCorrect10.append("0")
        ageFemaleIncorrect10.append(k)
        
    if j == "Male" and i == "written by program":
        countMaleIncorrect10.append("0")
        ageMaleIncorrect10.append(k)
        
# generate gender-based pie chart for Q7            
def graphQ7Gender(countMaleCorrect7, countMaleIncorrect7, countFemaleCorrect7, countFemaleInCorrect7):
    labels = "male correct", "male incorrect", "female correct", "female incorrect"
    sizes = [len(countMaleCorrect7), len(countMaleIncorrect7), len(countFemaleCorrect7), len(countFemaleInCorrect7)]
    colors = ["paleturquoise", "darkturquoise", "lightpink", "palevioletred"]
    explode = (0, 0, 0, 0)  

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct="%1.1f%%", shadow=False, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis("equal")
    plt.title("\nSpring begins shyly / With one hairpin of green grass / In a flower pot\n")
    fig = plt.figure()
    return fig       

# generate gender-based pie chart for Q10
def graphQ10Gender(countMaleCorrect10, countMaleIncorrect10, countFemaleCorrect10, countFemaleInCorrect10):
    labels = "male correct", "male incorrect", "female correct", "female incorrect"
    sizes = [len(countMaleCorrect10), len(countMaleIncorrect10), len(countFemaleCorrect10), len(countFemaleInCorrect7)]
    colors = ["paleturquoise", "darkturquoise", "lightpink", "palevioletred"]
    explode = (0, 0, 0, 0) 

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct="%1.1f%%", shadow=False, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis("equal")
    plt.title("\nDown evening ice becomes / A sawdust wind in rainstorm / The caw boy turning\n")
    fig = plt.figure()
    return fig       
  
# calculate the age ranges of men and women
# who participated in answering Q7
# utilized control flow and min and max functions
    
minMaleCorrect7 = min(ageMaleCorrect7)
maxMaleCorrect7  = max(ageMaleCorrect7)
minMaleIncorrect7 = min(ageMaleIncorrect7)
maxMaleIncorrect7 = max(ageMaleIncorrect7)

minAgeMale7 = 0
if minMaleCorrect7 < minMaleIncorrect7:
    minAgeMale7 = minMaleCorrect7
else:
    minAgeMale7 = minMaleIncorrect7
    
maxAgeMale7 = 0
if maxMaleCorrect7 > maxMaleIncorrect7:
    maxAgeMale7 = maxMaleCorrect7
else:
    maxAgeMale7 = maxMaleIncorrect7

minFemaleCorrect7 = min(ageFemaleCorrect7)
maxFemaleCorrect7  = max(ageFemaleCorrect7)
minFemaleIncorrect7 = min(ageFemaleIncorrect7)
maxFemaleIncorrect7 = max(ageFemaleIncorrect7)

minAgeFemale = 0
if minFemaleCorrect7 < minFemaleIncorrect7:
    minAgeFemale7 = minFemaleCorrect7
else:
    minAgeFemale7 = minFemaleIncorrect7
    
maxAgeFemale7 = 0
if maxFemaleCorrect7 > maxFemaleIncorrect7:
    maxAgeFemale7 = maxFemaleCorrect7
else:
    maxAgeFemale7 = maxFemaleIncorrect7
    
# (same as above^), but for Q10
# These are will yield the same results as for Q7 above,
# redid calculations to encourage clarity among variable
# names while calling on them in the main function

minMaleCorrect10 = min(ageMaleCorrect10)
maxMaleCorrect10  = max(ageMaleCorrect10)
minMaleIncorrect10 = min(ageMaleIncorrect10)
maxMaleIncorrect10 = max(ageMaleIncorrect10)

minAgeMale10 = 0
if minMaleCorrect10 < minMaleIncorrect10:
    minAgeMale10 = minMaleCorrect10
else:
    minAgeMale10 = minMaleIncorrect10
    
maxAgeMale10 = 0
if maxMaleCorrect10 > maxMaleIncorrect10:
    maxAgeMale10 = maxMaleCorrect10
else:
    maxAgeMale10 = maxMaleIncorrect10
      
minFemaleCorrect10 = min(ageFemaleCorrect10)
maxFemaleCorrect10  = max(ageFemaleCorrect10)
minFemaleIncorrect10 = min(ageFemaleIncorrect10)
maxFemaleIncorrect10 = max(ageFemaleIncorrect10)

minAgeFemale = 0
if minFemaleCorrect10 < minFemaleIncorrect10:
    minAgeFemale10 = minFemaleCorrect10
else:
    minAgeFemale10 = minFemaleIncorrect10
    
maxAgeFemale10 = 0
if maxFemaleCorrect10 > maxFemaleIncorrect10:
    maxAgeFemale10 = maxFemaleCorrect10
else:
    maxAgeFemale10 = maxFemaleIncorrect10

# The main function will display statistics from the survey
def main():
    
    # print statistics for overall survey
    print "\nA total of 74 people participted in the survey (link included in report).\n"
    print "\nOverall", round(avgCorrectAns,2)*100, "percent of participants answered correctly while " ,round(avgIncorrectAns,2)*100, "percent answered incorrectly."
    
    print "These are the questions people answered most and least accurately:\n"    
    print "People answered question", maxCorrect(correctAns)[1], "most accurately."
    print "People answered question", minCorrect(correctAns)[1], "least accurately.\n"
    print "or rather...\n"
    print "People answered question", maxIncorrect(incorrectAns)[1], "most inaccurately."
    print "People answered question", minIncorrect(incorrectAns)[1], "least inaccurately.\n"
    
    print "*****\n"
    
    # print statistics and graphs for Q7
    # this is the question people answered MOST accurately!
    print "Statistics for Q7:\n"
    print "Spring begins shyly / With one hairpin of green grass / In a flower pot\n"
    
    data = Counter(ageMaleCorrect7)
    data.most_common()  
            
    print "The range of men who participated in answering Q7 were between ages" ,minAgeMale7, "and", maxAgeMale7
    print "This includes a total of", len(countMaleCorrect7)+len(countMaleIncorrect7), "men"
    print "Most men who answered correctly were of age",data.most_common(1)[0][0]
    data = Counter(ageMaleIncorrect7)
    data.most_common()
    print "Most men who answered incorrectly were of age", data.most_common(1)[0][0]
    print
    print "The range of women who participated in answering Q7 were between ages" ,minAgeFemale7, "and", maxAgeFemale7
    print "This includes a total of", len(countFemaleCorrect7)+len(countFemaleInCorrect7), "men"
    print "Most women who answered correctly were of age",data.most_common(1)[0][0]
    data = Counter(ageFemaleIncorrect7)
    data.most_common()
    print "Most women who answered incorrectly were of age", data.most_common(1)[0][0]
    print
    print "*****\n"
        
    # print statistics and graphs for Q10
    # this is the question people answered LEAST accurately!
    print "Statistics for Q10:\n"
    print "Down evening ice becomes / A sawdust wind in rainstorm / The caw boy turning\n"
    data = Counter(ageMaleCorrect10)
    data.most_common() 
    
    print "The range of men who participated in answering Q10 were between ages" ,minAgeMale10, "and", maxAgeMale10
    print "This includes a total of", len(countMaleCorrect10)+len(countMaleIncorrect10), "men"
    print "Most men who answered correctly were of age",data.most_common(1)[0][0]
    data = Counter(ageMaleIncorrect10)
    data.most_common()
    print "Most men who answered incorrectly were of age", data.most_common(1)[0][0]
    print
    print "The range of women who participated in answering Q10 were between ages" ,minAgeFemale10, "and", maxAgeFemale10
    print "This includes a total of", len(countFemaleCorrect10)+len(countFemaleInCorrect10), "men"
    print "Most women who answered correctly were of age",data.most_common(1)[0][0]
    data = Counter(ageFemaleIncorrect10)
    data.most_common()
    print "Most women who answered incorrectly were of age", data.most_common(1)[0][0]
    print
    print "*****\n"
    
    # display pie charts for Q7 and Q10
    graphQ7(Q7correct, Q7incorrect)
    graphQ7Gender(countMaleCorrect7, countMaleIncorrect7, countFemaleCorrect7, countFemaleInCorrect7)
    graphQ10(Q10correct, Q10incorrect)
    graphQ10Gender(countMaleCorrect10, countMaleIncorrect10, countFemaleCorrect10, countFemaleInCorrect10)
    
if __name__ == "__main__": 
    main()