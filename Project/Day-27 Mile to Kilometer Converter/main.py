from tkinter import *


def miles_to_km():
    miles = float(input_box.get())
    km = round(miles * 1.609)
    answer.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=330, height=130)
window.config(padx=40, pady=40)

equal = Label(text="is equal to", font=("Arial", 12, "normal"))
equal.grid(column=0, row=1)
equal.config(padx=10, pady=10)

input_box = Entry(width=10)
input_box.grid(column=1, row=0)

answer = Label(text="0", font=("Arial", 12, "normal"))
answer.grid(column=1, row=1)
answer.config(padx=10, pady=10)

button = Button(text="Calculate", font=("Arial", 10, "bold"), command=miles_to_km)
button.grid(column=1, row=2)

miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

window.mainloop()
