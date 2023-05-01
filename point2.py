# exercises from Chapter 17, Classes and Methods

# turn time_to_int and print_time into methods 

class Time:
	"""Represents the time of day
	attributes: hour, minute, second
	"""
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def print_time(self):
		print(f'{self.hour:02}:{self.minute:02}:{self.second:02}')

class Point:
	""" represents a point in 2D space """
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return (f'({self.x}, {self.y})')

	def __add__(self, other):
		if isinstance(other, Point):
			return Point(self.x + other.x, self.y + other.y)
		else:
			return Point(self.x + other[0], self.y + other[1])

def main():
	time = Time()
	time.hour = 11
	time.minute = 5
	time.second = 3

	print(time.time_to_int())
	time.print_time()

	point = Point(4,5)
	print(f'point is {point}')
	point2 = Point(2,4)
	print(f'point2 is {point2}')

	# using __add and __str method together
	print(f'adding them together gives {point + point2}')

	# adding a tuple instead of another point
	move = (1, 1)
	print(f'adding {move} to point gives {point + move}')

main()
