"""
General functions to create pie-shaped polygons
using the Turtles package 

Exercise 4-3 of Think Python
"""

import turtle
import math

def pie(t, r, n):	
	angle = 360 / n
	for i in range(n):
		isosceles(t, r, angle/2)
		t.lt(angle)

def isosceles(t, r, angle):
    """Draws an icosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

if __name__ == '__main__':
	bob = turtle.Turtle()
	pie(bob, 80, 5)

	turtle.mainloop()


