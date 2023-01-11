import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # Detect collision with car
    for each_car in car.cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Use alternate method to check level_complete()
    if player.level_complete():
        player.go_to_start()
        scoreboard.level_up()

        # Increase the speed of the objects
        car.speed_up()

screen.exitonclick()
