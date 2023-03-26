"""function is_power
takes a, b and returns true if a is a power of b"""

def is_power(a,b):
	if a == b:
		return True
	if a % b == 0 and is_power(a/b, b):
		return True
	else:
		return False


print(is_power(17,2))