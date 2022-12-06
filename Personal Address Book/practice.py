import re

user_name = input("Enter Your Name: ")
while not re.match('^\S[A-Z|a-z]{3,29}$', user_name):
    print("--Please enter a valid UserName--")
    user_name = input("Please enter Your Name: ")
