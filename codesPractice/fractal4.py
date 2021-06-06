import random
import turtle

def yggdrasil(size, MarksTurtle):
    MarksTurtle.pensize(size / 10)

    if size < random.randint(1,2) * 20:
        MarksTurtle.color("white")
    else:
        MarksTurtle.color("red")

    if size > 5:
        MarksTurtle.forward(size)
        MarksTurtle.left(25)
        yggdrasil(size - random.randint(10, 20), MarksTurtle)
        MarksTurtle.right(50)
        yggdrasil(size - random.randint(10, 20), MarksTurtle)
        MarksTurtle.left(25)
        MarksTurtle.penup()
        MarksTurtle.backward(size)
        MarksTurtle.pendown()

#Creacion de la ventana
window = turtle.Screen()
window.bgcolor("black")
#Creacion de la tortuga Mark
mark = turtle.Turtle()
mark.color("red", "purple")
mark.left(90)
mark.speed(1)
mark.penup()
mark.setpos(0, -250)
mark.pendown()

yggdrasil(60, mark)
mark.penup()
mark.setpos(-250, -250)
mark.pendown()
yggdrasil(50, mark)

window.exitonclick()