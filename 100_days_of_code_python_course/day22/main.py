import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

right_paddle = Paddle(x_start=350, y_start=0, court=(800, 600))
left_paddle = Paddle(x_start=-350, y_start=0, court=(800, 600))

ball = Ball(court=(800, 600), speed=1)

scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.collision_with(right_paddle, left_paddle)
    ball.move()

    hit = ball.check_goal()
    if hit == -1:
        scoreboard.increase_r()
    elif hit == 1:
        scoreboard.increase_l()

    time.sleep(0.01)

screen.exitonclick()