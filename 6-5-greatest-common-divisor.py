# Find the greatest common divisor

def gdr(a,b):
	if b == 0:
		print(f'returning {a}')
		return a
	else:
		print(f'returning gdr({b}, {a%b})')
		return gdr(b, a % b)

print(gdr(234,133))