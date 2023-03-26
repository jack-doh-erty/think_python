# 9-2 words with no e

def has_no_e(word):
	if 'e' in word:
		return False
	return True

total = 0
no_e = 0

for line in open("words.txt"):
	word = line.strip()
	total += 1
	if has_no_e(word):
		no_e += 1

print(f'out of {total} words in the list, {no_e} do not contain the letter e, which is {round(no_e / total * 100, 1)}%')