# look for interlocking words
# e.g 'shoe' and 'cold' combine to make 'schooled'

# start with each word
# split into 2 alternating
# check if these are words

from inlist import search_bisection, word_list

def is_interlocking_word(word, word_list):
	first = word[::2]
	second = word[1::2]
	if search_bisection(first, word_list):
		if search_bisection(second, word_list):
			return True
	return False


if __name__ == '__main__':
	words = word_list()

	result = []

	for word in words:
		if is_interlocking_word(word, words):
			result.append([word])
			print(word)

	print(len(result), result.max())
