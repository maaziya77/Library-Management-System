import mysql.connector as mc

con = mc.connect(host="localhost", user="root", password="akb999", database="library")
cur = con.cursor()

def add_book():
    print('Add Book')
    bno = input("Enter book number: ")
    if bno.isdigit():
        cur.execute("SELECT * FROM bookdetails WHERE bno=" + bno)
        test = cur.fetchone()
        if test == None:
            bname = input("Enter the Book's Name: ")
            auth = input("Enter the Author of the Book: ")
            publ = input("Enter the Publisher of the Book: ")
            num = input("Enter the number of copies available: ")
            if num.isdigit():
                cur.execute("INSERT INTO bookdetails VALUES({} , '{}' , '{}' , '{}' , {})".format(bno, bname, auth, publ, num))
                print("Inserted Successfully!!!")
                con.commit()
            else:
                print("-" * 60)
                print('Invalid Entry!!!\nPlease enter an integer value')
                print("-" * 60)
        else:
            print('------------------------')
            print('A book already exists with this number')
            print('Please enter another book number')
            print('------------------------')
    else:
        print("-" * 60)
        print('Invalid Entry!!!\nPlease enter an integer value')
        print("-" * 60)

def update_book():
    print("-" * 60)
    print('UPDATE BOOK:')
    print("-" * 60)
    udb = input("Enter the book number of the book to be updated: ")
    if udb.isdigit():
        cur.execute("SELECT * FROM bookdetails WHERE bno=" + udb)
        test1 = cur.fetchone()
        print("-" * 60)
        if test1 == None:
            print('Invalid Entry!!!\nPlease enter an integer value')
            print("-" * 60)
        else:
            print("1. Update Book Name\n2. Update Author Name\n3. Update Publication Name\n4. Update Number of Copies Available")
            choice = int(input("Select an option from above: "))
            if choice == 1:
                uname = input("Enter the new book name here: ")
                cur.execute("UPDATE bookdetails SET bname='{}' WHERE bno={}".format(uname, udb))
                con.commit()
                print("Updated successfully !!!")
            elif choice == 2:
                uauth = input("Enter the new author name here: ")
                cur.execute("UPDATE bookdetails SET auth='{}' WHERE bno={}".format(uauth, udb))
                con.commit()
                print("Updated successfully !!!")
            elif choice == 3:
                upub = input("Enter the new publication name here: ")
                cur.execute("UPDATE bookdetails SET publ='{}' WHERE bno={}".format(upub, udb))
                con.commit()
                print("Updated successfully !!!")
            elif choice == 4:
                newnum = input("Enter the new number of copies of the book: ")
                if newnum.isdigit():
                    cur.execute("UPDATE bookdetails SET num={} WHERE bno={}".format(newnum, udb))
                    con.commit()
                    print("Updated successfully !!!")
                else:
                    print("-" * 60)
                    print('Invalid Entry!!!\nPlease enter an integer value')
                    print("-" * 60)
            else:
                print("Please enter an integer value!")

def del_book():
    print("-" * 60)
    print("DELETE BOOK:")
    print("-" * 60)
    bd = input("Enter the book no.: ")
    if bd.isdigit():
        cur.execute("DELETE FROM bookdetails WHERE bno={}".format(bd))
        con.commit()
        print("Deleted successfully !!!")
    else:
        print("-" * 60)
        print('Invalid Entry!!!\nPlease enter an integer value')
        print("-" * 60)

def lend_book():
    print("-" * 60)
    print("LEND BOOK:")
    print("-" * 60)
    from datetime import date, time, timedelta
    stid = input("Enter Student ID: ")
    if stid.isdigit():
        print()
    else:
        print("-" * 60)
        print('Invalid Entry!!!\nPlease enter an integer value')
        print("-" * 60)
    stname = input("Enter the Student Name: ")
    bno = input("Enter book number: ")
    if bno.isdigit():
        cur.execute("SELECT * FROM bookdetails WHERE bno=" + bno)
        test = cur.fetchone()
        if test == None:
            print("Invalid Book Number! Try Again")
        else:
            bname = input("Enter the name of the book: ")
            bdate = date.today()
            rdate = bdate + timedelta(days=7)
            cur.execute("INSERT INTO lent VALUES({},'{}',{},'{}','{}','{}','{}')".format(bno, bname, stid, stname, bdate, rdate, "No"))
            con.commit()
            cur.execute("UPDATE bookdetails SET num = num - 1 WHERE bno = {}".format(bno))
            con.commit()
            print("Lent Successfully !!!")
    else:
        print("-" * 60)
        print('Invalid Entry!!!\nPlease enter an integer value')
        print("-" * 60)

def return_book():
    print("-" * 60)
    print("RETURN BOOK:")
    print("-" * 60)
    from datetime import date, time, timedelta
    rdate = date.today()
    stid = input("Enter Student ID: ")
    if stid.isdigit():
        print()
    else:
        print("-" * 60)
        print('Invalid Entry!!!\nPlease enter an integer value')
        print("-" * 60)
    stname = input("Enter the Student Name: ")
    bno = input("Enter book number: ")
    if bno.isdigit():
        cur.execute("SELECT * FROM bookdetails WHERE bno=" + bno)
        test = cur.fetchone()
        if test == None:
            print("Invalid Book Number! Try Again")
        else:
            print()
    else:
        print("-" * 60)
        print('Invalid Entry!!!\nPlease enter an integer value')
        print("-" * 60)
    bname = input("Enter the name of the book: ")
    cur.execute("UPDATE lent SET returneddate='{}', returned='{}' WHERE userid={} AND bno={}".format(rdate, "yes", stid, bno))
    cur.execute("UPDATE bookdetails SET num = num + 1 WHERE bno = {}".format(bno))
    con.commit()
    print("Returned Successfully !!!")
