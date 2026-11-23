import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CATALOG_FILE = PROJECT_ROOT / "data" / "fictional_books_catalog.csv"



# ==========================
# Load Books
# ==========================

def load_books():

    try:
        with open(CATALOG_FILE, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    except FileNotFoundError:
        return []

books = load_books()

# ==========================
# Display Books
# ==========================

def display_books(books):

    if len(books) == 0:
        print("No matching books found")
        return

    columns = [
        ("Book Name", "Book_Name"),
        ("Author", "Author"),
        ("Genre", "Genre"),
        ("Year", "Publication_Year"),
        ("ISBN", "ISBN_Number"),
        ("Book Type", "Book_Type"),
    ]

    widths = [
        max(len(label), *(len(str(book.get(field, ""))) for book in books))
        for label, field in columns
    ]

    header = " | ".join(
        label.ljust(width)
        for (label, _), width in zip(columns, widths)
    )
    separator = "-+-".join("-" * width for width in widths)

    print(header)
    print(separator)

    for book in books:
        print(" | ".join(
            str(book.get(field, "")).ljust(width)
            for (_, field), width in zip(columns, widths)
        ))


# ==========================
# Filter Functions
# ==========================

def filter_by_title(books):

    title = input("Enter title or part of title: ").lower()

    filtered_books = []

    for book in books:

        if title in book["Book_Name"].lower():
            filtered_books.append(book)

    return filtered_books


def filter_by_author(books):

    author = input("Enter author name: ").lower()

    filtered_books = []

    for book in books:

        if author in book["Author"].lower():
            filtered_books.append(book)

    return filtered_books


def filter_by_year(books):

    year = input("Enter publication year: ")

    filtered_books = []

    for book in books:

        if book["Publication_Year"] == year:
            filtered_books.append(book)

    return filtered_books


def filter_by_genre(books):

    genre = input("Enter genre: ").lower()

    filtered_books = []

    for book in books:

        if genre == book["Genre"].lower():
            filtered_books.append(book)

    return filtered_books


# ==========================
# Sort Functions
# ==========================

def sort_by_title(books):

    return sorted(
        books,
        key=lambda book: book["Book_Name"].lower()
    )


def sort_by_author(books):

    return sorted(
        books,
        key=lambda book: book["Author"].lower()
    )


def sort_by_year(books):

    return sorted(
        books,
        key=lambda book: int(book["Publication_Year"])
    )

def sort_by_genre(books):

    return sorted(
        books,
        key=lambda book: book["Genre"].lower()
    )


# ==========================
# Sort Menu
# ==========================

def choose_sort(books):
    
    if len(books) == 0:
        print("No books available")
        return
    
    print("Sort Options")
    print("1. Title")
    print("2. Author")
    print("3. Publication Year")
    print("4. Genre")

    choice = input("Choose sort option: ")

    if choice == "1":
        return sort_by_title(books)

    elif choice == "2":
        return sort_by_author(books)

    elif choice == "3":
        return sort_by_year(books)

    elif choice == "4":
        return sort_by_genre(books)

    else:
        print("Invalid choice")
        return


# ==========================
# Filter and Sort Combined
# ==========================

def filter_and_sort():

    books = load_books()

    # AC11
    if len(books) == 0:
        print("No books available")
        return

    print("Filter Options")
    print("1. Title")
    print("2. Author")
    print("3. Publication Year")
    print("4. Genre")

    filter_choice = input("Choose filter option: ")

    if filter_choice == "1":
        books = filter_by_title(books)

    elif filter_choice == "2":
        books = filter_by_author(books)

    elif filter_choice == "3":
        books = filter_by_year(books)

    elif filter_choice == "4":
        books = filter_by_genre(books)

    else:
        print("Invalid choice")
        return

    # AC10
    if len(books) == 0:
        print("No matching books found")
        return

    sorted_books = choose_sort(books)
    if sorted_books is not None:
        display_books(sorted_books)


# ==========================
# Filter Only
# ==========================

def filter_menu():

    books = load_books()

    if len(books) == 0:
        print("No books available")
        return

    print("\nFilter Options")
    print("1. Title")
    print("2. Author")
    print("3. Publication Year")
    print("4. Genre")

    choice = input("Choose option: ")

    if choice == "1":
        books = filter_by_title(books)

    elif choice == "2":
        books = filter_by_author(books)

    elif choice == "3":
        books = filter_by_year(books)

    elif choice == "4":
        books = filter_by_genre(books)

    else:
        print("Invalid choice")
        return

    display_books(books)


# ==========================

while True:

    print("======= Filter Or Sort Books ========")
    print("1. Filter")
    print("2. Sort")
    print("3. Filter and Sort")
    print("4. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        filter_menu()

    elif choice=="2":
        sorted_books = choose_sort(books)
        if sorted_books is not None:
            display_books(sorted_books)

    elif choice=="3":
        filter_and_sort()

    elif choice == "4":
        print("Goodbye")
        break
    
    else:
        print("Invalid choice")
