from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Password Strength Checker")


l = Label(root, text="Enter Password:")
l.pack(pady=10)


entry = Entry(root, width=30, show="*")
entry.pack(pady=10)

l1 = Label(root, text="")
l1.pack(pady=10)


def showinput():
    user_input = entry.get()
    if len(user_input) <= 5:
        l1.config(text="Very Weak Password")
    elif len(user_input) <= 8:
        l1.config(text="Weak Password")
    elif len(user_input) <= 11:
        l1.config(text="Good Password")
    elif len(user_input) <= 14:
        l1.config(text="Strong Password")
    else:
        l1.config(text="Very Strong Password")


btn = Button(root, text="Check Strength", command=showinput)
btn.pack(pady=10)

root.mainloop()
