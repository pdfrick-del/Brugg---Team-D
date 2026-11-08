#---Import for the Code---
import csv
import getpass

#---Variables for the Code---
CSV_PATH = "Projekt/Brugg---Team-D/Librarian_Login_data.csv"

#---Functions for the Code---
def load_users():
  with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    users = list(reader)
  return users

while True:
#---Librarian Login---
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
            librarian_ID = input("Enter ID: ").strip().lower()
            password = getpass.getpass("Enter password: ", echo_char="*")

            users = load_users()

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
            break

        elif choice == "3":
            print("Please contact your admin.")
            break