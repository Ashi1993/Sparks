# - *- coding: utf- 8 - *-
import nltk
import tensorflow as tf
from nltk import sent_tokenize,word_tokenize
from corpus import finalCorpus

taglist = []
wordswithoutstopwords = {}


def removestopwords(text):
    words = word_tokenize(text)
    total = len(words)
    i = 1
    keys = finalCorpus.keys()
    print(keys)
    while i < total:
        if words[i] in keys:
            print(words[i]+" in")
            value = finalCorpus[words[i]]
            if value in taglist:
                wordswithoutstopwords[words[i]] = value
        else:
            continue
            #print(words[i]+" not in")
        i += 1

    return wordswithoutstopwords

readPath = './D1test.txt'
read_file = open(readPath,'r',encoding="utf16")
file = read_file.read()
removestopwords(file)
