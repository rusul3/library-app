# Book-barrow-database
## CS50 SQL
>This was my final project for conclude the CS50 SQL language.

## Features
User Capabilities Borrowing Books: Users should be able to check out books for a set period. Returning Books: Users can return books they have borrowed. Searching: Users can search for books by title, author, or category. Account Management: Users can view their borrowing history and current loans. Beyond Scope Purchasing Books: The system will not handle transactions or purchases. User Reviews and Ratings: Adding reviews or ratings for books is not included.

## Representation
Entities
Entities Users Attributes: user_id, username, full_name, email, password_hash, registration_date. Types and Constraints: user_id is an integer primary key; username, email are unique; password_hash is a text field for storing hashed passwords. Rationale: Ensures user uniqueness and secure password storage. Books Attributes: book_id, title, author_id, category_id, isbn, publication_year, available_copies, total_copies. Rationale: Captures essential book details and availability. Links to authors and categories through foreign keys. Authors and Categories Attributes: For authors - author_id, name, bio. For categories - category_id, name. Rationale: Allows books to be categorized and linked to their authors. Loans Attributes: loan_id, book_id, user_id, loan_date, due_date, return_date. Rationale: Tracks the borrowing details of each book.

Relationships
Users to Loans: One-to-Many. One user can have multiple loans. Books to Loans: One-to-Many. A book can have multiple loans (over time). Authors to Books: One-to-Many. An author can have multiple books. Categories to Books: One-to-Many. A category can include multiple books. please chek Book loan.png

## About CS50
CS50 is a openware course from Havard University and taught by David J. Malan and lovely staff (Brenda Anderson,Doug Lloyd,Glenn Holloway and Rongxin Liu)

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.
