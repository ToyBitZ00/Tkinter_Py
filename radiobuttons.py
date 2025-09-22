from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]


def order():
    if (x.get() == 0):
        print("You ordered Pizza!")
    elif (x.get() == 1):
        print("You ordered a Hamburger!")
    elif (x.get() == 2):
        print("You ordered a Hotdog!")
    else:
        print("Huh?")


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
                              compound='left',
                              indicatoron=0,
                              width=800,
                              command=order
                              )
    radioButton.pack(anchor=W)

window.mainloop()
