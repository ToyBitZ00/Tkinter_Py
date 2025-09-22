from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
hamburgerImage = PhotoImage(file='hamburger.png')
hotdogImage = PhotoImage(file='hotdog.png')

foodImages = [pizzaImage, hamburgerImage, hotdogImage]
x = IntVar()

for index in range(len(food)):
    radioButton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact', 50),
                              image=foodImages[index],
                              compound='left'
                              )
    radioButton.pack(anchor=W)


window.mainloop()
