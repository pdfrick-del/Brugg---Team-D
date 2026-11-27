# ---Imports for the Code---
import csv
import getpass
import string

# ---Functions for the Code---


def load_users(CSV_PATH):
    """Read users in CSV"""
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_users(CSV_PATH, users, fieldnames):
    """Save new user input in CSV"""
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows(users)


def get_name():
    """Enter a new name"""
    while True:
        new_name = input(
            "Enter your first name and last name: "
        ).strip().title()

        if len(new_name.split()) >= 2:
            return new_name

        print("Please enter your first and last name")


def get_username(users, current_user_id=None):
    """Enter a new username"""
    while True:
        new_user_name = input("Enter new username: ").strip().lower()

        if not new_user_name:
            continue

        for user in users:
            if (
                new_user_name == user["Username"]
                and user["UserID"] != current_user_id
            ):
                print(
                    "Username already exists\nError; return to new user name"
                )
                break
        else:
            print("Username is available")
            return new_user_name


def get_password():
    """Enter a new password"""
    while True:
        new_password = getpass.getpass(
            "Enter new password.\n"
            "Please make sure that the password is at least 8 characters long "
            "and does not contain any spaces.\n"
            "It must also contain at least one special character "
            "and one number: ",
            echo_char="*")

        if (
            len(new_password) >= 8
            and " " not in new_password
            and any(char.isdigit() for char in new_password)
            and any(char in string.punctuation for char in new_password)
        ):
            return new_password

        print("The password does not meet the requirements.")


def get_email(users, current_user_id=None):
    """Enter a new email"""
    while True:
        new_email = input("Enter your E-Mail: ").strip().lower()

        if (
            new_email.count("@") != 1
            or not new_email.split("@")[0]
            or "." not in new_email.split("@")[1]
            or " " in new_email
        ):
            print("Invalid email address. Please try again.")
            continue

        for user in users:
            if (
                new_email == user["Email"]
                and user["UserID"] != current_user_id
            ):
                print("Email already exists\nError; return to new email")
                break

        else:
            print("Email is available")
            return new_email


def update_user(CSV_PATH, Fieldnames, user, field, new_value):
    """overwrite a userfield in CSV"""
    users = load_users(CSV_PATH)

    for account in users:
        if account["UserID"] == user["UserID"]:
            account[field] = new_value
            user[field] = new_value
            save_users(CSV_PATH, users, Fieldnames)
            return


def get_payment_options():
    """Choosing Paymentoption"""
    print("Choose your payment option.\n TWINT\n Bank Card")

    while True:
        payment_option = input(
            "Enter your payment option: "
        ).strip().upper()

        if payment_option in ("TWINT", "BANK CARD"):
            return payment_option

        print("Error; return to payment option")
