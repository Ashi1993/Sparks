# - *- coding: utf- 8 - *-
import nltk
from nltk import sent_tokenize,word_tokenize
from getTitleWords import *

def selectTitleWords(titlewords, sent):
    count = 0
    words = word_tokenize(sent)
    total = len(words)
    for word in words:
        if word in titlewords:
            count +=1
    weightT = count / total

    # print(weightT)

    return weightT

# readPath = './D1test.txt'
# read_file = open(readPath,'r',encoding="utf16")
# file = read_file.read()
#
# selectTitleWords(file)