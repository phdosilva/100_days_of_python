# import turtle
# import turtle as tim

from turtle import Turtle, Screen
from random import random
from square import square
from dashed_line import dashed_line
from different_shapes import different_shapes
from random_walk import random_walk
from spirograph import spirograph

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

timmy_the_turtle.pensize(1)
timmy_the_turtle.speed('fastest')

spirograph(timmy_the_turtle, 100, 20)

screen = Screen()
screen.exitonclick()
