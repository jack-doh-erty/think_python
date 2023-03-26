# count the 'a's in 'banana'

print('banana'.count('a'))

def is_palindrome(word):
	return word == word[::-1]

print(is_palindrome('aabbccddccbbaa'))



# rotate word

def rotate_word(word, n):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	rotated = ''
	for letter in word.lower():
		rotated += alphabet[(ord(letter) - ord('a') + n) % 26]
	return rotated 

print(rotate_word('IBM', -1))
print(rotate_word('melon', -10))
print(rotate_word('cheer', 7))