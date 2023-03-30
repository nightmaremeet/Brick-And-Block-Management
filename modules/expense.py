import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from functions import on_click, reverse
import modules.settings as setting
import modules.connect as connect
conn = connect.MainDB("OtherExpenseInfo")


def expense_section(main_frame, Width, Height):
    o_amount = tk.StringVar()

    def insert_data():
        Reason = entryreason.get(1.0, "end-1c")
        Amount = o_amount.get()
        Date = entrydate.entry.get()

        if Reason == "" or Reason == " ":
            return on_click('Reason')
        if Amount == "" or Amount == " ":
            return on_click('Amount')
        if Date == "" or Date == " ":
            return on_click('Date')
        else:
            conn.insert((Reason, Amount, Date))

        for data in otherexpense_tree.Tree.get_children():
            otherexpense_tree.Tree.delete(data)

        for result in reverse(conn.read()):
            otherexpense_tree.Tree.insert(
                parent='', index='end', text="", values=(result), tag="orow")

    def update_data():
        selected_party = otherexpense_tree.Tree.selection()[0]
        update_name = otherexpense_tree.Tree.item(selected_party)['values'][0]
        conn.update((entryreason.get(1.0, "end-1c"),
                     o_amount.get(), entrydate.entry.get(), update_name))

        for data in otherexpense_tree.Tree.get_children():
            otherexpense_tree.Tree.delete(data)

        for result in reverse(conn.read()):
            otherexpense_tree.Tree.insert(
                parent='', index='end', text="", values=(result), tag="orow")

    def delete_data():
        selected_party = otherexpense_tree.Tree.selection()[0]
        deleteData = str(otherexpense_tree.Tree.item(
            selected_party)['values'][0])
        conn.delete((deleteData,), ids="otherID")

        for data in otherexpense_tree.Tree.get_children():
            otherexpense_tree.Tree.delete(data)

        for result in reverse(conn.read()):
            otherexpense_tree.Tree.insert(
                parent='', index='end', iid=result, text="", values=(result), tag="orow")

    def clear():
        for var in lstVars:
            if var == entryreason:
                var.delete(1.0, tk.END)
            else:
                var.set("")

    ################################################# other expense frame ###################################################

    other_expense_frame = ttk.Frame(main_frame)

    input_section = ttk.LabelFrame(
        other_expense_frame, text="Expense Details", bootstyle="primary")

    section3 = ttk.LabelFrame(
        other_expense_frame, text="Operations", bootstyle="primary")

    # labels
    lb = ttk.Label(other_expense_frame, text='Add Expense',
                   font=('Open Sans', 20, "bold"))

    lb.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    input_section.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    section3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

########################################## input_section Section ######################################################
# labels
    lstText = ("Amount", "Reason", "Date")
    for i in range(len(lstText)):
        setting.ContentLabel(input_section, lstText[i], (i, 0))

# entry
    setting.ContentEntry(input_section, o_amount, (0, 1))

    entryreason = ttk.Text(input_section, width=20,
                           height=5, font=('Open Sans', 14))
    date = ttk.StringVar()
    entrydate = ttk.DateEntry(
        input_section, width=20, dateformat=r"%d/%m/%Y", bootstyle="primary")
    entrydate.entry.config(textvariable=date)

# packing
    entryreason.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
    entrydate.grid(row=2, column=1, padx=5, pady=5)

########################################## Section3 Section ######################################################

    setting.Section3Btn(section3, "H", (insert_data,
                        update_data, delete_data, clear))

########################################## Tree Section ######################################################

    columns = ("ID", "Reason", "Amount", "Date")

    width = (40, 200, 200, 120)
    txt = ("ID", "Reason", "Amount", "Date")
    lstVars = (entryreason, o_amount, date)
    otherexpense_tree = setting.MainTree(frame=other_expense_frame, col=columns, grd=(
        3, 0), width=width, txt=txt, read=conn.read(), lstVar=lstVars, n_text=4)

    other_expense_frame.configure(width=Width, height=Height)
    other_expense_frame.pack()
