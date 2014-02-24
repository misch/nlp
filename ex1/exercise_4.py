#!/usr/bin/python
import sys

def factorial(number):
	factorial = 1
	
	for n in range(number):
		factorial = factorial * (n+1)

	return factorial


number = sys.argv[1]
try:
    number = int(number)
except ValueError:
    number = 0

fact = factorial(number)
print(str(number)+'! = '+ str(fact))
