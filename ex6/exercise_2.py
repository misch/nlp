#!/usr/bin/python

import re

f = open('output_ex1.txt')
expression = re.compile('^[a-zA-Z]{4}$')
alphabet = [chr(let) for let in range(ord('a'),ord('z')+1)]

initial_dict = set()
for word in f:
    initial_dict.add(word.strip())
f.close()

f = open('english_dictionary.txt')
english_dict = set()
for line in f:
    matches = expression.findall(line)
    for word in matches:
        english_dict.add(word.strip())
f.close()

new_dict = set(initial_dict)

for word in initial_dict:
    for idx, character in enumerate(word):
        for letter in alphabet:
            new_word = list(word)
            new_word[idx] = letter
            new_word = "".join(new_word).lower()
            if new_word in english_dict:
                new_dict.add(new_word)

out = open('output_ex2.txt','w')

for word in sorted(new_dict):
    out.write(word+"\n")
out.close()