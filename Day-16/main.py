from turtle import Turtle, Screen

import another_module
# print(another_module.another_variable)
print(another_module.variable)

# object = class()
timmy = Turtle()
print(timmy)
timmy.shape("turtle")

# Screen is the object & canvaheight is the attribute
my_screen = Screen()

print(my_screen.canvheight)
timmy.color("black", "red")  # object.color(pencolor, fillcolor)     #pencolor is border
timmy.forward(100)
my_screen.exitonclick()  # object.method()
