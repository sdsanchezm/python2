import turtle
import time
# s
window = turtle.Screen()
window.bgcolor("black")

mark = turtle.Turtle()
mark.color("blue", "green")
mark.speed(10000000)
mark.left(90)
mark.setpos(0, 0)
mark.pensize(4)

def circles1(Ncircles):
	for i in range(1, Ncircles + 1):
		mark.pendown()
		mark.forward(50)
		mark.circle(10)
		mark.backward(10)

def cope2(Nbranches):
	x1 = 360 / Nbranches
	for i in range(1, Nbranches + 1):
		circles1(3)
		mark.left(x1)
		mark.setpos(0, 0)

cope2(8)

mark.penup()
mark.setpos(500, 400)

turtle.exitonclick()