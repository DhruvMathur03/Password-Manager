import random
import string
import clipboard
import cli_ui

def password_generator(length):
    sample_space = string.ascii_letters + string.digits + string.punctuation
    password = ''.join((random.choice(sample_space) for i in range(length)))
    return password

def clear_screen():
    print('\033[H\033[J')

def password_generator_main():
    condition = True

    while condition:

        choices = ("1. Upper Case Characters", "2. Lower Case Characters", "3. Special Characters", "4. Numbers")
        
        for i in choices:
            print(i)

        num = input("Enter the number of different types of characters you want: ")

        if num == '1':
            choice = input("Enter the number corresponding to the type of character you want: ")

            if choice == '1':
                print("Your Password will only contain Upper Case Characters")
                length = int(input("Enter the number of characters you want in your password: "))
                sample_space = string.ascii_uppercase
                password = ''.join((random.choice(sample_space) for i in range(length)))
                print("Your randomly generated password is: ", password)
                con = cli_ui.ask_yes_no("Do you want this password?")

                if con == True:
                    clipboard.copy(password)
                    print("Password has been copied to your clipboard :)")
                    condition = False
                else:
                    condition = True

            elif choice == '2':
                print("Your Password will only contain Lower Case Characters")
                length = int(input("Enter the number of characters you want in your password: "))
                sample_space = string.ascii_lowercase
                password = ''.join((random.choice(sample_space) for i in range(length)))
                print("Your randomly generated password is: ", password)
                con = cli_ui.ask_yes_no("Do you want this password?")

                if con == True:
                    clipboard.copy(password)
                    print("Password has been copied to your clipboard :)")
                    condition = False
                else:
                    condition = True

            elif choice == '3':
                print("Your Password will only contain Special Characters")
                length = int(input("Enter the number of characters you want in your password: "))
                sample_space = string.punctuation
                password = ''.join((random.choice(sample_space) for i in range(length)))
                print("Your randomly generated password is: ", password)
                con = cli_ui.ask_yes_no("Do you want this password?")

                if con == True:
                    clipboard.copy(password)
                    print("Password has been copied to your clipboard :)")
                    condition = False
                else:
                    condition = True

            elif choice == '4':
                print("Your Password will only contain Numbers")
                length = int(input("Enter the number of characters you want in your password: "))
                sample_space = string.digits
                password = ''.join((random.choice(sample_space) for i in range(length)))
                print("Your randomly generated password is: ", password)
                con = cli_ui.ask_yes_no("Do you want this password?")

                if con == True:
                    clipboard.copy(password)
                    print("Password has been copied to your clipboard :)")
                    condition = False
                else:
                    condition = True

        elif num == '2':
            c1, c2 = input("Enter the numbers corresponding to the types of characters you want: ").split()

            if c1 == '1':

                if c2 == '2':
                    print("Your Password will contain Upper Case and Lower Case Characters")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.ascii_lowercase + string.ascii_uppercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '3':
                    print("Your Password will contain Upper Case and Special Characters")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.punctuation + string.ascii_uppercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '4':
                    print("Your Password will contain Upper Case Characters and Numbers")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.digits + string.ascii_uppercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

            elif c1 == '2':

                if c2 == '1':
                    print("Your Password will contain Upper Case and Lower Case Characters")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.ascii_lowercase + string.ascii_uppercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '3':
                    print("Your Password will contain Lower Case and Special Characters")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.punctuation + string.ascii_lowercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '4':
                    print("Your Password will contain Upper Case Characters and Numbers")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.digits + string.ascii_lowercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True


            elif c1 == '3':

                if c2 == '1':
                    print("Your Password will contain Upper Case and Special Characters")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.punctuation + string.ascii_uppercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '2':
                    print("Your Password will contain Lower Case and Special Characters")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.punctuation + string.ascii_lowercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '4':
                    print("Your Password will contain Special Characters and Numbers")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.digits + string.punctuation
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

            elif c1 == '4':

                if c2 == '1':
                    print("Your Password will contain Upper Case and Numbers")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.digits + string.ascii_uppercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '2':
                    print("Your Password will contain Numbers and Lower Case Characters")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.digits + string.ascii_lowercase
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

                elif c2 == '3':
                    print("Your Password will contain Special Characters and Numbers")
                    length = int(input("Enter the number of characters you want in your password: "))
                    sample_space = string.digits + string.punctuation
                    password = ''.join((random.choice(sample_space) for i in range(length)))
                    print("Your randomly generated password is: ", password)
                    con = cli_ui.ask_yes_no("Do you want this password?")

                    if con == True:
                        clipboard.copy(password)
                        print("Password has been copied to your clipboard :)")
                        condition = False
                    else:
                        condition = True

        elif num == '3':
            c1, c2, c3 = input("Enter the numbers corresponding to the types of characters you want: ").split()

            if c1 == '1':

                if c2 == '2':
                    
                    if c3 == '3':
                        print("Your Password will contain Upper Case, Lower Case and Special Characters")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    elif c3 == '4':
                        print("Your Password will contain Upper Case, Lower Case Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '3':

                    if c3 == '2':
                        print("Your Password will contain Upper Case, Lower Case and Special Characters")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '4':
                        print("Your Password will contain Upper Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '4':
                    
                    if c3 == '2':
                        print("Your Password will contain Upper Case, Lower Case Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '3':
                        print("Your Password will contain Upper Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.digits + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True
                    
            elif c1 == '2':

                if c2 == '1':
                    
                    if c3 == '3':
                        print("Your Password will contain Upper Case, Lower Case and Special Characters")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    elif c3 == '4':
                        print("Your Password will contain Upper Case, Lower Case Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '3':

                    if c3 == '1':
                        print("Your Password will contain Upper Case, Lower Case and Special Characters")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '4':
                        print("Your Password will contain Lower Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_lowercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '4':
                    
                    if c3 == '1':
                        print("Your Password will contain Upper Case, Lower Case Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '3':
                        print("Your Password will contain Lower Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_lowercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

            elif c1 == '3':

                if c2 == '1':
                    
                    if c3 == '2':
                        print("Your Password will contain Upper Case, Lower Case and Special Characters")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    elif c3 == '4':
                        print("Your Password will contain Upper Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '2':

                    if c3 == '1':
                        print("Your Password will contain Upper Case, Lower Case and Special Characters")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '4':
                        print("Your Password will contain Lower Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_lowercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '4':
                    
                    if c3 == '1':
                        print("Your Password will contain Upper Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '2':
                        print("Your Password will contain Upper Case, Lower Case and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True
                
            elif c1 == '4':

                if c2 == '2':
                    
                    if c3 == '1':
                        print("Your Password will contain Upper Case, Lower Case Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    elif c3 == '3':
                        print("Your Password will contain Lower Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_lowercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '3':

                    if c3 == '2':
                        print("Your Password will contain Lower Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.digits + string.ascii_lowercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '1':
                        print("Your Password will contain Upper Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                elif c2 == '1':
                    
                    if c3 == '2':
                        print("Your Password will contain Upper Case, Lower Case Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

                    if c3 == '3':
                        print("Your Password will contain Upper Case, Special Characters and Numbers")
                        length = int(input("Enter the number of characters you want in your password: "))
                        sample_space = string.ascii_uppercase + string.digits + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        print("Your randomly generated password is: ", password)
                        con = cli_ui.ask_yes_no("Do you want this password?")

                        if con == True:
                            clipboard.copy(password)
                            print("Password has been copied to your clipboard :)")
                            condition = False
                        else:
                            condition = True

        elif num == '4':
            print("Your Password will contain Upper Case Characters, Lower Case Characters, Special Characters and Numbers")
            length = int(input("Enter the number of characters you want in your password: "))
            sample_space = string.ascii_uppercase + string.punctuation + string.digits + string.ascii_lowercase
            password = ''.join((random.choice(sample_space) for i in range(length)))
            print("Your randomly generated password is: ", password)
            con = cli_ui.ask_yes_no("Do you want this password?")

            if con == True:
                clipboard.copy(password)
                print("Password has been copied to your clipboard :)")
                condition = False
            else:
                condition = True

