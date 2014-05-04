from pyparsing import *
import sys

if len(sys.argv) == 1:
    print('Please give a string as a command line argument to execute this script. A simple example could be "1 + 2".')
    exit()
else:
    s = sys.argv[1]
    print(s)
# in Ex 4, I kept this kind of abstract - here, however, it has to be very concrete
number = Word("0123456789")
variable = Word(alphas)

addExpression = Literal("+") | Literal("-")
multExpression = Literal("*") | Literal("/")

factor = number | variable
term = factor + multExpression + factor | factor

S = Forward()
S <<  term + ZeroOrMore(addExpression + S)

print(S.parseString(s))