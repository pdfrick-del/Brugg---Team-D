import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CATALOG_FILE = PROJECT_ROOT / "data" / "fictional_books_catalog.csv"
USER_FILE = PROJECT_ROOT / "data" / "Library_User_Login_data.csv"
RATINGS_FILE = PROJECT_ROOT / "data" / "Book_Ratings.csv"
BORROWING_FILES = (
    PROJECT_ROOT / "data" / "Book_Borrowing_records.csv",
    PROJECT_ROOT / "data" / "Books_Issued_Library_User.csv",
)
RATING_FIELDS = ["User_ID", "Book_ISBN", "Rating"]


def _read_csv(file_path, missing_ok=False):
    try:
        with file_path.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        if missing_ok:
            return []
        raise


def _find_book(isbn):
    return next(
        (
            book
            for book in _read_csv(CATALOG_FILE)
            if book.get("ISBN_Number", "").strip() == isbn
        ),
        None,
    )


def find_books(search_text):
    """Find catalog books by title, author, or ISBN."""
    search_text = search_text.strip().casefold()
    if not search_text:
        return []

    return [
        book
        for book in _read_csv(CATALOG_FILE)
        if any(
            search_text in book.get(field, "").casefold()
            for field in ("Book_Name", "Author", "ISBN_Number")
        )
    ]


def _borrowed_record_matches(record, user_id, isbn):
    record_user_id = record.get("User_ID") or record.get("UserID") or ""
    record_isbn = (
        record.get("Book_ISBN")
        or record.get("ISBN_Number")
        or record.get("ISBN")
        or ""
    )
    return record_user_id.strip() == user_id and record_isbn.strip() == isbn


def has_borrowed_book(user_id, isbn):
    """Check all known loan files, including records for books already returned."""
    for file_path in BORROWING_FILES:
        records = _read_csv(file_path, missing_ok=True)
        if any(
            _borrowed_record_matches(record, user_id, isbn)
            for record in records
        ):
            return True
    return False


def _load_ratings():
    return _read_csv(RATINGS_FILE, missing_ok=True)


def get_user_rating(user_id, isbn):
    for rating in _load_ratings():
        if (
            rating.get("User_ID") == user_id
            and rating.get("Book_ISBN") == isbn
        ):
            return int(rating["Rating"])
    return None


def get_rating_summary(isbn):
    ratings = [
        int(record["Rating"])
        for record in _load_ratings()
        if record.get("Book_ISBN") == isbn
    ]
    if not ratings:
        return None, 0
    return sum(ratings) / len(ratings), len(ratings)


def submit_rating(user_id, isbn, rating):
    """Save or replace one user's rating for a catalog book."""
    if isinstance(rating, bool):
        return False, "Rating must be a whole number between 1 and 5."
    if isinstance(rating, str):
        normalized_rating = rating.strip()
        if not normalized_rating.isdigit():
            return False, "Rating must be a whole number between 1 and 5."
        rating_value = int(normalized_rating)
    elif isinstance(rating, int):
        rating_value = rating
    else:
        return False, "Rating must be a whole number between 1 and 5."
    if rating_value < 1 or rating_value > 5:
        return False, "Rating must be a whole number between 1 and 5."

    if not user_id or not any(
        user.get("UserID") == user_id for user in _read_csv(USER_FILE)
    ):
        return False, "User not found."
    if _find_book(isbn) is None:
        return False, "Book not found."
    if not has_borrowed_book(user_id, isbn):
        return (
            False,
            "Only users who have borrowed this book can rate it.",
        )

    ratings = _load_ratings()
    updated = False
    saved_ratings = []
    for record in ratings:
        is_current_rating = (
            record.get("User_ID") == user_id
            and record.get("Book_ISBN") == isbn
        )
        if is_current_rating:
            if not updated:
                saved_ratings.append(
                    {
                        "User_ID": user_id,
                        "Book_ISBN": isbn,
                        "Rating": rating_value,
                    }
                )
                updated = True
        else:
            saved_ratings.append(record)

    if not updated:
        saved_ratings.append(
            {
                "User_ID": user_id,
                "Book_ISBN": isbn,
                "Rating": rating_value,
            }
        )

    with RATINGS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=RATING_FIELDS)
        writer.writeheader()
        writer.writerows(saved_ratings)

    return True, "Your rating has been submitted successfully."


def _display_book_details(book, user_id):
    isbn = book["ISBN_Number"]
    average, count = get_rating_summary(isbn)
    print(f"\n{book['Book_Name']} by {book['Author']}")
    print(f"ISBN: {isbn}")
    if average is None:
        print("Average rating: No ratings yet (0 ratings)")
    else:
        print(f"Average rating: {average:.1f}/5 ({count} ratings)")

    personal_rating = get_user_rating(user_id, isbn)
    if personal_rating is not None:
        print(f"Your rating: {personal_rating}/5 stars")

    if not has_borrowed_book(user_id, isbn):
        print("Only users who have borrowed this book can rate it.")
        return

    rating = input("Select a rating from 1-5 stars (or press Enter to return): ")
    if not rating.strip():
        return

    success, message = submit_rating(user_id, isbn, rating)
    print(message)
    if success:
        print(f"Your rating: {int(rating)}/5 stars")
        average, count = get_rating_summary(isbn)
        print(f"Average rating: {average:.1f}/5 ({count} ratings)")


def rate_book(user):
    """Open a book's details and let eligible logged-in users rate it."""
    user_id = user.get("UserID", "")
    if not user_id:
        print("User not found.")
        return

    search_text = input("Enter a book title, author, or ISBN: ").strip()
    if not search_text:
        print("No matching books found.")
        return

    matches = find_books(search_text)
    if not matches:
        print("No matching books found.")
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
            print("Invalid book selection.")
            return
        selected_book = matches[int(selection) - 1]

    _display_book_details(selected_book, user_id)