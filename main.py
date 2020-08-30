import cli_ui


def login():
    usrnm = cli_ui.ask_string("Username")
    pwd = cli_ui.ask_password("Password")

    if usrnm in dict1 and dict1[usrnm] == pwd:
        print("Logged in :)")
    else:
        print("Wrong Username/Password")

    return


def sign_in():
    email = cli_ui.ask_string("Please enter Email ID")

    if email in lst:
        print("An account linked to this ID already exists")
    else:
        lst.append(email)
        usrnm1 = cli_ui.ask_string("Please enter username")

        if usrnm1 in dict1:
            print("Username already exists, please try again")
        else:
            pwd1 = cli_ui.ask_password("please enter password")
            dict1[usrnm1] = pwd1

    return


dict1 = {"pugsey": "12345", "dhruv": "123456", "yash": "1234567"}
lst = ["d@gmail.com", "y@gmail.com", "p@gmail.com"]

choices = ['Login', 'Sign Up']
c = cli_ui.ask_choice("Would you like to", choices=choices)
print(c)

if c == "Login":
    login()
elif c == "Sign Up":
    sign_in()
