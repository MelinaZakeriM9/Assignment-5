import sqlite3

# I didn't specify the path bc it differs from device to device apparantly
debby = sqlite3.connect("test.db")

curs = debby.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS Expenses 
             (id INTEGER PRIMARY KEY, Date DATE, Category VARCHAR(100), Amount FLOAT, Description TEXT)
             """)
debby.commit()

def Add():
    newDate = input("Please enter the date of the transaction in yyyy-mm-dd format:\n")
    newCategory = input("Category:\n")
    newAmount = float(input("Amount:\n"))
    newDesc = input("Description:\n")

    sql = "INSERT INTO Expenses (Date, Category, Amount, Description) VALUES (?,?,?,?)"
    val = (newDate, newCategory, newAmount, newDesc)

    curs.execute(sql, val)
    debby.commit

def View():
    curs.execute("SELECT * FROM Expenses")
    for x in curs:
        print(x)
    
def Update():
    chID= input("Please enter the ID of the data you wish to update:\n")
    ch= int(input("""
    What do you want update?
        1. Date
        2. Category
        3. Amount
        4. Description
    """))

    newVal= input("Enter your new values:\n")
    
    if ch == 1:
        curs.execute("UPDATE Expenses SET Date = "+newVal+" WHERE id ="+chID)
    if ch == 2:
        curs.execute("UPDATE Expenses SET Category = "+newVal+" WHERE id ="+chID)
    if ch == 3:
        curs.execute("UPDATE Expenses SET Amount= "+newVal+" WHERE id ="+chID)
    if ch == 4:
        curs.execute("UPDATE Expenses SET Description = "+newVal+" WHERE id ="+chID)
    debby.commit

def Delete():
    ch = input("Enter the ID of the expense you wish to delete:\n")
    curs.execute("DELETE FROM Expenses WHERE id=" + ch)
    debby.commit

Run = True
while Run:
    key = int(input("""
        1. Add expence
        2. View expence history
        3. Update 
        4. Delete
        5. Exit
        """))

    if key == 1:
        Add()

    if key == 2:
        View()
    
    if key == 3:
        Update()

    if key == 4:
        Delete()

    if key == 5:
        Run = False