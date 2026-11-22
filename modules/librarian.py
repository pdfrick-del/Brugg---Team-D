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

            for user in users:
                if librarian_ID == user["LibrarianID"] and password == user["Password"]:
                    print("Welcome", user["Username"])
                    return user

            else:
                print("Incorrect login credentials; return to choice")

        elif choice == "2":
            return

        elif choice == "3":
            print("Please contact your admin.")
            return

#Menu Options: Add Books, Update Books, delete Books, search books
def libarian_menu(user):
    while True:
        print("What do you want to do", user["Username"], "?\n"
                "1. adding books\n2. updating books\n3. deleting books\n4. search books\n5. Log out")

        while True:
            choice_options = input("Choose 1, 2, 3, 4, 5 or 6: ")

            if choice_options in ("1", "2", "3", "4", "5", "6"):
                break

            print("Error; return to options.")

        if choice_options == "1. Add Book":
            break

        if choice_options == "2. Update Book":
            break

        if choice_options == "3. Delete Book":
            break

        if choice_options == "4. View Catalog":
            break

        if choice_options == "5. Filter Books":
            break

        if choice_options == "6. Sort Books":
            break

        if choice_options == "7.Filter and Sort Books":

            break

        if choice_options == "8. Exit":
            break


            print("logging out; return to choice")
            return