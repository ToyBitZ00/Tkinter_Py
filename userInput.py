from tkinter import *


def submit():
    print("Hello", entry.get())


window = Tk()
window.title("Entry Box Program")

entry = Entry(window,
              font=("Arial", 50),
              bg="black",
              fg="#00FF00")

entry.pack(side=LEFT)

submit_button = Button(window,
                       text="Submit",
                       command=submit,
                       font=('Comis Sans', 20),
                       compound="right")

submit_button.pack(side=RIGHT)

window.mainloop()
