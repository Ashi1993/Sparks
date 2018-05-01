# - *- coding: utf- 8 - *-
import nltk
import tensorflow as tf
from nltk import sent_tokenize,word_tokenize

def selectTitleWords(text):
    titlewords = ["කෝට්ටේ", "නරපතීන්", "පෘතුගීසීහු", "පෘතුගීසින්", "පැමිණීම", "දොම්", "ලොරෝන්සොගේ", "ලංකා", "ගමනය"]

    sentences = sent_tokenize(text)
    weightT = {}
    id = 1
    for sentence in sentences:
        count = 0
        words = word_tokenize(sentence)
        total = len(words)
        for word in words:
            if word in titlewords:
                count +=1
        weight = count / total
        weightT[id] = {
            "count" : count,
            "total" : total,
            "weight" : weight
        }
        id +=1

    n=1
    while n < len(weightT):
        print(weightT[n])
        n+=1
    return weightT

# readPath = './D1test.txt'
# read_file = open(readPath,'r',encoding="utf16")
# file = read_file.read()
#
# selectTitleWords(file)