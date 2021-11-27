from random import random


def different_shapes(turtle, width, number_of_shapes):
    shape_side_number = 3

    for _ in range(number_of_shapes):
        turtle.color(random(), random(), random())

        for _ in range(shape_side_number):
            turtle.forward(width)
            turtle.right(360/shape_side_number)

        shape_side_number += 1


