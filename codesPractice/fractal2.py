import turtle
from turtle import *
import time
from time import *
#speed
speed(10)
delay(0)
tracer(0,0)
#Initial Sequence 
list_0 = ["L","R","R","R","R","L","L"]
#list_1 = ["L"] Useless bit of code
#Loop control
running = 1
#Distance between each turn
size = 5
#Angle of each turn
angle = 90
#Last angle turn
last_angle = 90
#Canvas size 
screensize(2000,2000)
#color control
color_used = 1
colormode(255)
R_color = 1
G_color = 1
B_color = 1
RGB_color = [R_color, G_color, B_color]
#Hides turtle
hideturtle()
#Main Loop(Only Loop. lol)
while 1:
    time_0 = time()
    length = len(list_0)
    print("amount of iterations: ",length)
    update()
    for inc in range(1,length):
        if color_used == 1:
            color((R_color, G_color, B_color))
#List decoder
        if list_0[inc] == "R":
            #print(list_0)
            right(angle)
            forward(size)
        if list_0[inc] == "L":
            #print(list_0)
            left(angle)
            forward(size)
 
        R_color += 5
        if R_color >= 255:
            R_color = 1
            G_color += 5
            if G_color >= 255:
                G_color = 1
                B_color += 5
                     
    print("Current Color",R_color, G_color, B_color)
#Duplication and turning sequence             
    list_0.extend(list_0)
    right(last_angle)
    forward(size)
    list_0.append("R")
#only use this if you want to see the operation that is in progress
    #print(list_0)
    time_1 = time()
    print(int(time_1 - time_0),"seconds")