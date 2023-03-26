import math
print(math)

print(math.pi)

print(math.sin(2 * math.pi))

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print("I'm a lumberjack and I'm OK")
	print("I sleep all night and I work all day")

repeat_lyrics()

def print_twice(x):
	print(x)
	print(x)

print_twice('spam' * 3)

# exercise 3-1
def right_justify(s):
	whitespace = 70 - len(s)
	return (' ' * whitespace + s)

print(right_justify('monty'))

# exercise 3-2
def do_twice(f, v):
	f(v)
	f(v)

def print_spam():
	print('spam')

def do_four(f, v):
	do_twice(f, v)
	do_twice(f, v)

print('do_twice')
do_twice(print_twice, 'spam')

print('do_four')
do_four(print_twice, 'spam')