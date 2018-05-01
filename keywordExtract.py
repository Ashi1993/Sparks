# - *- coding: utf- 8 - *-
import nltk
# import tensorflow as tf
from nltk import word_tokenize
from nltk .probability import FreqDist
from evaluateDoc import totalDoc
from evaluateDoc import termfreq
# from wordstemming import stemwords
from removestopwords import *
from itertools import islice
import math
import MySQLdb

db = MySQLdb.connect("localhost","root","root","test1", charset='utf8', use_unicode=True)
cursor = db.cursor()

def calTF(doc, word, freq, total):
    TF = freq / total
    print(doc+" "+word+" "+str(TF))
    try:
        query = "INSERT INTO tfvalues (doc, word, tfval) VALUES ('%s', '%s', '%f')" % (doc, word, TF)
        # Execute the SQL command
        cursor.execute(query)
        db.commit()

    except:
        print("Error: unable to fecth data")
    return TF

def calIDF(word):
    #print(word)
    D = totalDoc
    count = termfreq.get(word)
    N = len(count)
    IDF = math.log(D / N)
    return IDF

def calTFIDF(doc, word, freq, total):
    TF = calTF(doc, word, freq, total)
    IDF = calIDF(word)
    TFIDF = TF * IDF
    return TFIDF

def keywordextraction(doc, wordlist):
    #print(wordlist)
    total = len(wordlist)
    # wordlist = stemwords(wordlist)
    wordlist = removestopwords(wordlist)
    wordlist = removepunc(wordlist)
    print(wordlist)
    frequency = FreqDist(wordlist)
    # print(frequency)

    tfidf = {}

    for word in wordlist:
        freq = frequency[word]
        #print(freq)
        TFIDF = calTFIDF(doc, word, freq, total)
        tfidf[word] = TFIDF

    tfidf = [(k, tfidf[k]) for k in sorted(tfidf, key=tfidf.get, reverse=True)]

    print(tfidf)
    print("\n\nKEYWORDS")

    n_items = list(islice(tfidf, 10))
    for key, value in n_items:
        print(key)




readPath = './Data/Data/3-මලවාණේ මහ බළකොටුව.txt'
read_file = open(readPath, 'r', encoding="utf16")
file = read_file.read()
list1 = word_tokenize(file)
print(list1)
keywordextraction('සන්ක්ශිප්ත ලන්කා ඉතිහාසය', list1)