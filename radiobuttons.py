from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

window = Tk()
for index in range(len(food)):
    radioButton = Radiobutton(window, text=food[index])
    radioButton.pack()
window.mainloop()
