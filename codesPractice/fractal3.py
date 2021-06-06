import turtle
from turtle import *

wn = turtle.Screen()
screensize(2000,2000)

turtle.speed(0)

turtle.colormode(255)

for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)
	turtle.color(100, 2*i, 10)

turtle.exitonclick()