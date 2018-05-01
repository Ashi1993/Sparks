# - *- coding: utf- 8 - *-
import nltk
#import tensorflow as tf
from nltk import sent_tokenize,word_tokenize
from removestopwords import removestopwords
import re

readPath = './Resources/Suffixes.txt'
read_file = open(readPath, 'r', encoding="utf16")
file = read_file.read()

suffixes = word_tokenize(file)
# print(suffixes)

def stemwords(wordlist):
    #print(wordlist)
    stemwords = {}
    stemmedwords = []
    stems = ["මල්වාන", "මල්වාණ", "යුද්ධය", "අගල", "අගළ"]
    wordlist1 = removepunc(wordlist)
    wordlist2 = removestopwords(wordlist1)
    print("Words after removing punctuations and numbers")
    print(wordlist2)
    wordlist3= sorted(wordlist2)
    length = len(wordlist3)
    #print(length)

    # for stem in stems:
    #     if wordlist3[0].startswith(stem):
    #         print(stem +" "+wordlist3[0])
    #         print(wordlist3[0].startswith(stem))
    #     else:
    #         print("out")
    #         print(wordlist3[0].startswith(stem))
    stemwords[wordlist3[0]] = wordlist3[0]
    i = 0
    while i < length:

        for stem in stems:
            if wordlist3[i].startswith(stem):
                stemwords[wordlist3[i]] = stem
                stemmedwords.append(stem)

            else:
                stemwords[wordlist3[i]] = checkSuffix(wordlist3[i])
                stemmedwords.append(checkSuffix(wordlist3[i]))
                stems.append(stemwords[wordlist3[i]])

        i += 1

    print(stemwords)

    return stemmedwords




def removepunc(words):
    wordlist = []
    punclist = [".", ",", "?", "!", ";", ":", "-", "(", ")", "[", "]", "{", "}", "'", '"', "..."]

    for n in words:
        if n not in punclist:
            x = re.match("[0-9]", n)
            if x == None:
                wordlist.append(n)

    return wordlist

def checkSuffix(word):
    for suffix in suffixes:
        if word.endswith(suffix):
            x = len(word)
            y = len(suffix)
            word_new = word.replace(suffix,"")
            stem1 = word_new
            break
        else:
            stem1 = word

    return stem1



# readPath = './Data/ලංකාවේ පුරාවෘත්ත/3-මලවාණේ මහ බළකොටුව.txt'
# read_file = open(readPath, 'r', encoding="utf16")
# file = read_file.read()
# list1 = word_tokenize(file)
# #print(list1)
# stemwords(list1)