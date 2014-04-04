#!/usr/bin/python

from ex5.exercise_2 import Dictionary
import re

f = open('input_ex1.txt')
expression = re.compile('[ .,][a-zA-Z]{4}[ .,]')
initial_capacity = 500
dict = Dictionary(initial_capacity)

for line in f:
    words = expression.findall(line)
    for word in words:
        word = word.translate(None,'.,')
        try:
            dict.insert(word.strip())
        except Exception,e:
            pass # do nothing
f.close()

out = open('output_ex1.txt','w')
for word_list in dict.hash_table:
    for word in word_list:
        out.write(word+"\n")

out.close()
print(dict.hash_table)
print(dict.size())