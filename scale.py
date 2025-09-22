from tkinter import *


def submit():
    print("The temperature is:", scale.get(), "degrees C")


window = Tk()

scale = Scale(window,
              from_=0,
              to=100)
scale.pack()

button = Button(window,
                text=('Submit'),
                command=submit)
button.pack()
window.mainloop()
