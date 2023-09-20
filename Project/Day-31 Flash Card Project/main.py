import os
import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# data_dict = {}


# Alternate method for saving progress
# try:
#     data = pandas.read_csv("data/words_to_csv.csv")
# except FileNotFoundError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     data_dict = original_data.to_dict(orient="records")
# else:
#     data_dict = data.to_dict(orient="records")

data = pandas.read_csv("data/french_words.csv")
# Converts data to list of dictionaries
data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    # Resets the after timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # Changing the text and colour
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # Change the card image
    canvas.itemconfig(canvas_image, image=card_back)


def right_word():
    global data_dict
    global data
    data_dict.remove(current_card)
    path = 'data/words_to_csv'
    if os.path.isfile(path):
        csv = pandas.read_csv("data/words_to_csv.csv")
        # Converts data to list of dictionaries
        data_dict = csv.to_dict(orient="records")
    else:
        data = pandas.DataFrame(data_dict)
        data.to_csv("data/words_to_csv.csv")
    next_card()
    return data_dict


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Button
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=right_word)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
