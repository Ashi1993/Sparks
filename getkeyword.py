# - *- coding: utf- 8 - *-
# import nltk
# from nltk import sent_tokenize,word_tokenize
from keywordExtract import *

def selectKeyWords(bookid, keywords , sent):
    count = 0
    tfidftotal = 0
    words = word_tokenize(sent)
    total = len(words)
    for word in words:
        # print("word "+ word)
        if word in keywords:
            # print("word == keyword")
            count +=1

            tree = ET.parse('TFIDFvalues.xml')
            root = tree.getroot()
            #
            for elem in root:
                # print(elem.attrib)
                if elem.attrib['name'] == bookid:
                    for subelem in elem:
            #         print(subelem.attrib['name'])
            #             print(subelem.text)
                        if subelem.attrib['name'] == word:
                            tfidf = subelem.text
                            # print(subelem.text)
            #
                            tfidftotal += float(tfidf)

    counttotal = count/total
    tfidftotalnew = tfidftotal/total
    weightK = (count + tfidftotal) / (2*total)

    # print(weightK)
    # print(counttotal)
    # print(tfidftotalnew)
    return weightK

# selectKeyWords('./Data/Data/3-මලවාණේ මහ බළකොටුව.txt', 'මල්වාණේ විසු පෘතුගිසි ජනරජවරුන්ගෙන් ඉතාමත් ප්‍රසිද්ධ වුයෙ කුස්තන්තිනු ද සා නම් සේනාපතියා ය.')