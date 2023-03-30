import sqlite3
import datetime

from functions import convert_date
#


class MainDB:
    def __init__(self, table):
        self.con = sqlite3.connect("./backup/database.db")
        self.cur = self.con.cursor()
        self.table = table

    def insert(self, val):
        try:
            current_dt = str(datetime.datetime.now())[:-7]
            self.cur.execute(
                f"INSERT INTO {self.table} VALUES(NULL,{'?, ' * (len(val)-1)}?, '{current_dt}')", val)
        except Exception as e:
            print(f"Failed !! due to {e}")
        self.con.commit()

    def delete(self, data, ids):
        self.cur.execute(f'''DELETE FROM {self.table} WHERE {ids}=?''', data)
        self.con.commit()

    def update(self, val, typ=""):
        if self.table == "RawMaterialPartyInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "partyName"=?, "partyAdress"=?, "partyPhoneNum"=?, "partyGST"=? WHERE partyID=?''', val)

        if self.table == "ProductionInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "recipeID"=?, "labourID"=?, "productionDate"=?, "product"=?, "numProduct"=?, "unitPerproduct"=?, "failedBrick"=?, "labourcost"=?, "totalProduct"=?, "totallabourcost"=?, "ref_date"=? WHERE pID=?''', val)

        if self.table == "OtherExpenseInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "reason"=?, "amount"=?, "date"=? WHERE otherID=?''', val)

        if self.table == "RecipeInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "recipeName" = ?, "batchCapacity" = ?, "flyashPer" = ?, "flyash" = ?, "dustPer" = ?, "dust" = ?, "cementPer" = ?, "cement" = ?, "admixturePer" = ?, "admixture" = ?, "otherPer" = ?, "other" = ? WHERE recipeID=?''', val)

        if self.table == "SalesPartyInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "spartyName"=?, "spartyAddress"=?, "spartyPhnum"=?, "spartyGST"=? WHERE sID=?''', val)

        if self.table == "RawMaterialTransactionInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "rawMaterial"=?, "material"=?, "price"=?, "totalPrice"=?, "vehicleNo"=?, "purchaseDate"=?, "ref_date"=? WHERE tID=?''', val)

        if self.table == "SalesTransactionInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "labourID"=?, "product"=?, "nproduct"=?, "priceProduct"=?, "totalPrice"=?, "vehicleType"=?, "vehicleNum"=?, "payment"=?, "loadingCharges"=?, "unloadingCharges"=?, "transportCharges"=?, "salesDate"=?, "deliveryAdd"=?,"remarks"=?, "ref_date"=? WHERE salesID=?''', val)

        if self.table == "LabourInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "labourHead"=?, "labourAadharCard"=?, "labourPhnum"=?, "blockchrg"=?, "brickchrg"=?, "tractorloadingchrg"=?, "tractorunloadingchrg"=?, "dumperloadingcharge"=?, "dumpeunloadingcharge"=? WHERE "labourID"=?''', val)

        if self.table == "LabourTransactionInfo":
            self.cur.execute(
                f'''UPDATE {self.table} SET "paymenttype"=?, "paymentamount"=?, "headname"=?, "paymentdate"=?, "ref_date"=? WHERE "labID"=?''', val)

        if self.table == "dates":
            if typ == "production":
                self.cur.execute(f'''
                    UPDATE {self.table} SET "productionID"=? WHERE dateID=?
                                ''', val)
            elif typ == "sales":
                self.cur.execute(f'''
                    UPDATE {self.table} SET "salesID"=? WHERE dateID=?
                                 ''', val)
            elif typ == "labour":
                self.cur.execute(f'''
                    UPDATE {self.table} SET "labourID"=? WHERE dateID=?
                                 ''', val)

        self.con.commit()

    def read(self):
        self.cur.execute(f"SELECT * FROM {self.table}")
        results = self.cur.fetchall()
        return results

    def partyread(self, partytype=""):
        if partytype == "Sales":
            self.cur.execute(f"SELECT * FROM {self.table} WHERE General='N'")
        else:
            self.cur.execute(f"SELECT * FROM {self.table} WHERE Noneparty='N'")
        results = self.cur.fetchall()
        return results

    def treeview(self, party_type=""):
        if party_type == "Sales":
            self.cur.execute('''SELECT SalesTransactionInfo.salesID, SalesPartyInfo.spartyName, SalesPartyInfo.spartyAddress, SalesPartyInfo.spartyPhnum,
                        SalesPartyInfo.spartyGST, SalesTransactionInfo.product, SalesTransactionInfo.nproduct, SalesTransactionInfo.priceProduct, 
                        SalesTransactionInfo.totalPrice, SalesTransactionInfo.vehicleType, SalesTransactionInfo.vehicleNum, 
                        SalesTransactionInfo.payment, SalesTransactionInfo.loadingCharges, SalesTransactionInfo.unloadingCharges,
                        SalesTransactionInfo.transportCharges, SalesTransactionInfo.salesDate, SalesTransactionInfo.deliveryAdd,
                        SalesTransactionInfo.remarks 
                        FROM SalesTransactionInfo JOIN SalesPartyInfo 
                        ON SalesTransactionInfo.salePartyID = SalesPartyInfo.sID;
                             ''')
        elif party_type == "Recipe":
            self.cur.execute('''SELECT pID, recipeName, productionDate, product, numproduct, unitPerproduct, failedBrick,
                        labourCost, totalProduct, totallabourcost
                        FROM ProductionInfo JOIN RecipeInfo 
                        ON 
                        ProductionInfo.recipeID = RecipeInfo.recipeID;
                            ''')
        elif party_type == "Labour":
            self.cur.execute('''
                             SELECT labID, paymenttype, paymentamount, headname, paymentdate
                            FROM LabourTransactionInfo JOIN LabourInfo ON LabourTransactionInfo.labourID = LabourInfo.labourID
                             ''')
        else:
            self.cur.execute('''SELECT RawMaterialTransactionInFo.tID, RawMaterialPartyInfo.partyName, RawMaterialPartyInfo.partyAdress,
                         RawMaterialPartyInfo.partyPhoneNum, RawMaterialPartyInfo.partyGST, RawMaterialTransactionInFo.rawMaterial,
                         RawMaterialTransactionInFo.material, RawMaterialTransactionInFo.price, RawMaterialTransactionInFo.totalPrice,
                         RawMaterialTransactionInFo.vehicleNo, RawMaterialTransactionInFo.purchaseDate
                         FROM RawMaterialPartyInfo
                         JOIN
                         RawMaterialTransactionInFo
                         ON RawMaterialPartyInfo.partyID=RawMaterialTransactionInFo.partyID WHERE tID>4
                         ''')
        results = self.cur.fetchall()
        return results

    def get_partyid(self, phnum, party_type=""):
        # print(phnum)
        if party_type == "Sales":
            self.cur.execute(
                f"SELECT sID FROM {self.table} WHERE spartyPhnum = ?", (str(phnum),))

        elif party_type == "Labour":
            self.cur.execute(
                f"SELECT labourID FROM 'LabourInfo' WHERE labourHead=?", (str(
                    phnum),)
            )
        elif party_type == "Recipe":
            self.cur.execute(
                f"SELECT recipeID FROM '{self.table}' WHERE recipeName = '{phnum}'"
            )
        else:
            self.cur.execute(
                f'''SELECT partyID FROM {self.table} WHERE partyPhoneNum = ? ''', (str(phnum),))

        results = self.cur.fetchall()
        # print(results)
        return results[0][0]

    def get_partyname(self, party_type=""):
        if party_type == "Sales":
            self.cur.execute(
                f"SELECT DISTINCT(spartyName) FROM '{self.table}' WHERE General='N'")

        elif party_type == "Labour":
            self.cur.execute(
                f"SELECT DISTINCT(labourHead) FROM 'LabourInfo'"
            )
        else:
            self.cur.execute(
                f"SELECT DISTINCT(partyName) FROM '{self.table}' WHERE Noneparty='N'")
        results = self.cur.fetchall()
        # print(results)
        return results

    def get_recipe_name(self):
        self.cur.execute(
            "SELECT RecipeName as RecipeName FROM RecipeInfo")
        result = self.cur.fetchall()
        lst = []
        for i in range(len(result)):
            lst.append(result[i][0])
        return lst

    def get_recipe_name_with_date(self, fdate, tdate, prod):
        self.cur.execute(
            f'''SELECT DISTINCT recipeName FROM ProductionInfo JOIN RecipeInfo ON ProductionInfo.recipeID = RecipeInfo.recipeID WHERE productionDate >= "{fdate}" AND productionDate <= "{tdate}" AND product="{prod}"''')
        return self.cur.fetchall()

    def view_party(self, selection, party_type=""):
        if party_type == "Sales":
            self.cur.execute(
                f"SELECT * FROM SalesPartyInfo WHERE spartyName= '{selection}'")
        elif party_type == "Production":
            self.cur.execute(
                f'''SELECT total(totalProduct) FROM ProductionInfo JOIN LabourInfo
                    ON ProductionInfo.labourID=LabourInfo.labourID
                    WHERE LabourInfo.labourHead= {selection}''')
        else:
            self.cur.execute(
                f"SELECT * FROM RawMaterialPartyInfo WHERE partyName= '{selection}'")
        results = self.cur.fetchall()
        return results

    def get_total_labour_charges(self, product, pdate):
        self.cur.execute(f'''
                        SELECT total(totallabourcost) FROM ProductionInfo WHERE product = '{product}' AND ref_date >= '{convert_date(pdate)}'
                        ''')
        return list(self.cur.fetchone())

    def generate_bill(self, val):
        self.cur.execute('''SELECT SalesTransactionInfo.salesID, SalesPartyInfo.spartyName, SalesPartyInfo.spartyAddress, SalesPartyInfo.spartyPhnum,
                        SalesPartyInfo.spartyGST, SalesTransactionInfo.product, SalesTransactionInfo.nproduct, SalesTransactionInfo.priceProduct, 
                        SalesTransactionInfo.totalPrice, SalesTransactionInfo.vehicleType, SalesTransactionInfo.vehicleNum, 
                        SalesTransactionInfo.payment, SalesTransactionInfo.loadingCharges, SalesTransactionInfo.unloadingCharges,
                        SalesTransactionInfo.transportCharges, SalesTransactionInfo.salesDate, SalesTransactionInfo.deliveryAdd,
                        SalesTransactionInfo.remarks 
                        FROM SalesTransactionInfo JOIN SalesPartyInfo 
                        ON SalesTransactionInfo.salePartyID = SalesPartyInfo.sID
                        WHERE SalesTransactionInfo.salesID = ?
                             ''', val)
        return list(self.cur.fetchone())

    def get_total_production(self, date):
        self.cur.execute(f'''
                            SELECT total(totalProduct) FROM ProductionInfo WHERE product="Brick" AND ref_date BETWEEN "{convert_date(date[0])}"
                            AND
                            "{convert_date(date[1])}"; 
                            ''')
        bricks = self.cur.fetchall()
        # print(bricks)
        self.cur.execute(f'''
                            SELECT total(totalProduct) FROM ProductionInfo WHERE product="Block" AND ref_date BETWEEN "{convert_date(date[0])}"
                            AND
                            "{convert_date(date[1])}";
                            ''')
        blocks = self.cur.fetchall()
        # print(blocks)
        return bricks[0][0], blocks[0][0]

    def get_total_sales(self, date):
        self.cur.execute(f'''
                         SELECT total(nproduct) FROM SalesTransactionInfo WHERE product="Brick" AND ref_date BETWEEN "{convert_date(date[0])}" AND "{convert_date(date[1])}";
                        ''')
        bricks = self.cur.fetchall()
        self.cur.execute(f'''
                         SELECT total(nproduct) FROM SalesTransactionInfo WHERE product="Block" AND ref_date BETWEEN "{convert_date(date[0])}" AND "{convert_date(date[1])}";
                        ''')
        blocks = self.cur.fetchall()
        return bricks[0][0], blocks[0][0]

    def get_rawMaterial_stock(self, date):
        self.cur.executescript(f'''
                            UPDATE RawMaterialTransactionInFo SET purchaseDate = "{date[0]}", ref_date = "{convert_date(date[0])}" WHERE tID = 0;   
                            UPDATE RawMaterialTransactionInFo SET purchaseDate = "{date[0]}", ref_date = "{convert_date(date[0])}" WHERE tID = 1;   
                            UPDATE RawMaterialTransactionInFo SET purchaseDate = "{date[0]}", ref_date = "{convert_date(date[0])}" WHERE tID = 2;   
                            UPDATE RawMaterialTransactionInFo SET purchaseDate = "{date[0]}", ref_date = "{convert_date(date[0])}" WHERE tID = 3;   
                            UPDATE RawMaterialTransactionInFo SET purchaseDate = "{date[0]}", ref_date = "{convert_date(date[0])}" WHERE tID = 4;   
                            ''')

        self.cur.execute(f'''
                        SELECT rawMaterial, sum(material), sum(price), sum(totalPrice)
                        FROM RawMaterialTransactionInFo WHERE
                        ref_date BETWEEN "{convert_date(date[0])}" AND "{convert_date(date[1])}"
                        GROUP BY rawMaterial
                        ORDER BY rawMaterial DESC ;
                        ''')
        result = self.cur.fetchall()
        maindict = {}
        for i in range(len(result)):
            maindict[result[i][0]] = (result[i][1], result[i][2], result[i][3])
        return maindict

    def get_raw_material_report(self, date):
        self.cur.execute(f'''
                        SELECT tid, purchaseDate, partyName, vehicleNo, rawMaterial, material, price, totalPrice
                        FROM RawMaterialTransactionInFo 
                        JOIN
                        RawMaterialPartyInfo ON
                        RawMaterialTransactionInFo.partyID = RawMaterialPartyInfo.partyID WHERE 
                        ref_date BETWEEN '{convert_date(date[0])}' AND '{convert_date(date[1])}' AND tID>4 
                        ''')
        return self.cur.fetchall()

    def get_sales_report(self, date, product):
        self.cur.execute(f'''
            SELECT salesID, salesDate, spartyName,product,nproduct,priceProduct,nproduct*priceProduct,vehicleType,vehicleNum,transportCharges,loadingCharges,
            loadingCharges*nproduct, unloadingCharges, unloadingCharges*nproduct, totalPrice,payment,remarks
            FROM 
            SalesTransactionInfo JOIN SalesPartyInfo 
            ON 
            SalesTransactionInfo.salePartyID = SalesPartyInfo.sID
            WHERE
            product = "{product}" AND
            ref_date BETWEEN "{convert_date(date[0])}" AND "{convert_date(date[1])}";
                    ''')
    # print(self.cur.fetchall())
        # result = self.cur.fetchall()
        return self.cur.fetchall()
    
    def get_sales_credit(self, date, product):
        self.cur.execute(f'''
            SELECT salesID, salesDate, spartyName,product,nproduct,priceProduct,nproduct*priceProduct,vehicleType,vehicleNum,transportCharges,loadingCharges,
            loadingCharges*nproduct, unloadingCharges, unloadingCharges*nproduct, totalPrice,payment,remarks
            FROM 
            SalesTransactionInfo JOIN SalesPartyInfo 
            ON 
            SalesTransactionInfo.salePartyID = SalesPartyInfo.sID
            WHERE
            product = "{product}" AND
            ref_date BETWEEN "{convert_date(date[0])}" AND "{convert_date(date[1])}"
            AND payment is 'Credit';    
                         ''')
        result = self.cur.fetchall()
        # print(result)
        return result

    def get_production_report(self, date, product):
        self.cur.execute(f'''
                        SELECT pID, productionDate, recipeName, numproduct, unitPerproduct, numproduct * unitPerproduct, 
                        failedBrick, totalProduct, totallabourcost
                        FROM ProductionInfo JOIN RecipeInfo 
                        ON 
                        ProductionInfo.recipeID = RecipeInfo.recipeID WHERE product="{product}" AND 
						ref_date BETWEEN '{convert_date(date[0])}' AND '{convert_date(date[1])}';
                         ''')
        result = self.cur.fetchall()
        # maindict = {}
        # for i in range(len(result)):
        #     maindict[result[i][0]] = (result[i][1], result[i][2], result[i][3],
        #                               result[i][4], result[i][5], result[i][6], result[i][7], result[i][8])

        # self.cur.execute(f'''
        #                 SELECT salesID, salesDate, deliveryAdd, loadingCharges, unloadingCharges, nproduct,
        #                 nproduct*loadingCharges+nproduct*unloadingCharges
        #                 FROM SalesTransactionInfo WHERE product="{product}" AND
        #                 loadingCharges>0 OR
        #                 unloadingCharges>0 AND
        #                 ref_date BETWEEN "{convert_date(date[0])}" AND "{convert_date(date[1])}" ;
        #                  ''')
        # result = self.cur.fetchall()
        return result

    def get_labour_report(self, date):
        self.cur.execute(f'''
                SELECT
                d.date,
                ifnull(p.product, 'NONE'), 
                ifnull(p.totalProduct, 0), 
                ifnull(p.totallabourcost, 0),
                ifnull(s.loadingCharges * s.nproduct, 0),
                ifnull(s.unloadingCharges * s.nproduct, 0),
                ifnull(l.paymenttype, 'NONE'),
                ifnull(l.paymentamount, 0)
                FROM Dates d
                LEFT JOIN (
                    SELECT *
                    FROM ProductionInfo
                ) p ON d.productionID = p.pID
                LEFT JOIN (
                    SELECT * 
                    FROM LabourTransactionInfo
                ) l ON d.labourID= l.labID
                LEFT JOIN (
                    SELECT *
                    FROM SalesTransactionInfo
                ) s ON d.salesID = s.salesID
                WHERE date_ref BETWEEN '{convert_date(date[0])}' AND '{convert_date(date[1])}'
                ORDER BY d.date_ref;
                         ''')
        # print(self.cur.fetchall())
        return self.cur.fetchall()

    def get_lab_out(self, date):
        self.cur.execute(f'''
                SELECT 
                total(ifnull(p.totallabourcost, 0)),
                total(ifnull(s.loadingCharges * s.nproduct, 0)),
                total(ifnull(s.unloadingCharges * s.nproduct, 0)),
                total(ifnull(l.paymentamount, 0))
                FROM Dates d
                LEFT JOIN (
                    SELECT *
                    FROM ProductionInfo
                ) p ON d.productionID = p.pID
                LEFT JOIN (
                    SELECT * 
                    FROM LabourTransactionInfo
                ) l ON d.labourID= l.labID
                LEFT JOIN (
                    SELECT *
                    FROM SalesTransactionInfo
                ) s ON d.salesID = s.salesID
                WHERE date_ref BETWEEN '{convert_date(date[0])}' AND '{convert_date(date[1])}'
                ORDER BY d.date_ref;
                         ''')
        return self.cur.fetchone()

    def getlabour_charge(self, headname):
        self.cur.execute(
            f'''SELECT blockchrg, brickchrg FROM LabourInfo WHERE labourHead="{headname}"''')
        return self.cur.fetchall()

    def get_charges(self, headname, product):
        if product == "Brick":
            self.cur.execute(f'''
                            SELECT tractorloadingchrgbrick, tractorunloadingchrgbrick, dumperloadingchargebrick, dumperunloadingchargebrick FROM LabourInfo WHERE labourHead="{headname}";
                            ''')
        elif product == "Block":
            self.cur.execute(f'''
                            SELECT tractorloadingchrgblock, tractorunloadingchrgblock, dumperloadingchargeblock, dumperunloadingchargeblock FROM LabourInfo WHERE labourHead="{headname}";
                            ''')

        return list(self.cur.fetchone())

    def getlabid(self, t, chrg):
        if t == "Production":
            self.cur.execute('''
                SELECT labourID FROM LabourInfo WHERE blockchrg={chrg} or brickchrg={chrg};
                ''')
        else:
            self.cur.execute('''
                SELECT labourID FROM LabourInfo WHERE tractorloadingchrg={chrg} or tractorunloadingchrg={chrg} or dumperloadingcharge={chrg} or dumpeunloadingcharge={chrg}
                ''')

        return self.cur.fetchone()[0]

    def getSaleID(self, id, tbl):
        self.cur.execute(f'''
                         SELECT {id} FROM {tbl} ORDER by {id} DESC;
                         ''')
        return self.cur.fetchone()[0]

    def checkDateRef(self, f_date, type=""):
        self.cur.execute("SELECT * from dates")
        result = 0
        # print()
        for i in self.cur.fetchall():
            if type == "production":
                if i[1] in f_date and (i[2] == 0):
                    result = 1
                    break
                else:
                    result = 0
            elif type == "sales":
                if i[1] in f_date and (i[3] == 0):
                    result = 1
                    break
                else:
                    result = 0
            elif type == "labour":
                if i[1] in f_date and (i[4] == 0):
                    result = 1
                    break
                else:
                    result = 0
        # print(result)
        return result

    def getDateId(self, date, type=""):
        if type == "production":
            self.cur.execute(f'''
                         SELECT dateID FROM dates WHERE date_ref = '{date}' AND productionID is 0;
                         ''')
        elif type == "sales":
            self.cur.execute(f'''
                         SELECT dateID FROM dates WHERE date_ref = '{date}' AND salesID is 0;
                         ''')
        elif type == "labour":
            self.cur.execute(f'''
                         SELECT dateID FROM dates WHERE date_ref = '{date}' AND labourID is 0;
                         ''')
        return self.cur.fetchone()[0]

    def getTransportReport(self, date, transporttype):
        self.cur.execute(f'''
                SELECT salesID, salesDate, spartyName, nproduct, vehicleNum, transportCharges, remarks FROM 
                SalesTransactionInfo JOIN SalesPartyInfo
                ON SalesTransactionInfo.salePartyID = SalesPartyInfo.sID
                WHERE ref_date BETWEEN "{convert_date(date[0])}" AND "{convert_date(date[1])}" 
                AND vehicleType = "{transporttype}";
                ''')
        return self.cur.fetchall()
