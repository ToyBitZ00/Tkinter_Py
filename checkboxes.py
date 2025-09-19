from tkinter import *


def display():
    if (x.get() == 1):
        print("You agree!")
    else:
        print("You don't agree!")


window = Tk()
# window.geometry("200x50")
# x = StringVar()
x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black')
check_button.pack()
window.mainloop()
