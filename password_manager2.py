#password_manager1.py
#create and show passwords for users
#Ishanika. S, Feb 22

name = ""
age = ""


password_list = []

user_list = [["Bdsc123", "Pass1234"]]

# Function used for user to store an existing password
def menu(name):
    mode = int(input("""Choose mode by entering a number: \n1.Add passwords \n2.View Passwords \n3.Exit"""))
    return mode

def add_password():
    pass_input = input("Enter a new password: ")
    password_list.append(pass_input)

def display():
    for password in password_list:
        print("{}".format(password))
        
# Intrduction to password manager 
print("Hi, welcome to password manager")

name = input("What is your name?")

print("Hi!", name)

#Main Routine
while True:
    #Asking for user input and .upper() function which converts user unput to uppercase
    user = input("Please enter: \nL to login or N to create an account: ").upper()
    if user == "L":
        u_username = input("Username: ")
        u_password = input("Password: ")
        if u_username and u_password in user_list:
            print("Welcome", name)
        break
      #Asking user for age after selecting to create an account
    elif user == "N":
        #User must be above the age of 13 in order to continue
        age = int(input("What is your age?: "))
        if age < 13:
            print("Apologies, you must be over 13 to use password manager")
            exit()
        else:
            print("Thank you")
        u_username = input("Enter unsername: ")
        while True:
            u_password = input("Your password must be at least 8 characters long, include a capital letter and a number. \nEnter password:").strip()
            if (any(passreqs.isupper() for passreqs in u_password) and any(passreqs.isdigit()for passreqs in u_password) and len(u_password) >= 8):
                user_list.append([u_username, u_password])
                print("Your account has been created!")
            else:
                print("Your password does not meet the password requirements. It must have at least 8 characters, imcorporate a capital letter as well as an integer")
            break
    else:
        print("That is an invalid option, please enter L to login ot N to create an account: ")
# Calling function to store existing passowrd
while True:
    chosen_option = menu(name)
    if chosen_option == 1:
        add_password()
    elif chosen_option == 2:
        display()
    elif chosen_option == 3:
        break
    else:
        print("That is an invalid option, Please enter again")

print("Thank you for using password manager")