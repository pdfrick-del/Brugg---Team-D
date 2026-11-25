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

### User Story 1: Library User Login and Account Information - Patrick:

As a library user, I want to select my user role and log in to my account so that I can access the system's features for a library user and view personal information.

#### AC1: Selecting the Library User role
- Given the program has started.
- When the user selects “Library User” as a user role.
- Then the system starts the login process required for the selected user role.

#### AC2: Creating a new account
- Given a library user is in the login process.
- When they select the option to create a new account.
- Then the system allows the user to enter their required username, email address, password, and payment information. If all required information is valid, the system creates and saves the new account.

#### AC3: Entering login credentials
- Given a library user is in the login process.
- When they select the option to log in.
- Then the system allows them to type in their e-mail and password.

#### AC4: Verification of login credentials
- Given a library user is entering their login credentials to log in.
- When the library user has submitted their e-mail and password.
- Then the system verifies these credentials; if correct, the user is logged in, else they get an error message and get back to the start of the login for the library user, where they can choose between logging in and creating an account.

#### AC5: Showing Options
- Given a library user is successfully logged in.
- Then the system displays a menu with the following options: viewing account information, viewing fees, searching for books to download, and requesting books. 

#### AC6: View and edit account information
- Given a library user is successfully logged in.
- When the library user decides on the option “view account”.
- Then the system shows them their UserID, Name, Password but censored, Username, Email, and saved payment information. The user can decide to edit this information and save it, except the UserID.
- And to change their password, the user must first enter their current password.

#### AC7: Forgotten Login Credentials
- Given a library user is in the login process.
- When the user selects the option “forgot login credentials”.
- Then the system displays the message: "Please contact your admin."

### User Story 2: Login librarian - Patrick:

As a librarian, I want to select my user role and log in to my account so that I can access the system's features for a librarian. The librarian account is already set up when the application starts.

#### AC1: Selecting the librarian role
- Given the program has started.
- When the user selects “Librarian” as a user role.
- Then the system starts the login process required for the selected user role.

#### AC2: Forgotten account information or new account
- Given a librarian is in the login process
- When they select "Forgot your account information or don't have an account?"
- Then the system displays the message: "Please contact your admin."

#### AC3: Entering login credentials
- Given a librarian is in the login process
- When they select "log in"
- Then the system allows them to enter their ID and password.

#### AC4: Verification of login credentials 
- Given a librarian is entering their login credentials to log in.
- When the librarian has submitted their ID and password.
- Then the system verifies these credentials; if correct, the user is logged in, else they get an error message and get back to the start of the login for the librarian.

### User Story 3: Manage Books- Amreen 

As a librarian, I want to add, update, and delete book records so that the library catalog remains accurate, up-to-date, and available for members to search, borrow, and return books.
#### Feature A: Add Book
#### AC1: Add a New Book
Given the librarian wants to add a new book to the catalog
When the librarian enters the following mandatory information:
•	Title
•	Author
•	ISBN
•	Genre/Category
•	Publication Year
•	Quantity and submits the book details then the book is added to the catalog successfully.
#### AC2: Validate Required Fields
Given the librarian is adding a new book
When one or more mandatory fields are empty
Then the system displays a validation message: Field/s is empty then the book is not added to the catalog.
#### AC3: Prevent Duplicate ISBNs
Given a book with the same ISBN already exists in the catalog
When the librarian attempts to add another book using that ISBN
Then the system rejects the request and displays the message:ISBN already exists.
#### AC4: Confirm Successful Addition
Given valid book information is provided
When the book is successfully saved
Then the system displays the message:Book added successfully and the book appears in the catalog.
#### Feature A: Update Book
#### AC5: Update Existing Book Details
Given a book exists in the catalog
When the librarian selects the book and updates one or more of the following fields:
•	Title
•	Author
•	Genre
•	Publication Year
•	Quantity then the book information is updated successfully.
#### AC6: Book Must Exist Before Update
Given the librarian wants to update a book
When the specified book cannot be found in the catalog
Then the system displays the message: Book not found and no updates are made.
#### AC7: Confirm Successful Update
Given a valid book exists in the catalog
When the librarian saves the updated information
Then the system displays the message:Book updated successfully.
#### Feature C: Delete Book
#### AC8: Delete Existing Book
Given a book exists in the catalog
When the librarian selects the delete option
Then the book is removed from the catalog and the system displays the message:Book has been deleted.
#### AC9: Book Must Exist Before Deletion
Given the librarian wants to delete a book
When the specified book cannot be found in the catalog
Then the system displays the message: Book not found and no deletion occurs.
#### AC10: Catalog Updated After Deletion
Given a book has been deleted successfully
When the librarian views the catalog
Then the deleted book is no longer displayed in the catalog.

### User Story 4: Filter and Sort Books- Amreen

As a librarian, I want to filter books by title, author name, publication year and  genre and sort the filtered results by these attributes so that I can quickly locate specific books and organize the displayed catalog without changing the stored book information.
### Acceptance Criteria
#### AC1: Filter by Title
Given a list of books exists in the catalog
When the librarian enters a title or part of a title as a filter
Then only books with matching titles are displayed.
#### AC2: Filter by Author
Given books with different authors exist
When the librarian enters an author name as a filter
Then only books written by the matching author are displayed.
#### AC3: Filter by Publication Year
Given books have publication years
When the librarian enters a publication year as a filter
Then only books published in that year are displayed.
#### AC4: Filter by Genre
Given books belong to multiple genres
When the librarian selects a genre filter
Then only books belonging to that genre are displayed.
#### AC5: Sort by Title
Given one or more books are displayed
When the librarian selects "Sort by Title"
Then the displayed books are ordered alphabetically from A-Z by title.
#### AC6: Sort by Author
Given one or more books are displayed
When the librarian selects "Sort by Author"
Then the displayed books are ordered alphabetically A-Z by author name.
#### AC7: Sort by Publication Year
Given one or more books are displayed
When the librarian selects "Sort by Publication Year"
Then the displayed books are ordered from oldest to newest.
#### AC8: Sort by Genre
Given one or more books are displayed
When the librarian selects "Sort by Genre"
Then the displayed books are ordered alphabetically by genre.
#### AC9: Filter and Sort Combined
Given a filter has been applied
When the librarian selects a sorting option
Then only the filtered books are displayed and sorted according to the selected attribute.
#### AC10: No Matching Results
Given books exist in the catalog
When the applied filter does not match any books
Then the system displays the message: No matching books found
#### AC11: Empty Catalog Handling
Given no books exist in the catalog
When the librarian requests filtering or sorting
Then the system displays the message:No books available
 
### User Story 5 : Issue Books- Amreen

#### AC1: User Must Be Registered and Logged In
 Given the user wants to issue a book
 When the user logs in using valid credentials
 Then the system verifies the user's account and allows the book issuing process to continue.

#### AC2: Book Must Exist
 Given the user wants to issue a book
 When the user selects or searches for a book by title, author or ISBN
 Then the system verifies that the book exists in the catalog and allows the issuing process to continue.

#### AC3: Book Must Be Available
 Given the user has selected an book
 When the user requests to issue the book
 Then the system checks whether the book is available and allows the issue request to proceed if access is available; otherwise, the system displays the message: Book currently unavailable.

#### AC4: Successful Issue Confirmation
 Given all validation checks have passed
 When the book is issued successfully
 Then the system displays: Book issued successfully.

#### AC5: Create Book Borrowing Record
 Given the book has been issued successfully
 When the issue process is completed
 Then the system creates a borrowing record containing:
User ID
Book ISBN
Issue Date
Expiry Date (7 days from the issue date)

#### AC6: User or Book Not Found
 Given the user initiates an book issue request
 When the user account or book does not exist
 Then the system rejects the request and displays one of the following messages:
  User not found
  E-book not found.
 
### User Story 6: Membership Fees - Patrick:

As a library user, I want to view my membership fees so that I know which I have paid lately and which are still outstanding.

#### AC1: Viewing membership fees
- Given a library user is logged in.
- When he chooses the option "membership fees".
- Then the system shows them the outstanding and upcoming fees as they are due.

#### AC2: Notification option
- Given a library user has opened the option "membership fees".
- When they decide on the option "notifications" within.
- Then the system gives them the option to activate notifications when a fee is outstanding, which will appear as a message when they log in.

#### AC3: Sending Notifications
- Given a library user has activated notifications for membership fees.
- When the libary user logs in and the program detects an outstanding amount for that user.
- Then the system displays a reminder message to the user as soon as they are loged in.

#### AC4: Late fees
- Given a library user has outstanding membership fees.
- When the user logs in and the annual fee review date (the first day of their registration month) has been reached.
- Then the system adds a late fee of 10% to the outstanding amount from previous years, provided the late fee for that year has not already been applied.

#### AC5: Discounts
- Given a library user has an account with a recorded creation date.
- When the program starts and detects that a library user has an account for at least 5 years.
- Then the system applies a discount to all upcoming membership fees, ensuring that each fee receives the discount only once.

  
### User Story 5 : Rate Books- Amreen

"As a library user, I want to rate books that I have read so that I can share my opinion and help other users choose books."

### Acceptance Criteria
### AC1: Rate a Borrowed Book

Given I am a logged-in library user
 And I have borrowed and read a book
 When I navigate to the book details page
 Then I should see an option to rate the book using a 1–5 star rating system.

### AC2: Submit a Rating

Given I am viewing a book's details page
 When I select a rating between 1 and 5 stars and click "Submit"
 Then my rating should be saved successfully
 And a confirmation message should be displayed.

### AC3: One Rating per User per Book

Given I have already rated a book
 When I attempt to rate the same book again
 Then the system should update my existing rating instead of creating a duplicate rating.

### AC4: Display Average Rating

Given a book has received ratings from users
 When any user views the book details page
 Then the average rating should be displayed
 And the total number of ratings should be shown.

### AC5: Restrict Ratings to Eligible Users

Given I have never borrowed a particular book
 When I view its details page
 Then I should not be allowed to submit a rating
 And the system should display a message indicating that only users who have borrowed the book can rate it.

### AC6: Validate Rating Value

Given I am submitting a rating
 When the rating value is less than 1 or greater than 5
 Then the system should reject the submission
 And display an appropriate validation message.

### AC7: View Personal Rating

Given I have previously rated a book
 When I return to the book details page
 Then my submitted rating should be visible to me.

### AC8: Rating Updates Statistics

Given a new rating is submitted or an existing rating is updated
 When the action is successfully completed
 Then the book's average rating should be recalculated automatically.

## Program Structure 🏛️

### Decision and Control Flow Logic

We used Mermaid to create ours flowcharts for our decision and control flow logic and used ChatGPT to help us learn the commands in Mermaid. We uploaded a Cheatsheet ChatGPT created for us to use Mermaid: Mermaid Cheat Sheet.md

The flowchart can be viewed in the file: Flowchart.md.


