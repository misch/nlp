#!/usr/bin/python
# usage: python exercise_10.py 0 1 3 2
import sys
from exercise_7_8_9 import MyComplex
x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])

complex1 = MyComplex(x1,y1)
complex2 = MyComplex(x2,y2)

f = open('exercise_10_output.txt','w')

f.write("1st number: \t" + str(complex1)+"\n")
f.write("2nd number: \t" + str(complex2)+"\n")

addSubResult = complex1.AddSub(complex2)
f.write("Sum: \t \t" + str(addSubResult[0])+"\n")
f.write("Difference: \t" + str(addSubResult[1])+"\n")

f.close()


