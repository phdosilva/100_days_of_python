from turtle import Turtle
from config import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self._score = 0

        with open('data', mode="r") as file:
            self._higher_score = int(file.read())

        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(SCOREBOARD_POSITION)

        self.clear()
        self.write(f'Score: 0 Higher score: {self._higher_score}', False, align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, align=SCOREBOARD_ALIGMENT, font=SCOREBOARD_FONT)

    def add(self):
        self._score += 1
        self.clear()
        self.write(f'Score: {self._score} Higher score: {self._higher_score}', False, align=SCOREBOARD_ALIGMENT,
                   font=SCOREBOARD_FONT)

    def reset(self):
        self._higher_score = self._score if self._score > self._higher_score else self._higher_score
        self._score = 0
        self.clear()
        self.write(f'Score: {self._score} Higher score: {self._higher_score}', False, align=SCOREBOARD_ALIGMENT,
                   font=SCOREBOARD_FONT)

        with open('data', mode="w") as file:
            file.write(str( self._higher_score ))
