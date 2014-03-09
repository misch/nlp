#!/usr/bin/python

import re

expression = re.compile('([^(b|B)].*[0-9]{2}.*)|^[0-9]{2}')

f = open('input_ex3.txt','r')

for line in f:
    matchObject = expression.match(line)
    if matchObject:
        print(line.strip())

f.close()