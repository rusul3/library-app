 CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL, -- Store password hashes, not plain text passwords
    registration_date DATE NOT NULL DEFAULT (date('now'))
 );

-- Create table for Authors of the books
  CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT
  );

-- Create table for Categories that books can belong to
  CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
 );

-- Create table for Books available for borrowing
  CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    category_id INTEGER,
    isbn TEXT UNIQUE,
    publication_year INTEGER,
    available_copies INTEGER NOT NULL,
    total_copies INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
  );

-- Create table for tracking Loans of books to users
  REATE TABLE loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    loan_date DATE NOT NULL DEFAULT (date('now')),
    due_date DATE NOT NULL,
    return_date DATE, -- Null if not returned yet
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
  );





-- Indexes for faster search operations on frequently searched columns
CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_authors_name ON authors(name);
CREATE INDEX idx_categories_name ON categories(name);
CREATE INDEX idx_loans_due_date ON loans(due_date);

-- View for listing all current loans (books that have not been returned yet)
CREATE VIEW current_loans AS
SELECT
    loans.loan_id,
    users.username,
    books.title,
    loans.loan_date,
    loans.due_date
FROM
    loans
JOIN users ON loans.user_id = users.user_id
JOIN books ON loans.book_id = books.book_id
WHERE
    loans.return_date IS NULL;

-- View for listing overdue loans
CREATE VIEW overdue_loans AS
SELECT
    loans.loan_id,
    users.username,
    books.title,
    loans.loan_date,
    loans.due_date
FROM
    loans
JOIN users ON loans.user_id = users.user_id
JOIN books ON loans.book_id = books.book_id
WHERE
    loans.return_date IS NULL AND loans.due_date < date('now');



