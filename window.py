from tkinter import *

window = Tk()  # Used to instantiate an instance of a windows
# window.geometry("600x600")
window.title("My First GUI Program")
icon = PhotoImage(file='App Icon.png')
window.iconphoto(True, icon)
# window.config(background="cyan")  # You can use RGB or Hex Code

# Widgets

photo = PhotoImage(file='settingNoBG.png')


# label = an area widget that holds text and/or an image within a window
label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='red',
              bg='yellow',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=100, y=100)


window.mainloop()  # Place window on the screen.
