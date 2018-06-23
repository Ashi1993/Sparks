# - *- coding: utf- 8 - *-
import nltk
from nltk import sent_tokenize
from sentLoc import getSentLoc
from paraLoc import getParaLoc
from titlewords import *
from getkeyword import *
from itertools import islice

writePath = './Summary/විහාර වග විත්ති.txt'
write_file = open(writePath, 'w', encoding="utf16")

def summarycreation(bookid, file, words):
    sumSent = {}
    keywordlist = []
    match = re.findall(r'(<p>(.*?)</p>)', file)
    p_id = 1
    p_total = len(match)

    keywords = keywordextraction(bookid, words)
    for key, value in keywords:
        keywordlist.append(key)
    # print(keywordlist)

    titlewords = getTitleWords(bookid, "book")

    for m in match:
        weightP = getParaLoc(m[1], p_id, p_total)
        sentences = sent_tokenize(m[1])
        s_total = len(sentences)

        s_id = 1
        for sent in sentences:
            # print(sent)
            # print(weightP)
            weightL = getSentLoc(sent, s_id, s_total)
            # print(weightL)
            weightT = selectTitleWords(titlewords, sent)
            # print(weightT)
            weightK = selectKeyWords(bookid, keywordlist, sent)
            # print(weightK)

            totalWeight = weightP + weightL + weightT + weightK
            sumSent[sent] = totalWeight
            s_id += 1
        p_id += 1

    sumsent = [(k, sumSent[k]) for k in sorted(sumSent, key=sumSent.get, reverse=True)]
    sumsentnew = []
    for sent in sumsent:
        sentwords = word_tokenize(sent[0])
        # print(sentwords)
        if '”' not in sentwords and '``' not in sentwords and '?' not in sentwords and '!' not in sentwords and '<' not in sentwords:
            # print("not in")
            sumsentnew.append(sent)

    # print(sumsent)
    # print("\n\nbookSummaary")
    booksummary = ''

    n_items = list(islice(sumsentnew, 20))
    for key, value in n_items:
        # print(key)
        # write_file.write(key + " ")
        booksummary = booksummary+" "+key

    # print(booksummary)
    return str(booksummary)

def chaptersummarycreation(bookid, file, words):
    db = MySQLdb.connect("localhost", "root", "root", "sparks", charset='utf8', use_unicode=True)
    cursor = db.cursor()
    totalsent = len(sent_tokenize(file))
    sumSent = {}
    keywordlist = []
    match = re.findall(r'(<p>(.*?)</p>)', file)
    p_id = 1
    p_total = len(match)
    keywords = keywordextraction(bookid, words)
    for key, value in keywords:
        keywordlist.append(key)
    # print(keywordlist)

    titlewords = getTitleWords(bookid, "chapter")

    for m in match:
        # print(m)
        weightP = getParaLoc(m[1], p_id, p_total)
        # print(weightP)
        sentences = sent_tokenize(m[1])
        # print(sentences)
        s_total = len(sentences)

        s_id = 1
        for sent in sentences:
            # print(sent)
            # print(weightP)
            weightL = getSentLoc(sent, s_id, s_total)
            # print(weightL)
            weightT = selectTitleWords(titlewords, sent)
            # print(weightT)
            weightK = selectKeyWords(bookid, keywordlist, sent)
            # print(weightK)

            totalWeight = weightP + weightL + weightT + weightK
            sumSent[sent] = totalWeight
            s_id += 1
        p_id += 1

    sumsent = [(k, sumSent[k]) for k in sorted(sumSent, key=sumSent.get, reverse=True)]
    sumsentnew = []
    for sent in sumsent:
        sentwords = word_tokenize(sent[0])
        # print(sentwords)
        if '”' not in sentwords and '``' not in sentwords and '?' not in sentwords and '!' not in sentwords and '<' not in sentwords:
            # print("not in")
            sumsentnew.append(sent)
    # print(sumsent)
    print("\n\nchapterSummaary")
    chaptersummary = ''

    n_sent = round(totalsent * 0.3)
    n_items = list(islice(sumsentnew, n_sent))
    for key, value in n_items:
        # print(key)
        chaptersummary = chaptersummary + " " + key

    return str(chaptersummary)

def paragraphsummarycreation(bookid, para, parawords):
    keywordlist = []
    sumSent = {}
    keywords = keywordextraction(bookid, parawords)
    for key, value in keywords:
        keywordlist.append(key)

    titlewords = getTitleWords(bookid, "paragraph")

    sentences = sent_tokenize(para)
    # print(sentences)
    s_total = len(sentences)

    s_id = 1
    for sent in sentences:
        # print(sent)
        # print(weightP)
        weightL = getSentLoc(sent, s_id, s_total)
        # print(weightL)
        weightT = selectTitleWords(titlewords, sent)
        # print(weightT)
        weightK = selectKeyWords(bookid, keywordlist, sent)
        # print(weightK)

        totalWeight = weightL + weightT + weightK
        sumSent[sent] = totalWeight
        s_id += 1

    sumsent = [(k, sumSent[k]) for k in sorted(sumSent, key=sumSent.get, reverse=True)]
    sumsentnew = []
    for sent in sumsent:
        sentwords = word_tokenize(sent[0])
        # print(sentwords)
        if '”' not in sentwords and '``' not in sentwords and '?' not in sentwords and '!' not in sentwords and '<' not in sentwords:
            sumsentnew.append(sent)
    # print(sumsent)
    print("\n\nparagraphsummary")
    paragraphsummary = ''

    n_sent = round(s_total * 0.3)
    n_items = list(islice(sumsentnew, n_sent))
    for key, value in n_items:
        print(key)
        paragraphsummary = paragraphsummary + " " + key

    return str(paragraphsummary)

# readPath = './Data/books/වර්තමාන ලංකාව සහ ලොක ඉතිහාසය.txt'
# read_file = open(readPath, 'r', encoding="utf16")
# file = read_file.read()
# summarycreation('./Data/books/වර්තමාන ලංකාව සහ ලොක ඉතිහාසය.txt', file)