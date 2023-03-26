"""Exercises 4.2 in ThinkPython
Jack Doherty, Feb-23"""

import turtle
import math

bob = turtle.Turtle()

def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
	# approximate as 100 individual sides of length 2*pi*r / 100
	polygon(t, (2*math.pi*r)/100, 100)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
	for i in range(2):
		arc(t,r,angle)
		t.lt(180-angle)

def flower(t, r, angle, petals):
	for i in range(petals):
		petal(t, r, angle)
		t.lt(360.0/petals)

def move(t, length):
	t.pu()
	t.fd(length)
	t.pd()

if __name__ == '__main__':
    flower(bob, 100, 25, 12)
    move(bob, 100)
    flower(bob, 45, 90, 6)
    move(bob, 100)
    flower(bob, 50, 60, 14)

    turtle.mainloop()

