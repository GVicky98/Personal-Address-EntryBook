import login
import quit
import signup

options_hp = 0  # hp -> homepage

def welcome():
    print("Welcome to PERSONAL ADDRESS BOOK \n"
          "Credits: G.Vignesh")
    print("1 => New User or Signup\n"
          "2 => Old User or Login\n"
          "3 => Exit")
    global options_hp
    try:
        options_hp = int(input("Enter the option: "))
    except (TypeError, ValueError):
        print("\n--Please enter a valid number--\n")
        welcome()
    else:
        if not (0 < int(options_hp) < 4):
            print("\n--Please enter a valid option--\n")
            welcome()
        else:
            option1 = options_hp
            match option1:
                case 1:
                    print("\n--Welcome to SIGNUP Process--\n")
                    signup.newUser()
                    print("--Please Login to continue--")
                    login.oldUser()
                case 2:
                    login.oldUser()
                case 3:
                    quit.exitApp()

