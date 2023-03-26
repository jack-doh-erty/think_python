def b(z):
	prod = a(z, z)
	print(z, prod)
	return prod

def a(x, y):
	print(f'a inputs, x={x}, y={y}')
	x = x + 1
	print(f'a returning {x} * {y} as {y*x}')
	return x * y

def c(x, y, z):
	print(f'c inputs, x={x}, y={y}, z={z}')
	total = x + y + z
	print(f'total={total}')
	square = b(total)**2
	return square

x = 1
y = x + 1
print(c(x, y+3, x+y))