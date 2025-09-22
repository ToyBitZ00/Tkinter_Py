from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radioButton = Radiobutton(
        window, text=food[index], variable=x, value=index)
    radioButton.pack()


window.mainloop()
