# - *- coding: utf- 8 - *-
import nltk
import tensorflow as tf
from nltk import sent_tokenize,word_tokenize
from titlewords import selectTitleWords
from sentLoc import getSentLoc
from paraLoc import getParaLoc

readPath = './D1test.txt'
read_file = open(readPath,'r',encoding="utf16")
file = read_file.read()

def token():
    tokenized_sentences = sent_tokenize(file)
    # print(tokenized_sentences)

    tokenized_words = word_tokenize(file)

    




# T = selectTitleWords(file)
# print(T)
#
# L = getSentLoc(file)
# print(L)
#
# P = getParaLoc(file)
# print(P)
#
# fdist = FreqDist(tokenized_words)
#     n = len(fdist)
#     print(n)
#
#     x = 0
#     while x < n:
#         for y in fdist:
#             print(y + " " + str(fdist[y]))
#             x += 1
#             # fdist.plot()"""
