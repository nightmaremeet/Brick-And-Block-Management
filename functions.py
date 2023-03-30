import os
import datetime
from ttkbootstrap.dialogs.dialogs import Messagebox


def on_click(str1):
    Messagebox().show_error('Error: Please Enter ' + str1 + ' !', 'Invalid Input')


def successful(path):
    # Messagebox().ok(f'{x} Generated Successfully', 'Bill')
    msg = Messagebox().yesno(
        "Message Generated!! Do you want to print the report??", "Open or Print", True)
    if msg == "Yes":
        os.startfile(r"{}".format(path),"print")
    else:
        pass
        # os.startfile(r"{}".format(path),"")

def reverse(tuples):
    new_tuple = tuples[::-1]
    return new_tuple


def convert_date(dt):
    return datetime.date(int(dt.split("/")[2]), int(dt.split("/")[1]), int(dt.split("/")[0])).strftime(r"%Y%m%d")
