from tkinter import *

# button = you click it, then it does stuff


def click():
    print("You clicked the button")


window = Tk()

button = Button(window,
                text="Click me!",
                command=click)

button.pack()
window.mainloop()
