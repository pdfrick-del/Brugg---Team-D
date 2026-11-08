import csv
from datetime import datetime, timedelta

BOOK_FILE = "fictional_book_catalog.csv"
MEMBER_FILE = "members.csv"
BORROW_FILE = "borrow_records.csv"


def issue_book():

    member_id = input("Enter Member ID: ")
    book_input = input("Enter Book Name or ISBN: ")

    # ==========================
    # AC1 - Verify Member Exists
    # ==========================

    member_found = False

    with open(MEMBER_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for member in reader:

            if member["Member_ID"] == member_id:
                member_found = True
                break

    if not member_found:
        print("Member not found")
        return

    # ==========================
    # AC2 - Verify Book Exists
    # ==========================

    book_found = False
    isbn_number = ""

    with open(BOOK_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for book in reader:

            if (book["ISBN_Number"] == book_input or
                    book["Book_Name"].lower() == book_input.lower()):

                book_found = True
                isbn_number = book["ISBN_Number"]
                break

    if not book_found:
        print("Book not found")
        return

    # ==========================
    # AC3 - Borrowing Limit
    # ==========================

    active_loans = 0

    try:

        with open(BORROW_FILE, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for record in reader:

                if record["Member_ID"] == member_id:
                    active_loans += 1

    except FileNotFoundError:
        pass

    if active_loans >= 5:
        print("Maximum borrowing limit reached")
        return

    # ==========================
    # AC5 - Create Record
    # ==========================

    borrow_date = datetime.today().date()

    due_date = borrow_date + timedelta(days=15)

    record = [
        member_id,
        isbn_number,
        borrow_date,
        due_date
    ]

    file_exists = False

    try:
        with open(BORROW_FILE, "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(BORROW_FILE, "a", newline="", encoding="utf-8") as file:

        fieldnames = [
            "Member_ID",
            "ISBN_Number",
            "Borrow_Date",
            "Due_Date"
        ]

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(fieldnames)

        writer.writerow(record)

    # ==========================
    # AC4 - Success Message
    # ==========================

    print("Book issued successfully")


# Menu Option

while True:

    print("\n===== ISSUE BOOK MENU =====")
    print("1. Issue Book")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        issue_book()

    elif choice == "2":
        print("Goodbye")
        break

    else:
        print("Invalid choice")