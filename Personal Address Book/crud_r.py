import main_menu
import mysql_entries
import crud_c

options_mp1 = 0

def view_entries(uid):
    print("\n--View Entries--\n")
    db_entries = mysql_entries.users_table().view_table(uid)
    print(f"Total number of Entries: {len(db_entries)}\n")
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

        mc1 = menu_choice1()
        match mc1:
            case 1:
                with open(f"{uid}.txt", 'w') as f:
                    for x in db_entries:
                        f.write(f"S.No:{x[0]}\n")
                        f.write(f"FirstName: {x[1]}, LastName: {x[2]}\n")
                        f.write(f"Mobile Number: {x[4]}, Date of Birth: {x[3]}\n")
                        f.write(f"Email id: {x[5]}\n")
                        f.write(f"Address: {x[6]}\n")
                        f.write(f"Personal Notes: {x[7]} \n\n")
                print(f"\n--File({uid}.txt) Download Success--")
                print("Redirecting to Main menu...")
                main_menu.menu_page(uid)
            case 2:
                print("\nRedirecting to Main menu...")
                main_menu.menu_page(uid)


def menu_choice1():
    print("Please select the correct option from below: ")
    print("1 => Download entries data\n"
          "2 => Back to Main menu\n")
    global options_mp1
    try:
        options_mp1 = int(input("Enter the option: "))
    except (TypeError, ValueError):
        print("\nPlease enter a valid number. Try Again!\n")
        menu_choice1()
    else:
        if not (0 < int(options_mp1) < 3):
            print("\nPlease enter a valid option!\n")
            menu_choice1()
    finally:
        return options_mp1
