import cli_ui
import sqlite3 as sql
import sys
import db
import user
import helper
import clipboard

database = db.DB("pugsey.db")
user_info = None

def login():
    global user_info
    print("Login")
    email = cli_ui.ask_string("Email")
    password = cli_ui.ask_password("Password")
    does_user_exist = database.find(
        'Users', f'email = "{email}" AND password="{password}"')

    if len(does_user_exist) > 0:
        user_info = user.User(does_user_exist[0][0], email, database)
        helper.clear_screen()
        print("Logged in")
        return True
    else:
        helper.clear_screen()
        print("Incorrect ID or Password")
        return False

def sign_up():
    print("Sign up")
    email = cli_ui.ask_string("Please enter Email ID")
    does_email_exist = database.find('Users', f'email = "{email}"')

    if len(does_email_exist) > 0:
        helper.clear_screen()
        print("An account linked to this ID already exists")
        return False
    else:
        pwd1 = cli_ui.ask_password("please enter password")
        database.insert('Users', {'email': email, 'password': pwd1})
        helper.clear_screen()
        return login()

def add_passwords():
    website = cli_ui.ask_string("Please enter the website\'s name")
    username = cli_ui.ask_string("Please enter your username")
    choice1 = cli_ui.ask_yes_no(
        "Would you like to generate a new password?", default=False)

    if choice1 == True:
        password = helper.password_generator_main()
        choice = cli_ui.ask_yes_no(
            "Would you like to add this password", default=False)
        if choice == True:
            user_info.add_password(website, username, password)
            print("The password has been added.")
        elif choice == False:
            helper.clear_screen()
            add_passwords()
    elif choice1 == False:
        password1 = cli_ui.ask_string("Please enter your password")
        user_info.add_password(website, username, password1)
        print("The password has been added.")
        helper.clear_screen()

    return True

def filter_website():
    website = cli_ui.ask_string("Please enter the name of the website")
    return user_info.filter_website(website)

def filter_username():
    username = cli_ui.ask_string("Please enter your common Username")
    return user_info.filter_username(username)

def edit():
    user_info.edit_account_choice()
    choices = ['Password', 'Username', 'Username and Password']
    a = cli_ui.ask_choice("What would you like to edit?", choices=choices)

    if a == 'Password':
        new_password = cli_ui.ask_string("Enter new Password")
        user_info.edit(f'password = "{new_password}"')
        helper.clear_screen()
        return True
    elif a == 'Username':
        new_username = cli_ui.ask_string("Enter new Username")
        user_info.edit(f'username = "{new_username}"')
        helper.clear_screen()
        return True
    elif a == 'Username and Password':
        new_password = cli_ui.ask_string("Enter new Password")
        new_username = cli_ui.ask_string("Enter new Username")
        user_info.edit(
            f'username = "{new_username}" AND password = "{new_password}"')
        helper.clear_screen()

        return True

def delete():
    user_info.delete()
    helper.clear_screen()
    return True

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
                     'Add New Passwords', 'Edit Passwords', 'Delete Passwords', 'Password Generator']

achoices = ['Filter by Website', 'Filter by Username', 'View All']

while flag:
    c = cli_ui.ask_choice("Would you like to", choices=logged_in_choices)
    
    if c == 'View Stored Passwords':
        a = cli_ui.ask_choice("Would you like to", choices=achoices)

        if a == 'Filter by Website':
            info = filter_website()
            helper.clear_screen()
            print(info)

        elif a == 'Filter by Username':
            info = filter_username()
            helper.clear_screen()
            print(info)
            
        elif a == 'View All':
            info = user_info.get_all_password()
            helper.clear_screen()
            print(info)
    
    elif c == 'Log Out':
        helper.clear_screen()
        sys.exit(0)
    
    elif c == 'Add New Passwords':
        helper.clear_screen()
        flag = add_passwords()
    
    elif c == 'Edit Passwords':
        helper.clear_screen()
        flag = edit()
    
    elif c == 'Delete Passwords':
        helper.clear_screen()
        flag = delete()
    
    elif c == 'Password Generator':
        helper.clear_screen()
        password = helper.password_generator_main()
        if password:
            choice = cli_ui.ask_yes_no(
            "Would you like to add this password", default=False)
            if choice == True:
                website = cli_ui.ask_string("Please enter the website\'s name")
                username = cli_ui.ask_string("Please enter your username")
                user_info.add_password(website, username, password)
                helper.clear_screen()
                print("The password has been added.")
            elif choice == False:
                helper.clear_screen()
        flag = True