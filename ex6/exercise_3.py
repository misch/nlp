#!/usr/bin/python

import re
import sys

# ensure that a command line parameter is given
if len(sys.argv) != 2:
    print("Please give a command line parameter.")
    sys.exit()

word_to_check = sys.argv[1]
alphabet = [chr(let) for let in range(ord('a'),ord('z')+1)]

# get dictionary
f = open('output_ex1.txt')
dict = set()
for word in f:
    dict.add(word.strip())
f.close()

proposals = set()

# case 1: one letter is missing
for idx in range(len(word_to_check)+1):
    for letter in alphabet:
        new_word = list(word_to_check.strip())
        new_word.insert(idx,letter)
        new_word = "".join(new_word)
        #print(new_word)
        if new_word in dict:
            proposals.add(new_word)


# case 2: 2 letters are interchanged
for idx in range(len(word_to_check.strip())-1):
    new_word = list(word_to_check.strip())

    # exchange letter with it's following one
    temp = new_word[idx]
    new_word[idx] = new_word[idx+1]
    new_word[idx+1] = temp
    new_word = "".join(new_word)
    if new_word in dict:
        proposals.add(new_word)

print(proposals)