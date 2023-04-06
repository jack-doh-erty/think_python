# implements fibonacci using a memo

import time

known = {0:0, 1:1}

def fibonacci(n):
	if n in known:
		return known[n]

	result = fibonacci(n-1) + fibonacci(n-2)
	known[n] = result
	return result

def slow_fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

start_time = time.time()
for i in range(50000):
	slow_fibonacci(i)
print(f'using slow took {time.time() - start_time} seconds')

start_time = time.time()
for i in range(50000):
	fibonacci(i)
print(f'using memo took {time.time() - start_time} seconds')

print(known[435])