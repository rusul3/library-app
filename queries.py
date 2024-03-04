import sqlite3


#Add a new user
def create_new_user(username, full_name, email, password_hash):
     try:
         conn = sqlite3.connect("BookDatabase.db")
         cur = conn.cursor()
         cur.execute("INSERT INTO users (username, full_name, email, password_hash) VALUES (?, ?, ?, ?)", (username, full_name, email, password_hash))
         conn.commit()

     except sqlite3.Error as e:
        print(f"Database error: {e}")
     finally:
        conn.close()
     
#check the user
def check_username_exists(username):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    result = cur.fetchone()
    conn.close()
    return result is not None        



#Add a new author
def INSERT_INTO_authors(name, bio):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO authors (name, bio) VALUES (?, ?)", (name, bio))
    conn.commit()
    conn.close()


#Add a new category
def INSERT_INTO_categories(name):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()




#Add a new book
def INSERT_new_books(title, author_id, category_id, isbn, publication_year, available_copies, total_copies):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author_id, category_id, isbn, publication_year, available_copies, total_copies) VALUES (?, (SELECT author_id FROM authors WHERE name = ?), (SELECT category_id FROM categories WHERE name = ?), ?, ?, ?, ?)", (title, author_id, category_id, isbn, publication_year, available_copies, total_copies))
    conn.commit()
    conn.close()


#Borrow a book (create a new loan)
def Borrow_book(book_id, user_id, due_date):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO loans (book_id, user_id, due_date) VALUES ((SELECT book_id FROM books WHERE title = ?), (SELECT user_id FROM users WHERE username = ?), ?)", (book_id, user_id, due_date))
    conn.commit()
    conn.close()


#Return a book (update the loan with a return date)
def Return_book(title):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("UPDATE loans SET return_date = date('now') WHERE loan_id = (SELECT loan_id FROM loans JOIN books ON loans.book_id = books.book_id WHERE books.title = ? AND return_date LIMIT 1) ", (title,))
    conn.commit()
    conn.close()


#Find all books by a specific author
def find_book(author_name):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT books.title, books.publication_year FROM books JOIN authors ON books.author_id = authors.author_id WHERE authors.name = ?", (author_name,))
    result = cur.fetchall()
    conn.close()
    return result



#List all current loans for a user
def current_loans(username):
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT books.title, loans.loan_date, loans.due_date FROM loans JOIN books ON loans.book_id = books.book_id JOIN users ON loans.user_id = users.user_id WHERE users.username = ? AND loans.return_date IS NULL", (username,))
    result = cur.fetchall()
    conn.close()
    return result

#Update available copies of a book (after a return or new purchase)
def Update_available():
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET available_copies = available_copies + 1  WHERE title = ?")
    cur.fetchall()
    conn.close()



#Delete a user (Note: Handle with care, especially if foreign key constraints exist)
def Delete_user():
    conn = sqlite3.connect("BookDatabase.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE username = ?")
    cur.fetchall()
    conn.close()

