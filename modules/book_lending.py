import csv
from datetime import date, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
USER_FILE = PROJECT_ROOT / "data" / "Library_User_Login_data.csv"
CATALOG_FILE = PROJECT_ROOT / "data" / "fictional_books_catalog.csv"
BORROWING_FILE = PROJECT_ROOT / "data" / "Book_Borrowing_records.csv"

BORROWING_FIELDS = [
    "User_ID",
    "Book_ISBN",
    "Issue_Date",
    "Expiry_Date",
    "Status",
    "Return_Date",
]


def _read_csv(file_path):
    with file_path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def _load_borrowings():
    if not BORROWING_FILE.exists():
        return []
    return _read_csv(BORROWING_FILE)


def _save_borrowings(records):
    with BORROWING_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=BORROWING_FIELDS)
        writer.writeheader()
        writer.writerows(records)


def _expire_borrowings(today=None):
    today = today or date.today()
    records = _load_borrowings()
    changed = False

    for record in records:
        if (
            record.get("Status") == "Issued"
            and date.fromisoformat(record["Expiry_Date"]) <= today
        ):
            record["Status"] = "Returned"
            record["Return_Date"] = today.isoformat()
            changed = True

    if changed:
        _save_borrowings(records)

    return records


def _find_book_by_isbn(isbn):
    for book in _read_csv(CATALOG_FILE):
        if book["ISBN_Number"] == isbn:
            return book
    return None


def _user_exists(user_id):
    return any(user["UserID"] == user_id for user in _read_csv(USER_FILE))


def _find_matching_books(search_text):
    search_text = search_text.casefold()
    return [
        book
        for book in _read_csv(CATALOG_FILE)
        if search_text in book["Book_Name"].casefold()
        or search_text in book["Author"].casefold()
        or search_text in book["ISBN_Number"].casefold()
    ]


def issue_book_record(user_id, isbn, issue_date=None):
    """Create a seven-day borrowing record for a registered user and catalog book."""
    if not _user_exists(user_id):
        return False, "User not found", None

    book = _find_book_by_isbn(isbn)
    if book is None:
        return False, "E-book not found", None

    issue_date = issue_date or date.today()
    records = _expire_borrowings(issue_date)

    if any(
        record.get("Book_ISBN") == isbn and record.get("Status") == "Issued"
        for record in records
    ):
        return False, "Book currently unavailable", None

    expiry_date = issue_date + timedelta(days=7)
    borrowing = {
        "User_ID": user_id,
        "Book_ISBN": isbn,
        "Issue_Date": issue_date.isoformat(),
        "Expiry_Date": expiry_date.isoformat(),
        "Status": "Issued",
        "Return_Date": "",
    }
    records.append(borrowing)
    _save_borrowings(records)
    return True, "Book issued successfully", borrowing


def has_book_access(user_id, isbn, today=None):
    """Return whether the user has an unexpired borrowing record for this book."""
    records = _expire_borrowings(today)
    return any(
        record.get("User_ID") == user_id
        and record.get("Book_ISBN") == isbn
        and record.get("Status") == "Issued"
        for record in records
    )


def display_issued_books(user):
    records = _expire_borrowings()
    user_records = [
        record
        for record in records
        if record.get("User_ID") == user["UserID"]
        and record.get("Status") == "Issued"
    ]

    if not user_records:
        print("You have no currently issued books.")
        return

    print("ISBN | Book Name | Issue Date | Due Date")
    print("-----+-----------+------------+---------")
    for record in user_records:
        book = _find_book_by_isbn(record["Book_ISBN"])
        book_name = book["Book_Name"] if book else "Book no longer in catalog"
        print(
            f"{record['Book_ISBN']} | {book_name} | "
            f"{record['Issue_Date']} | {record['Expiry_Date']}"
        )


def issue_book(user):
    user_id = user.get("UserID", "")
    if not user_id or not _user_exists(user_id):
        print("User not found")
        return

    search_text = input("Enter a book title, author, or ISBN: ").strip()
    if not search_text:
        print("E-book not found")
        return

    matches = _find_matching_books(search_text)
    if not matches:
        print("E-book not found")
        return

    if len(matches) == 1:
        selected_book = matches[0]
    else:
        for index, book in enumerate(matches, start=1):
            print(
                f"{index}. {book['Book_Name']} by {book['Author']} "
                f"(ISBN: {book['ISBN_Number']})"
            )

        selection = input("Choose a book by number: ").strip()
        if not selection.isdigit() or not 1 <= int(selection) <= len(matches):
            print("Invalid book selection")
            return
        selected_book = matches[int(selection) - 1]

    success, message, borrowing = issue_book_record(
        user_id, selected_book["ISBN_Number"]
    )
    print(message)
    if success:
        print(f"Issue date: {borrowing['Issue_Date']}")
        print(f"Due date: {borrowing['Expiry_Date']}")
