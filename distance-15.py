# Take 2 Point objects and return the distance between them
# Point classes contain x and y attributes

import math
import copy

class Point:
	""" represents a point in 2D space """

class Rectangle():
	"""
	represents a rectangle with width, height and corner

	the corner is represented as a point

	"""

def print_point(p):
	print(f'({p.x}, {p.y})')

def distance_between_points(p1, p2):
	return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def move_rectangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy

def move_rectangle_copy(rect, dx, dy):
	rect2 = copy.deepcopy(rect)
	move_rectangle(rect2, dx, dy)
	return rect2

if __name__ == '__main__':
	# using distance function
	p1 = Point()
	p1.x = 5
	p1.y = 10
	p2 = Point()
	p2.x = 3
	p2.y = 2
	print(f'distance between p1 and p2 is {distance_between_points(p1, p2)}')

	# moving rectangle
	box = Rectangle()
	box.width = 100
	box.height = 200
	box.corner = Point()
	box.corner.x = 0
	box.corner.y = 0
	print_point(box.corner)
	move_rectangle(box, 2, 2)
	print_point(box.corner)

	box2 = move_rectangle_copy(box, 5, 7)
	print_point(box2.corner)
	print(box is box2, box.corner is box2.corner)


