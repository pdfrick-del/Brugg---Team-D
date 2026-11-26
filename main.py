# ---Imports---
from modules import library_user, librarian


# ---User Login---
def main():
    """Control the main program flow."""
    while True:
        try:
            while True:
                print(
                    "Press CTRL + C any time to return to the main menu.\n"
                    "Are you a library user or a librarian?\n"
                    "Please type in 1 or 2 based on your role.\n"
                    "1. library user\n"
                    "2. librarian"
                )

                role = input("Choose 1 or 2: ").strip()

                if role in ("1", "2"):
                    break

                print("Error; return to user role")

            if role == "1":
                user, fees = library_user.libary_user_login()

                if user is not None:
                    library_user.libary_user_menu(user, fees)

            elif role == "2":
                user = librarian.librarian_login()

                if user is not None:
                    librarian.librarian_menu(user)

        except KeyboardInterrupt:
            print("\nOperation cancelled. Return to main menu.")


# ---Execute flow---
if __name__ == "__main__":
    main()
