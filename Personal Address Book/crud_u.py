import crud_c
import mysql_entries
import main_menu

options_u = 0

def edit_entries(uid):
    print("\n--Update Entries--\n")
    db_entries = mysql_entries.users_table().view_table(uid)
    if len(db_entries) <= 0:
        print("No Entries found. Please add some entries")
        crud_c.add_entries(uid)
    else:
        for x in db_entries:
            print(f"S.No: {x[0]}")
            print(f"FirstName: {x[1]}, LastName: {x[2]}")
            print(f"Mobile Number: {x[4]}, Date of Birth: {x[3]}")
            print(f"Email id: {x[5]}")
            print(f"Address: {x[6]}")
            print(f"Personal Notes: {x[7]}", end="\n\n")
    sno = input("Enter the S.No to Update the entry: ")
    sno_list = mysql_entries.users_table().get_sno_list(uid)
    try:
        int(sno)
    except (TypeError, ValueError):
        print("\n--Please enter valid serial number--")
        edit_entries(uid)
    else:
        while int(sno) not in sno_list:
            print("\n--Please enter valid serial number--")
            print(f"Available Serial numbers list: {sno_list}")
            sno = input("Enter the S.No to Update the entry: ")
        update_entry(uid, sno)

def update_entry(uid, sno):
    mc2 = menu_choice2()
    match mc2:
        case 1:
            fn = input("Enter the FirstName to be updated: ")
            while len(fn) == 0 or len(fn) >= 30:
                print("--Enter Only in specified no of chars!--")
                fn = input("Enter the FirstName to be updated: ")
            mysql_entries.users_table().update_entry(uid, 'Firstname', fn, sno)
            update_entry(uid, sno)

        case 2:
            ln = input("Enter the LastName to be updated: ")
            if len(ln) == 0:
                ln = "-"
            while len(ln) >= 30:
                print("--Enter Only in specified no of chars!--")
                ln = input("Enter the LastName to be updated: ")
            mysql_entries.users_table().update_entry(uid, 'Lastname', ln, sno)
            update_entry(uid, sno)

        case 3:
            yyy = input("Enter the Birth Year: ")
            while len(yyy) > 4:
                print("--Enter Only in specified no of chars!--")
                yyy = input("Enter the Birth Year: ")
            mmm = input("Enter the Birth Month: ")
            ddd = input("Enter the Birth Date: ")
            dob = f"{ddd}-{mmm}-{yyy}"
            mysql_entries.users_table().update_entry(uid, 'Birthday', dob, sno)
            update_entry(uid, sno)

        case 4:
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
            mysql_entries.users_table().update_entry(uid, 'Mobno', mob, sno)
            update_entry(uid, sno)

        case 5:
            mail = input("Enter the Email Id: ")
            if len(mail) == 0:
                mail = "-"
            while len(mail) > 40:
                print("--Enter Only in specified no of chars!--")
                mail = input("Enter the Email Id: ")
            mysql_entries.users_table().update_entry(uid, 'Mail_id', mail, sno)
            update_entry(uid, sno)

        case 6:
            loc = input("Enter the Address: ")
            if len(loc) == 0:
                loc = "-"
            while len(loc) > 200:
                print("--Enter Only in specified no of chars!--")
                loc = input("Enter the Address: ")
            mysql_entries.users_table().update_entry(uid, 'Address', loc, sno)
            update_entry(uid, sno)

        case 7:
            notes = input("Enter the Personal Notes: ")
            if len(notes) == 0:
                notes = "-"
            while len(notes) > 200:
                print("--Enter Only in specified no of chars!--")
                notes = input("Enter the Personal Notes: ")
            mysql_entries.users_table().update_entry(uid, 'Notes', notes, sno)
            update_entry(uid, sno)

        case 8:
            main_menu.menu_page(uid)


def menu_choice2():
    print("Enter the option below to update the data: ")
    print("1 => First Name\n"
          "2 => Last Name\n"
          "3 => Date of Birth\n"
          "4 => Mobile Number\n"
          "5 => Email\n"
          "6 => Address\n"
          "7 => Personal Notes\n"
          "8 => Back to Main menu")
    global options_u
    try:
        options_u = int(input("Enter the option: "))
    except (TypeError, ValueError):
        print("\nPlease enter a valid number. Try Again!\n")
        menu_choice2()
    else:
        if not (0 < int(options_u) < 9):
            print("\nPlease enter a valid option!\n")
            menu_choice2()
    finally:
        return options_u

