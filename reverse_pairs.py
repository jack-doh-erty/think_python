# look for instances of reverese pairs

from inlist import search_bisection, word_list

def is_reverse_pair(target, words):
	return search_bisection(target[::-1], words)

if __name__ == '__main__':
	words = word_list()

	for word in words:
		if is_reverse_pair(word, words):
			print(word, word[::-1])