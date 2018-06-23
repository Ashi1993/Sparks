# - *- coding: utf- 8 - *-
import nltk
from nltk import word_tokenize
from nltk .probability import FreqDist
from evaluateDoc import totalDoc
from evaluateDoc import evaluateDoc
from removestopwords import *
from itertools import islice
import math
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import MySQLdb

termfreq = evaluateDoc()

def calTF(doc, word, freq, total):
    TF = freq / total

    tree = ET.parse('TFvalues.xml')
    root = tree.getroot()

    items = "Null"

    for elem in root:
        # print(elem.attrib)
        if elem.attrib == doc:
            items = elem

    if items == "Null":
        items = ET.SubElement(root, 'book')
        items.set('name', doc)

    item1 = ET.SubElement(items, 'tfvalue')
    item1.set('name', word)
    item1.text = str(TF)

    # tree.write('TFvalues.xml')

    return TF


def calIDF(word):
    # print(word)
    D = totalDoc
    count = termfreq.get(word)
    # print(count)
    if count != None:
        N = len(count)
        IDF = math.log(D / N)
    else:
        IDF = 0
    return IDF


def calTFIDF(doc, word, freq, total):
    TF = calTF(doc, word, freq, total)
    IDF = calIDF(word)
    TFIDF = TF * IDF

    tree = ET.parse('TFIDFvalues3.xml')
    root = tree.getroot()

    items = "Null"

    for elem in root:
        # print(elem.attrib)
        if elem.attrib == doc:
            items = elem

    if items == "Null":
        items = ET.SubElement(root, 'book')
        items.set('name', doc)

    item1 = ET.SubElement(items, 'tfidfvalue')
    item1.set('name', word)
    item1.text = str(TFIDF)

    # tree.write('TFIDFvalues3.xml')

    return TFIDF

def keywordextraction(doc, wordlist):
    total = len(wordlist)
    wordlist = removestopwords(wordlist)
    wordlist = removepunc(wordlist)
    # print(wordlist)
    frequency = FreqDist(wordlist)
    # print(frequency)

    tfidf = {}
    db = MySQLdb.connect("localhost", "root", "root", "sparks", charset='utf8', use_unicode=True)
    cursor = db.cursor()

    for word in wordlist:
        # print(word)
        freq = frequency[word]
        #print(freq)
        TFIDF = calTFIDF(doc, word, freq, total)
        tfidf[word] = TFIDF
        # cursor.callproc('matchKeyword', [word])
        # cursor.execute("SELECT @_TEST_1")
        # row = cursor.fetchone()
        # print(row)
        # db.commit()

    tfidf = [(k, tfidf[k]) for k in sorted(tfidf, key=tfidf.get, reverse=True)]

    n_items = list(islice(tfidf, 15))
    return n_items

#
# readPath = './Data/books/වර්තමාන ලංකාව සහ ලොක ඉතිහාසය.txt'
# read_file = open(readPath, 'r', encoding="utf16")
# file = read_file.read()
# cleanr = re.compile('<.*?>')
# cleantext = re.sub(cleanr, '', file)
# list1 = word_tokenize(cleantext)
# # print(list1)
# keywordextraction('සන්ක්ශිප්ත ලන්කා ඉතිහාසය', list1)