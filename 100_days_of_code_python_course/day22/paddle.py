from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_start, y_start, court):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.penup()

        self._boundaries = tuple(a / 2 for a in list(court))

        self.goto(x_start, y_start)

    def up(self):
        if self.ycor() < self._boundaries[1] - self.shapesize()[0] * 20/2:
            y = self.ycor()
            self.goto(self.xcor(), y + 20)

    def down(self):
        if self.ycor() > -1 * (self._boundaries[1] - self.shapesize()[0] * 20/2):
            y = self.ycor()
            self.goto(self.xcor(), y - 20)


