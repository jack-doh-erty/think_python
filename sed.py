"""
A function that takes a string pattern, replacement string and 2 filenames
It reads the contents from the first file, replaces the string pattern with the replacement, then writes to a new file
A new file will be created if neccessary
"""

def sed(pattern, replacement, source, dest):
	try:
		fout = open(dest, 'w')
	except:
		print(f'failed to create file {dest}')

	for line in open(source):
		fout.write(line.replace(pattern, replacement))
		
	fout.close()

if __name__ == '__main__':
	sed('love', 'hate', 'test.txt', 'testout.txt')


