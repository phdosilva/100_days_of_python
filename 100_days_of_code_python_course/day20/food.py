from random import randint
from turtle import Turtle

from config import *

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("red")
        self.speed("fastest")
        self._set_new_position()

    def _set_new_position(self):
        x = randint(-14, 14)
        y = randint(-14, 14)
        self.goto(x * BASIC_DIMENSION, y * BASIC_DIMENSION)

    def eaten(self):
        self._set_new_position()
