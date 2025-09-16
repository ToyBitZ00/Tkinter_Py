from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("My First GUI Program")

icon = PhotoImage(file='App Icon.png')
window.iconphoto(True, icon)

window.mainloop()
