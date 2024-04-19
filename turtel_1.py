import turtle
from turtle import *

turtle.bgcolor('black')

square= turtle.Turtle()
square.speed(15)
square.pencolor('red')
for i in range(300):
    square.forward(i)
    square.left(91)



