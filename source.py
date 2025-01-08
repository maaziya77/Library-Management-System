print("------------------------------------------------------")
print("|                                                    |")
print("| WELCOME TO IGNITE LIBRARY !!!                      |")
print("|                                                    |")
print("------------------------------------------------------")
print(" ")
print(" ")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(" ")
print("----------------------LOGIN---------------------------")
print(" ")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::")

admins0 = {"Maaziya": 1974, "Arathi": 9339}

print(" ")
print(" ")
k = 0

while k == 0:
    adm = input("Enter Admin Name: ")
    if adm not in admins0:
        print(" ")
        print("-------------------Invalid Admin Name!!!------------------")
        continue
    else:
        print(" ")
        k = 0
        while k == 0:
            pwd = int(input("Enter Password: "))
            print(" ")
            print(" ")
            if pwd == admins0[adm]:
                print("Access Granted !")
                k = 1  # Added to break the loop after successful login.

print("-" * 120)
print("-" * 120)

from tabulate import tabulate
print(tabulate(z, headers=["Book Number", "Book Name", "Author", "Publication", "Number of Copies"]))
print("-" * 120)
print("-" * 120)

while True:
    print("1. Display Book Details")
    print("2. Add Book")
    print("3. Update details of a book")
    print("4. Delete a book")
    print("5. Lend a book")
    print("6. Return a book")
    print("7. View options for issued books")
    print("8. View details of Unreturned books")
    print("9. EXIT PAGE")
    print(" ")
    print("-" * 120)

    choice = int(input("Choose an option from above: "))
    print(" ")

    if choice == 1:
        print("------->1. View Details of All Books")
        print("------->2. View Details of a Specific Book")
        print("------->3. View Details of Books, Select By Author")
        print("------->4. View Details of Books, Select by Publication")
        print(" ")
        print("-" * 120)
        print(" ")

        choice3 = int(input("Select an option from above: "))
        print(" ")
        print("-" * 120)
        print(" ")

        if choice3 == 1:
            cur.execute("select * from bookdetails;")
            z = cur.fetchall()
            print("-" * 120)
            print("-" * 120)
            print(tabulate(z, headers=["Book Number", "Book Name", "Author", "Publication", "Number of Copies"]))
            print("-" * 120)
            print("-" * 120)

        elif choice3 == 2:
            bnum = input("Enter the book number: ")
            cur.execute("select * from bookdetails where bno={}".format(bnum))
            m = cur.fetchall()
            print("-" * 120)
            print("-" * 120)
            print(tabulate(m, headers=["Book Number", "Book Name", "Author", "Publication", "Number of Copies"]))
            print("-" * 120)
            print("-" * 120)

        elif choice3 == 3:
            auth2 = input("Enter author name: ")
            cur.execute("Select * from bookdetails where auth='{}'".format(auth2))
            r = cur.fetchall()
            print("-" * 120)
            print("-" * 120)
            print(tabulate(r, headers=["Book Number", "Book Name", "Author", "Publication", "Number of Copies"]))
            print("-" * 120)
            print("-" * 120)

        elif choice3 == 4:
            pub2 = input("Enter publication name: ")
            cur.execute("Select * from bookdetails where publ='{}'".format(pub2))
            h = cur.fetchall()
            print("-" * 120)
            print("-" * 120)
            print(tabulate(h, headers=["Book Number", "Book Name", "Author", "Publication", "Number of Copies"]))
            print("-" * 120)
            print("-" * 120)

    elif choice == 2:
        add_book()

    elif choice == 3:
        update_book()

    elif choice == 4:
        del_book()

    elif choice == 5:
        lend_book()

    elif choice == 6:
        return_book()

    elif choice == 7:
        print("-----> 1. Display today's Issue Details")
        print("-----> 2. Display Issue Details of the last 3 days")
        print("-----> 3. Display Issue Details of the last 7 days")
        print(" ")
        print("-" * 120)
        print(" ")

        choiced = int(input("Select an option from above: "))
        print(" ")

        if choiced == 1:
            from datetime import date, time, timedelta
            dt = str(date.today())
            cur.execute("select * from lent where borroweddate='{}'".format(dt))
            rd1 = cur.fetchall()
            print("-" * 120)
            print("-" * 120)
            print(tabulate(rd1, headers=["Book Number", "Book Name", "Student ID", "Student Name", "Borrow Date", "Return date", "Returned"]))
            print("-" * 120)
            print("-" * 120)

        elif choiced == 2:
            from datetime import date, time, timedelta
            dt1 = str(date.today() - timedelta(days=3))
            cur.execute("select * from lent where borroweddate>='{}'".format(dt1))
            rd2 = cur.fetchall()
            print("-" * 120)
            print("-" * 120)
            print(tabulate(rd2, headers=["Book Number", "Book Name", "Student ID", "Student Name", "Borrow Date", "Return date", "Returned"]))
            print("-" * 120)
            print("-" * 120)

        elif choiced == 3:
            from datetime import date, time, timedelta
            dt2 = str(date.today() - timedelta(days=7))
            cur.execute("select * from lent where returneddate>='{}'".format(dt2))
            rd3 = cur.fetchall()
            print("-" * 120)
            print("-" * 120)
            print(tabulate(rd3, headers=["Book Number", "Book Name", "Student ID", "Student Name", "Borrow Date", "Return date", "Returned"]))
            print("-" * 120)
            print("-" * 120)

    elif choice == 8:
        cur.execute("select * from lent where returned='{}'".format('No'))
        c = cur.fetchall()
        print("-" * 120)
        print("-" * 120)
        print(tabulate(c, headers=["Book Number", "Book Name", "Student ID", "Student Name", "Borrow Date", "Return date", "Returned"]))
        print("-" * 120)
        print("-" * 120)

    elif choice == 9:
        k = 1
        print("Thank you for visiting IGNITE Library!")
        continue

    else:
        print("-----------------------------------------------INVALID OPTION!-----------------------------------\nPlease choose an option from below.")
        print("")
        print("-" * 117)
        continue

else:
    print("Incorrect Password! Access Denied!")
continue

