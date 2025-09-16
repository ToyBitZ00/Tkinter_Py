from tkinter import *

# button = you click it, then it does stuff

count = 0


def click():
    global count
    count += 1
    print("You Clicked", count, "times")


window = Tk()

photo = PhotoImage(file='like.png')

button = Button(window,
                text="CLICK ME!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top')

button.pack()
window.mainloop()
