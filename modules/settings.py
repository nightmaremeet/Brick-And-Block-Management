import ttkbootstrap as ttk

import tkinter as tk
import functions
from ttkbootstrap.tableview import Tableview
# for Menu section


class MainBtn:
    def __init__(self, frame, cmd, txt, grd):

        style = ttk.Style()
        style.configure('Main.TButton', background="#3984f7", font=('Open Sans', 14),
                        foreground='white')
        tk.Grid.rowconfigure(frame, grd[0], weight=1)
        tk.Grid.columnconfigure(frame, grd[1], weight=1)
        ttk.Button(frame, command=cmd, text=txt, style="Main.TButton").grid(
            row=grd[0], column=grd[1], sticky="nsew", padx=(50, 20), pady=(50, 0))

# for Indication Label


class MainLabel():
    def __init__(self, frame, width, grd):
        self.lbl = tk.Label(
            frame, text=' ', bg='#3984f7', width=width, height=1, font=("Open Sans", 1))
        self.lbl.grid(row=grd[0], column=grd[1], sticky="n", padx=(50, 20))

    def config(self, bg):
        self.lbl.config(bg=bg)

# for section3


class Section3Btn:
    def __init__(self, frame, grd="V", cmd=(), px=5, py=5) -> None:
        self.buttonInsert = ttk.Button(
            frame, text='Add', command=cmd[0], bootstyle="success",
        )
        self.buttonUpdate = ttk.Button(
            frame, text='Update', command=cmd[1], bootstyle="info"
        )
        self.buttonDelete = ttk.Button(
            frame, text='Delete', command=cmd[2], bootstyle="danger"
        )
        self.buttonClear = ttk.Button(
            frame, text='Clear', command=cmd[3], bootstyle="warning"
        )
        if grd == "V":
            self.buttonInsert.grid(
                row=0, column=0, pady=py, padx=px, sticky="nsew")
            self.buttonUpdate.grid(
                row=1, column=0, pady=py, padx=px, sticky="nsew")
            self.buttonDelete.grid(
                row=2, column=0, pady=py, padx=px, sticky="nsew")
            self.buttonClear.grid(
                row=3, column=0, pady=py, padx=px, sticky="nsew")
        else:
            self.buttonInsert.grid(
                row=0, column=0, padx=px, pady=py, sticky="nsew")
            self.buttonUpdate.grid(
                row=0, column=1, padx=px, pady=py, sticky="nsew")
            self.buttonDelete.grid(
                row=0, column=2, padx=px, pady=py, sticky="nsew")
            self.buttonClear.grid(row=0, column=3, padx=px,
                                  pady=py, sticky="nsew")

# for tree


class MainTree:
    def __init__(self, frame, col, txt, width, lstVar, read, grd, h_fsize=14, c_fsize=11, rh=20, hrh=8, px=5, py=5, Text="Y", n_text=1, height=10) -> None:
        self.Text = Text
        self.n_text = n_text
        tk.Grid.rowconfigure(frame, grd[0], weight=1)
        tk.Grid.columnconfigure(frame, grd[1], weight=1)

        self.style = ttk.Style()
        self.style.configure("My.Treeview", rowheight=rh)
        self.style.configure("Treeview.Heading", font=(
            'Open Sans', h_fsize), background="#5191f0", foreground="white", rowheight=hrh)

        self.Tree = ttk.Treeview(
            frame, bootstyle="primary", style="My.Treeview", height=height)
        self.lstVar = lstVar
        self.Tree['columns'] = col
        self.Tree.column("#0", width=0, stretch=tk.NO)
        for index, (column, w) in enumerate(zip(col, width)):
            self.Tree.column(column, anchor=tk.W, width=w)
            self.Tree.heading(
                column, text=txt[index], anchor=tk.W)
        self.Tree.bind('<Double 1>', self.getrow)

        for data in self.Tree.get_children():
            self.Tree.delete(data)

        for i, result in enumerate(functions.reverse(read)):
            if i % 2 == 0:
                self.Tree.insert(
                    parent='', index='end', text="", values=(result), tag="orow")
            else:
                self.Tree.insert(
                    parent='', index='end', text="", values=(result), tag="erow")

        vs = ttk.Scrollbar(frame, bootstyle="primary-round",
                           orient="vertical", command=self.Tree.yview)
        self.Tree.config(yscrollcommand=vs.set(0, 1))
        vs.grid(row=grd[0], column=grd[1]+2, sticky=tk.NS)
        hs = ttk.Scrollbar(frame, bootstyle="primary-round",
                           orient="horizontal", command=self.Tree.xview)
        self.Tree.config(xscrollcommand=hs.set(0, 1))
        hs.grid(row=grd[0]+1, column=grd[1], columnspan=2, sticky=tk.EW)

        self.Tree.tag_configure(
            'orow', background='#faf9f5', font=('Open Sans', c_fsize))
        self.Tree.tag_configure(
            'erow', background='#d1e2ff', font=('Open Sans', c_fsize))

        self.Tree.grid(
            row=grd[0], column=grd[1], columnspan=2, sticky="nsew", padx=px, pady=py)

    def getrow(self, event):
        rowId = self.Tree.identify_row(event.y)
        item = self.Tree.item(self.Tree.focus())
        if self.Text == "Y":
            if self.n_text == 1:
                for i in range(len(self.lstVar)):
                    if i == 1:
                        self.lstVar[i].delete(1.0, tk.END)
                        self.lstVar[i].insert(tk.END, item['values'][i+1])
                    else:
                        self.lstVar[i].set(item['values'][i+1])
            elif self.n_text == 3:
                for i in range(len(self.lstVar)):
                    if i == 1 or i == len(self.lstVar)-2 or i == len(self.lstVar)-1:
                        self.lstVar[i].delete(1.0, tk.END)
                        self.lstVar[i].insert(tk.END, item['values'][i+1])
                    else:
                        self.lstVar[i].set(item['values'][i+1])
            elif self.n_text == 2:
                for i in range(len(self.lstVar)):
                    if i == len(self.lstVar)-5:
                        self.lstVar[i].delete(1.0, tk.END)
                        self.lstVar[i].insert(tk.END, item['values'][i+1])
                    else:
                        self.lstVar[i].set(item['values'][i+1])
            elif self.n_text == 4:
                for i in range(len(self.lstVar)):
                    if i == 0:
                        self.lstVar[i].delete(1.0, tk.END)
                        self.lstVar[i].insert(tk.END, item['values'][i+1])
                    else:
                        self.lstVar[i].set(item['values'][i+1])
            else:
                for i in range(len(self.lstVar)):
                    if i == len(self.lstVar)-1:
                        self.lstVar[i].delete(1.0, tk.END)
                        self.lstVar[i].insert(tk.END, item['values'][i+1])
                    else:
                        self.lstVar[i].set(item['values'][i+1])
        else:
            for i in range(len(self.lstVar)):
                self.lstVar[i].set(item['values'][i+1])

# for all entries in content


class ContentEntry:
    def __init__(self, frame, var, grd, colspan=1, rowspan=1, f_size=9, width=20, px=5, py=5) -> None:
        self.entry = ttk.Entry(frame, width=width,
                               font=('Open Sans', f_size), textvariable=var)
        self.entry.grid(row=grd[0], column=grd[1],
                        columnspan=colspan, rowspan=rowspan, padx=px, pady=py)


class ContentLabel:
    def __init__(self, frame, txt="", grd=(), f_size=9, var=None) -> None:
        self.label = ttk.Label(frame, textvariable=var, text=txt,
                               font=('Open Sans', f_size), anchor="w")
        self.label.grid(row=grd[0], column=grd[1], padx=5, pady=5)


class MenuBtn:
    def __init__(self, frame, var, label, grd, cmd=None) -> None:
        self.var = var
        self.menu = ttk.Menu(frame)
        self.menubtn = ttk.Menubutton(
            frame, textvariable=var, bootstyle="primary-outline", menu=self.menu, direction="flush")
        for i in label:
            self.menu.add_radiobutton(
                label=i, value=i, variable=var, command=cmd, activebackground="#3984f7")
        self.menubtn.grid(row=grd[0], column=grd[1], padx=5, pady=5)

    def get(self):
        return self.var.get()


class Table:
    def __init__(self, frame, col, read, grd, px=5, py=5, rh=4, h_fsize=9, hrh=20) -> None:
        # self.lstVar = lstVar
        # self.n_text = n_text
        # self.Text = Text
        # print(col)
        tk.Grid.rowconfigure(frame, grd[0], weight=1)
        tk.Grid.columnconfigure(frame, grd[1], weight=1)
        self.style = ttk.Style()
        # print(col)
        # print(read)
        self.style.configure("Treeview", font=(
            'Open Sans', 9))
        self.style.configure("Treeview.Heading", font=(
            'Open Sans', h_fsize, "bold"), background="#5191f0", foreground="white", rowheight=hrh)
        # print(read)
        self.tbl = Tableview(frame,
                             bootstyle="primary",
                             coldata=col,
                             rowdata=read,
                             searchable=True,
                             paginated=True,
                             # autofit=True,
                             pagesize=10,
                             height=20
                             )
        # self.tbl.config(style="Treeview")
        self.tbl.align_column_center()
        self.tbl.align_heading_center()
        # self.tbl.bind('<Double 1>', self.getrow)
        # for result in functions.reverse(read):
        #     self.tbl.insert_row("end", result)
        # self.tbl.reset_table()

        self.tbl.grid(
            row=grd[0], column=grd[1], columnspan=2, sticky="nsew", padx=px, pady=py)
    # def getrow(self, event):
    #     rowId = self.tbl.identify(y=event.y)
    #     item = self.tbl.getrow(self.tbl.focus())
    #     if self.Text == "Y":
    #         if self.n_text == 1:
    #             for i in range(len(self.lstVar)):
    #                 if i == 1:
    #                     self.lstVar[i].delete(1.0, tk.END)
    #                     self.lstVar[i].insert(tk.END, item['values'][i+1])
    #                 else:
    #                     self.lstVar[i].set(item['values'][i+1])
    #         elif self.n_text == 3:
    #             for i in range(len(self.lstVar)):
    #                 if i == 1 or i == len(self.lstVar)-2 or i == len(self.lstVar)-1:
    #                     self.lstVar[i].delete(1.0, tk.END)
    #                     self.lstVar[i].insert(tk.END, item['values'][i+1])
    #                 else:
    #                     self.lstVar[i].set(item['values'][i+1])
    #         elif self.n_text == 2:
    #             for i in range(len(self.lstVar)):
    #                 if i == len(self.lstVar)-5:
    #                     self.lstVar[i].delete(1.0, tk.END)
    #                     self.lstVar[i].insert(tk.END, item['values'][i+1])
    #                 else:
    #                     self.lstVar[i].set(item['values'][i+1])
    #         else:
    #             for i in range(len(self.lstVar)):
    #                 if i == len(self.lstVar)-1:
    #                     self.lstVar[i].delete(1.0, tk.END)
    #                     self.lstVar[i].insert(tk.END, item['values'][i+1])
    #                 else:
    #                     self.lstVar[i].set(item['values'][i+1])
    #     else:
    #         for i in range(len(self.lstVar)):
    #             self.lstVar[i].set(item['values'][i+1])
