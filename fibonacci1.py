import turtle
import time
# s
window = turtle.Screen()
window.bgcolor("black")

mark = turtle.Turtle()
mark.color("blue", "green")
mark.speed(10000000)
mark.pensize(4)

def factorial1(n):
	if n == 1:
		return 1;
	else:
		return n * factorial1(n - 1)

def drawBasics(markTurtle):
	markTurtle.pensize(1)
	for i in range(1,5):
		markTurtle.setpos(0, 0)
		markTurtle.forward(400)
		markTurtle.backward(400)
		markTurtle.right(90)


def fibonacci1(markTurtle, fibo, sequences):
	markTurtle.pensize(5)
	markTurtle.setheading( 0 )
	for j in range(1, sequences + 1):
		for i in range(1, 10):
			markTurtle.circle(i*fibo[i], 90)
		markTurtle.penup()
		markTurtle.setpos(0, 0)
		markTurtle.setheading( 0 )
		markTurtle.left( (360/sequences) * j )
		markTurtle.pendown()
	for j in range(1, sequences + 1):
		for i in range(1, 10):
			markTurtle.circle(i*fibo[i], -90)
		markTurtle.penup()
		markTurtle.setpos(0, 0)
		markTurtle.setheading( 0 )
		markTurtle.left( (360/sequences) * j )
		markTurtle.pendown()
	markTurtle.setpos(0, -380)
	markTurtle.circle(380)
	markTurtle.write("Home = ", True, align="center")



print( factorial1( 3 ) )
drawBasics(mark)

fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fibonacci1(mark, fibo, 9)

turtle.exitonclick()