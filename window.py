from tkinter import *

window = Tk()  # Used to instantiate an instance of a windows
window.geometry("420x420")
window.title("My First GUI Program")

icon = PhotoImage(file='App Icon.png')
window.iconphoto(True, icon)

window.config(background="black")  # You can use RGB or Hex Code

window.mainloop()  # Place window on the screen.
