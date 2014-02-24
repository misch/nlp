#!/usr/bin/python

def fibonacci(number):
	fibonacci = []

	for n in range(number+1):
		if n <= 1:
			fibonacci.append(n)
		else:
			fibonacci.append(fibonacci[n-1] + fibonacci[n-2])
	return fibonacci


print('Please enter an integer number:')
n = input()

print('Fibonacci sequence:')
print(fibonacci(n))
