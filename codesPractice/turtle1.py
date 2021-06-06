import random
import turtle

def fmark(tortuga, tortugaFactor):
	tortuga.pensize(tortugaFactor / 10)
	if tortugaFactor > 40:
		tortuga.color("red")
	else:
		tortuga.color("white")

	if tortugaFactor > 10:
		tortuga.forward(tortugaFactor)
		tortuga.left(30)
		fmark(tortuga, tortugaFactor - random.randint(10,20))
		tortuga.right(60)
		fmark(tortuga, tortugaFactor - random.randint(10,20))
		tortuga.left(30)
		tortuga.penup()
		tortuga.backward(tortugaFactor)
		tortuga.pendown()

window = turtle.Screen()
window.bgcolor("black")
#Creacion de la tortuga Mark
mark = turtle.Turtle()
mark.color("red", "green")
mark.left(90)
mark.speed(0)
mark.penup()
mark.setpos(0, -250)
mark.pendown()
print(random.randint(1,2))

#for i in range(1,5):
#	fmark(mark, 60)
#	mark.right(90)

fmark(mark, 100)
turtle.exitonclick()