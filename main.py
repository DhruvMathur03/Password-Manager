import cli_ui
import sqlite3 as sql
import sys
import db
import user
import helper
import clipboard

database = db.DB("pugsey.db")
logged_in_user = None
user_info = None


def login():
    global user_info
    global does_user_exist
    print("Login")
    email = cli_ui.ask_string("Email")
    password = cli_ui.ask_password("Password")

    does_user_exist = database.find(
        'Users', f'email = "{email}" AND password="{password}"')

    if len(does_user_exist) > 0:
        user_info = user.User(does_user_exist[0][0], email, database)
        print("Logged in")
        return True
    else:
        print("Incorrect ID or Password")
        return False


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


def add_passwords():
    website = cli_ui.ask_string("Please enter the website\'s name")
    username = cli_ui.ask_string("Please enter your username")
    password = cli_ui.ask_string("Please enter your password")
    user_info.add_password(website, username, password)
    return True


def filter_website():
    website = cli_ui.ask_string("Please enter the name of the website")
    return user_info.filter_website(website)


def filter_username():
    username = cli_ui.ask_string("Please enter your common Username")
    return user_info.filter_username(username)


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

logged_in_choices = ['View Stored Passwords', 'Log Out',
                     'Add New Passwords', 'Generate New Password']

achoices = ['Filter by Website', 'Filter by Username', 'View All']

while flag:
    c = cli_ui.ask_choice("Would you like to", choices=logged_in_choices)

    if c == 'View Stored Passwords':
        a = cli_ui.ask_choice("Would you like to", choices=achoices)

        if a == 'Filter by Website':
            info = filter_website()
            print(info)

        elif a == 'Filter by Username':
            info = filter_username()
            print(info)

        elif a == 'View All':
            info = user_info.get_all_password()
            print(info)

    elif c == 'Log Out':
        sys.exit(0)

    elif c == 'Add New Passwords':
        flag = add_passwords()

    elif c == 'Generate New Password':
        length = int(input("Enter required Length of Password :"))
        password = helper.password_generator(length)
        print(password)
        clipboard.copy(password)
        print("The password has been copied to your clipboard")
        choice = cli_ui.ask_yes_no(
            "Would you like to add this password", default=False)

        if choice == True:
            website = cli_ui.ask_string("Enter the website name")
            username = cli_ui.ask_string("Enter the username")
            user_info.add_password(website, username, password)

        elif choice == False:
            flag = True
