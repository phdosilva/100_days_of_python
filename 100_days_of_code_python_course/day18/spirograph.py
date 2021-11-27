from random import random


def spirograph (turtle, ratio, circle_quantity):
    for _ in range(circle_quantity):
        turtle.color(random(), random(), random())
        turtle.circle(ratio)
        turtle.left(360/circle_quantity)