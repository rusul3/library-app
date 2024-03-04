
-- Add a new user
INSERT INTO users (username, full_name, email, password_hash)
VALUES ('jdoe', 'John Doe', 'jdoe@example.com', 'hashed_password_here');
-- Replace 'hashed_password_here' with an actual hash of the user's password

-- Add a new author
INSERT INTO authors (name, bio)
VALUES ('Jane Austen', 'An English novelist known primarily for her six major novels.');
-- Repeat as necessary for other authors

-- Add a new category
INSERT INTO categories (name)
VALUES ('Fiction'), ('Non-Fiction'), ('Science Fiction'), ('Romance');
-- Add as many categories as needed

-- Add a new book
INSERT INTO books (title, author_id, category_id, isbn, publication_year, available_copies, total_copies)
VALUES ('Pride and Prejudice', (SELECT author_id FROM authors WHERE name = 'Jane Austen'), 
        (SELECT category_id FROM categories WHERE name = 'Fiction'), '1112223334445', 1813, 5, 5);
-- Adjust author, category, ISBN, publication year, and copy counts as necessary

-- Borrow a book (create a new loan)
INSERT INTO loans (book_id, user_id, due_date)
VALUES ((SELECT book_id FROM books WHERE title = 'Pride and Prejudice'), 
        (SELECT user_id FROM users WHERE username = 'jdoe'), 
        date('now', '+14 days'));
-- Assumes a 2-week loan period. Adjust book title and username as necessary

-- Return a book (update the loan with a return date)
UPDATE loans
SET return_date = date('now')
WHERE loan_id = (SELECT loan_id FROM loans 
                 JOIN books ON loans.book_id = books.book_id
                 WHERE books.title = 'Pride and Prejudice' AND return_date IS NULL
                 LIMIT 1);
-- This marks the first active loan of 'Pride and Prejudice' as returned

-- Find all books by a specific author
SELECT books.title, books.publication_year
FROM books
JOIN authors ON books.author_id = authors.author_id
WHERE authors.name = 'Jane Austen';
-- Replace 'Jane Austen' with any author's name as needed

-- List all current loans for a user
SELECT books.title, loans.loan_date, loans.due_date
FROM loans
JOIN books ON loans.book_id = books.book_id
JOIN users ON loans.user_id = users.user_id
WHERE users.username = 'jdoe' AND loans.return_date IS NULL;
-- Replace 'jdoe' with the desired username

-- Update available copies of a book (after a return or new purchase)
UPDATE books
SET available_copies = available_copies + 1 -- Use '- 1' to decrease when a book is borrowed
WHERE title = 'Pride and Prejudice';
-- Adjust title and increment/decrement as necessary

-- Delete a user (Note: Handle with care, especially if foreign key constraints exist)
DELETE FROM users WHERE username = 'jdoe';
