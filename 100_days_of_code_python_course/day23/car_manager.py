from turtle import Turtle
from random import choice, randrange


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 40
MOVE_INCREMENT = 10

ROAD_WIDTH = 260
ROAD_LENGTH = 360


class Car(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.color(choice(COLORS))
        self.penup()
        self.goto(xcor, ycor)


class CarManager:
    def __init__(self):
        self._cars = []
        self._create_list()
        self._speed = 1

    @property
    def cars(self):
        return self._cars

    def _create_list(self):
        for _ in range(int(2*ROAD_LENGTH/STARTING_MOVE_DISTANCE)):
            self._create_car()

    def _reset_list(self):
        for car in self._cars:
            car.hideturtle()
        self._cars = []

    def _create_car(self):
        if self._cars:
            self._cars.append(Car(self._cars[-1].xcor() + STARTING_MOVE_DISTANCE, randrange(-ROAD_WIDTH, ROAD_WIDTH)))
        else:
            self._cars.append(Car(ROAD_LENGTH + 20 + STARTING_MOVE_DISTANCE, randrange(-ROAD_WIDTH, ROAD_WIDTH)))

    def _delete_car(self, car):
        self._cars.remove(car)

    def _reset_car(self):
        car = self._cars.pop(0)
        car.goto(ROAD_LENGTH, randrange(-ROAD_WIDTH, ROAD_WIDTH))
        self._cars.append(car)

    def move(self):
        if self._cars[0] and self._cars[0].xcor() < -1*ROAD_LENGTH:
            self._reset_car()

        for car in self._cars:
            car.goto(car.xcor() - MOVE_INCREMENT*self._speed, car.ycor())

    def increase_difficult(self):
        self._speed *= 1.5
        self._reset_list()
        self._create_list()


