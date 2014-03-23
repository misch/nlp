#!/usr/bin/python
import re
import collections
import matplotlib.pyplot as plt
import numpy as np

##############
# Parse file #
##############
word_expression = re.compile("<?/?[a-zA-Z.,]+>?")

f = open('input_ex3.txt','r')
initial_split = word_expression.findall(f.read())
f.close()

words = []

# filter out the "<...>"-words
for word in initial_split:
    if not (word[0]=="<" and word[len(word)-1] == ">"):
        words.append(word)

##########################
# Count tokens and types #
##########################
number_of_word_tokens = len(words)
print("The text contains {} word tokens.".format(number_of_word_tokens))

count = collections.Counter()
for word in words:
    count[word] += 1

number_of_word_types = len(count)
print("The text contains {} word types.".format(number_of_word_types))

freq = []
n = 100
for word, frequency in count.most_common((n)):
    freq.append(frequency)

log_rank = [np.log(x) for x in range(1, n+1)]
log_frequency = [np.log(x) for x in freq]

#########
# Plots #
#########
plt.figure()
plt.plot(log_rank, log_frequency, 'xr')
plt.xlabel('log(rank)')
plt.ylabel('log(frequency)')

plt.figure()
plt.plot(range(1,101),freq)
plt.xlabel('rank')
plt.ylabel('frequency')
plt.show()