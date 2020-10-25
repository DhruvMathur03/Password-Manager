import cli_ui
import sqlite3 as sql
import sys
import db
import user


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
        user_info = user.User(f'{email}', database)
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
    tup = does_user_exist[0]
    user_ID = tup[0]
    insert_info = database.insert('user_data', {
                                  'website': f'{website}', 'username': f'{username}', 'password': f'{password}', 'user_ID': f'{user_ID}'})
    return True


def filter_website():
    website = cli_ui.ask_string("Please enter the name of the website")
    account_details = database.find('user_data', f'website = "{website}"')

    final_list = []

    for i in range(len(account_details)):
        current_list = account_details[i]

        final_list.append(
            {'username': current_list[2], 'password': current_list[3]})

    return final_list


def filter_username():
    username = cli_ui.ask_string("Please enter your common Username")
    account_details = database.find('user_data', f'username = "{username}"')

    final_list = []

    for i in range(len(account_details)):
        current_list = account_details[i]

        final_list.append(
            {'website': current_list[1], 'password': current_list[3]})

    return final_list


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

logged_in_choices = ['View Stored Passwords', 'Log Out', 'Add New Passwords']

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
