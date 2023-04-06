# find the rotated word pairs

from rotate_words import rotate_word

def word_dict():
	t = {}
	for word in open('words.txt'):
		t[word.strip().lower()] = True
	return t

def word_pairs(word, word_dict):
	for i in range(1,25):
		rotated_word = rotate_word(word, i)
		if rotated_word in word_dict:
			print(word, rotated_word, i)

if __name__ == '__main__':
	word_dict = word_dict()
	for word in word_dict:
		word_pairs(word, word_dict)