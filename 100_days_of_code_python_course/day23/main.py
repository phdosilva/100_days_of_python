import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move()
    screen.update()

    if player.has_scored():
        scoreboard.increase_score()
        car_manager.increase_difficult()

    game_is_on = not player.collided(*car_manager.cars)

scoreboard.gameover()

screen.exitonclick()