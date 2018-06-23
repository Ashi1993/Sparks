# - *- coding: utf- 8 - *-
# import nltk
from nltk import word_tokenize

text ='<br> (1) මධුර සහ තිණ්ණචේලි දිස්ත‍්‍රික්ක වලින් විශාල කොටසකින් සංයුක්ත වුණු පාණ්ඩ්‍ය රාජධානිය පළමු කොට කොල්කායි නගරය ද පසුව මධුරා පුරය ද ප‍්‍රධාන කොට පැවැත්තේ ය.'

words= word_tokenize(text)
print(words)

for word in words:
    # U + 0022
    if word == '<':
        print("yes")

if '”' in words:
    print("oh yes")
