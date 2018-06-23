# - *- coding: utf- 8 - *-
import nltk
from nltk import sent_tokenize,word_tokenize

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def getParaLoc(para, id, total):
    weightP = (total - id + 1)/total
    # print(weightP)

    return weightP

# readPath = './D1test.txt'
# read_file = open(readPath,'r',encoding="utf16")
# file = read_file.read()
#
# getParaLoc(file)