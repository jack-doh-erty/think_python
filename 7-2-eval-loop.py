# take user input and evaluate in python
# stop when user enters 'done'

while True:
	line = input('> ')
	if line == 'done':
		break
	print(eval(line))