import tkinter as tk
import ttkbootstrap as ttk
from functions import convert_date, on_click, reverse
import sqlite3
from modules.login import loginsection
import modules.settings as setting
import modules.connect as connect

conn1 = connect.MainDB(table="RawMaterialPartyInfo")
conn2 = connect.MainDB(table="RawMaterialTransactionInfo")


def raw_material_section(main_frame, Width, Height):
    # style = ttk.Style()
    # style.configure('O.TButton', background="#3984f7", font=('Open Sans', 14,),
    #                 foreground='white')

    def hide_menu_indicator():
        addPartyIndicate.config(bg='#c3c3c3')
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
        varName = tk.StringVar()
        varPhone = tk.StringVar()
        varGstno = tk.StringVar()

        def insert_data():
            Name = varName.get()
            Address = entryAddress.get(1.0, "end-1c")
            Phone_no = varPhone.get()
            Gst_no = varGstno.get()
            if id == "" or id == " ":
                return on_click('Id')
            if Name == "" or Name == " ":
                return on_click('Name')
            if Address == "" or Address == " ":
                return on_click('Address')
            if Phone_no == "" or Phone_no == " ":
                return on_click('Phone no')
            if Gst_no == "" or Gst_no == " ":
                return on_click('GST NO.')
            else:
                conn1.insert((str(Name), str(Address),
                              str(Phone_no), str(Gst_no), "N"))

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

        def delete_data():
            selected_party = tree.Tree.selection()[0]
            deleteData = str(tree.Tree.item(
                selected_party)['values'][0])
            conn1.delete((deleteData,), "partyID")

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
            conn1.update((varName.get(), entryAddress.get(1.0, "end-1c"),
                         varPhone.get(), varGstno.get(), update_name))

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

        def clear():
            for var in lstVars:
                if var == entryAddress:
                    var.delete(1.0, tk.END)
                else:
                    var.set("")

    ################################# Content Section (Add Party Frame) ######################################################

        add_party_frame = ttk.Frame(contentSection)

        partyinfo = ttk.LabelFrame(
            add_party_frame, text="Party Information", bootstyle="primary")

        section3 = ttk.LabelFrame(
            add_party_frame, text="Operations", bootstyle="primary")

        # labels
        lb = ttk.Label(add_party_frame, text='Add Party Details',
                       font=('Open Sans', 20, "bold"))

        lb.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        partyinfo.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        section3.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        

    ########################################## PartyInfo Section ######################################################
    # labels
        lstText = ("Party Name", "Address", "Phone No.", "GST No.")
        for i in range(len(lstText)):
            setting.ContentLabel(partyinfo, lstText[i], (i, 0))

    # entry
        setting.ContentEntry(partyinfo, varName, (0, 1))
        setting.ContentEntry(partyinfo, varPhone, (2, 1))
        setting.ContentEntry(partyinfo, varGstno, (3, 1))

        entryAddress = ttk.Text(partyinfo, width=20,
                                height=5, font=('Open Sans', 11))

    # packing
        entryAddress.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

    ########################################## Section3 Section ######################################################

        setting.Section3Btn(section3, "V", (insert_data,
                            update_data, delete_data, clear))

    ########################################## Tree Section ######################################################

        columns = ("ID", "Name", "Address", "Phone No.", "Gst No.")

        width = (50, 200, 250, 150, 150)
        txt = ("ID", "Name", "Address", "Phone No.", "GST No.")
        lstVars = (varName, entryAddress, varPhone, varGstno)
        tree = setting.MainTree(frame=add_party_frame, col=columns, grd=(
            2, 0), width=width, txt=txt, read=conn1.partyread(), lstVar=lstVars)

        for i in range(3):
            tk.Grid.rowconfigure(add_party_frame, i, weight=2)
        for j in range(3):
            tk.Grid.grid_columnconfigure(add_party_frame, j, weight=2)

        add_party_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
        # contentSection.grid_rowconfigure(0,weight=2)
        # contentSection.grid_columnconfigure(0,weight=2)

    ################################### end of addparty page #######################################

    def add_transaction_page():
        t_partyname = tk.StringVar()
        t_partyPhone = tk.StringVar()
        t_partygstno = tk.StringVar()
        t_partyamount = tk.StringVar()
        t_partyprice = tk.StringVar()
        t_totalamount = tk.StringVar()
        t_Partyvehicle = tk.StringVar()
        t_Partypurchase = tk.StringVar()

        def insert_data():
            findtotal()
            Name = t_partyname.get()
            Address = entryAddress.get(1.0, "end-1c")
            Phone_no = t_partyPhone.get()
            Gst_no = t_partygstno.get()
            Raw_material = rawmaterial.get()
            Amount = t_partyamount.get()
            Price = t_partyprice.get()
            Total = t_totalamount.get()
            vehicleNo = t_Partyvehicle.get()
            Purchasedate = entrypurchasedate.entry.get()
            if Name == "" or Name == " ":
                return on_click('Name')
            if Address == "" or Address == " ":
                return on_click('Address')
            if Phone_no == "" or Phone_no == " ":
                return on_click('Phone no')
            if Gst_no == "" or Gst_no == " ":
                return on_click('GST NO.')
            if Raw_material == "" or Raw_material == " ":
                return on_click('Raw material')
            if Amount == "" or Amount == " ":
                return on_click('Amount')
            if Price == "" or Price == " ":
                return on_click('Price')
            if Total == "" or Price == " ":
                return on_click('Total')
            if vehicleNo == "" or vehicleNo == " ":
                return on_click('vehicleNo')
            if Purchasedate == "" or Purchasedate == " ":
                return on_click('Purchase date')
            else:
                partyid = conn1.get_partyid(phnum=Phone_no)
                # print(partyid)
                conn2.insert((partyid, Raw_material,
                             Amount, Price, Total, vehicleNo, Purchasedate, convert_date(Purchasedate)))

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.treeview())):
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
            findtotal()
            try:
                conn1.update((t_partyname.get(), entryAddress.get(1.0, "end-1c"),
                              t_partyname.get(), t_partygstno.get(), update_name))
            except:
                pass
            selected_party = tree.Tree.selection()[0]
            update_name = tree.Tree.item(selected_party)['values'][0]
            conn2.update((rawmaterial.get(), t_partyamount.get(), t_partyprice.get(
            ), t_totalamount.get(), t_Partyvehicle.get(), entrypurchasedate.entry.get(), convert_date(entrypurchasedate.entry.get()), update_name))

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.treeview())):
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
            conn2.delete((deleteData,), "tID")

            for data in tree.Tree.get_children():
                tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.treeview())):
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

        def getpartyname():
            results = conn1.get_partyname()
            # print(results)
            Partylist = [partyname[0] for partyname in results]
            Partylist.append('General')
            return Partylist

        def viewparty(selection):
            if selection == 'General':
                partyname.entry.config(state="normal")
                partyphonenumber.entry.config(state="normal")
                partygst.entry.config(state="normal")
            else:
                partyinfo = conn1.view_party(selection)
                # print(partyinfo)
                t_partyname.set(partyinfo[0][1])
                entryAddress.delete(1.0, tk.END)
                entryAddress.insert(tk.END, partyinfo[0][2])
                # entryAddress.config(state="normal")
                t_partygstno.set(partyinfo[0][4])
                t_partyPhone.set(partyinfo[0][3])

        def findtotal():
            amount = t_partyamount.get()
            price = t_partyprice.get()
            if amount == "" or amount == " ":
                return on_click('Material')
            if price == "" or price == " ":
                return on_click('Price')
            total = float(amount) * float(price)
            t_totalamount.set(total)

        def clear():
            for var in lstVars:
                if var == entryAddress:
                    var.delete(1.0, tk.END)
                else:
                    var.set("")
            entrypartyselect.set("Select Party name")
            partyname.entry.config(state="readonly")
            partyphonenumber.entry.config(state="readonly")
            partygst.entry.config(state="readonly")

        def insertval():
            # print("Button has been clicked")
            if entrypartyselect.get() == "General":
                try:
                    conn1.insert((t_partyname.get(), entryAddress.get(
                        1.0, "end-1c"), t_partyPhone.get(), t_partygstno.get(), "Y"))
                except:
                    pass
            else:
                pass

    ############################ Content (Add Transaction) ############################################

        add_transaction_frame = ttk.Frame(contentSection)

        ttk.Label(add_transaction_frame, text="Add Transaction Details", font=("Open Sans", 20, "bold")).grid(
            row=0, column=0, columnspan=2, padx=15, pady=15)

        rawmaterialinfo = ttk.LabelFrame(
            add_transaction_frame, text="Raw material Information", bootstyle="primary")

        transactionparty = ttk.LabelFrame(
            add_transaction_frame, bootstyle="primary", text="Select Party")

        section3 = ttk.LabelFrame(
            add_transaction_frame, bootstyle="primary", text="Operations")

        rawmaterialinfo.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        transactionparty.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        section3.grid(row=2, column=0, columnspan=1,
                      padx=10, pady=10, sticky="nsew")

    ############################ Transactionparty frame ############################################

        # labels
        lstText = ("Select Party", "Name", "Address", "Phone no.", "Gst No.")
        for i in range(5):
            setting.ContentLabel(
                transactionparty, lstText[i], (i, 0), f_size=9)

        # optionmenu
        nameList = getpartyname()
        # print(nameList)
        entrypartyselect = tk.StringVar(transactionparty)
        entrypartyselect.set("Select Party name")
        setting.MenuBtn(transactionparty, entrypartyselect, nameList,
                        (0, 1), lambda: viewparty(entrypartyselect.get()))
        # entry
        partyname = setting.ContentEntry(transactionparty, t_partyname,
                                         (1, 1), f_size=11)
        partyname.entry.config(state="readonly")
        partyphonenumber = setting.ContentEntry(transactionparty, t_partyPhone,
                                                (3, 1), f_size=11)
        partyphonenumber.entry.config(state="readonly")
        partygst = setting.ContentEntry(transactionparty, t_partygstno,
                                        (4, 1), f_size=11)
        partygst.entry.config(state="readonly")

        entryAddress = ttk.Text(transactionparty, width=20,
                                height=5, font=('Open Sans', 11))

        # griding entry
        # entrypartyselect.grid(row=0, column=1, padx=5, pady=5)
        entryAddress.grid(row=2, column=1, padx=5, pady=5)

    #################################### rawMaterialInfo frame #####################################

        # labels
        lstText2 = ('Purchase Date', 'Select Raw material', 'Material(in Tonn)',
                    'Price(per Tonn)', 'Total Price', 'Vehicle No.')

        for i in range(len(lstText2)):
            setting.ContentLabel(
                rawmaterialinfo, lstText2[i], (i, 0), f_size=9)

        # radio buttons
        rawmaterial = tk.StringVar()
        lstText3 = ("FlyAsh", "Dust", "Cement", "Admixture", "Others")

        for i in range(5):
            try:
                ttk.Radiobutton(rawmaterialinfo, text=lstText3[i], command=insertval, variable=rawmaterial, bootstyle="success-toolbutton",
                                value=lstText3[i]).grid(row=1, column=i+1, padx=5, pady=5)
            except:
                pass

        # entry
        setting.ContentEntry(rawmaterialinfo, t_partyamount,
                             (2, 1), colspan=3, f_size=11)
        setting.ContentEntry(rawmaterialinfo, t_partyprice,
                             (3, 1), colspan=3, f_size=11)
        setting.ContentEntry(rawmaterialinfo, t_totalamount,
                             (4, 1), colspan=3, f_size=11).entry.config(state="readonly", textvariable=t_totalamount)
        setting.ContentEntry(rawmaterialinfo, t_Partyvehicle,
                             (5, 1), colspan=3, f_size=11)
        entrypurchasedate = ttk.DateEntry(
            rawmaterialinfo, width=20, dateformat=r"%d/%m/%Y", bootstyle="primary")

        # griding entries
        entrypurchasedate.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

    ######################################## Section3 frame #####################################

        setting.Section3Btn(section3, grd="H", cmd=(
            insert_data, update_data, delete_data, clear))

    ######################################## tree section #######################################

        columns = ("ID", "Name", "Address", "Phone No.", "Gst No.",
                   "Raw material", "Amount", "Price", "Total", "Vehicle No.", "Purchase date")

        width = (40, 80, 130, 80, 130, 80, 65, 55, 65, 130, 130)
        txt = ("ID", "Name", "Address", "PhoneNo.", "GstNo.",
               "RawMaterial", "Amt", "Price", "Total", "VehicleNo.", "D.O.P")
        lstVars = (t_partyname, entryAddress, t_partyPhone, t_partygstno, rawmaterial, t_partyamount, t_partyprice, t_totalamount, t_Partyvehicle, t_Partypurchase
                   )
        tree = setting.MainTree(frame=add_transaction_frame, col=columns, grd=(
            3, 0), width=width, txt=txt, read=conn2.treeview(), lstVar=lstVars, Text="Y",c_fsize=9, height=5)

        add_transaction_frame.grid(row=0, column=1)

    ############################### End of transaction details ################################

    # style.configure('Main.TButton', background="#3984f7", font=('Open Sans', 14,),
    #                 foreground='white')

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
    setting.MainBtn(menuSection, txt="Add Party", cmd=lambda: menu_indicate(
        addPartyIndicate, add_party_page), grd=(0, 0))
    setting.MainBtn(menuSection, txt="Add Transaction", cmd=lambda: menu_indicate(
        addTransactionIndicate, add_transaction_page), grd=(0, 1))

    # Labels
    addPartyIndicate = setting.MainLabel(menuSection, 120, (1, 0))
    addTransactionIndicate = setting.MainLabel(menuSection, 120, (1, 1))

    ################################### Pack section #############################################
    menuSection.configure(width=Width, height=Height)
    menuSection.pack(side="top", anchor="n", fill="x")
    contentSection.configure(width=Width, height=Height)
    contentSection.pack()
