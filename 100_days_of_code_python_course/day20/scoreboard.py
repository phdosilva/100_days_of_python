from turtle import Turtle
from config import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self._score = 0

        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(SCOREBOARD_POSITION)

        self.clear()
        self.write("Score: 0", False, align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)

    def add(self):
        self._score += 1
        self.clear()
        self.write(f'Score: {self._score}', False, align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)
