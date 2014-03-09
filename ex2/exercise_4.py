#!/usr/bin/python

import re

expression = re.compile('[A-Z][^0-9]*\.[A-Z][^0-9]*@.+\.com')

f = open('input_ex4.txt','r')

for line in f:
    matchObject = expression.match(line)
    if matchObject:
        print(line.strip())

f.close()