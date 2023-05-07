# Case study on word play

fin = open("words.txt")

# 9-1 words more than 20 characters
for line in fin:
	word = line.strip()
	if len(word) > 20:
		print(word)

# 9-2 has no e
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

print(f'out of {total} words in the list, {no_e} do not contain the letter e, {round(no_e / total * 100, 1)}%')