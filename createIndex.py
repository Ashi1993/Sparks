# - *- coding: utf- 8 - *-
import nltk
from nltk import word_tokenize
from keywordExtract import *

def createIndex(readPath, file):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', file)
    # print(cleantext)
    words = word_tokenize(cleantext)

    keywords = keywordextraction(readPath, words)
    # print(keywords)

    db = MySQLdb.connect("localhost", "root", "root", "sparks", charset='utf8', use_unicode=True)
    cursor = db.cursor()
    sql = "Select bookdetailID FROM bookDetails WHERE bookPath= '"+readPath+"' "
    cursor.execute(sql)
    row = cursor.fetchone()
    # print(row[0])
    db.commit()
    for key, value in keywords:
        # print(key)
        # sql1 = "INSERT INTO InvertedIndex (IndexID, IndexWord, MappedDoc) VALUES (NULL, 'තුමා', 10)"
        sql1 = "INSERT INTO InvertedIndex (IndexID, IndexWord, MappedDoc) VALUES (NULL, '" + key + "', '" + str(row[0]) + "')"

        # print(sql1)
        # cursor.execute(sql1)
        # db.commit()


# readPath = './Data/books/සෙන්කඩගලපුර ඉතිහාස.txt'
# read_file = open(readPath, 'r', encoding="utf16")
# file = read_file.read()
#
# createIndex('./Data/books/සෙන්කඩගලපුර ඉතිහාස.txt', file)