from turtle import Turtle
from random import choice


directions = {
    "top_right": (1, 1),
    "bottom_right": (1, -1),
    "top_left": (-1, 1),
    "bottom_left": (-1, -1)
              }


class Ball(Turtle):
    def __init__(self, court, speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self._boundaries = tuple(a/2 for a in list(court))
        print(self._boundaries)
        self._speed = (self._proportional_x_speed(*court)*speed, speed)
        self._direction: tuple[int, int] = directions[choice(list(directions))]

    def _proportional_x_speed(self, court_x, court_y):
        return court_x/court_y

    @property
    def x_speed(self):
        direction_value= self._direction[0]
        return self._speed[0] * direction_value

    @property
    def y_speed(self):
        direction_value = self._direction[1]
        return self._speed[1] * direction_value

    def _wall_colision(self):
        return self.distance(self.xcor(), self._boundaries[1]) <= 20\
               or self.distance(self.xcor(), -1 * self._boundaries[1]) <= 20

    def move(self):
        if self._wall_colision():
            self._direction = (self._direction[0], self._direction[1] * -1)

        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)

    def collision_with(self, paddle1: Turtle, paddle2: Turtle):
        paddle1_boundaries = abs(paddle1.xcor()) - (paddle1.shapesize()[1] * 20)
        paddle2_boundaries = abs(paddle2.xcor()) - (paddle2.shapesize()[1] * 20)

        if ((self.distance(paddle1) < 50 and self.xcor() > paddle1_boundaries)\
                or (self.distance(paddle1) < 50 and self.xcor() < -1 * paddle1_boundaries))\
            or ((self.distance(paddle2) < 50 and self.xcor() > paddle2_boundaries)\
                or (self.distance(paddle2) < 50 and self.xcor() < -1 * paddle2_boundaries)):
            self._direction = (self._direction[0] * -1, self._direction[1])

    def check_goal(self):
        if self.xcor() >= self._boundaries[0] or self.xcor() <= -1 * self._boundaries[0]:
            self._direction = tuple(d * -1 for d in list(self._direction))
            self._speed = tuple(s * 1.1 for s in list(self._speed))
            side = self.xcor()/abs(self.xcor())
            self.goto(0, 0)
            return side
        return 0