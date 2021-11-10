# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import defaultdict

word_dic =  defaultdict(int)

strng="there are so so so many colleges a around"

for word in strng.split(" "):
    word_dic[word] += 1
    
print(word_dic)