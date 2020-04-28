# The start of my app.
import os, time, datetime
import sqlite3

dateToday = datetime.date.today()

defaultPath = os.path.join(os.path.dirname(__file__), 'finanCalc.db')
def dbConnect(dbPath=defaultPath):
    con = sqlite3.connect(dbPath)
    return con

con = dbConnect()
cur = con.cursor()

# dropTable1 = """DROP TABLE sqlite_sequence;"""
# dropTable2 = """DROP TABLE lineitems;"""
# cur.execute(dropTable1)
# cur.execute(dropTable2)
# bills_table = cur.execute("SELECT sql FROM sqlite_master WHERE type='table';").fetchall()[0]

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


def createBill(con, bill_name, base_amount_due, actual_amount_due, due_date):
    sql = "insert into bills (bill_name, base_amount_due, actual_amount_due, due_date) values (?, ?, ?, ?)"
    cur.execute(sql, (bill_name, base_amount_due, actual_amount_due, due_date))
    con.commit()
    return cur.lastrowid

def createIncome(con, user, income_amount, pay_day_start, pay_day_frequency):
    sql = "insert into income (user, income_amount, pay_day_start, pay_day_frequency) values (?, ?, ?, ?)"
    cur.execute(sql, (user, income_amount, pay_day_start, pay_day_frequency))
    con.commit()
    return cur.lastrowid


def menu():
    print(f"""
Today's date is: {dateToday}
    
What would you like to do?

    1) View your bills.
    2) View your income.
    3) Add a bill.
    4) Add income.
    Q) Exit.

    Please press a number 1-4 to choose.

    """)
    choice = input("Please select an option: ")
    if choice.lower() == "q":
        print("You selected Q, exiting...")
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
        cur.execute("SELECT user, income_amount, pay_day_start, pay_day_frequency FROM income")
        formatted_result = [f"{user:<15}{income_amount:<16}{pay_day_start:<16}{pay_day_frequency:<15}" for user, income_amount, pay_day_start, pay_day_frequency in cur.fetchall()]
        user, income_amount, pay_day_start, pay_day_frequency = "User", "Payday Amount", "Payday Start", "Payday Frequency"
        print("\n\nYour Bills:\n")
        print('\n'.join([f"{user:<15}{income_amount:<16}{pay_day_start:<16}{pay_day_frequency:<15}"] + formatted_result))
        input("\n\nPress ENTER key to continue to main menu.")
        menu()
    elif choice == "3":
        bill1 = input("\nPlease enter the bill name: ")
        bill2 = float(input("Please enter what is normally due: "))
        bill3 = float(input("Please enter what you will pay: "))
        bill4 = input("Please enter the bill due date (YYYY-MM-DD): ")
        time.sleep(.5)
        print("Thanks, creating this bill...")
        createBill(con, bill1, bill2, bill3, bill4)
        print("Bill created!! Taking you back to main menu.")
        time.sleep(1.5)
        menu()
    elif choice == "4":
        income1 = input("\nPlease enter who this income belongs to: ")
        income2 = float(input("Please enter paycheck amount: "))
        income3 = input("Please enter next expected pay date (YYYY-MM-DD): ")
        income4 = input("Please indicate if pay schedule is biweekly, bimonthly, or monthly: ")
        time.sleep(.5)
        print("Thanks, adding income to the database...")
        createIncome(con, income1, income2, income3, income4)
        print("Income added!! Taking you back to main menu.")
        time.sleep(1.5)
        menu()
    else:
        print("PLEASE!!! Select an appropriate option!")
        time.sleep(1)
        menu()

menu()
