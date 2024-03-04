import sqlite3

def create_database():
    conn = sqlite3.connect("BookDatabase.db")
    conn.close()

def users ():
 conn = sqlite3.connect("BookDatabase.db")
 cur = conn.cursor()
 cur.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, full_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, registration_date DATE NOT NULL DEFAULT (date('now')))")
 conn.commit() # Making the action stay
 conn.close() # closing the table

#Create table for Authors of the books
def authors() :
 conn = sqlite3.connect("BookDatabase.db")
 cur = conn.cursor()
 cur.execute("CREATE TABLE authors (author_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, bio TEXT)")
 conn.commit() # Making the action stay
 conn.close() # closing the table

#Create table for Categories that books can belong to
def categories():
 conn = sqlite3.connect("BookDatabase.db")
 cur = conn.cursor()
 cur.execute("CREATE TABLE categories ( category_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)")
 conn.commit() # Making the action stay
 conn.close() # closing the table

#Create table for Books available for borrowing
def books():
 conn = sqlite3.connect("BookDatabase.db")
 cur = conn.cursor()
 cur.execute("CREATE TABLE books (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author_id INTEGER, category_id INTEGER, isbn TEXT UNIQUE, publication_year INTEGER, available_copies INTEGER NOT NULL, total_copies INTEGER NOT NULL, FOREIGN KEY (author_id) REFERENCES authors(author_id),FOREIGN KEY (category_id) REFERENCES categories(category_id))")
 conn.commit() # Making the action stay
 conn.close() # closing the table

#Create table for tracking Loans of books to users
def loans():
 conn = sqlite3.connect("BookDatabase.db")
 cur = conn.cursor()
 cur.execute("CREATE TABLE loans (loan_id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER NOT NULL, user_id INTEGER NOT NULL,loan_date DATE  (date('now')),due_date DATE NOT NULL,return_date DATE,FOREIGN KEY (book_id) REFERENCES books(book_id),FOREIGN KEY (user_id) REFERENCES users(user_id))")
 conn.commit() # Making the action stay
 conn.close() # closing the table


#Indexes for faster search operations on frequently searched columns
def faster_search():
     conn = sqlite3.connect("BookDatabase.db")
     cur = conn.cursor()
     cur.execute("CREATE INDEX idx_books_title ON books(title)")
     cur.execute("CREATE INDEX idx_authors_name ON authors(name)")
     cur.execute("CREATE INDEX idx_categories_name ON categories(name)")
     cur.execute("CREATE INDEX idx_loans_due_date ON loans(due_date)")
     conn.commit() # Making the action stay
     conn.close()


#View for listing all current loans (books that have not been returned yet)
def view_loan():
     conn = sqlite3.connect("BookDatabase.db")
     cur = conn.cursor()
     cur.execute("CREATE VIEW current_loans AS SELECT loans.loan_id, users.username, books.title, loans.loan_date, loans.due_date FROM loans JOIN users ON loans.user_id = users.user_id JOIN books ON loans.book_id = books.book_id WHERE loans.return_date IS NULL")
     conn.commit() # Making the action stay
     conn.close()


#View for listing overdue loans
def view_overdue_loan():
     conn = sqlite3.connect("BookDatabase.db")
     cur = conn.cursor()
     cur.execute("CREATE VIEW overdue_loans AS SELECT loans.loan_id, users.username, books.title, loans.loan_date, loans.due_date FROM loans JOIN users ON loans.user_id = users.user_id JOIN books ON loans.book_id = books.book_id WHERE loans.return_date IS NULL AND loans.due_date < date('now')")
     conn.commit() # Making the action stay
     conn.close()




##call the function 

users ()
authors()
categories()
books()
loans()
faster_search()
view_loan()
view_overdue_loan()



