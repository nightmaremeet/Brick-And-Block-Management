BEGIN TRANSACTION;
DROP TABLE IF EXISTS "OtherExpenseInfo";
CREATE TABLE IF NOT EXISTS "OtherExpenseInfo" (
	"otherID"	INTEGER,
	"reason"	VARCHAR(50),
	"amount"	INTEGER,
	"date"	VARCHAR(50),
	"created_on"	VARHCAR(20),
	PRIMARY KEY("otherID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "RawMaterialPartyInfo";
CREATE TABLE IF NOT EXISTS "RawMaterialPartyInfo" (
	"partyID"	INTEGER,
	"partyName"	VARCHAR(50),
	"partyAdress"	VARCHAR(100),
	"partyPhoneNum"	VARCHAR(12),
	"partyGST"	VARCHAR(50) UNIQUE,
	"Noneparty"	CHAR(1),
	"created_on"	VARCHAR(20),
	PRIMARY KEY("partyID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "RawMaterialTransactionInFo";
CREATE TABLE IF NOT EXISTS "RawMaterialTransactionInFo" (
	"tID"	INTEGER,
	"partyID"	INTEGER DEFAULT 0,
	"rawMaterial"	VARCHAR(50),
	"material"	INTEGER,
	"price"	INTEGER DEFAULT 0,
	"totalPrice"	INTEGER DEFAULT 0,
	"vehicleNo"	VARCHAR(30) DEFAULT 0,
	"purchaseDate"	VARCHAR(50),
	"ref_date"	VARCHAR(20),
	"created_on"	VARCHAR(20),
	PRIMARY KEY("tID" AUTOINCREMENT),
	FOREIGN KEY("partyID") REFERENCES "RawMaterialPartyInfo"("partyID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS "RecipeInfo";
CREATE TABLE IF NOT EXISTS "RecipeInfo" (
	"recipeID"	INTEGER,
	"recipeName"	VARCHAR(50),
	"batchCapacity"	INTEGER,
	"flyashPer"	VARCHAR(5),
	"flyash"	INTEGER,
	"dustPer"	VARCHAR(5),
	"dust"	INTEGER,
	"cementPer"	VARCHAR(5),
	"cement"	INTEGER,
	"admixturePer"	VARCHAR(5),
	"admixture"	INTEGER,
	"otherPer"	VARCHAR(5),
	"other"	INTEGER,
	"created_on"	VARCHAR(20),
	PRIMARY KEY("recipeID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "SalesPartyInfo";
CREATE TABLE IF NOT EXISTS "SalesPartyInfo" (
	"sID"	INTEGER,
	"spartyName"	VARCHAR(50),
	"spartyAddress"	VARCHAR(100),
	"spartyPhnum"	VARCHAR(12),
	"spartyGST"	VARCHAR(50),
	"General"	CHAR(1) DEFAULT 'N',
	"created_on"	VARCHAR(20),
	PRIMARY KEY("sID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "LabourInfo";
CREATE TABLE IF NOT EXISTS "LabourInfo" (
	"labourID"	INTEGER,
	"labourHead"	VARCHAR(50),
	"labourAadharCard"	VARCHAR(50) UNIQUE,
	"labourPhnum"	VARCHAR(12),
	"blockchrg"	INTEGER,
	"brickchrg"	INTEGER,
	"tractorloadingchrg"	INTEGER,
	"tractorunloadingchrg"	INTEGER,
	"dumperloadingcharge"	INTEGER,
	"dumpeunloadingcharge"	INTEGER,
	"created_on"	VARHCAR(20),
	PRIMARY KEY("labourID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "LabourTransactionInfo";
CREATE TABLE IF NOT EXISTS "LabourTransactionInfo" (
	"labID"	INTEGER,
	"labourID"	INTEGER,
	"paymenttype"	VARCHAR(30),
	"paymentamount"	INTEGER,
	"headname"	INTEGER,
	"paymentdate"	VARCHAR(10),
	"ref_date"	VARCHAR(20),
	"created_on"	VARCHAR(20),
	PRIMARY KEY("labID" AUTOINCREMENT),
	FOREIGN KEY("labourID") REFERENCES "LabourInfo"("labourID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS "ProductionInfo";
CREATE TABLE IF NOT EXISTS "ProductionInfo" (
	"pID"	INTEGER,
	"recipeID"	INTEGER,
	"labourID"	INTEGER,
	"productionDate"	VARCHAR(50),
	"product"	VARCHAR(50),
	"numProduct"	INTEGER,
	"unitPerproduct"	INTEGER,
	"failedBrick"	INTEGER,
	"labourcost"	INTEGER,
	"totalProduct"	INTEGER,
	"totallabourcost"	INTEGER,
	"ref_date"	VARCHAR(20),
	"created_on"	INTEGER,
	PRIMARY KEY("pID" AUTOINCREMENT),
	FOREIGN KEY("recipeID") REFERENCES "RecipeInfo"("recipeID") ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY("labourID") REFERENCES "LabourInfo"("labourID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS "SalesTransactionInfo";
CREATE TABLE IF NOT EXISTS "SalesTransactionInfo" (
	"salesID"	INTEGER,
	"salePartyID"	INTEGER,
	"labourID"	INTEGER,
	"product"	VARCHAR(50),
	"nproduct"	INTEGER,
	"priceProduct"	INTEGER,
	"totalPrice"	INTEGER,
	"vehicleType"	VARCHAR(50),
	"vehicleNum"	VARCHAR(50),
	"payment"	VARCHAR(50),
	"loadingCharges"	INTEGER,
	"unloadingCharges"	INTEGER,
	"transportCharges"	INTEGER,
	"salesDate"	VARCHAR(50),
	"deliveryAdd"	VARCHAR(100),
	"remarks"	VARCHAR(50),
	"ref_date"	VARCHAR(20),
	"created_on"	VARCHAR(20),
	PRIMARY KEY("salesID" AUTOINCREMENT),
	FOREIGN KEY("labourID") REFERENCES "LabourInfo"("labourID") ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY("salePartyID") REFERENCES "SalesPartyInfo"("sID") ON DELETE NO ACTION ON UPDATE NO ACTION
);
INSERT INTO "RawMaterialPartyInfo" ("partyID","partyName","partyAdress","partyPhoneNum","partyGST","Noneparty","created_on") VALUES (0,'',NULL,NULL,NULL,'Y',NULL);
INSERT INTO "RawMaterialTransactionInFo" ("tID","partyID","rawMaterial","material","price","totalPrice","vehicleNo","purchaseDate","ref_date","created_on") VALUES (0,0,'FlyAsh',0,0,0,'0','01/02/2023','20230201',NULL),
 (1,0,'Dust',0,0,0,'0','01/02/2023','20230201',NULL),
 (2,0,'Cement',0,0,0,'0','01/02/2023','20230201',NULL),
 (3,0,'Admixture',0,0,0,'0','01/02/2023','20230201',NULL),
 (4,0,'Others',0,0,0,'0','01/02/2023','20230201',NULL);
COMMIT;
