import mysql_entries
import quit
import homepage
import crud_c
import crud_r
import crud_u
import crud_d

options_mp = 0

def menu_page(uid):
    uname = mysql_entries.users_table().get_uname(uid)
    print(f"\nHello {uname}. Welcome to Main menu")
    choice = menu_choice()

    match choice:
        case 1:
            crud_r.view_entries(uid)
        case 2:
            crud_c.add_entries(uid)
        case 3:
            crud_u.edit_entries(uid)
        case 4:
            crud_d.delete_entries(uid)
        case 5:
            print("\n--Logout Success--\n")
            homepage.welcome()
        case 6:
            quit.exitApp()


def menu_choice():
    print("Please enter the correct option below: ")
    print("1 => View Entries\n"
          "2 => Add Entries\n"
          "3 => Edit Entries\n"
          "4 => Delete Entries\n"
          "5 => Logout\n"
          "6 => Exit app\n")
    global options_mp
    try:
        options_mp = int(input("Enter the option: "))
    except (TypeError, ValueError):
        print("\nPlease enter a valid number. Try Again!\n")
        menu_choice()
    else:
        if not (0 < int(options_mp) < 7):
            print("\nPlease enter a valid option!\n")
            menu_choice()
    finally:
        return options_mp

