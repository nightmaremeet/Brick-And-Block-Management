import tkinter as tk
import ttkbootstrap as ttk
from functions import on_click, reverse, convert_date
from modules.login import loginsection
import modules.settings as setting
import modules.connect as connect

conn1 = connect.MainDB(table="LabourInfo")
conn2 = connect.MainDB(table="LabourTransactionInfo")
conn3 = connect.MainDB(table="dates")

def labour_section(main_frame, Width, Height):
    style = ttk.Style()
    style.configure('O.TButton', background="#3984f7", font=('Open Sans', 14,),
                    foreground='white')

    def hide_menu_indicator():
        addLabourIndicate.config(bg='#c3c3c3')
        addTransactionIndicate.config(bg='#c3c3c3')

    def delete_pages():
        for frame in contentSection.winfo_children():
            frame.grid_forget()

    def menu_indicate(lb, page):
        hide_menu_indicator()
        lb.config(bg='#158aff')
        delete_pages()
        page()

    def add_party_page():
        varHeadName = tk.StringVar()
        varAadharnum = tk.StringVar()
        varPhone = tk.StringVar()
        varBlockChrg = tk.StringVar()
        varBrickChrg = tk.StringVar()
        varTracLchargeBrick = tk.StringVar()
        varTracLchargeBlock = tk.StringVar()
        varTracUchargeBrick = tk.StringVar()
        varTracUchargeBlock = tk.StringVar()
        varDumpLchargeBrick = tk.StringVar()
        varDumpLchargeBlock = tk.StringVar()
        varDumpUchargeBrick = tk.StringVar()
        varDumpUchargeBlock = tk.StringVar()

        def insert_data():
            Head_name = varHeadName.get()
            Aadarnum = varAadharnum.get()
            Phone_no = varPhone.get()
            Blocks = varBlockChrg.get()
            Bricks = varBrickChrg.get()
            LTracChrgeBrick = varTracLchargeBrick.get()
            LTracChrgeBlock = varTracLchargeBlock.get()
            UTracChrgeBrick = varTracUchargeBrick.get()
            UTracChrgeBlock = varTracUchargeBlock.get()
            LDumpchrgeBrick = varDumpLchargeBrick.get()
            LDumpchrgeBlock = varDumpLchargeBlock.get()
            UDumpchrgeBrick = varDumpUchargeBrick.get()
            UDumpchrgeBlock = varDumpUchargeBlock.get()
            if Head_name == "" or Head_name == " ":
                return on_click("Labour's Head")
            if Aadarnum == "" or Aadarnum == " ":
                return on_click('Aadhar Card Number')
            if Phone_no == "" or Phone_no == " ":
                return on_click('Phone no')
            if Blocks == "" or Blocks == " ":
                return on_click('Blocks Charges')
            if Bricks == "" or Bricks == " ":
                return on_click('Bricks Charges')
            if LTracChrgeBrick == "" or LTracChrgeBrick == " ":
                return on_click('Tractor Brick Loading Charges')
            if LTracChrgeBlock == "" or LTracChrgeBlock == " ":
                return on_click('Tractor Block Loading Charges')
            if UTracChrgeBrick == "" or UTracChrgeBrick == " ":
                return on_click('Tractor Brick Unloading Charges')
            if UTracChrgeBlock == "" or UTracChrgeBlock == " ":
                return on_click('Tractor Block Unloading Charges')
            if LDumpchrgeBrick == "" or LDumpchrgeBrick == " ":
                return on_click('Dumper Brick Loading Charges')
            if UDumpchrgeBlock == "" or UDumpchrgeBlock == " ":
                return on_click('Dumper Block Unloading Charges')
            if LDumpchrgeBlock == "" or LDumpchrgeBlock == " ":
                return on_click('Dumper Block Loading Charges')
            if UDumpchrgeBrick == "" or UDumpchrgeBrick == " ":
                return on_click('Dumper Brick Unloading Charges')
            else:
                conn1.insert((Head_name, Aadarnum, Phone_no, Blocks, Bricks,
                             LTracChrgeBrick, LTracChrgeBlock, UTracChrgeBrick, UTracChrgeBlock, LDumpchrgeBrick,
                             LDumpchrgeBlock, UDumpchrgeBrick, UDumpchrgeBlock))

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.read())):
                if i % 2 == 0:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def delete_data():
            selected_party = tree.Tree.selection()[0]
            deleteData = str(tree.Tree.item(
                selected_party)['values'][0])
            conn1.delete((deleteData,), "labourID")

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.partyread())):
                if i % 2 == 0:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def update_data():

            selected_party = tree.Tree.selection()[0]
            update_name = tree.Tree.item(selected_party)[
                'values'][0]
            conn1.update((varHeadName.get(), varAadharnum.get(), varPhone.get(), varBlockChrg.get(), varBrickChrg.get(
            ), varTracLchargeBrick.get(), varTracLchargeBlock.get(), varTracUchargeBrick.get(), varTracUchargeBlock.get(), varDumpLchargeBrick.get(), varDumpLchargeBlock.get(), varDumpUchargeBrick.get(), varDumpUchargeBlock.get(), update_name))

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.read())):
                if i % 2 == 0:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def clear():
            for var in lstVars:
                var.set("")

    ################################# Content Section (Add Party Frame) ######################################################

        add_party_frame = ttk.Frame(contentSection)

        partyinfo = ttk.LabelFrame(
            add_party_frame, text="Labour Information", bootstyle="primary")

        section3 = ttk.LabelFrame(
            add_party_frame, text="Operations", bootstyle="primary")

        chargesinfo = ttk.LabelFrame(
            add_party_frame, text="Charges", bootstyle="primary"
        )

        # labels
        lb = ttk.Label(add_party_frame, text='Add Labour Head Details',
                       font=('Open Sans', 20, "bold"))

        lb.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        partyinfo.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        chargesinfo.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        section3.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    ########################################## PartyInfo Section ######################################################
    # labels
        lstText = ("Labour Head Name", "Aadhar Card no.", "Phone Number",
                   "Block Charges(per unit)", "Brick Charges(per unit)")
        for i in range(len(lstText)):
            setting.ContentLabel(partyinfo, lstText[i], (i, 0))

        setting.ContentLabel(chargesinfo, "Brick", (0, 1))
        setting.ContentLabel(chargesinfo, "Block", (0, 2))

        setting.ContentLabel(chargesinfo, "Tractor Loading Charges", (1, 0))
        setting.ContentEntry(chargesinfo, varTracLchargeBrick, (1, 1))
        setting.ContentEntry(chargesinfo, varTracLchargeBlock, (1, 2))

        setting.ContentLabel(chargesinfo, "Tractor Unloading Charges", (2, 0))
        setting.ContentEntry(chargesinfo, varTracUchargeBrick, (2, 1))
        setting.ContentEntry(chargesinfo, varTracUchargeBlock, (2, 2))

        setting.ContentLabel(chargesinfo, "Dumper Loading Charge", (3, 0))
        setting.ContentEntry(chargesinfo, varDumpLchargeBrick, (3, 1))
        setting.ContentEntry(chargesinfo, varDumpLchargeBlock, (3, 2))

        setting.ContentLabel(chargesinfo, "Dumper Unloading Charge", (4, 0))
        setting.ContentEntry(chargesinfo, varDumpUchargeBrick, (4, 1))
        setting.ContentEntry(chargesinfo, varDumpUchargeBlock, (4, 2))

    # entry
        setting.ContentEntry(partyinfo, varHeadName, (0, 1))
        setting.ContentEntry(partyinfo, varAadharnum, (1, 1))
        setting.ContentEntry(partyinfo, varPhone, (2, 1))
        setting.ContentEntry(partyinfo, varBlockChrg, (3, 1))
        setting.ContentEntry(partyinfo, varBrickChrg, (4, 1))

    ########################################## Section3 Section ######################################################

        setting.Section3Btn(section3, "H", (insert_data,
                            update_data, delete_data, clear))

    ########################################## Tree Section ######################################################

        columns = ("ID", "Labour Head", "Aadhar No.",
                   "Phnum", "Block Charges", "Brick Charges", "TracLoad(Brick)", "TracLoad(Block)", "TracUnload(Brick)", "TracUnload(Block)", "DumpLoad(Brick)", "DumpLoad(Block)", "DumpUnload(Brick)", "DumpUndload(Block)")

        width = (50, 120, 70, 70, 70, 70, 70, 80, 70, 70,70,70,70,70)
        txt = ("ID", "Labour Head", "Aadhar No.",
               "Phnum", "Block Charges", "Brick Charges", "TracLoad(Brick)", "TracLoad(Block)", "TracUnload(Brick)", "TracUnload(Block)", "DumpLoad(Brick)", "DumpLoad(Block)", "DumpUnload(Brick)", "DumpUndload(Block)")
        lstVars = (varHeadName, varAadharnum,
                   varPhone, varBlockChrg, varBrickChrg, varTracLchargeBrick, varTracLchargeBlock, varTracUchargeBrick, varTracUchargeBlock, varDumpLchargeBrick, varDumpLchargeBlock, varDumpUchargeBrick, varDumpUchargeBlock)
        tree = setting.MainTree(frame=add_party_frame, col=columns, grd=(
            2, 0), width=width, txt=txt, read=conn1.read(), lstVar=lstVars, n_text=2, Text="N", h_fsize=11)

        for i in range(3):
            tk.Grid.rowconfigure(add_party_frame, i, weight=1)
        for j in range(3):
            tk.Grid.columnconfigure(add_party_frame, j, weight=1)

        add_party_frame.grid(row=0, column=0, padx=10, pady=10)

    ################################### end of addparty page #######################################

    def add_transaction_page():
        def insert_data():
            # findtotal()
            headname = t_headname.get()
            advancepayment = t_advancepayment.get()
            advancedate = entryAdvanceDate.get()
            paymenttype = t_paymenttype.get()
            if headname == "" or headname == " ":
                return on_click('Head Name')
            if advancepayment == "" or advancepayment == " ":
                return on_click('Advance payment')
            if advancedate == "" or advancedate == " ":
                return on_click('Advance Date')
            else:
                labourid = conn1.get_partyid(headname, "Labour")
                # print(labourid)
                conn2.insert((labourid, paymenttype, advancepayment, headname, advancedate, convert_date(advancedate)))

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)
# 
            for i, result in enumerate(reverse(conn2.treeview(party_type="Labour"))):
                if i % 2 == 0:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))
            labId = conn3.getSaleID("labID", "LabourTransactionInfo")
            try:
                dateID = conn3.getDateId(convert_date(advancedate),"labour")
            except:
                pass
            
            if conn3.checkDateRef(convert_date(advancedate), "labour"):
                conn3.update((labId,dateID),"labour")
            else:
                conn3.insert((convert_date(advancedate), 0, 0, labId, advancedate))
                
        def update_data():
            selected_party = tree.Tree.selection()[0]
            update_name = tree.Tree.item(selected_party)['values'][0]
            conn2.update((t_paymenttype.get(), t_advancepayment.get(), t_headname.get(), entryAdvanceDate.get(), convert_date(entryAdvanceDate.get()), update_name))

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn2.treeview(party_type="Labour"))):
                if i % 2 == 0:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def delete_data():
            selected_party = tree.Tree.selection()[0]
            deleteData = str(tree.Tree.item(
                selected_party)['values'][0])
            conn2.delete((deleteData,), "labID")

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn2.treeview(party_type="Labour"))):
                if i % 2 == 0:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def getHeadName():
            results = conn1.get_partyname(party_type="Labour")
            # print(results)
            headName = [headname[0] for headname in results]
            return headName

        def viewparty(selection):
            pass

        def clear():
            for var in lstVars:
                var.set("")
                t_headname.set("Select Head name")

        


    ############################ Content (Add Transaction) ############################################
        t_advancepayment = tk.StringVar()
        t_paymenttype = tk.StringVar()
        add_transaction_frame = ttk.Frame(contentSection)

        ttk.Label(add_transaction_frame, text="Add Labour Transaction Details", font=("Open Sans", 20, "bold")).grid(
            row=0, column=0, columnspan=2, padx=15, pady=15)

        transactionparty = ttk.LabelFrame(
            add_transaction_frame, bootstyle="primary", text="Labour Transaction")

        section3 = ttk.LabelFrame(
            add_transaction_frame, bootstyle="primary", text="Operations")

        transactionparty.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        section3.grid(row=1, column=1, columnspan=1,
                      padx=10, pady=10, sticky="nsew")

    ############################ Transactionparty frame ############################################

        # labels
        ttk.Radiobutton(transactionparty, text="Kharchi", variable=t_paymenttype, bootstyle="success-toolbutton",
                        value="Kharchi").grid(row=0, column=1, padx=15, pady=5, sticky="W")
        ttk.Radiobutton(transactionparty, text="Advance", variable=t_paymenttype, bootstyle="success-toolbutton",
                        value="Advance").grid(row=0, column=1, pady=5, sticky="E")

        lstText = ("Payment Type","Payment Amount", "Select Labour Head", "Payment Date")
        for i in range(len(lstText)):
            setting.ContentLabel(
                transactionparty, lstText[i], (i, 0), f_size=9)

        # optionmenu
        nameList = getHeadName()
        # print(nameList)
        t_headname = tk.StringVar(transactionparty)
        t_headname.set("Select Head")
        setting.MenuBtn(transactionparty, t_headname, nameList,
                        (2, 1), lambda: viewparty(t_headname.get()))
        # entry
        setting.ContentEntry(transactionparty, t_advancepayment,
                             (1, 1), f_size=11)

        entryAdvanceDate = tk.StringVar()
        dt = ttk.DateEntry(
            transactionparty, width=20, dateformat=r"%d/%m/%Y", bootstyle="primary")
        dt.entry.config(textvariable=entryAdvanceDate)

        # griding entries
        dt.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

    ######################################## Section3 frame #####################################

        setting.Section3Btn(section3, grd="V", cmd=(
            insert_data, update_data, delete_data, clear))

    ######################################## tree section #######################################

        columns = ("ID", "Payment Type", "Payment Amount", "Labour Head", "Payment Date")

        width = (40, 200, 200, 200, 200)
        txt = ("ID", "Payment Type", "Payment Amount", "Labour Head","Payment Date")
        lstVars = (t_paymenttype, t_advancepayment, t_headname, entryAdvanceDate)
        tree = setting.MainTree(frame=add_transaction_frame, col=columns, grd=(
            3, 0), width=width, txt=txt, read=conn2.treeview(party_type="Labour"), lstVar=lstVars, Text="N")

        add_transaction_frame.grid(row=0, column=1)

    ############################### End of transaction details ################################

    style.configure('Main.TButton', background="#3984f7", font=('Open Sans', 14,),
                    foreground='white')

    ################################# Frames Section #############################################
    rawMaterialFrame = ttk.Frame(main_frame)
    rawMaterialFrame.pack(fill="both")
    tk.Grid.columnconfigure(rawMaterialFrame, 0, weight=1)
    tk.Grid.rowconfigure(rawMaterialFrame, 0, weight=1)
    tk.Grid.rowconfigure(rawMaterialFrame, 1, weight=0)

    contentSection = ttk.Frame(rawMaterialFrame)
    menuSection = ttk.Frame(rawMaterialFrame, bootstyle="dark")

    ############################## Menu Frame #####################################################

    # Buttons
    setting.MainBtn(menuSection, txt="Add Labour", cmd=lambda: menu_indicate(
        addLabourIndicate, add_party_page), grd=(0, 0))
    setting.MainBtn(menuSection, txt="Labour Transaction", cmd=lambda: menu_indicate(
        addTransactionIndicate, add_transaction_page), grd=(0, 1))

    # Labels
    addLabourIndicate = setting.MainLabel(menuSection, 120, (1, 0))
    addTransactionIndicate = setting.MainLabel(menuSection, 120, (1, 1))

    ################################### Pack section #############################################
    menuSection.configure(width=Width, height=Height)
    menuSection.pack(side="top", anchor="n", fill="x")
    contentSection.configure(width=Width, height=Height)
    contentSection.pack()
