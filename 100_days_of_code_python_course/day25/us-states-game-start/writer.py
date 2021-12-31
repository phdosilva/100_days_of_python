from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write(self, name, x, y):
        self.goto(x, y)
        super().write(name, align="center")
