import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")


def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


# Draw a Circle
for _ in range(72):
    tim.color(random_colours())
    tim.circle(100)
    tim.left(5)

screen = Screen()
screen.exitonclick()
