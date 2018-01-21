# - *- coding: utf- 8 - *-
import nltk
import tensorflow as tf
from nltk import word_tokenize
from nltk .probability import FreqDist
import math

N = 100
n = 10
def calTF(freq, total):
    TF = freq / total
    return TF

def calIDF(word):
    IDF = math.log(N/n)
    return IDF

def calTFIDF(word, freq, total):
    TF = calTF(freq, total)
    IDF = calIDF(word)
    TFIDF = TF * IDF
    return TFIDF

def keywordextraction(wordlist):
    print(wordlist)
    total = len(wordlist)
    frequency = wordlist.FreqDist()
    print(frequency)

    tfidf = {}

    for word, freq in frequency:
        print(word+" "+freq)
        TFIDF = calTFIDF(word, freq, total)
        tfidf[word] = TFIDF

    print(tfidf)



readPath = './D1test.txt'
read_file = open(readPath, 'r', encoding="utf16")
file = read_file.read()
list1 = word_tokenize(file)
#print(list1)
keywordextraction(list1)