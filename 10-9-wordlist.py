# build a list from words.txt using 2 methods, see which is faster

import time

def using_append():
	t = []
	for word in open('words.txt'):
		t.append(word.strip())
	return t

def using_concat():
	t = []
	for word in open('words.txt'):
		t = t + [word.strip()]
	return t


start_time = time.time()
t = using_append()
print(f'using_append took {time.time() - start_time} seconds')
print(t[:10])

start_time = time.time()
t = using_concat()
print(f'using_concat took {time.time() - start_time} seconds')
print(t[:10])