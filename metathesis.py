# 12-3: Metathesis pairs
# transform one word into another by swapping 2 letters e.g. converse and conserve

# must contain the same letters, so use anagrams
# zip together and compare values
# if only 2 letters are different, they are anagram pairs

from inlist import word_list
from anagrams import anagram_sets

def find_metathesis_pairs(anagrams_sets):
	"""
	Takes a list of anagram sets and returns a list of tuples of metathesis pairs
	"""
	pairs = []
	for anagrams in anagrams_sets:
		for word_1 in anagrams:
			for word_2 in anagrams:
				if word_1 == word_2:
					break
				count = 0
				for x, y in zip(word_1, word_2):
					if x != y:
						count += 1
				if count == 2:
					pairs.append((word_1, word_2))
	return pairs


if __name__ == '__main__':
	anagram_sets = anagram_sets(word_list())
	pairs = find_metathesis_pairs(anagram_sets.values())

	for a, b in pairs:
		print(a,b)

	print(f'there are {len(pairs)} metathesis pairs in the word list')

