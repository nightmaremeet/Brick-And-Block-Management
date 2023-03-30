import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def loginsection(contentsection):
    answer = simpledialog.askstring("Password", "Enter Password:",show="*", parent=contentsection)
    if answer == '12345678':
        return 1
    else:  
        messagebox.showerror("showerror", "Invalid Password")
        return loginsection(contentsection)

# root = tk.Tk()

# loginsection(root)

# root.mainloop()
