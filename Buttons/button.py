from tkinter import *

# button = you click it, then it does stuff


def click():
    print("You clicked the button")


window = Tk()

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00")

button.pack()
window.mainloop()
