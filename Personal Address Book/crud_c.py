import mysql_entries
import crud_r

def add_entries(uid):
    print("\n--Add Entries--\n")
    fn = input("Enter the FirstName: ")
    while len(fn) == 0 or len(fn) >= 30:
        print("--Enter Only in specified no of chars!--")
        fn = input("Enter the FirstName: ")

    ln = input("Enter the LastName: ")
    if len(ln) == 0:
        ln = "-"
    while len(ln) >= 30:
        print("--Enter Only in specified no of chars!--")
        ln = input("Enter the LastName: ")

    yyy = input("Enter the Birth Year: ")
    while len(yyy) > 4:
        print("--Enter Only in specified no of chars!--")
        yyy = input("Enter the Birth Year: ")
    mmm = input("Enter the Birth Month: ")
    ddd = input("Enter the Birth Date: ")
    dob = f"{ddd}-{mmm}-{yyy}"

    pfx = input("Enter the Country code: ")
    while len(pfx) > 5:
        print("--Enter Only in specified no of chars!--")
        pfx = input("Enter the Country code: ")
    sfx = input("Enter the Mobile Number: ")
    if len(sfx) == 0:
        sfx = "-"
    while len(sfx) > 14:
        print("--Enter Only in specified no of chars!--")
        sfx = input("Enter the Mobile Number: ")
    mob = f"{pfx} {sfx}"

    mail = input("Enter the Email Id: ")
    if len(mail) == 0:
        mail = "-"
    while len(mail) > 40:
        print("--Enter Only in specified no of chars!--")
        mail = input("Enter the Email Id: ")

    loc = input("Enter the Address: ")
    if len(loc) == 0:
        loc = "-"
    while len(loc) > 200:
        print("--Enter Only in specified no of chars!--")
        loc = input("Enter the Address: ")

    notes = input("Enter the Personal Notes: ")
    if len(notes) == 0:
        notes = "-"
    while len(notes) > 200:
        print("--Enter Only in specified no of chars!--")
        notes = input("Enter the Personal Notes: ")

    mysql_entries.users_table().create_entry(uid, fn, ln, dob, mob, mail, loc, notes)
    crud_r.view_entries(uid)
