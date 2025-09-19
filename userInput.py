from tkinter import *


def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()
window.title("Entry Box Program")

entry = Entry(window,
              font=("Arial", 50),
              bg="black",
              fg="#00FF00")
entry.pack(side=LEFT)
entry.insert(0, "Spongebob")

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
