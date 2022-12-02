import mysql_idpass
import homepage
import pass_access
import main_menu


def oldUser():
    print("\n--Welcome to LOGIN Process--\n")
    count_id = 0

    while count_id < 3:
        count_id += 1
        id_check = checkRegid()
        if id_check:
            upass = input("Enter your password: ")
            count_pass = 0
            while count_pass < 3:
                count_pass += 1
                passCheck = checkUpass(id_check, upass)
                if passCheck:
                    print("\n--Login Success!--")
                    main_menu.menu_page(id_check)
                    # Main-menu page will be called here

                    break
                else:
                    if not checkUpass(id_check, upass) and count_pass < 3:
                        print("\nWrong Password. Please Try again!")
                        upass = input("Enter your password: ")
                    pass
                if count_pass >= 3:
                    print("\nPassword attempt limit reached!\n")
                    pass_access.access_denied(id_check)
            break
        else:
            print("\nUser ID not Valid. Try Again!")
            pass
        if count_id >= 3:
            print("\nLogin limit exceeded. Please try after sometime!\n")
            homepage.welcome()


def checkRegid():
    uid = input("Enter your User ID: ").lower()
    idlist = mysql_idpass.get_idlist()
    if uid in idlist:
        return uid
    else:
        return False


def checkUpass(uid, upass):
    db_pass = mysql_idpass.userid().get_password(uid)
    if upass == db_pass:
        return True
    else:
        return False
