#!/usr/bin/python

import re

# Ueh - found out that non-consuming regex-stuff;
# The '?=' makes non-consuming checking possible
dont_start_with_capital = '(?=[^A-Z])'  # make that check non-consuming using ?=
                                        # otherwise words starting with a number will not be excluded
                                        # because the number will be 'eaten' by [^A-Z]

at_least_6_letters_but_no_numbers = '^[^0-9]{6,}$'  # - From beginning (^) to end ($) the word should not contain any numbers.
                                                    # - A word contains more than 5 letters - i.e. from 6 up to arbitrary many letters.

expression = re.compile(dont_start_with_capital+at_least_6_letters_but_no_numbers)

f = open('input_ex5.txt','r')

numberOfWords = 0

for line in f:
    if len(line.strip()) != 0:  # only consider non-empty lines
        for word in line.split():
            word = word.translate(None,".,")    # remove dots and commas
            if expression.match(word):
                numberOfWords += 1
f.close()

print(numberOfWords)