# - *- coding: utf- 8 - *-
import nltk
# import tensorflow as tf
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import PlaintextCorpusReader
from removestopwords import removestopwords

termfreq = {}
terms = []
corpus_root = './Data/books'
docs = PlaintextCorpusReader(corpus_root, '.*')

fields = docs.fileids()
totalDoc = len(fields)

def evaluateDoc():

    for doc in fields:
        # print(doc)
        words = []
        file = ""
        readPath = './Data/books/' + doc
        # print(readPath)
        read_file = open(readPath, 'r', encoding="utf16")
        file = read_file.read()

        words = word_tokenize(file)
        words = removestopwords(words)
        words2 = sorted(words)
        for word in words2:
            x = termfreq.get(word)
            # print(x)
            if x == None:
                termfreq.setdefault(word, []).append(doc)
            else:
                if doc not in x:
                    termfreq.setdefault(word, []).append(doc)

    # print("Evaluate doc")
    print(termfreq)

    return termfreq

