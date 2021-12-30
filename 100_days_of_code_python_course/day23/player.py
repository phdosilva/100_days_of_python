from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.speed("fastest")

        self.goto(STARTING_POSITION)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def _reset_player(self):
        self.goto(STARTING_POSITION)

    def has_scored(self):
        if self.ycor() > FINISH_LINE_Y:
            self._reset_player()
            return True
        return False

    def collided(self, *cars):
        for car in cars:
            if self.distance(car) < 30:
                return True
        return False



