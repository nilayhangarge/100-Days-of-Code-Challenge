import colorgram

# Extracting colours from image using colorgram
colors = colorgram.extract('sample.png', 30)
rgb_colors = []

for color in colors:
    # Inserting values in list
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

# rgb_colors without white shades
color_list = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38),
              (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16),
              (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45),
              (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Setting the turtle start position setpos(x,y)
tim.setpos(-225, -225)

# y-loop
for _ in range(10):
    # x-loop
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    # Setting next row position
    tim.left(180)  # Setheading is an alternative of left/right
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen = turtle.Screen()
screen.exitonclick()
