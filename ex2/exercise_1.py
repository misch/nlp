#!/usr/bin/python

import re

expression = re.compile('^(abc|acab|acabababc|ababab)$')

expression2 = re.compile('^(ab?c)$')

line = 'abc'


matchObject = expression2.match(line)
if matchObject:
    print(matchObject.group(0))
else:
    print("Not found.")
