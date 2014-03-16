import re
import collections

word_expression = re.compile("<?/?[a-zA-Z]+>?")

f = open('input_ex4.txt','r')
initial_split = word_expression.findall(f.read())
f.close()

words = []

# filter out the "<...>"-words
for word in initial_split:
    if not (word[0]=="<" and word[len(word)-1] == ">"):
        words.append(word)

count = collections.Counter()
for i in range(0,len(words)-1):
    bigram = tuple(words[i:i+2])
    count[bigram] += 1

print("Please enter a threshold:")
threshold = input()

outfile = open('ouput_ex4.txt','w')
outfile.write("The following bigrams occur more than " + str(threshold) + " times: \n\n")
for bigram, frequency in count.most_common(len(count)):
    if frequency > threshold:
        outfile.write(str(frequency)+ ": \t\t"+str(bigram) + "\n")
outfile.close()