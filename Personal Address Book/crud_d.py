import crud_c
import mysql_entries
import main_menu

def delete_entries(uid):
    print("\n--Delete Entries--\n")
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
    sno = input("Enter the S.No to Delete the entry: ")
    sno_list = mysql_entries.users_table().get_sno_list(uid)
    try:
        int(sno)
    except (TypeError, ValueError):
        print("\n--Please enter valid serial number--")
        delete_entries(uid)
    else:
        while int(sno) not in sno_list:
            print("\n--Please enter valid serial number--")
            print(f"Available Serial numbers list: {sno_list}")
            sno = input("Enter the S.No to Delete the entry: ")
        del_entry(uid, sno)

def del_entry(uid, sno):
    print("Enter 1 to confirm delete")
    confirm_del = input("Are you sure to delete the entry: ")
    try:
        int(confirm_del)
    except (TypeError, ValueError):
        print("--Delete process cancelled--")
        delete_entries(uid)
    else:
        if int(confirm_del) == 1:
            mysql_entries.users_table().delete_entry(uid, sno)
            main_menu.menu_page(uid)
        else:
            print("--Delete process cancelled--")
            delete_entries(uid)