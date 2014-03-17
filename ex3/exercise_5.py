#!/usr/bin/python
import re

word_expression = re.compile("<?/?[a-zA-Z.,]+>?")

f = open('input_ex4.txt','r')
initial_split = word_expression.findall(f.read())
f.close()

words = []

# filter out the "<...>"-words
for word in initial_split:
    if not (word[0]=="<" and word[len(word)-1] == ">"):
        words.append(word)

n = 10
outfile = open('output_ex5.txt','w')
france_regex = re.compile("france.?", re.IGNORECASE)
for i in range(1,len(words)):
    if france_regex.match(words[i]):
            context = words[max(i-n,0):min(i+n+1,len(words))]
            start_idx = 0
            end_idx = len(context)
            for count, thing in enumerate(context):
                if '.' in thing:
                    if count < n:
                        start_idx = count+1
                    else:
                        end_idx = count+1
                        break
            context = context[start_idx:end_idx]

            outfile.write(' '.join(context)+"\n")
outfile.close()