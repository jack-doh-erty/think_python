""" exercises from chapter 16, Classes and Functions """

class Time:
	"""Represents the time of day
	attributes: hour, minute, second
	"""

def print_time(time):
	print(f'{time.hour:02}:{time.minute:02}:{time.second:02}')

def is_after(t1, t2):
	""" returns True if t1 is after t2 """
	return (t1.hour, t1.mintute, t1.second) > (t2.hour, t2.mintute, t2.second) 

def time_to_int(time):
	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second
	return seconds

def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time

def add_time(t1, t2):
	seconds = time_to_int(t1) + time_to_int(t2)
	return int_to_time(seconds)

def increment(time, seconds):
	int_time = time_to_int(time)
	return int_to_time(int_time + seconds)

def valid_time(time):
	if time.hour < 0 or time.minute < 0 or time.second < 0:
		return False
	if time.minute > 60 or time.second > 60:
		return False
	return True

def mul_time(time, n):
	assert valid_time(time)
	return int_to_time(time_to_int(time) * n)

def main():
	time = Time()
	time.hour = 11
	time.minute = 5
	time.second = 3

	time2 = Time()
	time2.hour = 1
	time2.minute = 50
	time2.second = 23

	assert valid_time(time) and valid_time(time2)

	print_time(time)
	print_time(time2)
	added_time = add_time(time, time2)
	print('added time: ')
	print_time(added_time)

	inc_time = increment(time, 65)
	print('incremenetal time: ')
	print_time(inc_time)

	mul = mul_time(time, 1.5)


	print('mul time: ')
	print_time(mul)

if __name__ == '__main__':
	main()

