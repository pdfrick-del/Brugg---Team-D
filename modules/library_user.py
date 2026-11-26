#---Imports for the Code---
import getpass
from datetime import date
from pathlib import Path
from modules import book_lending, user_data, membership_fees

#---Variables for the Code---
CSV_PATH_LOGIN = Path(__file__).resolve().parent.parent / "data" / "Library_User_Login_data.csv"
CSV_PATH_FEES = Path(__file__).resolve().parent.parent / "data" / "Library_User_Fees_data.csv"
FIELDNAMES_LOGIN = ["UserID", "Name", "Username", "Password", "Role", "Email", "Payment_Options"]
FIELDNAMES_FEES = ["UserID", "Account_Creation_Date", "Anual_Fee", "Late_Fee", "Outstanding_Amount", "Discounts", "Notifications", "Last_Update"]

#---Libary User Login---
def libary_user_login():
    while True:
        users = user_data.load_users(CSV_PATH_LOGIN)
        fees = user_data.load_users(CSV_PATH_FEES)
    
        print("Do you have a library user account?\n 1. YES\n 2. NO\n 3. Yes, but I forgot one of my login credentials.")

        while True:
            choice = input("Choose 1, 2 or 3: ")

            if choice in ("1", "2", "3"):
                break

            print("Error; return to choice")

        if choice == "1":
            email = input("Enter email: ").strip().lower()
            password = getpass.getpass("Enter password: ", echo_char="*")
            user_id = ""

            logged_in = False

            for user in users:
                if email == user["Email"] and password == user["Password"]:
                    user_id = user["UserID"]
                    print("Welcome", user["Username"])
                    logged_in = True
                    break

            if logged_in:
                for fee in fees:
                    if user_id == fee["UserID"]:
                        return user, fee
            
            print("Incorrect login credentials; return to choice")

        elif choice == "2":
            while True:
                highest_id = max((int(user["UserID"][1:]) for user in users), default=0)
                new_user_id = f"U{highest_id + 1:03d}"

                new_name = user_data.get_name()
                new_user_name = user_data.get_username(users)
                new_password = user_data.get_password()
                new_email = user_data.get_email(users)
                payment_option = user_data.get_payment_options()

                registration_date = date.today().isoformat()
                while True:
                    users.append({
                        "UserID": new_user_id,
                        "Name": new_name,
                        "Username": new_user_name,
                        "Password": new_password,
                        "Role": "Library User",
                        "Email": new_email,
                        "Payment_Options": payment_option
                    })

                    user_data.save_users(CSV_PATH_LOGIN, users, FIELDNAMES_LOGIN)
                    
                    fees.append({
                        "UserID": new_user_id,
                        "Account_Creation_Date": registration_date,
                        "Anual_Fee": 50,
                        "Late_Fee": 0,
                        "Outstanding_Amount": 50,
                        "Discounts": 0,
                        "Notifications" : "NO",
                        "Last_Update": registration_date
                    })

                    user_data.save_users(CSV_PATH_FEES, fees, FIELDNAMES_FEES)
                    print("Your account has been created; return to Log in.")
                    break
                break

        elif choice == "3":
            print("Please contact your admin.")

#---Menu---
def libary_user_menu(user, fees):
    #---Review of Fees---
    if membership_fees.update_membership_fees(fees):
        registration_date = date.fromisoformat(fees["Account_Creation_Date"])
        outstanding_amount = float(fees["Outstanding_Amount"])

        discount = membership_fees.calculate_discount(registration_date)
        anual_fee = membership_fees.calculating_anual_fee(registration_date)
        outstanding_amount = membership_fees.adding_current_anual_fee(outstanding_amount, anual_fee)
        late_fee = membership_fees.late_fee(outstanding_amount, anual_fee)
        outstanding_amount = membership_fees.adding_current_late_fee(outstanding_amount, late_fee)

        user_data.update_user(CSV_PATH_FEES, FIELDNAMES_FEES, fees, "Discounts", discount)
        user_data.update_user(CSV_PATH_FEES, FIELDNAMES_FEES, fees, "Anual_Fee", anual_fee)
        user_data.update_user(CSV_PATH_FEES, FIELDNAMES_FEES, fees, "Late_Fee", late_fee)
        user_data.update_user(CSV_PATH_FEES, FIELDNAMES_FEES, fees, "Outstanding_Amount", outstanding_amount)
        user_data.update_user(CSV_PATH_FEES, FIELDNAMES_FEES, fees, "Last_Update", date.today())
                                

    while True:

        while True:
            if fees['Notifications'] == "YES":
                if float(fees['Outstanding_Amount']) > 0:
                    print(f"You have unpaid fees: CHF{fees['Outstanding_Amount']}.-")
                    break
            else:
                break


        print("What do you want to do", user["Username"], "?\n"
              "1. viewing account information\n2. viewing fees\n3. searching books\n"
              "4. Issued Books\n5. Issue a book\n6. Log out")
    
        while True:
            choice_options = input("Choose 1, 2, 3, 4, 5 or 6: ")

            if choice_options in ("1", "2", "3", "4", "5", "6"):
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
                        user_data.update_user(CSV_PATH_LOGIN, FIELDNAMES_LOGIN, user, "Name", user_data.get_name())
                        break

                    elif choice_edit == "2":
                        user_data.update_user(CSV_PATH_LOGIN, FIELDNAMES_LOGIN, user, "Username", user_data.get_username(user_data.load_users(CSV_PATH_LOGIN), user["UserID"]))
                        break
            
                    elif choice_edit == "3":
                        password = getpass.getpass("Enter password: ", echo_char="*")

                        if password == user["Password"]:
                            user_data.update_user(CSV_PATH_LOGIN, FIELDNAMES_LOGIN, user, "Password", user_data.get_password())
                            break

                        else:
                            print("Incorrect password")

                    elif choice_edit == "4":
                        user_data.update_user(CSV_PATH_LOGIN, FIELDNAMES_LOGIN, user, "Email", user_data.get_email(user_data.load_users(CSV_PATH_LOGIN), user["UserID"]))
                        break

                    elif choice_edit == "5":
                        user_data.update_user(CSV_PATH_LOGIN, FIELDNAMES_LOGIN, user, "Payment_Options", user_data.get_payment_options())
                        break

                    elif choice_edit == "6":
                        break

                if choice_edit == "6":
                    print("Return to choice options")
                    break

            #---Placeholder Options---
        if choice_options == "2":
            while True:
                print("What do you want to do", user["Username"], "?\n"
                      "1. View Fee Information\n2. Activate Notification\n3.Return to choice options")

                while True:
                    choice_fees = input ("Choose 1, 2 or 3: ")

                    if choice_fees == "1":
                        print(f"User ID: {fees['UserID']}\n" f"Account Creation Date: {fees['Account_Creation_Date']}\n" 
                              f"Anual Fee: {fees['Anual_Fee']}\n" f"Late Fee: {fees['Late_Fee']}\n" 
                              f"Outstanding Amount: {fees['Outstanding_Amount']}\n" f"Discounts: {fees['Discounts']}\n")
                        break

                    elif choice_fees == "2":
                        print("Would you like to activate notifications for your fees?\n1.Yes\n2.No")
                        choice_notifications = input ("Choose 1, or 2: ")

                        if choice_notifications == "1":
                            user_data.update_user(CSV_PATH_FEES, FIELDNAMES_FEES, user, "Notifications", "YES" )
                            break

                        elif choice_notifications == "2":
                            user_data.update_user(CSV_PATH_FEES, FIELDNAMES_FEES, user, "Notifications", "NO" )
                            break

                    elif choice_fees == "3":
                        break

                if choice_fees == "3":
                    print("Return to choice options")
                    break
                
        if choice_options ==  "3":
            break

        if choice_options ==  "4":
            book_lending.display_issued_books(user)

        if choice_options == "5":
            book_lending.issue_book(user)

        if choice_options == "6":
            print("logging out; return to choice")
            return

        