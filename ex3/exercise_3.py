#!/usr/bin/python
s = "Keep it short and simple!"
n = 3

for i in range(0,len(s)-(n-1)):
    print(s.replace(' ','_')[i:i+n])