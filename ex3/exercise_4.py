import re
import collections

word_expression = re.compile("<?/?[a-zA-Z]+>?")

f = open('input_ex4.txt','r')
initial_split = word_expression.findall(f.read())
f.close()

words = []
for word in initial_split:
    if not (word[0]=="<" and word[len(word)-1] == ">"):
        words.append(word)

bigrams = []
count = collections.Counter()
for i in range(0,len(words)-1):
    bigram = tuple(words[i:i+2])
    bigrams.append(bigram)
    count[bigram] += 1

for lala, freq in count.most_common(len(count)):
    if freq > 200:
        print(str(lala)+ ": "+str(freq))

#print(len(bigrams_unique))


#print(initial_split[0:100])
#print(words[0:15])
#print(words[15:30])
#print(words[30:45])
#print(words[45:60])
#print(words[60:75])
#print(words[75:90])
#print(words[90:105])