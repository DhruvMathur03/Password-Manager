import random
import string
import clipboard
import cli_ui

def printdashes():
    print("------------------------------------------------------------------------------------------------------------------------------------------------")

def clear_screen():
    print('\033[H\033[J')

def password_generator_main(type1, type2, type3, type4):
    condition = True

    while condition:
        length = int(input("How many characters do you want in your password? "))

        if type1 == True:

            if type2 == True:

                if type3 == True:

                    if type4 == True:
                        sample_space = string.ascii_letters + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        elif c == False:
                            condition = True                        
                        
                    else:
                        sample_space = string.ascii_letters + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        elif c == False:
                            condition = True 

                else:

                    if type4 == True:
                        sample_space = string.ascii_letters + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                        
                    else:
                        sample_space = string.ascii_letters
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                    
            else:

                if type3 == True:

                    if type4 == True:
                        sample_space = string.ascii_uppercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                        
                    else:
                        sample_space = string.ascii_uppercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                else:
                    if type4 == True:
                        sample_space = string.ascii_uppercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                        
                    else:
                        sample_space = string.ascii_uppercase
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 

        else:
            
            if type2 == True:

                if type3 == True:

                    if type4 == True:
                        sample_space = string.ascii_lowercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                        
                    else:
                        sample_space = string.ascii_lowercase + string.punctuation 
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 

                else:

                    if type4 == True:
                        sample_space = string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                        
                    else:
                        sample_space = string.ascii_lowercase
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                    
            else:

                if type3 == True:

                    if type4 == True:
                        sample_space = string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                        
                    else:
                        sample_space = string.punctuation 
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 

                else:
                    if type4 == True:
                        sample_space = string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clear_screen()
                        printdashes()
                        print("Your password is: ", password)
                        printdashes()
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clipboard.copy(password)
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password

                        else:
                            condition = True 
                        
                    else:
                        print("You didn't choose any type of character.")
                        c = cli_ui.ask_yes_no("Do you want to retry?")

                        if c == True:
                            condition = True
                        
                        else:
                            clear_screen()
                            condition = False
                            return False