# ---Imports---
import getpass
from pathlib import Path

from modules import user_data

# ---Variables for the Code---
CSV_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "Librarian_Login_data.csv"
)


def librarian_login():
    """Execute Login for librarian."""
    while True:
        print(
            "Do you want to log in?\n"
            "1. YES\n"
            "2. NO\n"
            "3. Forgot your account information or don't have an account?"
        )

        while True:
            choice = input("Choose 1 to 3: ").strip()

            if choice in ("1", "2", "3"):
                break

            print("Error; return to choice")

        if choice == "1":
            librarian_id = input("Enter ID: ").strip()
            password = getpass.getpass("Enter password: ", echo_char="*")

            users = user_data.load_users(CSV_PATH)

            for user in users:
                if (
                    librarian_id == user["LibrarianID"]
                    and password == user["Password"]
                ):
                    print("Welcome", user["Username"])
                    return user

            else:
                print("Incorrect login credentials; return to choice")

        elif choice == "2":
            return

        elif choice == "3":
            print("Please contact your admin.")
            return


# ---Menu Options: Add Books, Update Books, delete Books, search books---
def librarian_menu(user):
    """Execute menu for librarian."""
    while True:
        print(
            "What do you want to do", user["Username"], "?\n"
            "1. Add Book\n"
            "2. Update Book\n"
            "3. Delete Book\n"
            "4. View Catalog\n"
            "5. Filter Books\n"
            "6. Sort Books\n"
            "7. Filter and Sort Books\n"
            "8. Exit"
        )

        while True:
            choice_options = input("Choose 1 to 8: ").strip()

            if choice_options in ("1", "2", "3", "4", "5", "6", "7", "8"):
                break

            print("Error; return to options.")

        if choice_options == "1":
            pass

        elif choice_options == "2":
            pass

        elif choice_options == "3":
            pass

        elif choice_options == "4":
            pass

        elif choice_options == "5":
            pass

        elif choice_options == "6":
            pass

        elif choice_options == "7":
            pass

        elif choice_options == "8":
            print("logging out; return to choice")
            return
