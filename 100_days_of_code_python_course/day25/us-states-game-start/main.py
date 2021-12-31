from turtle import Screen, shape
from writer import Writer

import pandas

screen = Screen()
screen.title("U.S. States Game")

image_path = "blank_states_img.gif"
screen.addshape(image_path)
shape(image_path)

states_data = pandas.read_csv("50_states.csv")

writer = Writer()

right_guesses = []

game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f'{len(right_guesses)}/50 States Correct', prompt="What's another state's name?")
    if answer is None or len(right_guesses) >= 50:
        game_is_on = False
    else:
        answer = answer.title()

    if not states_data[states_data["state"] == answer].empty:

        right_guesses.append(answer)

        x_coordinates = int(states_data["x"][states_data["state"] == answer])
        y_coordinates = int(states_data["y"][states_data["state"] == answer])

        writer.write(answer, x_coordinates, y_coordinates)


list_not_guessed_states = list(filter(lambda state: state not in right_guesses, states_data.state.to_list()))

pandas.DataFrame(list_not_guessed_states).to_csv("states_to_learn.csv")

screen.exitonclick()
