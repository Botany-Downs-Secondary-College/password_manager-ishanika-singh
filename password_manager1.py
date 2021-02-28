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