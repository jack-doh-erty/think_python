# Another cartalk puzzler
# Looking for words that are homophones when you remove the first or second letter

from pronounce import read_dictionary
from inlist import word_list

def homophones(word, pron_dict, word_dict):
	# has to be at least 3 chars and have a defined pronouciation
	if len(word) < 3 or word not in pron_dict:
		return None
	first = word[1:]
	second = word[0] + word[2:]
	if first in word_dict and second in word_dict and first in pron_dict and second in pron_dict:
		pron = pron_dict[word]
		if pron_dict[first] == 	pron:
			if pron_dict[second] == pron:
				print(word, first, second)
	return None

def word_dict():
	t = {}
	for word in open('words.txt'):
		t[word.strip()] = 0
	return t

if __name__ == '__main__':
	pron_dict = read_dictionary()
	results = []
	word_dict = word_dict()
	for word in word_dict:
		homophones(word, pron_dict, word_dict)


