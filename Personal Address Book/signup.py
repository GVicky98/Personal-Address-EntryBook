import mysql_idpass
import re

def newUser():
    user_name = input("Enter Your Name: ")
    while not re.match('^\S[A-Z|a-z]{3,29}$', user_name):
        print("--Please enter a valid UserName--")
        user_name = input("Please enter Your Name: ")

    print("\nThis will be used to recover password incase you forget password!")
    user_mob_no = input("Enter Your Mobile Number: ")
    while not re.match('^\d{10,}$', user_mob_no):
        print("--Please enter a valid Mobile Number--")
        user_mob_no = input("Enter Your Mobile Number: ")

    print("\nUserid must be unique")
    user_id = input("Enter the UserID: ").lower()
    while not re.match('^\w{3,20}$', user_id):
        print("\n--Please enter the valid Userid--\n")
    userid_list = mysql_idpass.get_idlist()

    while user_id in userid_list:
        print("\n--User ID already taken. Please Try again--\n")
        user_id = input("Enter the UserID: ")

    print("\nPassword must be 3 to 20 chars long")
    p1 = input("Create a new password: ")
    while not re.match('^\w{3,20}$', p1):
        print("\n--Please enter a valid Password--\n")
        p1 = input("Create a new password: ")

    p2 = input("Confirm Password: ")

    while p1 != p2:
        print("\n--Password Mismatching--\n")
        p2 = input("Confirm Password: ")
    if p1 == p2:
        userpass = p1

    c1 = mysql_idpass.create_new_user(user_name, user_id, userpass, user_mob_no)
    c1.create_user()
    print("Redirecting to a login page...\n")
