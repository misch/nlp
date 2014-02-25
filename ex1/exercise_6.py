#!/usr/bin/python
import sys

def f(x):
	return g(x) + 1
     
def g(x):
	try:
		return 1/float(x)
	except ZeroDivisionError:
		print( "Oh god. 0 division? It's simple math...")
		sys.exit(1)     

### main 
print f(0)
