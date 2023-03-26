# 10-2 cumsum of list

def cumsum(t):
	res = []
	for i in range(len(t)):
		res.append(sum(t[:i+1]))
	return res

print(cumsum([1,2,3]))

# 10-3 middle

def middle(t):
	return t[1:-1]

print(middle([1,2,3,4]))


# 10-4 chop, remove the first and last elements of the list. returns None

def chop(t):
	del t[0]
	del t[-1]

t = [1,2,3,4]
print(t)
chop(t)
print(t)

# 10-5 is_sorted

def is_sorted(t):
	return t == sorted(t)

t = [1,2,3]
print(t)
t.sort()
print(t)

print(is_sorted([1,2,3]))
print(is_sorted(['a', 'b', 'a']))

# 10-6 is_anagram

def is_anagram(str1, str2):
	return sorted(list(str1)) == sorted(list(str2))

print(is_anagram('jack', 'ckaj'))

# 10-7 has duplicates

def has_duplicates(t):
	return len(t) != len(set(t))

print(has_duplicates('aab'))
print(has_duplicates('ab'))