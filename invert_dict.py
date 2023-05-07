# invert a dictionary using setdefault

def invert_dict(d):
	inverse = {}
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
	return inverse

if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1, s=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)
