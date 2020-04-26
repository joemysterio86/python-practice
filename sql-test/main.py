import os, time
import sqlite3
# from PyQt5 import uic
# from PyQt5 import QtSql
# from PyQt5.QtWidgets import (QMainWindow, QTableView, QApplication, QAbstractItemView)
# from PyQt5.QtCore import Qt

# Form, Window = uic.loadUiType("test.ui")

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'sql-test.db')
def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

con = db_connect()
cur = con.cursor()

# dropTable1 = """DROP TABLE sqlite_sequence;"""
# dropTable2 = """DROP TABLE lineitems;"""
# cur.execute(dropTable1)
# cur.execute(dropTable2)
bills_table = cur.execute("SELECT sql FROM sqlite_master WHERE type='table';").fetchall()[0]

billsTableCreate = """
CREATE TABLE IF NOT EXISTS bills (
    id integer PRIMARY KEY,
    bill_name varchar(255) NOT NULL,
    base_amount_due real NOT NULL,
    actual_amount_due real NOT NULL,
    due_date datetime NOT NULL
);"""

incomeTableCreate = """
CREATE TABLE IF NOT EXISTS income (
	id integer PRIMARY KEY,
	user varchar(255) NOT NULL,
	income_amount real NOT NULL,
	pay_day_start datetime NOT NULL,
	pay_day_frequency varchar(255) NOT NULL
);"""

cur.execute(billsTableCreate)
cur.execute(incomeTableCreate)
# print(bills_table)


# if bills_table:
#     print("The bills table is here!")
#     print(cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
# else:
#     print("This table IS NOT HERE!!! So let me make it for you.")
#     # cur.execute(bills_sql)
#     print(cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bills';").fetchall())


def create_bills(con, bill_name, base_amount_due, actual_amount_due, due_date):
    sql = "insert into bills (bill_name, base_amount_due, actual_amount_due, due_date) values (?, ?, ?, ?)"
    cur.execute(sql, (bill_name, base_amount_due, actual_amount_due, due_date))
    con.commit()
    return cur.lastrowid

def create_income(con, user, income_amount, pay_day_start, pay_day_frequency):
    sql = "insert into income (user, income_amount, pay_day_start, pay_day_frequency) values (?, ?, ?, ?)"
    cur.execute(sql, (user, income_amount, pay_day_start, pay_day_frequency))
    con.commit()
    return cur.lastrowid


def menu():
    print("""What would you like to do?
    1) View your bills.
    2) View your income.
    3) Add a bill.
    4) Add income.
    Q) Exit.

    Please press a number 1-4 to choose.

    """)
    choice = input("Enter a number: ")
    if choice.lower() == "q":
        print("You selected 5, exiting...")
        exit()
    elif choice == "1":
        cur.execute("SELECT bill_name, base_amount_due, actual_amount_due, due_date FROM bills")
        formatted_result = [f"{bill_name:<20}{base_amount_due:<14}{actual_amount_due:<14}{due_date:<15}" for bill_name, base_amount_due, actual_amount_due, due_date in cur.fetchall()]
        bill_name, base_amount_due, actual_amount_due, due_date = "Bill", "Monthly Due", "Current Due", "Due Date"
        print("\n\nYour Bills:\n")
        print('\n'.join([f"{bill_name:<20}{base_amount_due:<14}{actual_amount_due:<14}{due_date:<15}"] + formatted_result))
        input("\n\nPress ENTER key to continue to main menu.")
        menu()
    elif choice == "2":
        print(cur.execute("SELECT id, bill_name, base_amount_due, actual_amount_due, due_date FROM bills").fetchall())
        time.sleep(.5)
        menu()
    elif choice == "3":
        bill1 = input("Please enter the bill name: ")
        bill2 = float(input("Please enter what is normally due: "))
        bill3 = float(input("Please enter what you will pay: "))
        bill4 = input("Please enter the bill due date (YYYY-MM-DD): ")
        time.sleep(.5)
        print("Thanks, creating this bill...")
        create_bills(con, bill1, bill2, bill3, bill4)
        print("Bill created!! Taking you back to main menu.")
        time.sleep(1.5)
        menu()
    elif choice == "4":
        print("You entered 4!")
        time.sleep(.5)
        menu()
    else:
        print("PLEASE!!! Select an appropriate option!")
        time.sleep(1)
        menu()

menu()



# create_product(con, 'Something About Something', 99.99)

# cur.execute("delete from products where id=6")
# con.commit()


# print(cur.execute("""select price
# from products
# where id=5""").fetchone()[0])

# print(cur.execute("""select price
# from products
# where id=4""").fetchone()[0])

# print(price1)
# print(price2)

# book = cur.fetchall()[0][1]

# app = QApplication([])
# app.setStyleSheet("QPushButton { margin: 10ex; }")
# button = QPushButton('Click to see value!')
# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText(book)
#     alert.exec_()
# button.clicked.connect(on_button_clicked)
# button.show()
# app.exec_()

# app = QApplication([])
# app.setStyleSheet("QMessageBox { margin: 10ex; }")
# msgbox = QMessageBox(QMessageBox.Information, 'A Thing!', book)
# msgbox.show()
# app.exec_()


# def load_initial_data(self):
#     # where cur is the cursor
#     self.cur.execute("select * from products")
#     rows = self.cur.fetchall()[0][1]

#     for row in rows:
#         inx = rows.index(row)
#         self.tableView.insertRow(inx)
#         # add more if there is more columns in the database.
#         # self.tableWidget_2.setItem(inx, 0, QTableWidgetItem(row[1]))
#         # self.tableWidget_2.setItem(inx, 1, QTableWidgetItem(row[2]))
#         # self.tableWidget_2.setItem(inx, 2, QTableWidgetItem(row[3]))



# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec_()