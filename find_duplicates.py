"""
Searches a directory and sub-directories and lists all files with a given suffix e.g. '.mp3'
Uses checksums and unix diff to find duplicates
"""

import os
import string

def files(suffix):
	# returns a list of all files in cwd with given suffix
	res = []

	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			root, ext = os.path.splitext(name)
			if ext == suffix:
				res.append(name)
	return res

def find_duplicates(files):
	# for a list of files in cwd, use md5 and diff to find any duplicates
	res = {}
	duplicates = []
	for file in files:
		cmd = 'md5 ' + file
		fp = os.popen(cmd)
		md5 = fp.read().strip(string.whitespace + string.punctuation).split(' = ')
		_, checksum = md5
		if checksum not in res:
			res[checksum] = [file]
		else:
			res[checksum].append(file)
			
	for values in res.values():
		if len(values) > 1:
			duplicates.append(values)
	return duplicates

def diff(files):
	# run unix diff on files given in a list
	return None

files = files('.py')
print(find_duplicates(files))

