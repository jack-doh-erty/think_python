# read a file, break each line into words with punctuation and whitespace removed
# covert to lowercase

import string
from homophone import word_dict

def read_words(filename):
	t = []
	fp = open(filename)
	skip_header(fp)
	for line in fp:
		for word in line.replace('-', ' ').split():
			word = word.strip(string.whitespace + string.punctuation)
			t.append(word.lower())
	return t

def skip_header(fp, start_line = '*** START OF'):
	# iterate through fp until the start line in reached
	for line in fp:
		if line.startswith(start_line):
			break

def count_words(word_list):
	words = {}
	for word in word_list:
		words[word] = words.get(word, 0) + 1
	return words

def subtract(d1, d2):
	# returns items in d1 that aren't in d2 as a dict
	res = {}
	for word in d1:
		if word not in d2:
			res[word] = None
	return res

def set_subtract(s1, s2):
	return s1 - s2

if __name__ == '__main__':

	filenames = ['crime_and_punishment.txt', 'emma.txt']
	dictionary_words = word_dict()

		
	for filename in filenames:
		word_list = read_words(filename)
		hist = count_words(word_list)

		print(type(set(word_list)))
		print(type(set(hist)))
		print(set(word_list) - set(hist))


		print(f'{filename} contains {sum(hist.values())} words of {len(hist)} distinct words')
		print(f'the top 20 most common words are:')
		for word in sorted(hist, key=hist.get, reverse=True)[:20]:
			print(word, hist[word], sep='\t')
		print(f'the words not in the dictionary are {subtract(word_list, dictionary_words).keys()}')
		print(f'Using set subtraction instead gives {set_subtract(set(word_list), set(hist))}')
