# Ackermann Function
# Exercise 6.2

def ackermann(m,n):
	print(f'a({m},{n})')
	if m == 0:
		print(f'returning {n} + 1')
		return n + 1
	if m > 0 and n == 0:
		print(f'a({m}-1, 1)')
		return ackermann(m-1, 1)
	if m > 0 and n > 0:
		print(f'a({m}-1, a({m}, {n} - 1))')
		return ackermann(m-1, ackermann(m, n-1))

print(ackermann(3,4))