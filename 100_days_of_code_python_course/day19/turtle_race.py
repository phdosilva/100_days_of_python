from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(width=500, height=400)


turtles = []

for _ in range(5):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtles.append(turtle)

initial_positions = [(-240, -100), (-240, -50), (-240, 0), (-240, 50), (-240, 100)]
turtle_colors = ["red", "blue", "green", "yellow", "purple"]

for i, turtle in enumerate(turtles):
    turtle.color(turtle_colors[i])
    turtle.goto(initial_positions[i])

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

is_race_on = True

winners = []

while is_race_on:
    for turtle in turtles:
        turtle.forward(randint(1, 10))
        if turtle.xcor() > 240:
            is_race_on = False
            winners.append(turtle)

if len(winners) == 1 and winners[0].pencolor() == user_bet:
    winner = winners[0]
    print(f'The winner is {winner.pencolor()} and you\'ve won!')
elif len(winners) == 1:
    winner = winners[0]
    print(f'The winner is {winner.pencolor()} and you\'ve lost!')
else:
    print('We had a tie between:')
    for winner in winners:
        print(f'{winner.pencolor()};')
    print('And you\'ve lost!')

screen.exitonclick()
