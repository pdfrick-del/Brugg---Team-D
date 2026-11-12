#---Import for the Code---
import csv
import getpass
import string
from pathlib import Path

#---Variables for the Code---
CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "Library_User_Login_data.csv"
FIELDNAMES = ["UserID", "Name", "Username", "Password", "Role", "Email", "Payment_Options"]

#---Functions for the Code---
def load_users():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_users(users):
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(users)



while True:
    users = load_users()

  #---Libary User Login---
    while True:
    
        print("Do you have a library user account?\n 1. YES\n 2. NO")

        while True:
            choice = input("Choose 1 or 2: ")

            if choice in ("1", "2"):
                break

            print("Error; return to choice")

        if choice == "1":
            email = input("Enter email: ").strip().lower()
            password = getpass.getpass("Enter password: ", echo_char="*")

            logged_in = False

            for user in users:
                if email == user["Email"] and password == user["Password"]:
                    print("Welcome", user["Username"])
                    logged_in = True
                    break

            if logged_in:  
                break

            print("Incorrect login credentials; return to choice")

        elif choice == "2":
            while True:
                new_name = input("Enter your first name and last name: ").strip().title()

                if len(new_name.split()) >= 2:
                    break

                print("Please enter your first and last name")

            while True:
                new_user_name = input("Enter new username: ").strip().lower()
          
                if not new_user_name:
                    continue

                for user in users:
                    if new_user_name == user["Username"]:
                        print("Username already exists\nError; return to new user name")
                        break
                else:
                    print("Username is available")
                    break

            while True:
                new_password = getpass.getpass(
                    "Enter new password.\n"
                    "Please make sure that the password is at least 8 characters long and does not contain any spaces.\n"
                    "It must also contain at least one special character and one number: ", 
                    echo_char="*")

                if (len(new_password) >= 8 
                    and " " not in new_password
                    and any(char.isdigit() for char in new_password)
                    and any(char in string.punctuation for char in new_password)):
                    break
        
                print("The password does not meet the requirements.")

            while True:
                new_email = input("Enter your E-Mail: ").strip().lower()

                if (new_email.count("@") != 1
                    or not new_email.split("@")[0] 
                    or "." not in new_email.split("@")[1] 
                    or " " in new_email):
                    print("Invalid email address. Please try again.")
                    continue

                for user in users:
                    if new_email == user["Email"]:
                        print("Email already exists\nError; return to new email")
                        break

                else:
                    print("Email is available")
                    break    
      
            print("Choose your payment option.\n TWINT\n Bank Card")

            while True:
                payment_option = input("Enter your payment option: ").strip().upper()
      
                if payment_option in ("TWINT", "BANK CARD"):
                    break
                
                print("Error; return to payment option")

            highest_id = max((int(user["UserID"][1:]) for user in users), default=0)
            new_user_id = f"U{highest_id + 1:03d}"

            users.append({
                "UserID": new_user_id,
                "Name": new_name,
                "Username": new_user_name,
                "Password": new_password,
                "Role": "Library User",
                "Email": new_email,
                "Payment_Options": payment_option 
            })

            save_users(users)
            print("Your account has been created; return to Log in.")

  #---Menu---
    while logged_in:
        print("What do you want to do", user["Username"], "?")
        #---Placeholder Options---
        print("1. viewing account information\n2. viewing fees\n3. searching books\n4. requesting books\n5. Log out")
    
        while True:
            choice_options = input("Choose 1, 2, 3, 4 or 5: ")

            if choice_options in ("1", "2", "3", "4", "5"):
                break

            print("Error; return to options.")
    
        if choice_options == "1":
            while True:
                print(f"User ID: {user['UserID']}\n" f"Name: {user['Name']}\n" f"Username: {user['Username']}\n"
                      f"Password: {"*" * len(user['Password'])}\n" f"Role: {user['Role']}\n" f"Email: {user['Email']}\n" f"Payment Options: {user['Payment_Options']}")

                print("Would you like to edit your account information?")
                print("1. Name\n2. Username\n3. Password\n4. Email\n5. Payment Options\n6 No")

                while True:
                    choice_edit = input ("Choose 1, 2, 3, 4, 5 or 6: ")

                    if choice_edit == "1":
                        users = load_users()

                        new_name = input("Enter your new name: ").strip().title()
                        user["Name"] = new_name

                        for account in users:
                            if account["UserID"] == user["UserID"]:
                                account["Name"] = new_name
                                break
            
                        save_users(users)
                        break

                    if choice_edit == "2":
                        users = load_users()

                        new_user_name = input("Enter new username: ").strip().lower()
                        user["Username"] = new_user_name

                        for account in users:
                            if account["UserID"] == user["UserID"]:
                                account["Username"] = new_user_name
                                break
            
                        save_users(users)
                        break
            
                    if choice_edit == "3":
                        users = load_users()
                        break

                    if choice_edit == "4":
                        users = load_users()

                        new_email = input("Enter your E-Mail: ").strip().lower()
                        user["Email"] = new_email
            
                        for account in users:
                            if account["UserID"] == user["UserID"]:
                                account["Email"] = new_email
                                break

                        save_users(users)
                        break

                    if choice_edit == "5":
                        users = load_users()
                        break

                    if choice_edit == "6":
                        break

                if choice_edit == "6":
                    print("No Changes; return to choice options")
                    break

        #---Placeholder Options---
        if choice_options == "2" or choice_options == "3" or choice_options == "4":
            break

        if choice_options == "5":
            print("logging out; return to choice")
            logged_in = False
            break