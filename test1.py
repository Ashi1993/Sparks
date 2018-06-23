# - *- coding: utf- 8 - *-
# import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import nltk
import re
from nltk.corpus import PlaintextCorpusReader
from nltk import sent_tokenize, word_tokenize
import MySQLdb

# tree = ET.parse('keywords.xml')
# root = tree.getroot()
#
# for elem in root:
#     print(elem.attrib)
#     for subelem in elem:
#         print(subelem.text)


#
# tree = ET.parse('TFvalues.xml')
# root = tree.getroot()
#
# for elem in root:
#     print(elem.attrib)
#     for subelem in elem:
#         print(subelem.attrib)
#         print(subelem.text)

# items = ET.SubElement(root, 'book')
# items.set('name','item1')
# item1 = ET.SubElement(items, 'tfvalue')
# item1.set('name','item1')
# item1.text = 'item1abc'
#
# tree.write('TFvalues.xml')
#
# for elem in root:
#     print(elem.attrib)
#     for subelem in elem:
#         print(subelem.attrib)
#         print(subelem.text)

corpus_root = './UCSC Sinhala Tagged Corpus V1/UCSC Sinhala Tagged Corpus V1'
docs = PlaintextCorpusReader(corpus_root, '.*')

fields = docs.fileids()
totalDoc = len(fields)

db = MySQLdb.connect("localhost","root","root","sparks", charset='utf8', use_unicode=True)
cursor = db.cursor()

writepath = "./Data/Data/corpusV.txt"
write_file = open(writepath, 'w', encoding="utf16")


x = 0
for n in fields:
    readpath = './UCSC Sinhala Tagged Corpus V1/UCSC Sinhala Tagged Corpus V1/' + n
    # print(readpath)
    read_file = open(readpath, 'r', encoding="utf16")
    file = read_file.read()
    match = re.split(r'<[/ A-Z a-z][A-Z a-z 0-9]*>', file)
    # print(match)

    text = []
    finalCorpus = {}
    for n in match:
        if n == "\n" or n == "\n\n" or n == '' or n == "\ufeff":
            continue
        else:
            text.append(n)
            lines = n.splitlines()
            for a in lines:
                if a == '':
                    continue
                else:
                    splitted = n.split(" ")
                    for split in splitted:
                        # print("n")
                        # print(split)
                        if split != ' ':
                            # write_file.write(split)
                            # write_file.write("\n")
                            entry = split.split("_")
                            if len(entry) > 1:
                                # print(entry[0])
                                key = entry[0]
                                value = entry[1]
                                finalCorpus[key] = value
                                if key.startswith('\n'):
                                    # print(key)
                                    key = key.replace('\n', '')
                                if value.find('\n') != -1:
                                    value= value.split("\n")[0]
                                    # print(key)
                                # print(key)
                                # sql = "SELECT Tag FROM PoSTag WHERE Word="+key
                                # # cursor.callproc('getTag', [key])
                                # cursor.execute(sql)
                                # row1 = cursor.fetchone()
                                # print(row1)
                                # if row1[0] == None:
                                #     print("inside")
                                try:
                                    cursor.callproc('adddata', (key, value))
                                    #     # print(sql)
                                    cursor.execute("SELECT @_TEST_1")
                                    row = cursor.fetchone()
                                    db.commit()
                                except:
                                    continue

                                # # print(row[0])
                                # db.commit()
                                # corpus_file.write(key + "\n")
                            else:
                                continue
x += 1

print(text)
# print(finalCorpus)