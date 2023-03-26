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

def circle(t, r):
	# approximate as 100 individual sides of length 2*pi*r / 100
	polygon(t, (2*math.pi*r)/100, 100)

def arc(t, r, angle):
	for i in range(int(100*(angle/360))):
		t.fd(int((2*math.pi*r)/100))
		t.lt(360/100)

#polygon(bob, 20, 7)
#circle(bob, 100)
arc(bob, 50, 90)

turtle.mainloop()




