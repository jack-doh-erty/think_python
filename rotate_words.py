# count the 'a's in 'banana'

def is_palindrome(word):
	return word == word[::-1]

# rotate word
def rotate_word(word, n):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	rotated = ''
	for letter in word.lower():
		rotated += alphabet[(ord(letter) - ord('a') + n) % 26]
	return rotated 

if __name__ == '__main__':
	print(rotate_word('IBM', -1))
	print(rotate_word('melon', -10))
	print(rotate_word('cheer', 7))
	print(is_palindrome('aabbccddccbbaa'))