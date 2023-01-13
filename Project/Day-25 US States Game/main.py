from turtle import Turtle, Screen

import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")

# Set image as turtle shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Obtaining x and y values
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# # On click action
# turtle.onscreenclick(get_mouse_click_coor)
#
# #Alternative for exit_on_click but keeps screen on even if clicked
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(data)} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        correct_answer = data[data.state == answer_state]
        x_cor = int(correct_answer.x)
        y_cor = int(correct_answer.y)
        names = Turtle()
        names.penup()
        names.hideturtle()
        names.goto(x_cor, y_cor)
        names.write(answer_state, align="center", font=("courier", 9, "normal"))
        guessed_states.append(answer_state)
