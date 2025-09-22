from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radioButton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact', 50)
                              )
    radioButton.pack(anchor=W)


window.mainloop()
