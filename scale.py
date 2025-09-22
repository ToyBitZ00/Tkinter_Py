from tkinter import *


def submit():
    print("The temperature is:" + str(scale.get()) + " degrees C")


window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # VERTICAL or HORIZONTAL
              font=('Consolas', 20),
              tickinterval=10,  # Adds numeric indicators for value
              # showvalue=0,  # No longer shows the value when scrolling
              resolution=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'

              )
scale.pack()

button = Button(window,
                text=('Submit'),
                command=submit
                )
button.pack()

window.mainloop()
