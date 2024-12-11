from sympy import *

x =symbols('x')
f = 1/x
result = limit(f, x, oo)
print(result)

n = symbols('n')
f = (1 + (1/n)) ** n
result = limit(f, n, oo)

print(result)
print(result.evalf())
