# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
from turtle import Turtle, Screen

tim = Turtle()


def turtle_colour(n): colours = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red", "Silver"]


tim.color(colours[n])


def draw_shape(sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


num_of_sides = 3
colour_option = 0

for _ in range(3, 11):
    turtle_colour(colour_option)
    draw_shape(num_of_sides)
    num_of_sides += 1
    colour_option += 1

screen = Screen()
screen.exitonclick()
