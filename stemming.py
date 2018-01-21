# - *- coding: utf- 8 - *-
import nltk
import tensorflow as tf
from nltk import sent_tokenize,word_tokenize
from corpus import finalCorpus
import locale

def stemwords(wordlist):
    #print(wordlist)
    length = len(wordlist)
    #print(length)
    alpabet = "zyxwvutsrqponmlkjihgfedcba"
    inputList = ["cat", "dog", "ant", "zebra", "rat"]
    # new_list = sorted(inputList, key=lambda word: [alpabet.index(c) for c in word[0]])

readPath = './D1test.txt'
read_file = open(readPath, 'r', encoding="utf16")
file = read_file.read()
list1 = word_tokenize(file)
#print(list1)
stemwords(list1)