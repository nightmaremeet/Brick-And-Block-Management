import os
import tkinter as tk
import ttkbootstrap as ttk
from openpyxl import load_workbook
from functions import convert_date, on_click, reverse, successful
import modules.settings as setting
import modules.connect as connect
conn1 = connect.MainDB("SalesPartyInfo")
conn2 = connect.MainDB("SalesTransactionInfo")
conn3 = connect.MainDB("dates")
#


def selling_section(main_frame, Width, Height):

    def hide_menu_indicator():
        add_party_indicate.config(bg='#c3c3c3')
        add_transaction_indicate.config(bg='#c3c3c3')
        Stock_indicate.config(bg='#c3c3c3')

    def delete_pages():
        for frame in content_section.winfo_children():
            frame.destroy()

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
            Name = str(varName.get())
            Address = str(entryAddress.get(1.0, "end-1c"))
            Phone_no = str(varPhone.get())
            Gst_no = str(varGstno.get())
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
                conn1.insert((Name, Address, Phone_no, Gst_no, "N"))

            for data in my_tree.Tree.get_children():
                my_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.partyread(partytype="Sales"))):
                if i % 2 == 0:
                    my_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    my_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            my_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            my_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def delete_data():
            selected_party = my_tree.Tree.selection()[0]
            deleteData = str(my_tree.Tree.item(selected_party)['values'][0])
            conn1.delete(deleteData, "sID")

            for data in my_tree.Tree.get_children():
                my_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.partyread(partytype="Sales"))):
                if i % 2 == 0:
                    my_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    my_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            my_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            my_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def update_data():
            selected_party = my_tree.Tree.selection()[0]
            update_name = my_tree.Tree.item(selected_party)['values'][0]
            conn1.update((varName.get(), entryAddress.get(1.0, "end-1c"),
                         varPhone.get(), varGstno.get(), update_name))

            for data in my_tree.Tree.get_children():
                my_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.partyread(partytype="Sales"))):
                if i % 2 == 0:
                    my_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    my_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            my_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            my_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def clear():
            for var in lstVars:
                if var == entryAddress:
                    var.delete(1.0, tk.END)
                else:
                    var.set("")

    ################################################ add party frame ###################################################

        add_party_frame = ttk.Frame(content_section)

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

        my_tree = setting.MainTree(frame=add_party_frame, col=columns, grd=(
            2, 0), width=width, txt=txt, read=conn1.partyread(partytype="Sales"), lstVar=lstVars)

        for i in range(3):
            tk.Grid.rowconfigure(add_party_frame, i, weight=1)
        for j in range(3):
            tk.Grid.columnconfigure(add_party_frame, j, weight=1)

        add_party_frame.grid(row=0, column=0, padx=10, pady=10)

    def add_transaction_page():

        def insert_data():
            allcharges()
            Product = entryproduct.get()
            nproduct = t_product.get()
            productprice = t_productprice.get()
            totalprice = t_totalpamount.get()
            vehicletype = vehiclevars.get()
            vehicleNo = t_Partyvehicle.get()
            paymenttype = paymentvars.get()
            loading = t_loading.get()
            unloading = t_unloading.get()
            transport_charges = t_transport_charges.get()
            sellingdate = entrysellingdate.get()
            deliveryaddress = entrydeliveryAddress.get(1.0, "end-1c")
            remarks = entryRemarks.get(1.0, "end-1c")
            lhead = t_headname.get()
            if Product == "Select Product":
                return on_click('Product')
            if nproduct == "" or nproduct == "":
                return on_click("Number of Products")
            if productprice == "" or productprice == "":
                return on_click("Product price")
            if lhead == "" or lhead == " ":
                return on_click("Labour Head")
            if vehicletype == "" or vehicletype == " ":
                return on_click('Vehicle Type')
            if vehicleNo == "" or vehicleNo == " ":
                return on_click('vehicleNo')
            if transport_charges == "" or transport_charges == " ":
                return on_click('Transport Charge')
            if paymenttype == "" or paymenttype == " ":
                return on_click('paymenttype')
            if sellingdate == "" or sellingdate == " ":
                return on_click('Sales date')
            if deliveryaddress == "" or deliveryaddress == " ":
                return on_click('Delivery Address')
            if remarks == "" or remarks == " ":
                return on_click('Remarks')
            else:
                sid = conn1.get_partyid(t_partyPhone.get(), party_type="Sales")
                labourid = conn1.get_partyid(lhead, "Labour")
                conn2.insert((sid, labourid, Product, nproduct, productprice, totalprice, vehicletype, vehicleNo,
                             paymenttype, loading, unloading, transport_charges, sellingdate, deliveryaddress, remarks, convert_date(sellingdate)))

            for data in transaction_tree.Tree.get_children():
                transaction_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.treeview("Sales"))):
                if i % 2 == 0:
                    transaction_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    transaction_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            transaction_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            transaction_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))
            saleID = conn3.getSaleID("salesID", "SalesTransactionInfo")
            try:
                dateID = conn3.getDateId(convert_date(sellingdate), "sales")
            except:
                pass

            if conn3.checkDateRef(convert_date(sellingdate), "sales"):
                conn3.update((saleID, dateID), "sales")
            else:
                conn3.insert((convert_date(sellingdate),
                             0, saleID, 0, sellingdate))

        def update_data():
            # getval()
            allcharges()
            selected_party = transaction_tree.Tree.selection()[0]
            update_name = transaction_tree.Tree.item(selected_party)[
                'values'][0]
            # setvalues('Brick')
            labourid = conn1.get_partyid(t_headname.get(), "Labour")
            conn2.update((labourid, entryproduct.get(), t_product.get(), t_productprice.get(), t_totalpamount.get(), vehiclevars.get(),
                          t_Partyvehicle.get(), paymentvars.get(), t_loading.get(), t_unloading.get(), t_transport_charges.get(), entrysellingdate.get(), entrydeliveryAddress.get(1.0, "end-1c"), entryRemarks.get(1.0, "end-1c"), convert_date(entrysellingdate.get()), update_name))
            for data in transaction_tree.Tree.get_children():
                transaction_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.treeview("Sales"))):
                if i % 2 == 0:
                    transaction_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    transaction_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            transaction_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            transaction_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def delete_data():
            selected_party = transaction_tree.Tree.selection()[0]
            deleteData = str(transaction_tree.Tree.item(
                selected_party)['values'][0])
            conn2.delete((deleteData,), "salesID")

            for data in transaction_tree.Tree.get_children():
                transaction_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.treeview("Sales"))):
                if i % 2 == 0:
                    transaction_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    transaction_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            transaction_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            transaction_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def getpartyname():
            results = conn1.get_partyname('Sales')
            Partylist = [partyname[0] for partyname in results]
            Partylist.append('General')
            return Partylist

        def viewparty(selection):
            if str(selection) == 'General':
                partyname.entry.config(state="normal")
                partyphone.entry.config(state="normal")
                partygst.entry.config(state="normal")
                entryAddress.delete(1.0, tk.END)
                t_partyname.set("")
                t_partyPhone.set("")
                t_partygstno.set("")
            else:
                result = conn1.view_party(selection, "Sales")
                t_partyname.set(result[0][1])
                entryAddress.delete(1.0, tk.END)
                entryAddress.insert(tk.END, result[0][2])
                # entryAddress.config(state=tk.DISABLED)
                t_partyPhone.set(result[0][3])
                t_partygstno.set(result[0][4])

        def setvalues(selection):
            if str(selection) == "Brick":
                setting.ContentLabel(
                    transactionparty, "No of Brick", (0, 2)).label.grid_configure(sticky="n")
            elif str(selection) == "Block":
                setting.ContentLabel(
                    transactionparty, "No of Block", (0, 2)).label.grid_configure(sticky="n")
            setting.ContentLabel(
                transactionparty, "Amount(per Unit)", (2, 2)).label.grid_configure(sticky="n")
            setting.ContentLabel(
                transactionparty, "Total Amount", (3, 2)).label.grid_configure(sticky="n")
            setting.ContentEntry(transactionparty, t_product, (1, 2), px=50)
            setting.ContentEntry(
                transactionparty, t_productprice, (2, 2)).entry.grid_configure(sticky="s")
            setting.ContentEntry(
                transactionparty, t_totalpamount, (4, 2)).entry.config(state="readonly")

        def generate_bill():
            selected_party = transaction_tree.Tree.selection()[0]
            partyid = transaction_tree.Tree.item(selected_party)['values'][0]
            # print(partyid)
            result = conn2.generate_bill((partyid,))
            key = ("ID", "Name", "Address", "Phone No.", "Gst No.", 'Product', 'No of Unit', 'price per unit', 'totalprice',
                   'Vehicle type', 'Vehicle No.', 'Payment Type', 'loading', 'unloading', 'Sales date', 'delivery address', 'remarks', 'Transport Charges')

            res = {}

            for key in key:
                for value in result:
                    res[key] = value
                    result.remove(value)
                    break
            # print(res)
            template = load_workbook("./templates/Bill2.xlsx")
            bill = template.active
            # print(result)
            bill["E4"] = res['ID']
            bill["E3"] = res['Sales date']
            bill["B7"] = res['Name']
            bill["B9"] = res['Address']
            bill["B11"] = res['Phone No.']
            bill["E7"] = res['Gst No.']
            bill["B14"] = res['Product']
            bill["C14"] = res["No of Unit"]
            bill["D14"] = res["price per unit"]
            bill["E14"] = res["totalprice"]
            bill["E19"] = res["totalprice"]
            bill["E9"] = res["Vehicle No."]
            template.save(
                filename=f"./SalesBill/{res['Name']}_{res['ID']}.xlsx")
            successful(f"SalesBill\\{res['Name']}_{res['ID']}.xlsx")

        def clear():
            for var in lstVars:
                if var == entryAddress or var == entrydeliveryAddress or var == entryRemarks:
                    var.delete(1.0, tk.END)
                else:
                    var.set("")
            t_transport_charges.set("0")
            t_loading.set("0")
            t_unloading.set("0")
            t_product.set("0")
            t_productprice.set("0")
            t_totalpamount.set("0")
            partyname.entry.config(state="readonly")
            partyphone.entry.config(state="readonly")
            partygst.entry.config(state="readonly")
            t_partyname.set("")
            t_partyPhone.set("")
            t_partygstno.set("")
            entryproduct.set("Brick")
            entrypartyselect.set('Select Party name')

        def getval():
            ltracchrg, utracchrg, ldumpchrg, udumpchrg = conn2.get_charges(
                t_headname.get(), entryproduct.get())
            if vehiclevars.get() == "Tractor":
                lchr.config(value=ltracchrg, text=ltracchrg)
                uchr.config(value=utracchrg, text=utracchrg)
                t_loading.set(ltracchrg)
                t_unloading.set(utracchrg)
            elif vehiclevars.get() == "Dumper":
                lchr.config(value=ldumpchrg, text=ldumpchrg)
                uchr.config(value=udumpchrg, text=udumpchrg)
                t_loading.set(ldumpchrg)
                t_unloading.set(udumpchrg)
            else:
                lchr.config(value=0)
                uchr.config(value=0)
                t_loading.set("0")
                t_unloading.set("0")

        def allcharges():
            t_totalpamount.set(
                f"{(float(t_product.get())*float(t_productprice.get())) - float(t_transport_charges.get()) - (float(t_product.get()) * float(t_loading.get())) - (float(t_product.get()) * float(t_unloading.get()))}")

        def gen_insert():
            try:
                conn1.insert((t_partyname.get(), entryAddress.get(
                    1.0, tk.END), t_partyPhone.get(), t_partygstno.get(), "Y"))
            except:
                pass

        def viewparty2(selection):
            # ltracchrg, utracchrg, ldumpchrg, udumpchrg = conn2.get_charges(selection)
            # if vehiclevars.get() == "Tractor":
            #     lchr.config(value=ltracchrg, text=ltracchrg)
            #     uchr.config(value=utracchrg, text=utracchrg)
            #     t_loading.set(ltracchrg)
            #     t_unloading.set(utracchrg)
            # elif vehiclevars.get() == "Dumper":
            #     lchr.config(value=ldumpchrg, text=ldumpchrg)
            #     uchr.config(value=udumpchrg, text=udumpchrg)
            #     t_loading.set(ldumpchrg)
            #     t_unloading.set(udumpchrg)
            # else:
            #     lchr.config(value=0)
            #     uchr.config(value=0)
            #     t_loading.set("0")
            #     t_unloading.set("0")
            pass

        def getHeadName():
            results = conn1.get_partyname(party_type="Labour")
            # print(results)
            headName = [headname[0] for headname in results]
            return headName
        
        def on_entry_focus_in(event, type=""):
            if type == 'nproduct':
                t_product.set("")
            elif type == 'productprice':
                t_productprice.set("")
            elif type == "transport":
                t_transport_charges.set("")


############################ Content (Add Transaction) ############################################

        add_transaction_frame = ttk.Frame(content_section)

        ttk.Label(add_transaction_frame, text="Add Transaction Details", font=("Open Sans", 20, "bold")).grid(
            row=0, column=0, columnspan=1, padx=15, pady=15)

        transactioninfo = ttk.LabelFrame(
            add_transaction_frame, text="Transport Information", bootstyle="primary")

        transactionparty = ttk.LabelFrame(
            add_transaction_frame, bootstyle="primary", text="Select Party")

        section3 = ttk.LabelFrame(
            add_transaction_frame, bootstyle="primary", text="Operations")

        transactioncharges = ttk.LabelFrame(
            add_transaction_frame, text="Labour Charges Information", bootstyle="primary")

        section3.grid(row=0, column=1,
                      padx=10, pady=10, sticky="nsew")

        transactionparty.grid(row=1, column=0, rowspan=2,
                              padx=10, pady=10, sticky="nsew")
        transactioninfo.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        transactioncharges.grid(
            row=2, column=1, padx=10, pady=10, sticky="nsew")

    ############################ Transactionparty frame ############################################

        t_partyname = tk.StringVar()
        t_partyPhone = tk.StringVar()
        t_partygstno = tk.StringVar()
        t_product = tk.StringVar()
        t_product.set("0")
        t_productprice = tk.StringVar()
        t_productprice.set("0")
        t_totalpamount = tk.StringVar()
        t_totalpamount.set("0")
        t_Partyvehicle = tk.StringVar()
        t_loading = tk.StringVar()
        t_loading.set("0")
        t_transport_charges = tk.StringVar()
        t_transport_charges.set("0")
        t_unloading = tk.StringVar()
        t_unloading.set("0")

        # labels
        lstText = ("Select Party", "Name", "Address", "Phone no.",
                   "Gst No.", "Select Product", "Select Labour", "Sales date")
        for i in range(len(lstText)):
            setting.ContentLabel(
                transactionparty, lstText[i], (i, 0), f_size=9)

        # optionmenu
        nameList = getpartyname()
        entrypartyselect = tk.StringVar(transactionparty)
        entrypartyselect.set("Select Party name")
        setting.MenuBtn(transactionparty, entrypartyselect, nameList, (0, 1),
                        lambda: viewparty(entrypartyselect.get())).menubtn.config(width=18)

        # entry
        partyname = setting.ContentEntry(transactionparty, t_partyname,
                                         (1, 1), f_size=11)
        partyname.entry.config(state="readonly")
        partyphone = setting.ContentEntry(transactionparty, t_partyPhone,
                                          (3, 1), f_size=11)
        partyphone.entry.config(state="readonly")
        partygst = setting.ContentEntry(transactionparty, t_partygstno,
                                        (4, 1), f_size=11)
        partygst.entry.config(state="readonly")

        entryAddress = ttk.Text(transactionparty, width=20,
                                height=3, font=('Open Sans', 11))

        productlist = ['Brick', 'Block']
        entryproduct = tk.StringVar()
        entryproduct.set("Brick")
        setting.MenuBtn(transactionparty, entryproduct, productlist, (5, 1),
                        lambda: setvalues(entryproduct.get())).menubtn.config(width=18)
        # if str(entryproduct.get()) == "Brick":
        #     setting.ContentLabel(
        #         transactionparty, "No of Brick", (0, 2)).label.grid_configure(sticky="n")
        # elif str(entryproduct.get()) == "Block":
        #     setting.ContentLabel(
        #         transactionparty, "No of Block", (0, 2)).label.grid_configure(sticky="n")
        nameList = getHeadName()
        # print(nameList)
        t_headname = tk.StringVar()
        t_headname.set("Select Head")
        setting.MenuBtn(transactionparty, t_headname, nameList,
                        (6, 1), lambda: viewparty2(t_headname.get()))

        setting.ContentLabel(
            transactionparty, "No. of Units", (0, 2)).label.grid_configure(sticky="n")
        setting.ContentLabel(
            transactionparty, "Amount(per Unit)", (2, 2)).label.grid_configure(sticky="n")
        setting.ContentLabel(
            transactionparty, "Total Amount", (3, 2)).label.grid_configure(sticky="n")
        
        setting.ContentEntry(transactionparty, t_product, (1, 2), px=50).entry.bind("<FocusIn>", lambda event: on_entry_focus_in(event,"nproduct"))
        pp = setting.ContentEntry(
            transactionparty, t_productprice, (2, 2))
        pp.entry.grid_configure(sticky="s")
        pp.entry.bind("<FocusIn>", lambda event: on_entry_focus_in(event,"productprice"))
        setting.ContentEntry(
            transactionparty, t_totalpamount, (4, 2)).entry.config(state="readonly")

        setting.ContentLabel(
            transactionparty, "Payment Type", (5, 2)).label.grid_configure(sticky="n")
        paymentvars = tk.StringVar()
        ttk.Radiobutton(transactionparty, text="Cash", command=gen_insert, variable=paymentvars, bootstyle="success-toolbutton",
                        value="Cash").grid(row=6, column=2, sticky="w", padx=60, pady=5)
        ttk.Radiobutton(transactionparty, text="Credit", command=gen_insert, variable=paymentvars, bootstyle="success-toolbutton",
                        value="Credit").grid(row=6, column=2, sticky="e", padx=80, pady=5)
        # griding entry
        entrysellingdate = tk.StringVar()
        dt2 = ttk.DateEntry(
            transactionparty, width=18, dateformat=r"%d/%m/%Y", bootstyle="primary")
        dt2.entry.config(textvariable=entrysellingdate)
        entryAddress.grid(row=2, column=1, padx=5, pady=5)
        dt2.grid(row=7, column=1, padx=5, pady=5)

    ################################################ transaction frame ######################################################

        lstText = ("Select Vehicle Type", "Vehicle No.",
                   "Transport Charges", "Delivery Address")

        for i in range(len(lstText)):
            setting.ContentLabel(
                transactioninfo, lstText[i], (i, 0), f_size=9)

        vehiclevars = tk.StringVar()
        ttk.Radiobutton(transactioninfo, command=getval, text="Tractor", variable=vehiclevars, bootstyle="success-toolbutton",
                        value="Tractor").grid(row=0, column=1, sticky="w", padx=5, pady=5)
        ttk.Radiobutton(transactioninfo, command=getval, text="Dumper", variable=vehiclevars, bootstyle="success-toolbutton",
                        value="Dumper").grid(row=0, column=1, sticky="e", padx=25, pady=5)
        ttk.Radiobutton(transactioninfo, command=getval, text="Other", variable=vehiclevars, bootstyle="success-toolbutton",
                        value="Other").grid(row=0, column=2, sticky="w", padx=5, pady=5)

        setting.ContentEntry(
            transactioninfo, t_Partyvehicle, (1, 1), f_size=11)
        # transchr = ttk.Checkbutton(transactioninfo, onvalue=0, offvalue=0, command=allcharges,
        #                            text="0", width=13, bootstyle="success-round-toggle", variable=t_transport_charges)
        
        setting.ContentEntry(
            transactioninfo, t_transport_charges, (2, 1), f_size=11).entry.bind("<FocusIn>", lambda event: on_entry_focus_in(event,"transport"))

        entrydeliveryAddress = ttk.Text(
            transactioninfo, width=20, height=4, font=("Open Sans", 11))
        entrydeliveryAddress.grid(
            row=3, column=1, rowspan=2, padx=5, pady=5)
        # transchr.grid(row=2, column=1, pady=5)
    ################################################ transaction charges frame ######################################################

        lsttext = ("Loading Charge", "Unloading Charges", "Remarks")

        for i in range(len(lsttext)):
            setting.ContentLabel(
                transactioncharges, lsttext[i], (i, 0), f_size=9)

        lchr = ttk.Radiobutton(transactioncharges, command=allcharges, value=0,
                               text="Yes", width=8, bootstyle="success", variable=t_loading)
        lchr.grid(row=0, column=1, pady=5, sticky="W")
        uchr = ttk.Radiobutton(transactioncharges, command=allcharges, value=0,
                               text="Yes", width=8, bootstyle="success", variable=t_unloading)
        uchr.grid(row=1, column=1, sticky="W")

        ttk.Radiobutton(transactioncharges, command=allcharges, value=0,
                        text="No", width=8, bootstyle="success", variable=t_loading).grid(row=0, column=1, sticky="E")
        ttk.Radiobutton(transactioncharges, command=allcharges, value=0,
                        text="No", width=8, bootstyle="success", variable=t_unloading).grid(row=1, column=1, sticky="E")
        # getval()
        entryRemarks = ttk.Text(
            transactioncharges, width=20, height=2, font=("Open Sans", 11))

        entryRemarks.grid(row=2, column=1, padx=5, pady=5)

    ######################################## Section3 frame ###################################

        setting.Section3Btn(section3, grd="H", cmd=(
            insert_data, update_data, delete_data, clear))
        ttk.Button(section3, text="Generate Bill", command=generate_bill,
                   bootstyle="dark").grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

    ######################################## tree section #######################################

        columns = ("ID", "Name", "Address", "Phone No.", "Gst No.", 'Product', 'No of Unit', 'price per unit', 'totalprice',
                   'Vehicle type', 'Vehicle No.', 'Payment Type', 'loading', 'unloading', 'Transport Charges', 'Sales date', 'delivery address', 'remarks')

        txt = ("ID", "Name", "Add", "PhNo.", "GstNo.", "Product", "(N)", "per(u)", "Total",
               "Vtype", "VNo.", "Pymt", "Load", "Unload", "Transport Charges", "Sales(dt)", "Delivery", "Remark")
        width = (35, 55, 50, 65, 50, 55, 40, 65,
                 55, 70, 60, 60, 60, 60, 70, 70, 70, 60)

        lstVars = (t_partyname, entryAddress, t_partyPhone, t_partygstno, entryproduct, t_product, t_productprice, t_totalpamount, vehiclevars,
                   t_Partyvehicle, paymentvars, t_loading, t_unloading, t_transport_charges, entrysellingdate, entrydeliveryAddress, entryRemarks)

        transaction_tree = setting.MainTree(frame=add_transaction_frame, col=columns, grd=(
            3, 0), width=width, txt=txt, read=conn2.treeview("Sales"), lstVar=lstVars, h_fsize=12, c_fsize=9, n_text=3, height=5)

        add_transaction_frame.grid(row=0, column=1)

    ############################### End of transaction details ################################

    def stock_page():
        s_brickproduced = tk.StringVar()
        s_blockproduced = tk.StringVar()
        s_bricksold = tk.StringVar()
        s_blocksold = tk.StringVar()
        s_brickavaliable = tk.StringVar()
        s_blockavaliable = tk.StringVar()

        def findtotal():
            startdate = sdt.entry.get()
            enddate = edt.entry.get()
            pbricks, pblocks = conn2.get_total_production((startdate, enddate))
            # print(pbricks, pblocks)
            s_brickproduced.set(str(pbricks))
            s_blockproduced.set(str(pblocks))
            sbricks, sblocks = conn2.get_total_sales((startdate, enddate))
            # print(sbricks, sblocks)
            s_bricksold.set(str(sbricks))
            s_blocksold.set(str(sblocks))
            s_brickavaliable.set(str(pbricks-sbricks))
            s_blockavaliable.set(str(pblocks-sblocks))
    ############################################### stock frame ###########################################################

        stock_frame = ttk.Frame(content_section)
        date_section = ttk.LabelFrame(
            stock_frame, text='Date Selection', bootstyle="primary")
        display_section = ttk.LabelFrame(
            stock_frame, text='Stock Display', bootstyle="primary")
        lb = ttk.Label(stock_frame, text='Stock Details',
                       font=('Open Sans', 20, "bold"))

        lb.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        date_section.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        display_section.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    ###################################################### date section ##################################################

        setting.ContentLabel(date_section, "Start Date", (0, 0))
        setting.ContentLabel(date_section, "End Date", (0, 2))

        getdata_btn = ttk.Button(
            date_section, text='Show', command=findtotal, bootstyle="warning")

        sdt = ttk.DateEntry(date_section, width=20,
                            dateformat=r"%d/%m/%Y", bootstyle="primary")
        edt = ttk.DateEntry(date_section, width=20,
                            dateformat=r"%d/%m/%Y", bootstyle="primary")

        sdt.grid(row=0, column=1, padx=5, pady=5)
        edt.grid(row=0, column=3, padx=5, pady=5)
        getdata_btn.grid(row=0, column=4, padx=10, pady=10)

    #################################################### display section #########################################

        setting.ContentLabel(display_section, "Total Produce", (0, 1))
        setting.ContentLabel(display_section, "Total Sold", (0, 2))
        setting.ContentLabel(display_section, "Available", (0, 3))
        setting.ContentLabel(display_section, "Brick", (1, 0))
        setting.ContentLabel(display_section, "Block", (2, 0))

        setting.ContentEntry(display_section, s_brickproduced,
                             (1, 1)).entry.config(state="readonly")
        setting.ContentEntry(display_section, s_bricksold,
                             (1, 2)).entry.config(state="readonly")
        setting.ContentEntry(display_section, s_brickavaliable,
                             (1, 3)).entry.config(state="readonly")
        setting.ContentEntry(display_section, s_blockproduced,
                             (2, 1)).entry.config(state="readonly")
        setting.ContentEntry(display_section, s_blocksold,
                             (2, 2)).entry.config(state="readonly")
        setting.ContentEntry(display_section, s_blockavaliable,
                             (2, 3)).entry.config(state="readonly")

        stock_frame.pack()

    ############################################ main frame #######################################################
    selling_frame = ttk.Frame(main_frame)
    selling_frame.pack(fill="both")
    tk.Grid.columnconfigure(selling_frame, 0, weight=1)
    tk.Grid.rowconfigure(selling_frame, 0, weight=1)
    tk.Grid.rowconfigure(selling_frame, 1, weight=0)

    content_section = ttk.Frame(selling_frame)
    menuSection = ttk.Frame(selling_frame, bootstyle="dark")

    ############################## Menu Frame #####################################################

    # Buttons
    setting.MainBtn(menuSection, txt="Add Party", cmd=lambda: menu_indicate(
        add_party_indicate, add_party_page), grd=(0, 0))
    setting.MainBtn(menuSection, txt="Add Transaction", cmd=lambda: menu_indicate(
        add_transaction_indicate, add_transaction_page), grd=(0, 1))
    setting.MainBtn(menuSection, txt="Products Stock", cmd=lambda: menu_indicate(
        Stock_indicate, stock_page), grd=(0, 2))

    # Labels
    add_party_indicate = setting.MainLabel(menuSection, 120, (1, 0))
    add_transaction_indicate = setting.MainLabel(menuSection, 120, (1, 1))
    Stock_indicate = setting.MainLabel(menuSection, 120, (1, 2))

    ################################### Pack section #############################################
    menuSection.configure(width=Width, height=Height)
    menuSection.pack(side="top", anchor="n", fill="x")
    content_section.configure(width=Width, height=Height)
    content_section.pack()
