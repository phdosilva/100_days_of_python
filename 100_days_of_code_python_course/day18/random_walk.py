from random import random, choice


def random_walk(turtle, width, steps_number):
    for _ in range(steps_number):
        turtle.color(random(), random(), random())
        angle = choice([0, 90, 180, 270])

        turtle.right(angle)
        turtle.forward(width)

