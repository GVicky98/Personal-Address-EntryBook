import mysql_idpass

def newUser():
    user_name = input("Enter Your Name: ")
    print("\nEnter the correct mobile number inorder to recover your password!")
    user_mob_no = int(input("Enter Your Mobile Number: "))
    print("\nUsername must be unique")
    user_id = input("Enter the UserID: ").lower()
    userid_list = mysql_idpass.get_idlist()

    while user_id in userid_list:
        print("User ID already taken. Please Try again.\n")
        user_id = input("Enter the UserID: ")

    p1 = input("\nCreate a new password: ")
    p2 = input("Confirm Password: ")

    while p1 != p2:
        print("\nPassword Mismatching. Please Try Again.")
        p2 = input("Confirm Password: ")
    if p1 == p2:
        userpass = p1

    c1 = mysql_idpass.create_new_user(user_name, user_id, userpass, user_mob_no)
    c1.create_user()
    print("You will be redirected to a login page...\n")
