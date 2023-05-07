def uses_all(word, letters):
	return set(word).issuperset(set(letters))

all_vowels = []

for line in open('words.txt'):
	word = line.strip()
	if uses_all(word, 'aeiou'):
		all_vowels.append(word)

print(f'{len(all_vowels)} words contains all the vowels. The longest is {max(all_vowels, key=len)} and the first 5 are {all_vowels[:5]}')