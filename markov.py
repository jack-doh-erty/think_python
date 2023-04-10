"""
Using Markov analysis to generate random text from an input
Output a dictionary that maps from prefixes to a collection of possible suffixes

"""

import random
from word_frequency import skip_header

def read_words(filename):
	t = []
	fp = open(filename)
	skip_header(fp)
	for line in fp:
		for word in line.replace('-', ' ').split():
			t.append(word)
	return t

def markov(text, n):
	"""
	Takes text and outputs a dictionary of prefixes and possible suffixes
	n is the length of the prefix
	"""

	res = {}

	for i in range(n,len(text)):
		prefix = tuple(text[i-n:i])
		suffix = text[i]
		if prefix in res:
			res[prefix].append(suffix)
		else:
			res[prefix] = [suffix]

	return res

def random_words(d, n):
	"""
	generate a random set of n words based on a markov dictionary d
	"""
	res = []

	# select an initial prefix and result
	prefix = random.choice(list(d.keys()))
	res.append(random.choice(d[prefix]))

	# from this, loop through the rest
	for i in range(n):
		previous = res[-1],
		prefix = prefix[1:] + previous
		suffix = random.choice(d[prefix])
		res.append(suffix)
	return ' '.join(res)

if __name__ == '__main__':
	words = read_words('emma.txt')
	markov = markov(words, 6)
	print(random_words(markov, 100))