#import numpy as np
from os import path
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

file = open('Shakespeare','r')
ReadFile = open('text.txt','r')
ReadFile_Contents = ReadFile.read()
# print (ReadFile_Contents)
ReadFile.close()
# if you want to use stopwords, here's an example of how to do this
stopwords = set(line.strip() for line in open('stop words'))
'''with open('stop words') as my_words:
  my_list = my_words.read().lower().splitlines()
print(my_list)'''
# create your data structure here.
wordcount = {}
# Instantiate a dictionary, and for every word in the file, add to
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation,
# and use case demiliters. The functions lower() and split() will be useful!

for word in file.read().lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("-", "")
    word = word.replace("'", "")
    word = word.replace(",", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace(";", "")
    word = word.replace(":", "")
    word = word.replace("_", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("~", "")
    word = word.replace("/", "")
    word = word.replace("$", "")
    word = word.replace("@", "")
    word = word.replace("\"", "")
    word = word.replace("\'", "")
    word = word.replace("", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
# del(wordcount['\xe2\x80\x9ci'])
# Shermol's Looping Method. Can we complete this method tho?
#  S_WordCount = {}
# for word in wordcount:
#     if len(S_WordCount) > 9:
#         for tester in S_WordCount:
#             if wordcount[word] > S_WordCount[tester]:
#                 del(S_WordCount[tester])
#                 S_WordCount[word] = wordcount[word]
#                 break
#     else:
#         S_WordCount[word] = wordcount[word]
# print S_WordCount

'''Working Sorting Method'''
def find_max_name(words):
    max_name = ""
    for term in words:
        if max_name != "":
            if words[max_name] < words[term]:
                max_name = term
        else:
            max_name = term
    return max_name
# print wordcount
# print ""


final_list = {}

Top_Word = 0
while Top_Word < 9:
    final_list[find_max_name(wordcount)] = wordcount[find_max_name(wordcount)]
    del(wordcount[find_max_name(wordcount)])
    Top_Word = Top_Word + 1

# print final_list


sorted_words = []

# for terms in final_list:
#     sorted_words.append(str(terms) + " : " + str(final_list[terms]))
#     sorted_words.sort()


# print sorted_words
# print find_max_name(wordcount)
# print wordcount[find_max_name(wordcount)]

for key, value in sorted(final_list.iteritems(), key=lambda (k,v): (v,k)):
    sorted_words.append("%s: %s" % (key, value))
#

sorted_words = sorted_words[::-1]
print sorted_words

# text = 'quick brown fox jumped over the lazy dog dog dog dog'
text = sorted_words
wordcloud = WordCloud().generate(ReadFile_Contents)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
