
# install cryptography module by using "pip install cryptography command"

# import cryptography module

from cryptography.fernet import Fernet

# import pathlib module to check existing files
from pathlib import Path

master_passwd = input("Input master password: ")

# Master password = "cupcake"

if master_passwd == "cupcake":
    print("Authentication successful!")

else:
    print("Invalid password")
    quit()


# Check if key.key already exists. Else, create a new key file
path_to_key_file = 'key.key'
path = Path(path_to_key_file)

def create_key():

    if path.is_file():
        pass

    else:
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
            print("New shiny key generated for encryption!!")

create_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

# Function to add account and it accepts two parameters
def add_passwd(account_name, uname, passwd):

    # File handling using context manager

    with open("passwords.txt", 'a') as files:
        files.write(account_name + "|" + fer.encrypt(uname.encode()).decode() + "|" + fer.encrypt(passwd.encode()).decode() + "\n")

# Function to view passwords

def view_passwd():
    # Try and except block to catch errors for file handling

    try:
        with open("passwords.txt", 'r') as files:
            for line in files.readlines():
                raw_list = line.rstrip() # rstrip will strip the "\n" and display

                # Below inline code will split the values when it encounters pipe ('|') symbol and stores it in LHS respectively
                # Note: Split returns the values in the form of list new_username,new_password = ["pinku", puchku"]

                account_name, new_username,new_password = raw_list.split("|")

                print("Account name:", account_name, ", Username:", fer.decrypt(new_username.encode()).decode(), ", Password: ", fer.decrypt(new_password.encode()).decode())

    except FileNotFoundError as file_404:
        print("There are NO passwords to show. Try adding one instead.\n")

        # print("Error message from the system:\n" + str(file_404))

while True:

    task = input("ADD or VIEW password? Press 'q' to quit: ").lower()

    if task == "q":
        print("Bye!")
        break

    elif task == "add":
        account_name = input("Type Account name: ")
        new_username = input("Type username: ")
        new_password = input("Type password: ")

        add_passwd(account_name, new_username, new_password)

    elif task == "view":
        view_passwd()

    else:
        print("Invalid input")
        continue


# Notes:

# We use decode to remove the binary notation (b'text' is different from 'text')