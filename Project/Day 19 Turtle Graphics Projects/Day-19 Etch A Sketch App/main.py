from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(45)


def clockwise():
    tim.right(45)


def clear():
    tim.reset()


screen.listen()

screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
