#!/usr/bin/python

import re

expression = re.compile('^(abc|(a(b|c))+c?)$')
lines = ['abc','acab','acabababc','ababab','abcababc']

for line in lines:
    matchObject = expression.match(line)
    if matchObject:
        print(matchObject.group(0))
    else:
        print("Not found.")