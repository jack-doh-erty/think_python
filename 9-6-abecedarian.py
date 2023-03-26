# find abecedarian words where the letters are in alphabetical order

def is_abecedarian(word):
	prev = word[0]
	for letter in word:
		if prev > letter:
			return False
		prev = letter
	return True

abecedarian = []

for line in open('words.txt'):
	word = line.strip()
	if is_abecedarian(word):
		abecedarian.append(word)

print(max(abecedarian, key=len))
print(len(abecedarian))