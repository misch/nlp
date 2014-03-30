#!/usr/bin/python

from exercise_2 import Dictionary
import re

f = open('input_ex3.txt')
expression = re.compile('[a-zA-Z]{3,}')
initial_capacity = 500
dict = Dictionary(initial_capacity)

for line in f:
    words = expression.findall(line)
    for word in words:
        try:
            dict.insert(word)
        except Exception,e:
            pass # do nothing
f.close()

total_collisions = 0
max_collisions_per_word = 0
collision_words = []
for string_list in dict.hash_table:
    if len(string_list) > 1:
        current = len(string_list) -1
        total_collisions += current
        if max_collisions_per_word < current:
            max_collisions_per_word = current

for string_list in dict.hash_table:
    if len(string_list) == max_collisions_per_word:
        collision_words.append(string_list)
        collision_words.append("\n")

percentage_empty = 100 - 100*(dict.size()/float(dict.capacity))

out = open('output_ex3.txt','w')
out.write("Initial capacity: {}\n".format(initial_capacity))
out.write("There were totally {} collisions.\n".format(total_collisions))
out.write("Final size of dictionary: {}\n".format(dict.size()))
out.write("Total capacity of the dictionary: {} (--> {}% empty)\n".format(dict.capacity, percentage_empty))
out.write("The maximal number of collisions for a word was {}. The following words collided:\n\n".format(max_collisions_per_word))
for string_list in collision_words:
    out.write(str(string_list))
out.close()