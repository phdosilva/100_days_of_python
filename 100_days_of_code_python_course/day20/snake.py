from turtle import Screen, Turtle

BASIC_DIMENSION = 20


class Snake:
    def __init__(self):
        self._segments = []
        self._create_snake()

    @property
    def _head(self) -> Turtle:
        return self._segments[0]

    def _create_snake(self):
        for seg_num in range(3):
            t = Turtle()
            t.color("white")
            t.shape("square")
            t.penup()
            t.goto((-1 * seg_num * BASIC_DIMENSION, 0))
            self._segments.append(t)

    def move(self):
        for i in range(len(self._segments) - 1, 0, -1):
            x = self._segments[i - 1].xcor()
            y = self._segments[i - 1].ycor()
            self._segments[i].goto((x, y))
        self._segments[0].forward(BASIC_DIMENSION)

    def up(self):
        if (self._head.heading() == 0):
            self._head.left(90)
        elif (self._head.heading() == 180):
            self._head.right(90)
        else:
            pass

    def down(self):
        if (self._head.heading() == 180):
            self._head.left(90)
        elif (self._head.heading() == 0):
            self._head.right(90)
        else:
            pass

    def left(self):
        if (self._head.heading() == 90):
            self._head.left(90)
        elif (self._head.heading() == 270):
            self._head.right(90)
        else:
            pass

    def right(self):
        if (self._head.heading() == 270):
            self._head.left(90)
        elif (self._head.heading() == 90):
            self._head.right(90)
        else:
            pass
