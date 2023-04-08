# return a random value from a histogram
# where the propbability is propotion of the freqneucy
# e.g. for {'a':2, 'b':1}, a should be returned 2/3 of the time and b 1/3 of the time

import random
from word_frequency import read_words, skip_header, count_words
from bisect import bisect
import time

def choose_random(hist):
	t = []
	for key, freq in hist.items():
		t.extend([key] * freq)
	return random.choice(t)

def choose_random2(hist):
	freqs = []
	words = []
	total_freq = 0
	for word, freq in hist.items():
		total_freq += freq
		words.append(word)
		freqs.append(total_freq)
	x = random.randint(0, total_freq-1)
	index = bisect(freqs, x)
	return words[index]

if __name__ == '__main__':
	words = read_words('emma.txt')
	hist = count_words(words)

	for method in ['choose_random', 'choose_random2']:
		start_time = time.time()
		res = []
		for i in range(100):
			if method == 'choose_random':
				res.append(choose_random(hist))
			else:
				res.append(choose_random2(hist))
		print(res[:10])
		print(f'Using {method} method took {time.time() - start_time}')
