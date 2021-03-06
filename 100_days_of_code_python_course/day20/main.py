from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from config import *

BASIC_DIMENSION: int = 20

screen = Screen()
screen.setup(width=30*BASIC_DIMENSION, height=30*BASIC_DIMENSION)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake(MAP_BOUNDARIES)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    if not snake.validate_movement():
        snake.reset()
        scoreboard.reset()
        food.eaten()
    screen.update()
    time.sleep(0.05)

    snake.move()

    if (snake.distance_to(food) < 5):
        food.eaten()
        snake.ate()
        scoreboard.add()

scoreboard.game_over()

screen.exitonclick()