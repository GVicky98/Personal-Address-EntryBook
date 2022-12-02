import homepage
import login
import mysql_idpass

def access_denied(id_check):
    option2 = homepage.check_options()
    uid = id_check
    match option2:
        case 1:
            print("\nRedirecting to Homepage\n")
            homepage.welcome()

        case 2:
            print("\nTo recover your password,")
            umob = input("Enter your mobile number: ")

            try:
                int(umob)
            except (ValueError, TypeError):
                print("Invalid Mobile Number Format.")
                homepage.welcome()
            else:
                umob = int(umob)
                a = mysql_idpass.check_umob(uid, umob)
                if a is False:
                    print("\n--Wrong Mobile Number--\n"
                          "You will be redirected to the Homepage...\n")
                    homepage.welcome()
                else:
                    print(f"\nYour Password is: '{a}' \n"
                          f"--Please Login to continue--")
                    login.oldUser()


