import sys
import json
from collections import *
from math import *
import operator

"""
Returns the documents ordered by their relevance to a query.
Takes the inverted index and length vectors as input (which are computed offline).
Submit a query and the script computes the cosine similarity of tf-idf vectors of all documents
with the query vector. 
"""

#creates a dictionary of doc_ids and lengths and an empty dictionary of cosine scores
length_vectors = {}                     
#open the json file containg lengths of tf-idf vectors of all documents
# line = [doc_id, length_of_vector]
cosine_similarity = {}
# doc_lengths = open("./InvertedIndex/length.json", "r",encoding = "utf16")
with open("./InvertedIndex/length.json","r",encoding = "utf16") as f:
    doc_lengths = f.read()
data = json.loads(doc_lengths)
for key, value in data.items():
    doc_id = value[0]
    length = value[1]
    length_vectors[doc_id] = length
    cosine_similarity[doc_id] = 0

#creates a dictionary of words and the [doc, tf-idf]
Index = {}
#open the inverted index
# line = [word, [doc_id, tf-idf]]
# inverted_index = open("./InvertedIndex/index.json", "r",encoding = "utf16")
with open("./InvertedIndex/index.json","r",encoding = "utf16") as f:
    inverted_index = f.read()
data = json.loads(inverted_index)
for key, value in data.items():
    word =  value[0]
    count = value[1]
    docs = value[2]
    Index[word] = docs


#computes the cosine similarity
def relevance(query):
    similarity = {}
    query_vector = query.split(' ')
    indexkeys = Index.keys()
    for x in query_vector:
        if x in indexkeys:
            print("in")
            relevant_docs = Index[x]
            for d in relevant_docs:
                document = d[0]
                score = d[1]
                cosine_similarity[document] = cosine_similarity[document] + score
        else:
            print("not in")
    for y in cosine_similarity.keys():
        cosine_similarity[y] = float(cosine_similarity[y])/float(len(query_vector)*length_vectors[y])
    sorted_similarity = sorted(cosine_similarity.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_similarity

#Enter query
search_query = "දොස්තර රෝහල"
result = relevance(search_query)
for r in result:
    print(r)
    print(r[0])
