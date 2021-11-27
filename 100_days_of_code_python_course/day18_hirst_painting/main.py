from colors import Colors
from turtle import Turtle, Screen, colormode
import random

colors = Colors('painting.jpg')
colormode(255)
timmy = Turtle()

start_position = (-250, -250)

timmy.penup()

for i in range(10):
    for j in range(10):
        timmy.goto(((j * 50) + start_position[0]), (( i * 50) + start_position[1]))
        timmy.dot(20, random.choice(colors))

screen = Screen()
screen.exitonclick()





