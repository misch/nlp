#!/usr/bin/python

import re

expression = re.compile('.*a.*a.*a.*')

f = open('input_ex2.txt','r')

for line in f:
    matchObject = expression.match(line)
    if matchObject:
        print(line.strip())

f.close()