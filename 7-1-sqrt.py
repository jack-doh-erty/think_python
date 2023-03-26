# estimate a square root

import math
from tabulate import tabulate

def sqrt(a):
	x = a / 2 # starting with a shit guess
	y = 0
	print(f'target: {math.sqrt(a)}')
	while True:
		print(x, y)
		y = (x + a/x) / 2
		if abs(y-math.sqrt(a)) < 0.000001:
			return y
		x = y

print(sqrt(10000))

def test_square_root(n):
	table = []
	table.append(['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'])
	table.append(['-', '-'*7, '-'*7,'-'*7,])
	for i in range(1,n+1):
		guess = sqrt(i)
		msqrt = math.sqrt(i)
		table.append([i, guess, msqrt, guess-msqrt])
	print(tabulate(table))

print(test_square_root(10))