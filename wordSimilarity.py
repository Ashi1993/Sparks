# - *- coding: utf- 8 - *-
import nltk
import MySQLdb
from nltk.corpus import PlaintextCorpusReader
from removestopwords import *

encoding = "utf-8"

stemwords_list = {}
word_cluster ={}


def ngrams(input, n):
  # input = input.split(' ')
  input_new = []
  for letter in input:
      input_new.append(letter)
  # print(input_new)
  output = []
  x = len(input_new)
  # print(x)
  for i in range(x):
    if i == 0:
      for y in range(n+1):
        output.append(input[i:y])
    elif i > n:
        output.append(input[i:x])
    else:
        output.append(input[i:i + n])
  return output

ngram_list = {}

def checkWordSimilarity(file):
    # print(file)
    stemwords_list = {}
    word_cluster = {}
    list1 = word_tokenize(file)
    list = removestopwords(list1)
    for word in list:
        output = ngrams(word, 3)
        outputLen = len(output)
        for k, v in ngram_list.items():
            count = 0
            values = ngram_list[k]
            valueLen = len(values)
            for val in values:
                if output.count(val) > 0:
                    count = count + 1

            wt = (2 * count) / (outputLen + valueLen)
            if wt > 0.7 and wt< 1:
                stemwords_list[word] = k
                # print(word + " " + k)
        ngram_list[word] = output


    for k,v in stemwords_list.items():
        # print(k +" "+v)
        k_exist = word_cluster.get(k, "key")
        # print("k_exist")
        # print(k_exist)
        if k_exist != "key":
            if v not in k_exist:
                k_exist.append(v)
                # print("k_exist")
                # print(k_exist)

        else:
            v_exist = word_cluster.get(v, "key")
            # print("v_exist")
            # print(v_exist)
            if v_exist != "key":
                if k not in v_exist:
                    v_exist.append(k)
                    # print("v_exist")
                    # print(v_exist)
            else:
                nk = len(ngram_list[k])
                nv = len(ngram_list[v])
                if nk > nv:
                    word_cluster[v] = [k]
                else:
                    word_cluster[k] = [v]
                # print(word_cluster)

    # print(ngram_list)
    # print(ngram_list["ආණ්ඩුව"])
    # print(ngram_list["ආණ්ඩුවේ"])
    # print(stemwords_list)
    # print("\n\n")
    # print(word_cluster)

    return word_cluster


# corpus_root = './Data/Data'
# docs = PlaintextCorpusReader(corpus_root, '.*')
# fields = docs.fileids()
#
# for doc in fields:
#     # readPath = './Data/Data/' + doc
#     readPath = './Data/Data/කෝට්ටේ නරපතීන් සහ පෘතුගීසීහු.txt'
#     read_file = open(readPath, 'r', encoding="utf16")
#     file = read_file.read()
#     checkWordSimilarity(file)

# readPath = './Data/books/සංක්ෂිප්ත ලංකා ඉතිහාසය 2.txt'
# read_file = open(readPath, 'r', encoding="utf16")
# file = read_file.read()
# checkWordSimilarity(file)
