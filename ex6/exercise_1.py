#!/usr/bin/python

import re

f = open('input_ex1.txt')
expression = re.compile('[ .,][a-zA-Z]{4}[ .,]')

words = set()
for line in f:
    matches = expression.findall(line)
    for word in matches:
        word = word.translate(None,'.,')
        words.add(word.strip())
f.close()

out = open('output_ex1.txt','w')

for word in words:
    out.write(word+"\n")

out.close()