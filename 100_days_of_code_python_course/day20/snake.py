from turtle import Screen, Turtle
from config import *
from food import Food


class Snake:
    def __init__(self, boundaries: tuple[int, int, int, int]):
        self._segments: list[Turtle] = []

        for seg_num in range(3):
            t = self._create_segment(x=-1 * seg_num * BASIC_DIMENSION, y=0)
            self._segments.append(t)

        x1, x2, y1, y2 = boundaries
        self._x_boundaries = (x1, x2)
        self._y_boundaries = (y1, y2)

    @property
    def _head(self) -> Turtle:
        return self._segments[0]

    def _create_segment(self, x, y):
        t = Turtle()
        t.color("white")
        t.shape("square")
        t.penup()
        t.goto(x, y)
        return t


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

    def distance_to(self, t: Turtle):
        x = t.xcor()
        y = t.ycor()
        return self._head.distance(x, y)

    def ate(self):
        x = self._segments[-1].xcor()
        y = self._segments[-1].ycor()
        t = self._create_segment(x, y)
        self._segments.append(t)

    def validate_movement(self):
        if not (self._x_boundaries[0] < self._head.xcor() < self._x_boundaries[1] \
                and self._y_boundaries[0] < self._head.ycor() < self._y_boundaries[1]):
            return False

        for segment in self._segments[1:]:
            if self._head.distance(segment.xcor(), segment.ycor()) < 10:
                return False

        return True

    def reset(self):
        list(map(lambda seg: seg.hideturtle(), self._segments))
        self.__init__((*self._x_boundaries, *self._y_boundaries))
