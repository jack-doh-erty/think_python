# find a word using besection

import time
import bisect

# load words.txt into a list using append
def word_list():
	t = []
	for word in open('words.txt'):
		t.append(word.strip())
	return t

# search for a word using bisection
def search_bisection(target, words):
	"""
	Search for target in words using bisection.
	Words must be a sorted list
	Return the index of the word or None if the target doesn't exist
	"""
	if len(words) == 0:
		return False

	i = len(words) // 2 # floor division

	if words[i] == target:
		return True

	if words[i] > target:
		# word is in the first half
		return search_bisection(target, words[:i])
	else:
		# word is in the second half
		return search_bisection(target, words[i+1:])

def cheat_bisect(target, words):
	return bisect.bisect(words, target)


if __name__ == '__main__':
	words = word_list()
	print(words[:5])

	targets = ['arrow', 'scissors', 'sometimes', 'zebra']

	for target in targets:
		start_time = time.time()
		print(target in words)
		print(f'using in took {time.time() - start_time} seconds')

		start_time = time.time()
		print(search_bisection(target, words))
		print(f'using bisection took {time.time() - start_time} seconds')

		start_time = time.time()
		print(cheat_bisect(target, words))
		print(f'using module took {time.time() - start_time} seconds')