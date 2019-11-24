import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

mark = turtle.Turtle()
mark.color("blue", "green")
mark.speed(10000000)
mark.left(90)
mark.setpos(0, 0)
mark.pensize(4)

def cope1(Ncopes):
	for i in range(1, Ncopes + 1):
		mark.pendown()
		mark.forward(15)
		mark.left(45)
		mark.forward(10)
		mark.backward(10)
		mark.right(90)
		mark.forward(10)
		mark.backward(10)
		mark.left(45)
		mark.forward(10)

def cope2(Nbranches):
	x1 = 360 / Nbranches
	for i in range(1, Nbranches + 1):
		cope1(3)
		mark.left(x1)
		mark.setpos(0, 0)

cope2(8)

mark.penup()
mark.setpos(500, 400)

turtle.exitonclick()