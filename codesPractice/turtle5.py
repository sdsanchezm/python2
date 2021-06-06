import turtle
import random

window = turtle.Screen()
window.bgcolor("black")

jamecho = turtle.Turtle()
jamecho.color("red", "blue")
jamecho.speed(0)
jamecho.penup()
jamecho.setpos(0,0)
jamecho.pendown()

def shape(turtle1, sides, distance):
	for i in range(1,sides+1):
		jamecho.right(360/sides)
		jamecho.forward(distance)

def shape_turned(turtle1, sides, distance, giro):
	for i in range(1,int(720/giro)):
		shape(turtle1, sides, distance*0.3*i)
		turtle1.right(giro)

#shape(jamecho, 10,100)
shape_turned(jamecho, 3, 10, 5)

turtle.exitonclick()