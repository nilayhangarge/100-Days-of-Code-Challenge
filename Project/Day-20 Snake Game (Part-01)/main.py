import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turns animation on/off and set delay for update drawings.
screen.tracer(0)

snake = Snake()

# Event Listeners
screen.listen()
# Arrow Keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # The screen will update directly here, no previous animation will be displayed
    screen.update()
    time.sleep(0.1)  # Adding 1sec delay

    snake.move()

screen.exitonclick()
