import turtle

window = turtle.Screen()
david = turtle.Turtle()
david.forward(50)
david.left(50)
david.forward(40)

def randomx1(x):
    for i in range(0,x):
        david.forward(i*10)
        david.left(20)

turtle.mainloop()
