#!/usr/bin/python

class MyComplex:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def __str__(self): # can be used by invoking "print(...)" on a MyComplex instance
		if (self.y >= 0):
			sign = "+"
		else:
			sign = ""
		return str(self.x) + "*i" + sign + str(self.y)
	def AddSub(self, complexNumber):
		add = MyComplex(self.x + complexNumber.x, self.y + complexNumber.y)
		sub = MyComplex(self.x - complexNumber.x, self.y - complexNumber.y)
		return (add,sub)
