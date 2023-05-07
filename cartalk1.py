# word with 3 pairs of double letters

# at least 6 letters
# 3 repeated
# next to each other

def three_letter_couplets(word):
	i = 0
	while i < len(word) - 6:
		if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
			return True
		i += 1
	return False

couplets = []

for line in open('words.txt'):
	word = line.strip()
	if three_letter_couplets(word):
		couplets.append(word)

print(couplets)
print(max(couplets, key=len))
print(len(couplets))