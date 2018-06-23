# - *- coding: utf- 8 - *-
import nltk
from nltk import *
import re
from nltk.corpus import PlaintextCorpusReader
import MySQLdb
from evaluateDoc import *
from removestopwords import *
import math

wordlist = []
corpus_root = './Data/books'
docs = PlaintextCorpusReader(corpus_root, '.*')

fields = docs.fileids()
totalDoc = len(fields)

db = MySQLdb.connect("localhost", "root", "root", "sparks", charset='utf8', use_unicode=True)
cursor = db.cursor()
sql = "SELECT * FROM PoSTag"
cursor.execute(sql)
result = cursor.fetchall()
for r in result:
    wordlist.append(r[1])

print(wordlist)
newlist = []

termfreq = evaluateDoc()

for doc in fields:
    words = []
    file = ""
    readPath = './Data/books/' + doc
    read_file = open(readPath, 'r', encoding="utf16")
    file = read_file.read()
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', file)

    words = word_tokenize(cleantext)
    words = removestopwords(words)

    for word in words:
        if word not in wordlist:
            newlist.append(word)


writePath = "./word.txt"
write_file = open(writePath, 'w', encoding="utf16")
for word in newlist:
    # print(w/ord)
    c = termfreq.get(word)
    if c != None:
       n = len(termfreq.get(word))
    else:
        n=0
    # print(word + " " + termfreq[word])
    # n = termfreq[word]
    write_file.write(word+"\n")