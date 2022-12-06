import homepage
import login
import mysql_idpass

options_pd = 0  # pd -> password denied

def access_denied(id_check):
    uid = id_check
    print("1 => Return to Homepage\n"
          "2 => Recover Password")
    global options_pd
    try:
        options_pd = int(input("Enter the option: "))
    except (TypeError, ValueError):
        print("\n--Please enter a valid number--\n")
        access_denied(id_check)
    else:
        if not (0 < int(options_pd) < 3):
            print("\n--Please enter a valid option--\n")
            access_denied(id_check)
        else:
            option2 = options_pd
        match option2:
            case 1:
                print("\n--Redirecting to Homepage--\n")
                homepage.welcome()

            case 2:
                print("\nTo recover your password,")
                umob = input("Enter your mobile number: ")

                try:
                    int(umob)
                except (ValueError, TypeError):
                    print("\n--Invalid Mobile Number format--\n"
                          "You will be redirected to the Homepage...\n")
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

