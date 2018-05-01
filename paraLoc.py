# - *- coding: utf- 8 - *-
import nltk
import tensorflow as tf
from nltk import sent_tokenize,word_tokenize

def getParaLoc(text):
    sentences = sent_tokenize(text)
    weightP = {}
    id = 1

    for sentence in sentences:
        total = len(sentences)
        linear = (total - id + 1)/total
        hyperbolic = (1/id)
        if id < ((total + 1) / 2):
            quadratic = 1 - ((2/(total - 1))*(id - 1))
        elif id > ((total + 1) / 2):
            quadratic = 1 - ((2 / (total - 1)) * (total - 1))
        elif id == ((total + 1) / 2):
            quadratic = 0.1

        weightP[id] = {
            "linear" : linear,
            "hyperbolic" : hyperbolic,
            "quadratic" : quadratic
        }
        id += 1

    n = 1
    while n < len(weightP):
        print(weightP[n])
        n += 1
    return weightP

# readPath = './D1test.txt'
# read_file = open(readPath,'r',encoding="utf16")
# file = read_file.read()
#
# getParaLoc(file)