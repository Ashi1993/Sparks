# - *- coding: utf- 8 - *-
import nltk
# import tensorflow as tf
from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import re

taglist = []
wordswithoutstopwords = []


def removestopwords(words):
    words = removepunc(words)
    wordswithoutstopwords = []
    # print("removestopword")
    total = len(words)
    sortedwords = set(stopwords.words('sinhala'))
    # print(stopwords)
    i = 0
    while i < total:
        if words[i]  not in sortedwords:

            wordswithoutstopwords.append(words[i])
            #print("if")
        i += 1


    # print("stopwords")
    # print(wordswithoutstopwords)

    return wordswithoutstopwords



def removepunc(words):
    wordlist = []
    punclist = [".", ",", "?", "!", ";", ":", "-", "(", ")", "[", "]", "{", "}", "'", '"', "..."]

    for n in words:
        if n not in punclist:
            x = re.match("[0-9]", n)
            if x == None:
                wordlist.append(n)

    return wordlist

# readPath = './Data/ලංකාවේ පුරාවෘත්ත/3-මලවාණේ මහ බළකොටුව.txt'
# read_file = open(readPath,'r',encoding="utf16")
# file = read_file.read()
# words = word_tokenize(file)
# removestopwords(words)
