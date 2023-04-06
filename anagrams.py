# Read a word list and print a list of all the anagrams

# read each work and create a sorted string as key
# if the sorted key already exists, append the word, otherwise create a new list

from inlist import word_list

def anagram_sets(word_list):
	anagrams = {}
	results = {}
	for word in word_list:
		key = ''.join(sorted(word))
		if key not in anagrams:
			anagrams[key] = [word]
		else:
			anagrams[key].append(word)
	# return words with >1 anagram
	for key, value in anagrams.items():
		if len(value) > 1:
			results[key] = value
	return results


if __name__ == '__main__':
	anagram_sets = anagram_sets(word_list())

	# print sorted list of anagram sets
	for anagrams in sorted(anagram_sets.values(), key=len, reverse=True):
		print(len(anagrams), anagrams)


	# scrabble bingo with 8 letters, 7 in rack and 1 on the board
	seven_letter_anagrams = [v for v in anagram_sets.values() if len(v[0]) == 8]
	for anagrams in sorted(seven_letter_anagrams, key=len):
		print(len(anagrams), anagrams)



