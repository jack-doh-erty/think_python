""" create a Circle class and functions to determine overlaps
	with Points and Rectangles
"""

import math
import copy

class Circle:
	""" represents a circle with a centre and radius
		centre is a Point object
	"""

class Point:
	""" represents a point in 2D space """

class Rectangle:
	"""
		represents a rectangle with width, height and corner
		the corner is represented as a point
	"""

def distance_between_points(p1, p2):
	return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circle, point):
	return distance_between_points(circle.centre, point) <= circle.radius

def move_point_copy(point, dx, dy):
	point2 = copy.deepcopy(point)
	point2.x += dx
	point2.y += dy
	return point2

def rect_in_circle(circle, rect):
	point0 = move_point_copy(rect.corner, 0, 0)
	point1 = move_point_copy(rect.corner, 0, rect.height)
	point2 = move_point_copy(rect.corner, rect.width, rect.height)
	point3 = move_point_copy(rect.corner, rect.width, 0)
	for point in [point0, point1, point2, point3]:
		print(f'x: {point.x}, y: {point.y}')
		if not point_in_circle(circle, point):
			return False
	return True

# point in circle
circle = Circle()
circle.radius = 75
circle.centre = Point()
circle.centre.x = 150
circle.centre.y = 100

inside = Point()
inside.x = 170
inside.y = 160

outside = Point()
outside.x = 226
outside.y = 100

print(point_in_circle(circle, inside))
print(point_in_circle(circle, outside))

# rect in circle
box = Rectangle()
box.width = 10
box.height = 20
box.corner = Point()
box.corner.x = 150
box.corner.y = 100

print(rect_in_circle(circle, box))

