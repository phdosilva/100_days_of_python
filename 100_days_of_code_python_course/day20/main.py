from turtle import Screen, Turtle
import time

from snake import Snake

BASIC_DIMENSION: int = 20

screen = Screen()
screen.setup(width=30*BASIC_DIMENSION, height=30*BASIC_DIMENSION)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

screen.exitonclick()