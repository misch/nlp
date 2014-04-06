#!/usr/bin/python

import re

f = open('input_ex1.txt')
expression = re.compile('[ .,][a-zA-Z]{4}[ .,]')

words = set()
for line in f:
    matches = expression.findall(line)
    for word in matches:
        word = word.translate(None,'.,')
        words.add(word.strip().lower())
f.close()

out = open('output_ex1.txt','w')

for word in sorted(words):
    out.write(word+"\n")

out.close()