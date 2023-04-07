"""
Another cartalk puzzler
Find the longest word where 1 letter can be removed at a time and still form a valid word
For example, sprite, spite, spit, pit, it, I
"""

# take a word and find all the words formed by removing one letter - it's "children"
# A word is reducable if any of it's children are reducable, with an empty string as the base case
# store words and the reducable children that are known to be reducable

from inlist import word_list
from dict_search import word_dict

missing = ['a', 'i']
word_dict = word_dict()

for word in missing:
	word_dict[word] = 0

def find_children(word, word_dict):
	"""
	finds all the words with 1 fewer letter than the input word
	returns a dictionary of word : 0 of children
	"""
	children = {}
	for i in range(0, len(word)):
		child = word[:i] + word[i+1:]
		if child in word_dict:
			children[child] = 0
	return children

def is_reducable(word, word_dict, result=[]):
	result.append(word)
	if word in ['a', 'i']:
		return result
	children = find_children(word, word_dict)
	if len(children) == 0:
		return False
	for child in children:
		return is_reducable(child, word_dict, result)

if __name__ == '__main__':
	reducable = {}
	for word in word_dict:
		result = is_reducable(word, word_dict, result = [])
		if result:
			reducable[word] = result

	for value in sorted(reducable, key=len):
		print(len(value), value, reducable[value])

