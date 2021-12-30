from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

        self.color("black")
        self.goto(0, 240)
        self._score = 0

        self.write()

    def increase_score(self):
        self._score += 1
        self.write()

    def write(self):
        super().clear()
        super().write(f'Score: {self._score}', align="center", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        super().write(f'Game over', align="center", font=FONT)
