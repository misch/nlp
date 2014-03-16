#!/usr/bin/python
import re

f = open('input_ex1.txt','r')

# Regex to match tags. The brackets are
# organized s.t. match-group 1 always
# contains the first word within the tag.
tag_expression = re.compile("</?(.*?)[ .*?>|>]")

# The first 2 lines contain the xml version and the root tag.
# This could perhaps be a bad assumption in general...
xml_version = f.readline().strip()
root_element = f.readline().strip()

tags = set()

for line in f:
        match = tag_expression.match(line)
        if match:
            tags.add(match.group(1))
f.close()

out = open('output_ex1.txt','w')

out.write("Root: " + root_element + "\n\n")
for tag in tags:
    out.write(tag + "\n")
out.close()