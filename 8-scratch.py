word = 'aaa'
print(word[:])


# counter

def letter_count(word, letter):
	count = 0 
	for test in word:
		if test == letter:
			count += 1
	return count 

print(letter_count('jemima', '')) 