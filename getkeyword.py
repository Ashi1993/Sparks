# - *- coding: utf- 8 - *-
# import nltk
# from nltk import sent_tokenize,word_tokenize
from keywordExtract import *

def selectKeyWords(doc, sent):
    readPath = doc
    keywords = []
    read_file = open(readPath, 'r', encoding="utf16")
    file = read_file.read()
    # words = word_tokenize(file)
    # keywords = keywordextraction(doc, words)
    count = 0
    words = word_tokenize(sent)
    total = len(words)
    for word in words:
        if word in keywords:
            count +=1
    weightK = count / total

    # print(weightT)
    return weightK
