# Brugg - Team - D - Library Book Sorting System 📚

## Authors 👥

- Amreen Anis Ahmed Khan: amreenanisahmed.khan@students.fhnw.ch
- Patrick Frick: patrick.frick@students.fhnw.ch

## Project Objectives According to Template 📄

This project is intended to:

- Practice the complete process from problem analysis to implementation
- Apply basic Python programming concepts learned in the Programming Foundations module
- Demonstrate the use of console interaction, data validation, and file processing
- Produce clean, well-structured, and documented code
- Prepare students for teamwork and documentation in later modules

## Statement of Integrity 📜

We hereby declare

- To clearly document the use of generative AI
- To divide the work fairly and contribute equally to the project
- Cite external sources when necessary

## Information About the Database 💾

In this project a database will be used:

- This database is fictive
- It was created with ChatGPT
-  It is considered a tool to demonstrate our program

## Tools and Programming Languages 🛠️

- Python
- Git and Github
- Mermaid
- ChatGPT

## Analysis 📝 

### Problem

### Scenario 

### User Roles

| Role | Description |
|---|---|
|Librarian| |
|Library user| |

### User Stories 📖

### User Story 1: Filter and Sort Books- Amreen
As a librarian, I want to filter books by title, author name, publication year and  genre and sort the filtered results by these attributes so that I can quickly locate specific books and organize the displayed catalog without changing the stored book information.
### Acceptance Criteria
### AC1: Filter by Title
Given a list of books exists in the catalog
When the librarian enters a title or part of a title as a filter
Then only books with matching titles are displayed.
### AC2: Filter by Author
Given books with different authors exist
When the librarian enters an author name as a filter
Then only books written by the matching author are displayed.
### AC3: Filter by Publication Year
Given books have publication years
When the librarian enters a publication year as a filter
Then only books published in that year are displayed.
### AC4: Filter by Genre
Given books belong to multiple genres
When the librarian selects a genre filter
Then only books belonging to that genre are displayed.
### AC5: Sort by Title
Given one or more books are displayed
When the librarian selects "Sort by Title"
Then the displayed books are ordered alphabetically from A-Z by title.
### AC6: Sort by Author
Given one or more books are displayed
When the librarian selects "Sort by Author"
Then the displayed books are ordered alphabetically A-Z by author name.
### AC7: Sort by Publication Year
Given one or more books are displayed
When the librarian selects "Sort by Publication Year"
Then the displayed books are ordered from oldest to newest.
### AC8: Sort by Genre
Given one or more books are displayed
When the librarian selects "Sort by Genre"
Then the displayed books are ordered alphabetically by genre.
### AC9: Filter and Sort Combined
Given a filter has been applied
When the librarian selects a sorting option
Then only the filtered books are displayed and sorted according to the selected attribute.
### AC10: No Matching Results
Given books exist in the catalog
When the applied filter does not match any books
Then the system displays the message: No matching books found
### AC11: Empty Catalog Handling
Given no books exist in the catalog
When the librarian requests filtering or sorting
Then the system displays the message:No books available
 
### User Story 2: Manage Books- Amreen 
As a librarian, I want to add, update, and delete book records so that the library catalog remains accurate, up-to-date, and available for members to search, borrow, and return books.
### Feature A: Add Book
### AC1: Add a New Book
Given the librarian wants to add a new book to the catalog
When the librarian enters the following mandatory information:
•	Title
•	Author
•	ISBN
•	Genre/Category
•	Publication Year
•	Quantity and submits the book details then the book is added to the catalog successfully.
### AC2: Validate Required Fields
Given the librarian is adding a new book
When one or more mandatory fields are empty
Then the system displays a validation message: Field/s is empty then the book is not added to the catalog.
### AC3: Prevent Duplicate ISBNs
Given a book with the same ISBN already exists in the catalog
When the librarian attempts to add another book using that ISBN
Then the system rejects the request and displays the message:ISBN already exists.
### AC4: Confirm Successful Addition
Given valid book information is provided
When the book is successfully saved
Then the system displays the message:Book added successfully and the book appears in the catalog.
Feature B: Update Book
### AC5: Update Existing Book Details
Given a book exists in the catalog
When the librarian selects the book and updates one or more of the following fields:
•	Title
•	Author
•	Genre
•	Publication Year
•	Quantity then the book information is updated successfully.
### AC6: Book Must Exist Before Update
Given the librarian wants to update a book
When the specified book cannot be found in the catalog
Then the system displays the message: Book not found and no updates are made.
### AC7: Confirm Successful Update
Given a valid book exists in the catalog
When the librarian saves the updated information
Then the system displays the message:Book updated successfully.
### Feature C: Delete Book
### AC8: Delete Existing Book
Given a book exists in the catalog
When the librarian selects the delete option
Then the book is removed from the catalog and the system displays the message:Book has been deleted.
### AC9: Book Must Exist Before Deletion
Given the librarian wants to delete a book
When the specified book cannot be found in the catalog
Then the system displays the message: Book not found and no deletion occurs.
### AC10: Catalog Updated After Deletion
Given a book has been deleted successfully
When the librarian views the catalog
Then the deleted book is no longer displayed in the catalog.
 
### User Story 3: Issue Books to Members- Amreen 
As a librarian, I want to issue books to registered members so that borrowing transactions are recorded accurately and members do not exceed the maximum borrowing limit of five books.
### Feature: Issue Book
### AC1: Member Must Exist
Given the member wants to issue a book
When the member enters his Member ID
Then the system verifies that the member exists in the library system and allows the issuing process to continue.
### AC2: Book Must Exist
Given the member wants to issue a book
When the member enters a Book name or ISBN
Then the system verifies that the book exists in the catalog and allows the issuing process to continue.
### AC3: Enforce Borrowing Limit
Given a valid member exists
When the member tries to issue a book 
Then the system checks the number of the member's active loans and if the member has fewer than five active loans, the book can be issued otherwise the issuing request is rejected and the system displays the message: Maximum borrowing limit reached.
### AC4: Successful Issue Confirmation
Given the book has been issued successfully
When the issue process is completed
Then the system displays: Book issued successfully.
### AC5: Create Borrowing Record
Given all validation checks have passed
When the book is issued successfully
Then the system creates a borrowing record containing:
•	Member ID
•	Book ISBN
•	Borrow Date
•	Due Date (15 days from the borrow date)
### AC6: Member or Book Not Found
Given the librarian initiates a book issue transaction
When the Member ID or Book ISBN does not exist
Then the system rejects the transaction and displays one of the following messages:Member not found or Book not found.
 
#### User Story 4 - Patrick:

As a libary user, I want to see my membership fees.

Acceptance Criteria:
1. The system remembers when I last paid my fees.
2. It shows when the next date is to pay my fees.
3. Based on how long I am a member, I get an individual discount on my fees.

#### User Story 5 - Patrick:

As a library user, I want to sort books by genre so that I can find books around the topics I am interested in.

Acceptance Criteria:
1. The system sorts books themed by genre.
2. Books in the same genre are grouped together
3. The system only displays the requested genre.

#### User Story 6 - Patrick:
As a library user, I want to see until when I have to bring my books back via deadlines.

Acceptance Criteria:
1. The system displays which books are currently lent by the user.
2. The system sorts them by deadline, from the earliest deadlines to the latest.
3. If a deadline is missed, the system gives the user a warning.

## Program Structure 🏛️

### Decision and Control Flow Logic

We used Mermaid to create ours flowcharts for our decision and control flow logic and used ChatGPT to help us learn the commands in Mermaid. We uploaded a Cheatsheet ChatGPT created for us to use Mermaid: Mermaid Cheat Sheet.md

The flowchart can be viewed in the file: Flowchart.md.


