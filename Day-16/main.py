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

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
