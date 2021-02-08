import random
import string
import clipboard
import cli_ui

def clear_screen():
    print('\033[H\033[J')

def password_generator_main():
    condition = True

    while condition:
        type1 = cli_ui.ask_yes_no("Do you want Upper Case Characters in your password?")
        type2 = cli_ui.ask_yes_no("Do you want Lower Case Characters in your password?")
        type3 = cli_ui.ask_yes_no("Do you want Special Characters in your password?")
        type4 = cli_ui.ask_yes_no("Do you want Numbers in your password?")

        if type1 == True:

            if type2 == True:

                if type3 == True:

                    if type4 == True:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_letters + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True                        
                        
                    else:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_letters + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 

                else:

                    if type4 == True:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_letters + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                        
                    else:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_letters
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                    
            else:

                if type3 == True:

                    if type4 == True:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_uppercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                        
                    else:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_uppercase + string.punctuation
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                else:
                    if type4 == True:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_uppercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                        
                    else:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_uppercase
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 

        else:
            
            if type2 == True:

                if type3 == True:

                    if type4 == True:
                        llength = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_lowercase + string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                        
                    else:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_lowercase + string.punctuation 
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 

                else:

                    if type4 == True:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_lowercase + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                        
                    else:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.ascii_lowercase
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                    
            else:

                if type3 == True:

                    if type4 == True:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.punctuation + string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 
                        
                    else:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.punctuation 
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
                            condition = True 

                else:
                    if type4 == True:
                        length = int(input("How many characters do you want in your password? "))
                        sample_space = string.digits
                        password = ''.join((random.choice(sample_space) for i in range(length)))
                        clipboard.copy(password)
                        clear_screen()
                        print('''--------------------------------------------------------------------------------------------------------------
Your password is:''', password, '''
--------------------------------------------------------------------------------------------------------------''')
                        c = cli_ui.ask_yes_no("Do you like this password? ")

                        if c == True:
                            clear_screen()
                            print("The password has been copied to your clipboard.")
                            condition = False
                            return password
                        if c == False:
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