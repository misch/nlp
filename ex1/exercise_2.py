#!/usr/bin/python

print('Please enter a string: ')
input_string = raw_input()

for letter in input_string[::-1]:
	print(letter)
