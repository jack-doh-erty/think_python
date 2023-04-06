# takes a string and prints the letters in decreasing order of frequency

# convert string to list
# create a dictionary of letter : count
# sort and return letters 

def most_frequent(t):
	result = {}
	for letter in t.lower():
		result[letter] = result.setdefault(letter, 0) + 1
	return sorted(result, key=result.get, reverse=True)
	#return result

def histogram(t):
	# take a string and return a dict of letter : count 
	result = {}
	for letter in t.lower():
		result[letter] = result.setdefault(letter, 0) + 1
	return result

def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()

emma = read_file('emma.txt')

hist = histogram(emma)
for letter in sorted(hist, key=hist.get, reverse=True):
	print(letter)