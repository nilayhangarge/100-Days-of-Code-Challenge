import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


tim.speed("fast")
tim.pensize(10)
directions = [0, 90, 180, 270]

for _ in range(80):
    tim.color(random_color())
    tim.forward(30)
    # setheading - set the turtle according to the angle
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
