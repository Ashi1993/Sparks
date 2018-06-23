# - *- coding: utf- 8 - *-
import nltk
from nltk import sent_tokenize,word_tokenize

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def getSentLoc(sent, id, total):
    weightL = (1/id)

    # print(weightL)

    return weightL

# readPath = './D1test.txt'
# read_file = open(readPath,'r',encoding="utf16")
# file = read_file.read()
#
# getSentLoc(file)