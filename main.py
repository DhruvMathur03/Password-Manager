import cli_ui
import sqlite3 as sql
import sys
import db


database = db.DB("pugsey.db")
logged_in_user = None


def login():
    print("Login")
    email = cli_ui.ask_string("Email")
    password = cli_ui.ask_password("Password")

    does_user_exist = database.find(
        'Users', f'password = "{password}", email = "{email}"')

    if len(does_user_exist) > 0:
        print("Logged in")
    else:
        print("Incorrect ID or Password")
        return login()


def sign_up():
    print("Sign up")
    email = cli_ui.ask_string("Please enter Email ID")
    does_email_exist = database.find('Users', f'email = "{email}"')

    if len(does_email_exist) > 0:
        print("An account linked to this ID already exists")
        return False
    else:
        pwd1 = cli_ui.ask_password("please enter password")
        database.insert('Users', {'email': email, 'password': pwd1})
        return login()


choices = ['Login', 'Sign Up', 'Exit']

flag = False

while not flag:
    c = cli_ui.ask_choice("Would you like to", choices=choices)

    if c == "Login":
        flag = login()
    elif c == "Sign Up":
        flag = sign_up()
    elif c == "Exit":
        sys.exit(0)
