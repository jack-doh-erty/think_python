"""Draws an archemedia spiral

Exercse 4-5 in Think Python
"""

import turtle

def spiral(t, length, n, a, b):

	theta = 0.00

	for i in range(n):
		t.fd(length)
		dtheta = 1  / (a + b * theta)

		t.lt(dtheta)
		theta += dtheta

bob = turtle.Turtle()
spiral(bob, 3, 1000, 0.1, 0.002)

turtle.mainloop()