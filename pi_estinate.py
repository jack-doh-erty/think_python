""" Generate a numerical approximation of pi within 1e-15 of math value """

import math
from tabulate import tabulate

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

def approximate_pi():
	const = (2 * math.sqrt(2)) / 9801
	est = 0
	k = 0
	x = 0
	table = [['constant', 'estimate_of_pi', 'k', 'sum']]
	while abs(est - math.pi) > 1e-20:
		print(const, est, k, x)
		table.append([const, est, k, x])
		x += (factorial(4*k) * (1103 + 26390*k)) / (factorial(k)**4 * 396**(4*k))
		est = 1 / (const * x)
		k += 1
	print(tabulate(table))
	return est

print(approximate_pi())