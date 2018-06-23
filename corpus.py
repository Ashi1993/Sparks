import glob
import json
from nltk.corpus import PlaintextCorpusReader


corpus_root = './Data/books'
docs = PlaintextCorpusReader(corpus_root, '.*')

writePath = './InvertedIndex/big_input.json'
write_file = open(writePath,'r',encoding="utf16")


for f in docs.fileids():
    record = {}
    readPath = './Data/books/' + f
    # print(readPath)
    read_file = open(readPath, 'r', encoding="utf16")
    file = read_file.read()
    record[f] = file

print(record)

data = json.dumps(record)
print(type(data))
print(data)

with open ("./InvertedIndex/big_input.json", 'w', encoding="utf16") as input:
    input.write(data)
    
#
# read_files = glob.glob("./Data/books/*.txt")
# print(read_files)
# for f in read_files:
#     input = open (f, 'r', encoding="utf16")
#     contents = input.read()
#     record = [f, contents]
#     print(json.dumps(record))