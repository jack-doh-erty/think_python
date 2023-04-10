"""
Import anagram sets and extends with 2 new functions:
store_anagrams to store the results in a "shelf"
read_anagrams to look up a word and return the list of anagrams
"""

from anagrams import anagram_sets
from inlist import word_list

import shelve
import sys

def store_anagrams(anagrams, filename='anagram_db'):
	"""
	stores a dictionary of anagrams in a "shelf"

	anagrams: a dict of anagrams
	filename: persistent storage
	"""

	d = shelve.open(filename)
	for key, value in anagrams.items():
		d[key] = value
	d.close()

def read_anagrams(key, filename='anagram_db'):
	"""
	reads a list of anagrams from a shelf

	anagrams: a dict of anagrams
	filename: persistent storage
	"""
	d = shelve.open(filename)
	try:
		res = d[key]
	except KeyError:
		return []
	return res

def main(script, command='make_db'):
	filename = 'anagram_db'
	if command == 'make_db':
		print(f'creating database {filename}')
		anagrams = anagram_sets(word_list())
		store_anagrams(anagrams, filename)
	else:
		print(f'finding anagrams for {command}')
		print(read_anagrams(''.join(sorted(command)), filename))

if __name__ == '__main__':
    main(*sys.argv)
