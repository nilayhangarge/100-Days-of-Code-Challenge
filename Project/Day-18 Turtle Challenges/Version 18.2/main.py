# Draw a Dashed line
from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(15):
    timmy.pd()  # Pen down - drawing when moving
    timmy.forward(10)
    timmy.pu()  # Pen up - no drawing when moving
    timmy.forward(10)

screen = Screen()
screen.exitonclick()
