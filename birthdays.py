# proving the birthday paradox

# create 100 classes of 23 student, each with random birthday
# calculate the proportion of classes that have a duplicate birthday

from random import randint

def has_duplicate(t):
	return len(t) != len(set(t))

def test_class(num_students):
	t = []
	for i in range(num_students):
		t.append(randint(1, 365))
	return has_duplicate(t)

def run_simultation(num, num_students):
	counter = 0
	for i in range(num):
		if test_class(num_students):
			counter += 1
	return counter / num


num = 10000
num_students = 23

print(f'with {num} simulations of classes with {num_students} students, {run_simultation(num, num_students)*100}% had matching bdays')


