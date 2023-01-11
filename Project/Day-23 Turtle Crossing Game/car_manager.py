import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            y_cor = random.randint(-250, 250)
            car.goto(300, y_cor)
            self.cars.append(car)

    def move_car(self):
        for each_car in self.cars:
            each_car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
