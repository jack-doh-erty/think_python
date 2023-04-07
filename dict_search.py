# Using a dict to quickly search a list of words
# compare against other search methods

from inlist import search_bisection, word_list
import time

def word_dict():
	t = {}
	for word in open('words.txt'):
		t[word.strip()] = 0
	return t

def find_word_in_dict(word, word_dict):
	return word_dict[word] == 0


if __name__ == '__main__':

	word_dict = word_dict()
	word_list = word_list()

	targets = ['adaxial', 'add', 'addaxes', 'bathroom', 'heaven', 'chocolate', 'nobody', 'here', 'happening', 'animal']

	# using dictionary
	start_time = time.time()
	for word in targets:
		find_word_in_dict(word, word_dict)
	print(f'using dict took {time.time() - start_time} seconds')
	
	# using bisection
	start_time = time.time()
	for word in targets:
		search_bisection(word, word_list)
	print(f'using bisection took {time.time() - start_time} seconds')





