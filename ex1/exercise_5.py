#!/usr/bin/python

swiss_websites = []

f = open('input_ex5.txt','r')

for line in f:
	line = line.strip()
	if line[len(line)-3:] == '.ch':
			swiss_websites.append(line)

f.close()
print(swiss_websites)
