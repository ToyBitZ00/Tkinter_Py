from tkinter import *


def display():
    username = entry_button.get()
    print("Hello", username)

    if (x.get() == 1):
        print("You agree!")
    else:
        print("You don't agree!")


def delete():
    entry_button.delete(0, END)


def backspace():
    entry_button.delete(len(entry_button.get())-1, END)


window = Tk()
window.config(bg='black')
window.title("CheckBox with User Input")
# window.geometry("200x50")
# x = StringVar()
x = IntVar()

python_logo = PhotoImage(file='python_logo.png')

label = Label(window,
              text="CHECK BUTTON",
              font=('Comic Sans', 40),
              fg='#00FF00',
              bg='black')
label.pack(side=TOP)

entry_button = Entry(window,
                     font=('Comic Sans', 30),
                     fg='#00FF00',
                     bg='gray')
entry_button.pack(side=TOP)

delete_button = Button(window,
                       text="Delete",
                       font=('Arial', 20),
                       fg='#00FF00',
                       bg='black',
                       command=delete)
delete_button.pack(side=TOP)

bakcspace_button = Button(window,
                          text="Backspace",
                          font=('Arial', 20),
                          fg='#00FF00',
                          bg='black',
                          command=backspace)
bakcspace_button.pack(side=TOP)

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
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_logo,
                           compound="left")
check_button.pack()
window.mainloop()
