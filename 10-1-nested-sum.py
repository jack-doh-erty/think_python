# nested sum of a list of list of ints

def nested_sum(t):
	return sum([sum(item) for item in t])

example = [[1,2], [3], [4,5,6]]

print(nested_sum(example))
