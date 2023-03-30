import tkinter as tk
import ttkbootstrap as ttk
from modules.rawmaterial import raw_material_section
from modules.production import production_section
from modules.selling import selling_section
from modules.expense import expense_section
from modules.labour import labour_section
from modules.report import report_section
from functions import *
from hotreload import run_with_reloader

root = ttk.Window()
root.attributes("-fullscreen", True)
Width = root.winfo_screenwidth()
Height = root.winfo_screenheight()
# root.state('zoomed')
root.title("Brick Management System")
# root.geometry("%dx%d" % (Width, Height))
root.resizable(True, True)
style = ttk.Style()
style.configure('Main.TButton', background="#3984f7", font=('Open Sans', 14,),
                foreground='white')
style.configure('D.TButton', background="#f53636", font=('Open Sans', 14,),
                foreground='white')
# style.configure()


def hide_indicator():
    rawMaterialIndicate.config(background="#3984f7")
    salesIndicate.config(background="#3984f7")
    labourIndicate.config(background="#3984f7")
    expenseIndicate.config(background="#3984f7")
    productionIndicate.config(background="#3984f7")
    reportIndicate.config(background="#3984f7")


def indicate(lb, page):
    hide_indicator()
    lb.config(background="white")
    delete_pages()
    page()


def delete_pages():
    for frame in mainFrame.winfo_children():
        frame.destroy()


def rawMaterialPage():
    raw_material_section(
        mainFrame, mainFrame.winfo_screenheight(), mainFrame.winfo_screenwidth())


def productionPage():
    production_section(mainFrame, mainFrame.winfo_screenheight(),
                       mainFrame.winfo_screenwidth())


def salesPage():
    selling_section(mainFrame, mainFrame.winfo_screenheight(),
                    mainFrame.winfo_screenwidth())


def reportPage():
    report_section(mainFrame, mainFrame.winfo_screenheight(),
                   mainFrame.winfo_screenwidth())


def expensePage():
    expense_section(mainFrame, mainFrame.winfo_screenheight(),
                    mainFrame.winfo_screenwidth())


def labourPage():
    labour_section(mainFrame, mainFrame.winfo_screenheight(),
                   mainFrame.winfo_screenwidth())

############################################### Frames Section #####################################################


optionsFrame = ttk.Frame(root, bootstyle="dark")
mainFrame = ttk.Frame(root)
# ttk.Style(theme="meet")

############################################### OptionsFrame Section ################################################

# Labels
rawMaterialIndicate = tk.Label(
    optionsFrame, text=" ", background="#3984f7", font=('Open Sans', 30,))
productionIndicate = tk.Label(
    optionsFrame, text=" ", background="#3984f7", font=('Open Sans', 30,))
labourIndicate = tk.Label(
    optionsFrame, text=" ", background="#3984f7", font=('Open Sans', 30,))
salesIndicate = tk.Label(
    optionsFrame, text=" ", background="#3984f7", font=('Open Sans', 30,))
reportIndicate = tk.Label(optionsFrame, text=" ",
                          background="#3984f7", font=('Open Sans', 30,))
expenseIndicate = tk.Label(
    optionsFrame, text=" ", background="#3984f7", font=('Open Sans', 30,))

# Buttons
rawMaterialBtn = ttk.Button(optionsFrame, text="Raw Material", style="Main.TButton", bootstyle="link", width=optionsFrame.winfo_screenwidth()//90,
                            command=lambda: indicate(rawMaterialIndicate, rawMaterialPage))
productionBtn = ttk.Button(optionsFrame, text="Production", style="Main.TButton", bootstyle="link", width=optionsFrame.winfo_screenwidth()//90,
                           command=lambda: indicate(productionIndicate, productionPage))
salesBtn = ttk.Button(optionsFrame, text="Sales", style="Main.TButton", bootstyle="link", width=optionsFrame.winfo_screenwidth()//90,
                      command=lambda: indicate(salesIndicate, salesPage))
labourBtn = ttk.Button(optionsFrame, text="Labour", style="Main.TButton", bootstyle="link", width=optionsFrame.winfo_screenwidth()//90,
                       command=lambda: indicate(labourIndicate, labourPage))
reportBtn = ttk.Button(optionsFrame, text="Reports", style="Main.TButton", bootstyle="link", width=optionsFrame.winfo_screenwidth()//90,
                       command=lambda: indicate(reportIndicate, reportPage))
expenseBtn = ttk.Button(optionsFrame, text="Other Expenses", style="Main.TButton", bootstyle="link", width=optionsFrame.winfo_screenwidth()//90,
                        command=lambda: indicate(expenseIndicate, expensePage))
exitBtn = ttk.Button(optionsFrame, text="Exit", style="D.TButton", bootstyle="danger", width=optionsFrame.winfo_screenwidth()//100,
                     command=lambda: root.quit())

# resizing
for i in range(6):
    tk.Grid.rowconfigure(optionsFrame, i, weight=1)
    # row_no += 1
tk.Grid.columnconfigure(optionsFrame, 0, weight=1)
tk.Grid.columnconfigure(optionsFrame, 1, weight=1)


# formatting
rawMaterialBtn.grid(
    row=0, column=1, pady=optionsFrame.winfo_screenheight()//25, padx=(0, 5), sticky="nsew")
productionBtn.grid(
    row=1, column=1, pady=optionsFrame.winfo_screenheight()//25, padx=(0, 5), sticky="nsew")
salesBtn.grid(
    row=2, column=1, pady=optionsFrame.winfo_screenheight()//25, padx=(0, 5), sticky="nsew")
labourBtn.grid(
    row=3, column=1, pady=optionsFrame.winfo_screenheight()//25, padx=(0, 5), sticky="nsew")
reportBtn.grid(
    row=4, column=1, pady=optionsFrame.winfo_screenheight()//25, padx=(0, 5), sticky="nsew")
expenseBtn.grid(
    row=5, column=1, pady=optionsFrame.winfo_screenheight()//25, padx=(0, 5), sticky="nsew")
exitBtn.grid(
    row=6, column=1, pady=optionsFrame.winfo_screenheight()//25, padx=(0, 15), sticky="nsew")

rawMaterialIndicate.grid(row=0, column=0, padx=(
    0, 0), pady=optionsFrame.winfo_screenheight()//25)
productionIndicate.grid(row=1, column=0, padx=(
    0, 0), pady=optionsFrame.winfo_screenheight()//25)
salesIndicate.grid(row=2, column=0, padx=(
    0, 0), pady=optionsFrame.winfo_screenheight()//25)
labourIndicate.grid(row=3, column=0, padx=(
    0, 0), pady=optionsFrame.winfo_screenheight()//25)
reportIndicate.grid(row=4, column=0, padx=(
    0, 0), pady=optionsFrame.winfo_screenheight()//25)
expenseIndicate.grid(row=5, column=0, padx=(
    0, 0), pady=optionsFrame.winfo_screenheight()//25)

############################################### mainFrame Section ################################################
lb = ttk.Label(
    mainFrame, text='Brick and Block Management System', font=('Bold', 30))
lb.grid(row=0, column=1, sticky="nwes", padx=50, pady=50)


############################################### Packing Section ################################################

tk.Grid.rowconfigure(mainFrame, 0, weight=1)
tk.Grid.columnconfigure(mainFrame, 1, weight=1)

for i in range(2):
    for j in range(6):
        tk.Grid.columnconfigure(optionsFrame, i, weight=1)
        tk.Grid.rowconfigure(optionsFrame, j, weight=1)

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=0)
tk.Grid.columnconfigure(root, 1, weight=1)


mainFrame.configure(height=Height, width=Width//40)
mainFrame.grid(row=0, column=1, sticky="nwes")
optionsFrame.configure(height=Height, width=Width//40)
optionsFrame.grid(row=0, column=0, sticky="nwes")


# tk.Grid.columnconfigure(root,0,weight=1)
if __name__ == "__main__":
    # root.mainloop()
    run_with_reloader(root, "<Control-R>", "<Control-r>")

############################################## End Section ########################################################
