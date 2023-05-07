# uses only a set of letters

def uses_only(word, allowed_letters):
	return set(word).issubset(set(allowed_letters))

for line in open('words.txt'):
	word = line.strip()
	if uses_only(word, 'acefhlo'):
		print(word)