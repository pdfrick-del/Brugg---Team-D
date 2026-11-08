import csv
CATALOG_FILE = "fictional_books_catalog.csv"


def add_book():

    book_name = input("Book Name: ")
    author = input("Author: ")
    genre = input("Genre: ")
    page_count = input("Page Count/Duration Minutes: ")
    publication_year = input("Publication Year: ")
    isbn = input("ISBN Number: ")
    book_type = input("Book Type: ")

    # AC2 - Validate Required Fields
     
    if not all([
        book_name,
        author,
        genre,
        page_count,
        publication_year,
        isbn,
        book_type
    ]):
        print("Field/s is empty")
        return

    # AC3 - Prevent Duplicate ISBN
    with open(CATALOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for book in reader:
            if book["ISBN_Number"] == isbn:
                print("ISBN already exists")
                return

    # Generate next serial number
    with open(CATALOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        books = list(reader)

    sr_no = len(books) + 1

    # AC1 - Add Book
    with open(CATALOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            sr_no,
            book_name,
            author,
            genre,
            page_count,
            publication_year,
            isbn,
            book_type
        ])

    # AC4 - Success Message
    print("Book added successfully")


def update_book():

    isbn = input("Enter ISBN Number: ")

    books = []
    found = False

    with open(CATALOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for book in reader:

            if book["ISBN_Number"] == isbn:

                found = True

                book["Book_Name"] = input("New Book Name: ")
                book["Author"] = input("New Author: ")
                book["Genre"] = input("New Genre: ")
                book["Publication_Year"] = input("New Publication Year: ")
                book["PageCount_DurationMinutes"] = input(
                                                          
                    "New Page Count/Duration Minutes: "
                )
                book["Book_Type"] = input("New Book Type: ")

            books.append(book)

    # AC6
    if not found:
        print("Book not found")
        return

    fieldnames = [
        "Sr_No",
        "Book_Name",
        "Author",
        "Genre",
        "PageCount_DurationMinutes",
        "Publication_Year",
        "ISBN_Number",
        "Book_Type"
    ]

    with open(CATALOG_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

    # AC7
    print("Book updated successfully")


def delete_book():

    isbn = input("Enter ISBN Number: ")

    books = []
    found = False

    with open(CATALOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for book in reader:

            if book["ISBN_Number"] == isbn:
                found = True
                continue

            books.append(book)

    # AC9
    if not found:
        print("Book not found")
        return

    fieldnames = [
        "Sr_No",
        "Book_Name",
        "Author",
        "Genre",
        "PageCount_DurationMinutes",
        "Publication_Year",
        "ISBN_Number",
        "Book_Type"
    ]

    with open(CATALOG_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

    # AC8
    print("Book has been deleted")


def view_catalog():

    with open(CATALOG_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for book in reader:

            print("\n---------------------------")
            print("Serial No:", book["Sr_No"])
            print("Book Name:", book["Book_Name"])
            print("Author:", book["Author"])
            print("Genre:", book["Genre"])
            print("Pages/Duration:", book["PageCount_DurationMinutes"])
            print("Publication Year:", book["Publication_Year"])
            print("ISBN Number:", book["ISBN_Number"])
            print("Book Type:", book["Book_Type"])


# Main Menu

while True:

    print("===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. View Catalog")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        update_book()

    elif choice == "3":
        delete_book()

    elif choice == "4":
        view_catalog()

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")