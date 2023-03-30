import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from functions import convert_date, on_click, reverse
import sqlite3
# from tkcalendar import DateEntry
import modules.settings as setting
import modules.connect as connect

font = ("Open Sans", 11)

conn1 = connect.MainDB(table="RecipeInfo")
conn2 = connect.MainDB(table="ProductionInfo")
conn3 = connect.MainDB(table="dates")

def production_section(main_frame, Width, Height):

    def hide_menu_indicator():
        add_recipe_indicate.config(bg='#c3c3c3')
        Production_per_day_indicate.config(bg='#c3c3c3')
        material_used_indicate.config(bg='#c3c3c3')

    def delete_pages():
        for frame in content_section.winfo_children():
            frame.destroy()

    def menu_indicate(lb, page):
        hide_menu_indicator()
        lb.config(bg='#158aff')
        delete_pages()
        page()

    def add_recipe_page():
        def entervalue():
            checktotal = float(flyashvar.get())+float(dustvar.get())+float(
                cementvar.get())+float(admixturevar.get())+float(othervar.get())
            if checktotal == 100:
                m_flyash.set(
                    f"{round((float(r_batchcapacity.get()) * (float(flyashvar.get())/100)),ndigits=2)}")
                m_dust.set(
                    f"{round((float(r_batchcapacity.get()) * (float(dustvar.get())/100)),ndigits=2)}")
                m_cement.set(
                    f"{round((float(r_batchcapacity.get()) * (float(cementvar.get())/100)),ndigits=2)}")
                m_admixture.set(
                    f"{round((float(r_batchcapacity.get()) * (float(admixturevar.get())/100)),ndigits=2)}")
                m_others.set(
                    f"{round((float(r_batchcapacity.get()) * (float(othervar.get())/100)),ndigits=2)}")
            else:
                on_click("valid Raw Material Proportions")
                return

        def insert_data():
            entervalue()
            recipeName = str(r_name.get())
            batchcapacity = str(r_batchcapacity.get())
            flyash = str(m_flyash.get())
            flyashval = str(flyashvar.get())
            dust = str(m_dust.get())
            dustval = str(dustvar.get())
            cement = str(m_cement.get())
            cementval = str(cementvar.get())
            admixture = str(m_admixture.get())
            admixtureval = str(admixturevar.get())
            others = str(m_others.get())
            othersval = str(othervar.get())
            if recipeName == "" or recipeName == " ":
                return on_click('recipeName')
            if batchcapacity == "" or batchcapacity == " ":
                return on_click('batchcapacity')
            if flyash == "" or flyash == " ":
                return on_click('flyash')
            if dust == "" or dust == " ":
                return on_click('dust')
            if cement == "" or cement == " ":
                return on_click('cement')
            if admixture == "" or admixture == " ":
                return on_click('admixture')
            if others == "" or others == " ":
                return on_click('others')
            if flyashval == "":
                return
            else:
                conn1.insert((recipeName, batchcapacity, flyash, flyashval, dust, dustval,
                              cement, cementval, admixture, admixtureval, others, othersval))

            for data in recipe_tree.Tree.get_children():
                recipe_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.read())):
                if i % 2 == 0:
                    recipe_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    recipe_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            recipe_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            recipe_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def update_data():
            entervalue()
            selected_recipe = recipe_tree.Tree.selection()[0]
            update_name = recipe_tree.Tree.item(selected_recipe)['values'][0]

            conn1.update((r_name.get(), r_batchcapacity.get(), m_flyash.get(), flyashvar.get(), m_dust.get(), dustvar.get(
            ), m_cement.get(), cementvar.get(),  m_admixture.get(), admixturevar.get(), m_others.get(), othervar.get(), update_name))

            for data in recipe_tree.Tree.get_children():
                recipe_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn1.read())):
                if i % 2 == 0:
                    recipe_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    recipe_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            recipe_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            recipe_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def delete_data():
            selected_recipe = recipe_tree.Tree.selection()[0]
            deleteData = str(recipe_tree.Tree.item(
                selected_recipe)['values'][0])
            conn1.delete((deleteData,), "recipeID")

            for data in recipe_tree.Tree.get_children():
                recipe_tree.Tree.delete(data)

            for result in reverse(conn1.read()):
                recipe_tree.Tree.insert(
                    parent='', index='end', iid=result, text="", values=(result), tag="orow")

            for i, result in enumerate(reverse(conn1.read())):
                if i % 2 == 0:
                    recipe_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    recipe_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            recipe_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            recipe_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def clear():
            for var in lstVars:
                var.set("")

    ##################################### addrecipe frame #####################################################
        add_recipe_frame = ttk.Frame(content_section)

        # label
        lb = ttk.Label(add_recipe_frame, text='Add Recipe Details',
                       font=('Open Sans', 20, "bold"))
        lb.grid(row=0, column=0, padx=20, pady=20)

        # label frame
        recipeinfo = ttk.LabelFrame(
            add_recipe_frame, text="Recipe Information", bootstyle="primary")
        recipe_section3 = ttk.LabelFrame(
            add_recipe_frame, text="Operations", bootstyle="primary")

        # griding label frame
        recipeinfo.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        recipe_section3.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    ##################################### recipeinfo frame ####################################################

        # labels
        lstText = ("Recipe Name", "Batch Capacity (in Kg)", "Flyash(F)",
                   "Dust(D)", "Cement(C)", "Admixture(A)", "Other(O)")
        for i in range(2):
            setting.ContentLabel(recipeinfo, lstText[i], (i, 0))

        for i in range(5):
            setting.ContentLabel(recipeinfo, lstText[i+2], (i+1, 2))

        # variables of all entries
        r_name = tk.StringVar()
        r_batchcapacity = tk.StringVar()
        m_flyash = tk.StringVar()
        m_dust = tk.StringVar()
        m_cement = tk.StringVar()
        m_admixture = tk.StringVar()
        m_others = tk.StringVar()
        # entries
        ttk.Label(
            recipeinfo, text="(kg)", font=font).grid(row=0, column=3, padx=10, pady=10)
        textVar1 = (r_name, r_batchcapacity, m_flyash,
                    m_dust, m_cement, m_admixture, m_others)
        for i in range(2):
            setting.ContentEntry(recipeinfo, textVar1[i], (i, 1), width=15)
            # ttk.Entry(recipeinfo, width=15,font=font, textvariable=textVar[i]).grid(row=i, column=1, padx=5, pady=5)

        for i in range(5):
            setting.ContentEntry(
                recipeinfo, textVar1[i+2], (i+1, 3), width=10).entry.config(state="readonly")
            # ttk.Entry(recipeinfo, width=15,font=font, textvariable=textVar[i+2]).grid(row=i+1, column=3, padx=5, pady=5)

        # entries variable 2
        flyashvar = tk.StringVar()
        dustvar = tk.StringVar()
        cementvar = tk.StringVar()
        admixturevar = tk.StringVar()
        othervar = tk.StringVar()

        ttk.Label(
            recipeinfo, text="(%)", font=font).grid(row=0, column=4, padx=10, pady=10)

        textVar2 = (flyashvar, dustvar, cementvar, admixturevar, othervar)

        # entries 2
        for i in range(5):
            setting.ContentEntry(
                recipeinfo, textVar2[i], (i+1, 4), width=15)

    ##################################################### recipe_section3 frame #####################################################

        # button
        setting.Section3Btn(recipe_section3, cmd=(
            insert_data, update_data, delete_data, clear))

    ###################################################### tree ############################################################

        columns = ("ID", "Recipe Name", "Batch Capacity", "Flyash", "Flyashper", "Dust",
                   "Dustper", "Cement", "Cementper", "Admixture", "Admixtureper", "Others", "Othersper")
        txt = ("ID", "Name", "Btch", "F(kg)", "F(%)", "D(kg)",
               "D(%)", "C(kg)", "C(%)", "A(kg)", "A(%)", "O(kg)", "O(%)")
        lstVars = (r_name, r_batchcapacity,  m_flyash, flyashvar, m_dust, dustvar, m_cement, cementvar, m_admixture, admixturevar,
                   m_others, othervar)
        width = (40, 70, 70, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60)
        recipe_tree = setting.MainTree(
            add_recipe_frame, col=columns, lstVar=lstVars, read=conn1.read(), width=width, txt=txt, grd=(2, 0), Text="N")

        add_recipe_frame.pack()
    ######################################################  ############################################################

    def Production_per_day_page():
        p_no_of_palettes = tk.StringVar()
        p_bricks_per_palettes = tk.StringVar()
        p_fail_bricks = tk.StringVar()
        m_totalbricks = tk.StringVar()
        p_total_labour_charge = tk.StringVar()

        def insert_data():
            entervalue()
            recipeName = entryrecipeselect.get()
            productiondate = dt.entry.get()
            product = entryproduct.get()
            noofpalettes = p_no_of_palettes.get()
            bricksperpalettes = p_bricks_per_palettes.get()
            failbricks = p_fail_bricks.get()
            totalbricks = m_totalbricks.get()
            totallabourcharge = p_total_labour_charge.get()
            lhead = t_headname.get()

            if recipeName == "Select recipe":
                return on_click('recipeName')
            if productiondate == "" or productiondate == " ":
                return on_click('Production Date')
            if product == "Select Product":
                return on_click('Product')
            if noofpalettes == "" or noofpalettes == " ":
                return on_click("no of palettes")
            if bricksperpalettes == "" or bricksperpalettes == " ":
                return on_click("bricks per palettes")
            if (failbricks == "" or failbricks == " ") or int(failbricks) > int(noofpalettes) * int(bricksperpalettes) :
                return on_click("failbricks")
            if totalbricks == "" or totalbricks == " ":
                return on_click("total bricks")
            if totallabourcharge == "" or totallabourcharge == " ":
                return on_click("total labour charge")
            if lhead == "" or lhead == " ":
                return on_click("labour head")
            else:
                recipeId = conn1.get_partyid(recipeName, "Recipe")
                labourid = conn1.get_partyid(lhead, "Labour")
                conn2.insert((recipeId, labourid, productiondate, product, noofpalettes,
                              bricksperpalettes, failbricks, chrge.get(), totalbricks, totallabourcharge, convert_date(productiondate)))

            for data in production_tree.Tree.get_children():
                production_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn2.treeview("Recipe"))):
                if i % 2 == 0:
                    production_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    production_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            production_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            production_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))
            
            productionID = conn3.getSaleID("pID", "ProductionInfo")
            try:
                dateID = conn3.getDateId(convert_date(productiondate),"production")
            except:
                pass

            if conn3.checkDateRef(convert_date(productiondate), "production"):
                conn3.update((productionID,dateID), "production")
            else:
                conn3.insert((convert_date(productiondate), productionID, 0, 0, productiondate))

        def update_data():
            labour_charge = conn1.getlabour_charge(t_headname.get())
            if entryproduct.get() == "Block":
                chrge.set(labour_charge[0][0])
            else:
                chrge.set(labour_charge[0][1])
            entervalue()
            selected_recipe = production_tree.Tree.selection()[0]
            update_name = production_tree.Tree.item(selected_recipe)[
                'values'][0]
            labourid = conn1.get_partyid(t_headname.get(), "Labour")
            recipeId = conn1.get_partyid(entryrecipeselect.get(), "Recipe")
            conn2.update((recipeId, labourid, dt.entry.get(), entryproduct.get(), p_no_of_palettes.get(), p_bricks_per_palettes.get(
            ), p_fail_bricks.get(), str(chrge.get()), m_totalbricks.get(), p_total_labour_charge.get(), convert_date(dt.entry.get()), update_name))

            for data in production_tree.Tree.get_children():
                production_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn2.treeview("Recipe"))):
                if i % 2 == 0:
                    production_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    production_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            production_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            production_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def delete_data():
            selected_production = production_tree.Tree.selection()[0]
            deleteData = str(production_tree.Tree.item(
                selected_production)['values'][0])
            conn2.delete((deleteData,), "pID")

            for data in production_tree.Tree.get_children():
                production_tree.Tree.delete(data)

            for i, result in enumerate(reverse(conn2.treeview("Recipe"))):
                if i % 2 == 0:
                    production_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="orow")
                else:
                    production_tree.Tree.insert(
                        parent='', index='end', text="", values=(result), tag="erow")

            production_tree.Tree.tag_configure(
                'orow', background='#faf9f5', font=('Open Sans', 11))
            production_tree.Tree.tag_configure(
                'erow', background='#d1e2ff', font=('Open Sans', 11))

        def getrecipename():
            results = conn2.get_recipe_name()
            recipelist = [recipename for recipename in results]
            # recipelist.append('General')
            return recipelist

        def entervalue():
            m_totalbricks.set((float(p_no_of_palettes.get(
            ))*float(p_bricks_per_palettes.get()))-float(p_fail_bricks.get()))
            total = float(m_totalbricks.get())*float(chrge.get())
            p_total_labour_charge.set(round(total, 2))

        def getHeadName():
            results = conn1.get_partyname(party_type="Labour")
            # print(results)
            headName = [headname[0] for headname in results]
            return headName

        def viewparty(selection):
            labour_charge = conn1.getlabour_charge(selection)
            if entryproduct.get() == "Block":
                chrge.set(labour_charge[0][0])
            else:
                chrge.set(labour_charge[0][1])

        def clear():
            for var in lstvars:
                var.set("")
            entryrecipeselect.set("Select Recipe")
            entryproduct.set("Select Product")

    ####################################### production per day frame ###################################################
        production_per_day_frame = tk.Frame(content_section)

        productioninfo = ttk.LabelFrame(
            production_per_day_frame, text="Recipe Information", bootstyle="primary")
        production_section3 = ttk.LabelFrame(
            production_per_day_frame, bootstyle="primary", text="Operations")

        lb = ttk.Label(production_per_day_frame, text='Add Production Details',
                       font=('Open Sans', 20, "bold"))

        lb.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        productioninfo.grid(row=1, column=0, padx=5, pady=5)

        production_section3.grid(
            row=1, column=1, pady=5, padx=5)
    ######################################### productioninfo frame ##################################################

        # labels
        lstText = ('Select Recipe', 'Production Date', "Select Product", 'No. of palettes', 'Units per palettes',
                   'Fail Units', "Select Labour", 'Total Units', 'Total Labour Cost')
        for i in range(6):
            setting.ContentLabel(productioninfo, lstText[i], (i, 0))

        for i in range(3):
            setting.ContentLabel(
                productioninfo, lstText[i+6], (i, 2))

        # menuoptions
        recipelist = getrecipename()
        entryrecipeselect = tk.StringVar()
        entryrecipeselect.set("Select Recipe")
        setting.MenuBtn(productioninfo, entryrecipeselect, recipelist, (0, 1))
        # dateEntry
        entryproductiondate = tk.StringVar()
        dt = ttk.DateEntry(productioninfo, width=20,
                           dateformat=r"%d/%m/%Y", bootstyle="primary")
        dt.entry.config(textvariable=entryproductiondate)
        dt.grid(row=1, column=1, padx=5, pady=5)

        productlist = ['Brick', 'Block']
        entryproduct = tk.StringVar()
        entryproduct.set("Select Product")
        chrge = tk.StringVar()
        # if entryproduct.get() == "Block":
        #     chrge.set(labour_charge[0][0])
        # else:
        #     chrge.set(labour_charge[0][1])
        setting.MenuBtn(productioninfo, entryproduct, productlist, (2, 1))

        # entry

        #
        nameList = getHeadName()
        # print(nameList)
        t_headname = tk.StringVar()
        t_headname.set("Select Head")
        setting.MenuBtn(productioninfo, t_headname, nameList,
                        (0, 3), lambda: viewparty(t_headname.get()))

        setting.ContentEntry(
            productioninfo, p_no_of_palettes, (3, 1), f_size=11)
        setting.ContentEntry(
            productioninfo, p_bricks_per_palettes, (4, 1), f_size=11)
        setting.ContentEntry(productioninfo, p_fail_bricks, (5, 1), f_size=11)
        # setting.ContentEntry(
        #     productioninfo, p_labour_charge, (6, 1), f_size=11)
        setting.ContentEntry(productioninfo, m_totalbricks,
                             (1, 3), f_size=11).entry.config(state="readonly")
        setting.ContentEntry(
            productioninfo, p_total_labour_charge, (2, 3), f_size=11).entry.config(state="readonly")
    ############################################ section 3 frame ###################################################

        setting.Section3Btn(production_section3, grd="V", cmd=(
            insert_data, update_data, delete_data, clear))

    ############################################ tree section ####################################################
        columns = ("ID", "Recipe Name", "Production date", "Product", "No of Palettes", "Units Per Palettes",
                   "Fail Units", "Labour Charge(Per Unit)", "Total Units", "Total Labour Charge")
        txt = ("ID", "Recipe", "P(Date)", "Product", "Palettes(N)", "Palettes(Unit)",
               "Failed(Unit)", "LCharge(Unit)", "Total(Unit)", "Total LCharge")
        width = (35, 75, 100, 85, 115, 120, 90, 90, 100, 100)
        lstvars = (entryrecipeselect, entryproductiondate, entryproduct, p_no_of_palettes,
                   p_bricks_per_palettes, p_fail_bricks, chrge, m_totalbricks, p_total_labour_charge)
        production_tree = setting.MainTree(frame=production_per_day_frame, col=columns, grd=(
            2, 0), width=width, txt=txt, read=conn2.treeview("Recipe"), lstVar=lstvars, Text="N")

        production_per_day_frame.pack()

    ############################################################################################################

    def material_used_page():
        m_totalbricks = tk.StringVar()
        m_brickweight = tk.StringVar()
        m_batch_capacity = tk.StringVar()
        m_bricks_per_batch = tk.StringVar()
        m_flyash = tk.StringVar()
        m_dust = tk.StringVar()
        m_cement = tk.StringVar()
        m_admixture = tk.StringVar()
        m_others = tk.StringVar()
        entryrecipeselect = tk.StringVar()
        entryrecipeselect.set("Select recipe")

        def getrecipename():
            startdate = str(entrystartdate.get())
            enddate = str(entryenddate.get())
            results = conn2.get_recipe_name_with_date(
                startdate, enddate, productvars.get())
            fun_recipelist = [recipename for recipename, in results]
            return fun_recipelist

        def getrecipedetail(selection):
            startdate = str(entrystartdate.get())
            enddate = str(entryenddate.get())
            conn = sqlite3.connect("./backup/database.db")
            cursor = conn.cursor()
            cursor.execute(
                f'''SELECT DISTINCT(batchcapacity), flyash, dust, cement, admixture, other FROM RecipeInfo 
                    JOIN ProductionInfo ON  RecipeInfo.recipeID = ProductionInfo.recipeID
                    WHERE RecipeInfo.recipeName="{selection}" AND 
                    ProductionInfo.ref_date >= "{convert_date(startdate)}" AND ProductionInfo.ref_date <= "{convert_date(enddate)}" 
                    AND ProductionInfo.product = "{productvars.get()}";''')
            result = list(cursor.fetchone())
            m_batch_capacity.set(result[0])
            m_flyash.set(f"{result[1]}%")
            m_dust.set(f"{result[2]}%")
            m_cement.set(f"{result[3]}%")
            m_admixture.set(f"{result[4]}%")
            m_others.set(f"{result[5]}%")
            cursor.execute(f'''SELECT total(totalProduct) FROM RecipeInfo JOIN ProductionInfo ON RecipeInfo.recipeID = ProductionInfo.recipeID
                           WHERE ref_date >= "{convert_date(startdate)}" AND ref_date <= "{convert_date(enddate)}" AND recipeName = "{selection}"
                           AND ProductionInfo.product = "{productvars.get()}";
                           ''')
            totalbricks = list(cursor.fetchone())
            m_totalbricks.set(totalbricks[0])
            calculate_data()

        def showrecipe():
            recipelist = getrecipename()
            setting.MenuBtn(output_section, entryrecipeselect, recipelist,
                            (0, 1), lambda: getrecipedetail(entryrecipeselect.get()))

        def calculate_kg(materialval):
            result = float(m_bricks_per_batch.get()) * (float(materialval)/100)
            return result

        def calculate_data():
            m_bricks_per_batch.set(
                float(m_totalbricks.get())/float(m_brickweight.get()))
            flyashvar.set(
                f"{round(calculate_kg(m_flyash.get()[:-1]), ndigits=4)} kg")
            dustvar.set(
                f"{round(calculate_kg(m_dust.get()[:-1]), ndigits=4)} kg")
            cementvar.set(
                f"{round(calculate_kg(m_cement.get()[:-1]), ndigits=4)} kg")
            admixturevar.set(
                f"{round(calculate_kg(m_admixture.get()[:-1]), ndigits=4)} kg")
            othervar.set(
                f"{round(calculate_kg(m_others.get()[:-1]), ndigits=4)} kg")

    ########################################### rawmaterial frame ###################################################

        rawmaterial_frame = ttk.Frame(content_section)
        lb = ttk.Label(rawmaterial_frame, text='Used Raw Materials Details',
                       font=('Open Sans', 20, "bold"))
        lb.grid(row=0, column=0, padx=50, pady=50)
        date_section = ttk.LabelFrame(
            rawmaterial_frame, text='Date Selection', bootstyle="primary")
        output_section = ttk.LabelFrame(
            rawmaterial_frame, text='output section', bootstyle="primary")
        calculate_section = ttk.LabelFrame(
            rawmaterial_frame, text='Calculations', bootstyle="primary")
        date_section.grid(row=1, column=0, padx=5, pady=5)
        output_section.grid(row=1, column=1, padx=5, pady=5)
        calculate_section.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    ######################################## date section #####################################################

        setting.ContentLabel(date_section, "Start Date", grd=(0, 0))
        setting.ContentLabel(date_section, "End Date", grd=(0, 2))
        setting.ContentLabel(
            date_section, "Weight of Unit (in Kg)", grd=(1, 0))
        setting.ContentLabel(
            date_section, "Select Product", grd=(2, 0))

        ttk.Button(date_section, text='Show', bootstyle="warning",
                   command=showrecipe).grid(row=1, column=3, padx=5, pady=5)

        entrystartdate = tk.StringVar()
        dt = ttk.DateEntry(
            date_section, width=20, dateformat=r"%d/%m/%Y", bootstyle="primary")
        dt.entry.config(textvariable=entrystartdate)

        entryenddate = tk.StringVar()
        dt2 = ttk.DateEntry(
            date_section, width=20, dateformat=r"%d/%m/%Y", bootstyle="primary")
        dt2.entry.config(textvariable=entryenddate)

        setting.ContentEntry(date_section, m_brickweight, (1, 1))

        productvars = tk.StringVar()
        ttk.Radiobutton(date_section, text="Brick", variable=productvars, bootstyle="success-toolbutton",
                        value='Brick').grid(row=2, column=1, padx=5, pady=5)
        ttk.Radiobutton(date_section, text="Block", variable=productvars, bootstyle="success-toolbutton",
                        value='Block').grid(row=2, column=2, padx=5, pady=5)

        dt.grid(row=0, column=1, padx=5, pady=5)
        dt2.grid(row=0, column=3, padx=5, pady=5)

    ####################################### output section ##############################################

        setting.ContentLabel(
            output_section, "Select Recipe", grd=(0, 0))
        setting.ContentLabel(output_section, "Total Units",
                             grd=(1, 0))
        setting.ContentLabel(
            output_section, "Batch Capacity (in Kg)", grd=(2, 0))

        # recipe_select = tk.StringVar()
        # setting.MenuBtn(output_section, recipe_select, nameList, (0, 1),
        #                 lambda: viewparty(entrypartyselect.get())).menubtn.config(width=18)

        setting.ContentEntry(output_section, m_totalbricks,
                             (1, 1)).entry.config(state="readonly")
        setting.ContentEntry(
            output_section, m_batch_capacity, (2, 1)).entry.config(state="readonly")

    ############################################ calculation section ###########################################

        setting.ContentLabel(
            calculate_section, "Number of Units per Batch (in Kg)", grd=(7, 0))
        setting.ContentLabel(
            calculate_section, " ", grd=(6, 0))
        setting.ContentLabel(
            calculate_section, "Amount (in %)", grd=(0, 1))
        setting.ContentLabel(
            calculate_section, "Amount (in kg)", grd=(0, 2))
        setting.ContentLabel(
            calculate_section, "Flyash", grd=(1, 0))
        setting.ContentLabel(
            calculate_section, "Dust", grd=(2, 0))
        setting.ContentLabel(
            calculate_section, "Cement", grd=(3, 0))
        setting.ContentLabel(
            calculate_section, "Admixture", grd=(4, 0))
        setting.ContentLabel(
            calculate_section, "Other", grd=(5, 0))

        setting.ContentEntry(
            calculate_section, m_bricks_per_batch, (7, 1)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, m_flyash,
                             (1, 1)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, m_dust,
                             (2, 1)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, m_cement,
                             (3, 1)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, m_admixture,
                             (4, 1)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, m_others,
                             (5, 1)).entry.config(state="readonly")

        flyashvar = tk.StringVar()
        dustvar = tk.StringVar()
        cementvar = tk.StringVar()
        admixturevar = tk.StringVar()
        othervar = tk.StringVar()
        setting.ContentEntry(calculate_section, flyashvar,
                             (1, 2)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, dustvar,
                             (2, 2)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, cementvar,
                             (3, 2)).entry.config(state="readonly")
        setting.ContentEntry(
            calculate_section, admixturevar, (4, 2)).entry.config(state="readonly")
        setting.ContentEntry(calculate_section, othervar,
                             (5, 2)).entry.config(state="readonly")

        rawmaterial_frame.pack()

        # material_used_frame.pack(pady=10)
    #################################################### Main Frame #######################################################

    production_frame = ttk.Frame(main_frame)
    production_frame.pack(fill="both")
    menu_section = ttk.Frame(production_frame, bootstyle="dark")
    content_section = ttk.Frame(production_frame)

    tk.Grid.columnconfigure(production_frame, 0, weight=1)
    tk.Grid.rowconfigure(production_frame, 0, weight=1)
    tk.Grid.rowconfigure(production_frame, 1, weight=0)

    ################################################## menusection frame #######################################################

    # buttons
    setting.MainBtn(menu_section, txt="Add Recipe", cmd=lambda: menu_indicate(
        add_recipe_indicate, add_recipe_page), grd=(0, 0))
    setting.MainBtn(menu_section, txt="Production per day", cmd=lambda: menu_indicate(
        Production_per_day_indicate, Production_per_day_page), grd=(0, 1))
    setting.MainBtn(menu_section, txt="Material Used", cmd=lambda: menu_indicate(
        material_used_indicate, material_used_page), grd=(0, 2))

    # labels
    add_recipe_indicate = setting.MainLabel(menu_section, 120, (1, 0))
    Production_per_day_indicate = setting.MainLabel(menu_section, 120, (1, 1))
    material_used_indicate = setting.MainLabel(menu_section, 120, (1, 2))

    #################################################### packing ############################################################
    menu_section.configure(width=Width, height=Height)
    menu_section.pack(side="top", anchor="n", fill="x")
    content_section.configure(width=Width, height=Height)
    content_section.pack()
