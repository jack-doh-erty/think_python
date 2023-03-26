""" returns the hypotenuse of a right angle triangle
given the lengths of the other 2 sides"""

import math

def hypotenuse(a,b):
	return math.sqrt(a**2 + b**2)

print(hypotenuse(3,4))

"""returns True if y is between x and z"""

def is_between(x,y,z):
	return x <= y <= z

print(is_between(1,2,2))

# fibonacci

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
	print(i, fibonacci(i))

