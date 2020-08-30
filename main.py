import cli_ui

dict1 = {"pugsey": "12345", "dhruv": "123456", "yash": "1234567"}
lst = {"d@gmail.com", "y@gmail.com", "p@gmail.com"}

choices = ['Login', 'Sign Up']
c = cli_ui.ask_choice("Would you like to", choices=choices)
print(c)

if c == "Login":
    def login():
        usrnm = cli_ui.ask_string("Username")
        if usrnm in dict1:
            pswd = cli_ui.ask_password("Password")
            if pswd in dict1:
                print("Logged in :)")
            else:
                print("Wrong Password")
        else:
            print("Incorrect username")
        return

if c == "Sign Up":
    def sign_in():
        eml = cli_ui.ask_string("Please enter Email ID")
        if eml in lst:
            print("An account linked to this ID already exists")

        else:

            usrnm1 = cli_ui.ask_string("Please enter username")
            if usrnm1 in dict1:
                print("Username already exists, please try again")
            else:
                pwd1 = cli_ui.ask_password("please enter password")
                dict1[usrnm1] = pwd1
        return
login()
