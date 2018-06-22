import MapReduce
import sys
from collections import *
from math import *
from nltk.corpus import PlaintextCorpusReader
import io

"""
Inverted Index for Vector Space model of Information Retrieval in the Simple Python
MapReduce Framework. Takes documents as input and create an index of tf-idf scores
for each term in the document.
"""

mr = MapReduce.MapReduce()

# =============================
corpus_root = './Data/books'
docs = PlaintextCorpusReader(corpus_root, '.*')
fields = docs.fileids()
number_of_documents  = len(fields)

def mapper(record):
    # record : [doc_id, doc_contents]
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    max_freq = 0
    word_freq = defaultdict(int)
    words = value.split()
    for w in words:
        word_freq[w] = word_freq[w] + 1      
    for w in words:
        if (word_freq[w] > max_freq):
            max_freq = word_freq[w]
        else:
            max_freq = max_freq
    #print max_freq
    for w in words:
        tf_norm = float(word_freq[w])/float(max_freq)
        mr.emit_intermediate(w,[key, tf_norm])

def reducer(key, list_of_values):
    # key: term
    # value: [doc_id, normalized term frequency]
    index = []
    count = 0
    for x in list_of_values:
        if not(x in index):
            index.append(x)
            count =  count + 1
    df = float(number_of_documents)/float(count)        
    idf = log(df, 2) 
    for y in index:
        y[1] = y[1]*idf
    mr.emit((key,count, index))
    
#output = [term, no of docs containing the term, tf-idf]

# # =============================
# def createIndex(file):
#     mr.execute(file, mapper, reducer)

readpath = './InvertedIndex/big_input.txt'
file = io.open(readpath, 'r', encoding = "utf16")
text = file.read()
# print(text)
mr.execute(text, mapper, reducer)

  
