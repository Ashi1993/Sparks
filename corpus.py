# - *- coding: utf- 8 - *-
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import PlaintextCorpusReader
import re

corpus_root = './UCSC Sinhala Tagged Corpus V1/UCSC Sinhala Tagged Corpus V1'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

fields = wordlists.fileids()
#print(fields)

readPath = './corpus.txt'
corpus_file = open(readPath,'w',encoding="utf16")

x=0
for n in fields:
    readpath = './UCSC Sinhala Tagged Corpus V1/UCSC Sinhala Tagged Corpus V1/'+n
    #print(readpath)
    read_file = open(readpath, 'r', encoding="utf16")
    file = read_file.read()
    match = re.split(r'<[/ A-Z a-z][A-Z a-z 0-9]*>', file)
    #print(match)

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
                        entry = split.split("_")
                        if len(entry)>1:
                            #print(entry[0])
                            key = entry[0]
                            value = entry[1]
                            finalCorpus[key] = value
                            corpus_file.write(key+"\n")
                        else:
                            continue
x+=1

#print(finalCorpus)

