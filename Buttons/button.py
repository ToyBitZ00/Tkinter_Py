from tkinter import *

# button = you click it, then it does stuff


def click():
    print("You clicked the button")


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
                image=photo)

button.pack()
window.mainloop()
