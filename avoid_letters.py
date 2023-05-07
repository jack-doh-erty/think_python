# 9-3 avoid letters

import itertools

def avoid(word, forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True

forbidden = 'dhnsh'
total, no_letters = 0, 0

for line in open('words.txt'):
	total += 1
	word = line.strip()
	if avoid(word, forbidden):
		no_letters += 1

print(f'out of {total:,} words, {no_letters:,} do not contain any of the forbidden letters {forbidden}, which is {round(no_letters / total * 100, 1)}%')

# loop through all 5 letter combinations to find the smallest

def no_letters(forbidden):
	no_letters = 0
	for line in open('words.txt'):
		word = line.strip()
		if avoid(word, forbidden):
			no_letters += 1
	return no_letters

seed ='abcdefghijklmnopqrstuvwxyz' 
com_set = itertools.combinations(seed,5)

lowest = 130000

for combo in com_set:
	if no_letters(combo) < lowest:
		print(combo, lowest)
		lowest = no_letters(combo)
		answer = combo, lowest

print(answer)
