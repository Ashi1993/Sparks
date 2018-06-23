# - *- coding: utf- 8 - *-
import nltk
from nltk import sent_tokenize,word_tokenize
from removestopwords import *
import re
import MySQLdb

def getTitleWords(bookid, type):
    titlewords = []
    titles = []
    db = MySQLdb.connect("localhost", "root", "root", "sparks", charset='utf8', use_unicode=True)
    cursor = db.cursor()
    sql = "SELECT bookDetails.bookPath FROM bookDetails WHERE bookDetails.bookdetailID = " + bookid
    cursor.execute(sql)
    row = cursor.fetchone()
    readPath = row[0]
    print(row[0])
    db.commit()

    read_file = open(readPath, 'r', encoding="utf16")
    file = read_file.read()
    match = re.findall(r'(<h[0-9]>(.*?)</h[0-9]>)', file)
    match2 = re.findall(r'(<h2>(.*?)</h2>)', file)
    match3 = re.findall(r'(<h4>(.*?)</h4>)', file)
    for m2 in match2:
        # print(m2[1])
        titles.append(m2[1])

    for m3 in match3:
        # print(m3[1])
        titles.append(m3[1])
    # print(titles)
    for m in match:
        # print(m[1])
        words = word_tokenize(m[1])
        for word in words:
            if word.isnumeric() == False:
                titlewords.append(word)

    if type != "book":
        match4 = re.findall(r'(<h5>(.*?)</h5>)', file)
        for m in match4:
            # print(m3[1])
            titles.append(m[1])

    titlewords = removestopwords(titlewords)
    # print(titlewords)


    return titlewords


# getTitleWords('./Data/books/වර්තමාන ලංකාව සහ ලොක ඉතිහාසය.txt')