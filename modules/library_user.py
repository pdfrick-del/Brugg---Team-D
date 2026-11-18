#---Imports for the Code---
import getpass
from pathlib import Path
from modules import user_data

#---Variables for the Code---
CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "Library_User_Login_data.csv"
FIELDNAMES = ["UserID", "Name", "Username", "Password", "Role", "Email", "Payment_Options"]

#---Libary User Login---
def libary_user_login():
    while True:
        users = user_data.load_users(CSV_PATH)
    
        print("Do you have a library user account?\n 1. YES\n 2. NO\n 3. Yes, but I forgot one of my login credentials.")

        while True:
            choice = input("Choose 1, 2 or 3: ")

            if choice in ("1", "2", "3"):
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
                return user

            print("Incorrect login credentials; return to choice")

        elif choice == "2":
            highest_id = max((int(user["UserID"][1:]) for user in users), default=0)
            new_user_id = f"U{highest_id + 1:03d}"

            new_name = user_data.get_name()
            new_user_name = user_data.get_username(users)
            new_password = user_data.get_password()
            new_email = user_data.get_email(users)
            payment_option = user_data.get_payment_options()

            users.append({
                "UserID": new_user_id,
                "Name": new_name,
                "Username": new_user_name,
                "Password": new_password,
                "Role": "Library User",
                "Email": new_email,
                "Payment_Options": payment_option 
            })

            user_data.save_users(CSV_PATH, users, FIELDNAMES)
            print("Your account has been created; return to Log in.")

        elif choice == "3":
            print("Please contact your admin.")

#---Menu---
def libary_user_menu(user):
    while True:
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
                        user_data.update_user(CSV_PATH, FIELDNAMES, user, "Name", user_data.get_name())
                        break

                    elif choice_edit == "2":
                        user_data.update_user(CSV_PATH, FIELDNAMES, user, "Username", user_data.get_username(user_data.load_users(CSV_PATH), user["UserID"]))
                        break
            
                    elif choice_edit == "3":
                        password = getpass.getpass("Enter password: ", echo_char="*")

                        if password == user["Password"]:
                            user_data.update_user(CSV_PATH, FIELDNAMES, user, "Password", user_data.get_password())
                            break

                        else:
                            print("Incorrect password")

                    elif choice_edit == "4":
                        user_data.update_user(CSV_PATH, FIELDNAMES, user, "Email", user_data.get_email(user_data.load_users(CSV_PATH), user["UserID"]))
                        break

                    elif choice_edit == "5":
                        user_data.update_user(CSV_PATH, FIELDNAMES, user, "Payment_Options", user_data.get_payment_options())
                        break

                    elif choice_edit == "6":
                        break

                if choice_edit == "6":
                    print("Return to choice options")
                    break

            #---Placeholder Options---
        if choice_options == "2" or choice_options == "3" or choice_options == "4":
            break

        if choice_options == "5":
            print("logging out; return to choice")
            return