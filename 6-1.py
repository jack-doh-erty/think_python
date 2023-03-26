""" function that compares 2 values """

def compare(x,y):
	if x > y:
		return 1
	if x < y:
		return -1
	else:
		return 0

print(compare(3,2))
print(compare(2,3))
print(compare(3,3))
print(compare(3,-2))