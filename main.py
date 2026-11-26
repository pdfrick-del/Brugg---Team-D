#---Imports for the Code---A
from modules import library_user, librarian

#---User Login---
while True:
    print("Press CTRL + C any time to return to the main menu.")

    while True:
        try:
            print("Are you a library user or a librarian? Please type in 1 or 2 based on your role.")
            print("1. library user")
            print("2. librarian")

            role = " "

            while role not in ("1", "2"):
                role = input("Choose 1 or 2: ")
                if role != "1" and role != "2":
                    print("Error; return to user role")

            if role == "1":
                user, fees = library_user.libary_user_login()

                if user is not None: 
                    library_user.libary_user_menu(user, fees)

            if role == "2":
                user = librarian.libarian_login()

                if user is not None:
                    librarian.libarian_menu(user)

        except KeyboardInterrupt:
            print("\nOperation cancelled. Return to main menu.")
            break