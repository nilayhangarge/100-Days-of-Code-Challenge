import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turns animation on/off and set delay for update drawings.
screen.tracer(0)

# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in STARTING_POSITIONS:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()

game_is_on = True
while game_is_on:
    # The screen will update directly here, no previous animation will be displayed
    screen.update()
    time.sleep(0.1)  # Adding 1sec delay

    # snake.move()

screen.exitonclick()
