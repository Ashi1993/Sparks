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
#print(suffixes)

def stemwords(wordlist):
    #print(wordlist)
    stemwords = {}
    stemmedwords = []
    wordlist1 = removepunc(wordlist)
    wordlist2 = removestopwords(wordlist1)
    wordlist3= sorted(wordlist2)
    length = len(wordlist3)
    print(wordlist3)
    #print(length)

    for suffix in suffixes:
        if wordlist3[0].endswith(suffix):
            print(suffix)
            word_new = wordlist[0].replace(suffix, "")
            stemwords[wordlist3[0]] = word_new
            print(stemwords[wordlist3[0]])
            wordlist3[0] = word_new
            break


        stemwords[wordlist3[0]] = wordlist3[0]
        print(stemwords[wordlist3[0]])

    i = 1
    while i < length:
        stem =  wordlist3[i-1]
        if wordlist3[i].startswith(stem):
            for suffix in suffixes:
                if wordlist3[i].endswith(suffix):
                    stemwords[wordlist3[i]] = stem
                    stemmedwords.append(stem)
                else:
                    stemwords[wordlist3[i]] = wordlist3[i]
                    stemmedwords.append(stem)

            else:
                stemwords[wordlist3[i]] = wordlist3[i]
                stemmedwords.append(stem)
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
            # word_new = word.replace(suffix,"")
            stem1 = ""
            break
        else:
            stem1 = word

    return stem1



readPath = './Data/ලංකාවේ පුරාවෘත්ත/3-මලවාණේ මහ බළකොටුව.txt'
read_file = open(readPath, 'r', encoding="utf16")
file = read_file.read()
list1 = word_tokenize(file)
#print(list1)
stemwords(list1)