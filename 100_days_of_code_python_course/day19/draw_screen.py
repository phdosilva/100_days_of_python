from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_back():
    timmy.back(10)


def turn_right():
    timmy.right(90)


def turn_left():
    timmy.left(90)


def clean_screen():
    timmy.speed("fastest")
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    timmy.speed("normal")


screen.setup(width=500, height=400)

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clean_screen, key="c")

screen.listen()

screen.exitonclick()