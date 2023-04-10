# prints the names of all files in a directory, including sub-directories

import os

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)

		if os.path.isfile(path):
			print(path)
		else:
			walk(path)

print(walk(os.getcwd()))

def walk2():
	for root, dirs, files in os.walk(".", topdown=False):
	   for name in files:
	      print(os.path.join(root, name))
	   for name in dirs:
	      print(os.path.join(root, name))
print(walk2())