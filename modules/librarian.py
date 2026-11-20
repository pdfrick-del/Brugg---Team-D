#---Import for the Code---
import getpass
from modules import user_data
from pathlib import Path

#---Variables for the Code---
CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "Librarian_Login_data.csv"

def libarian_login():
    while True:
        print("Do you want to log in?")
        print("1. YES")
        print("2. NO")
        print("3. Forgot your account information or don't have an account?")

        choice = ""

        while choice not in ("1", "2", "3"):
            choice = input("Choose 1, 2 or 3: ")
            if choice not in ("1", "2", "3"):
                print("Error; return to choice")

        if choice == "1":
            librarian_ID = input("Enter ID: ").strip()
            password = getpass.getpass("Enter password: ", echo_char="*")

            users = user_data.load_users(CSV_PATH)

            logged_in = False

            for user in users:
                if librarian_ID == user["LibrarianID"] and password == user["Password"]:
                    print("Welcome", user["Username"])
                    logged_in = True
                    break

            else:
                print("Incorrect login credentials; return to choice")

            if logged_in:  
                break

        elif choice == "2":
            return

        elif choice == "3":
            print("Please contact your admin.")
            return

#Menu Options: Add Books, Update Books, delete Books, search books
