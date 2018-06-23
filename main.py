# - *- coding: utf- 8 - *-
import nltk
from nltk import word_tokenize
from wordSimilarity import *
from summarization import *
from createIndex import *
import MySQLdb

def createSummary(bookid):
    db = MySQLdb.connect("localhost", "root", "root", "sparks", charset='utf8', use_unicode=True)
    cursor = db.cursor()
    s_id = bookid
    sql = "SELECT bookDetails.bookPath FROM bookDetails WHERE bookDetails.bookdetailID = " +bookid
    cursor.execute(sql)
    row = cursor.fetchone()
    readPath = row[0]
    # print(row[0])
    db.commit()

    read_file = open(readPath, 'r', encoding="utf16")
    file = read_file.read()
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', file)

    word_cluster = checkWordSimilarity(cleantext)

    words = word_tokenize(cleantext)

    for word in words:
        for key, value in word_cluster.items():
            values = word_cluster[key]
            if word in values:
                word.replace(word, key)

    book_summary = summarycreation(bookid, file, words)
    sql = 'INSERT INTO bookSummary VALUES ('+s_id+', '+bookid+',  "<p>'+book_summary+'</p>")'
    # cursor.execute(sql)
    db.commit()

    c_title = {}
    n = 0
    titles = re.findall(r'(<h4>(.*?)</h4>)', file)
    count = len(titles)
    for t in titles:
        c_title[n] = t[1]
        n+=1

    match = re.split(r'<h4>', file)

    cs_id = int(bookid+"0")
    c_id = int(bookid+"00")
    x=-1
    for m in match:
        matches = re.findall(r'(<h2>(.*?)</h2>)', m)
        if len(matches) >=1:
            continue
        else:
            if x!= count:
                x += 1
                cleanr = re.compile('<.*?>')
                cleantext = re.sub(cleanr, '', m)
                word_cluster = checkWordSimilarity(cleantext)

                words = word_tokenize(cleantext)

                for word in words:
                    for key, value in word_cluster.items():
                        values = word_cluster[key]
                        if word in values:
                            word.replace(word, key)

                chapter_summary = chaptersummarycreation(bookid, m, words)
                print(">......>>>>>" + str(c_id))
                sql = 'INSERT INTO ChapterSummary VALUES (' + str(cs_id) + ', ' + bookid + ', ' + str(c_id) + ', "<h4>' + str(c_title[x]) + '</h4>",  "<p>' + chapter_summary + '</p>")'
                # print(sql)
                # cursor.execute(sql)
                db.commit()

                paras = re.findall(r'(<p>(.*?)</p>)', m)
                ps_id = int(bookid + str(c_id)+"00")
                p_id = int(str(bookid)+str(c_id)+ "000")
                for para in paras:
                    print(para[1])
                    cleanr = re.compile('<.*?>')
                    cleantext = re.sub(cleanr, '', para[1])
                    para_word_cluster = checkWordSimilarity(cleantext)

                    parawords = word_tokenize(cleantext)

                    for word in parawords:
                        for key, value in para_word_cluster.items():
                            values = para_word_cluster[key]
                            if word in values:
                                word.replace(word, key)

                    paragraph_summary = paragraphsummarycreation(bookid, para[1], parawords)
                    print(paragraph_summary)
                    print(">......>>>>>"+str(ps_id))
                    sql = 'INSERT INTO ParagraphSummary VALUES (' + str(ps_id) + ', ' + bookid + ', ' + str(c_id) + ', ' + str(p_id) + ',  "<p>' + paragraph_summary + '</p>")'
                    # print(sql)
                    cursor.execute(sql)
                    db.commit()

                    ps_id += 1
                    p_id += 1

        cs_id +=1
        c_id +=1

createSummary("5")
