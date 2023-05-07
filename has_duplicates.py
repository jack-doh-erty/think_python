# 11-4 has duplicates with dictionary

# use dictionary to find if a list has duplicates

import time

# using dict and for loop
def has_duplicates(t):
	known = {}
	for item in t:
		if item in known:
			return True
		known[item] = True
	return False

# faster version using sets
def has_duplicates2(t):
	return len(t) != len(set(t))

if __name__ == '__main__':

	test_list = [i for i in range(100000)]
	test_list.append(999)

	# using dictionary
	start_time = time.time()
	print(has_duplicates(test_list))
	print(f'using dict took {round(time.time() - start_time, 4)} seconds')
	
	# using sets
	start_time = time.time()
	print(has_duplicates2(test_list))
	print(f'using sets took {round(time.time() - start_time, 4)} seconds')