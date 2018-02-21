# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:33:12 2018

@author: dgarciagarci
"""
#this is a change
#import
import collections
import io

f = io.open("98-0.txt", mode="r", encoding="utf-8")
#file=open("98-0.txt","r")
#file=open("mytxt.txt")
print("empiezo")
wordcount_dict ={}
wordcount_list =[]
wordcount_set = set()

for word in f.read().lower().split():
    wordcount_set.add(word)
    if word not in wordcount_list:
        wordcount_list.append(word)
    if word not in wordcount_dict:
        wordcount_dict[word] = 1
    else:
        wordcount_dict[word] += 1



print("numero en el dictionary=" + str(len(wordcount_dict)))
print("numero en la lista=" + str(len(wordcount_list)))
print("numero en set="+str(len(wordcount_set)))

d = collections.Counter(wordcount_dict)

#print(d.most_common(10))
for word, count in d.most_common(10):
	print(word, ": ", count)



#print(f.read(1))
#print("hola")
#print(f.read())
#word=file.readline()
#print(word)
