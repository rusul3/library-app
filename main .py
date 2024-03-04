
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import font
from random import randint
from queries import  INSERT_new_books, INSERT_INTO_categories, INSERT_INTO_authors, create_new_user, Borrow_book, Return_book, find_book, current_loans, check_username_exists
from PIL import Image, ImageTk
import sqlite3
import tkinter as tk


# Create root screen
root = tk.Tk()
root.geometry("1000x1000")
root.title("Book Database Application")

background =  "#2E8B57"
root.config(bg=background) # Change root background
mainStyle = Style()
# Configure styles for main frame and navigation bar frame
mainStyle.configure("Main.TFrame", background=background)


# Create the main window and start window
def startpage():
    global mainFrame
    # Where the myjority of content will fit in
    mainFrame = Frame(root, style="Main.TFrame")
    mainFrame.place(width=1000, height=1000)

    #welcome message
    welcome = Label(mainFrame, text="Hi Nice To See You ", font=("Times New Roman", 45),background=background)
    welcome.place(x=250, y=20)

    # Load image
    image = Image.open("books.jpg")
    image = image.resize((500, 200))
    photo = ImageTk.PhotoImage(image)

    # Create label with the image
    logo = Label(mainFrame, image=photo)
    logo.image = photo
    logo.place(x=250, y=150)

    # Start the app
    openButton = Button(mainFrame, text="Sign In", command=signIN)
    openButton.place(width=350, height=50, x=300, y=380)
    root.mainloop()

# Create labels and entry fields for user input
def signIN():
 global username_entry
 global full_name_entry
 global email_entry
 global password_entry
 global SinIn_page
 global accountExists

 #remove_all_widgets(SinIn_page)

 SinIn_page = Frame(mainFrame, style="Main.TFrame")
 SinIn_page.place(width=1000, height=1000)

 Label(SinIn_page, text="Username:").grid(row=6, column=10, sticky="e")
 username_entry = Entry(SinIn_page)
 username_entry.grid(row=6, column=12)

 Label(SinIn_page, text="FullName:").grid(row=8, column=10, sticky="e")
 full_name_entry = Entry(SinIn_page)
 full_name_entry.grid(row=8, column=12)

 Label(SinIn_page, text="Email:").grid(row=10, column=10, sticky="e")
 email_entry = Entry(SinIn_page)
 email_entry.grid(row=10, column=12)
 

 Label(SinIn_page, text="Password:").grid(row=12, column=10, sticky="e")
 password_entry = Entry(SinIn_page, show="*")
 password_entry.grid(row=12, column=12)
 
 accountExists = Label(mainFrame, background=background)
 accountExists.place(width=124, x=88, y=370)


# Button to create a new user
 create_button = Button(SinIn_page, text="Enter User", command = new_user)
 create_button.grid(row=16, column=10)
 
 # Function to validate the password
def password_check(password_entry):
    special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
    name = password_entry.get()
    msg = ""#Turn off password_check.
    if len(name) == 0:
        msg = 'password can\'t be empty'
    else:
        try:
            if not any(ch in special_ch for ch in name):
                msg = 'Atleast 1 special character required!'
            elif not any(ch.isupper() for ch in name):
                msg = 'Atleast 1 uppercase character required!'
            elif not any(ch.islower() for ch in name):
                msg = 'Atleast 1 lowercase character required!'
            elif not any(ch.isdigit() for ch in name):
                msg = 'Atleast 1 number required!'
            elif len(name) < 8:
                msg = 'Password must be minimum of 8 characters!'
            else:
                msg = 'Success!'
                choose_enter()
                
        except Exception as ep:
            messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)

# Function to create a new user
def new_user():
    Username = username_entry.get() 
    FullName =full_name_entry.get() 
    Email = email_entry.get()
    Password = password_entry.get()
    
    if password_check(password_entry):
     if not check_username_exists(Username):
      create_new_user(Username, FullName, Email, Password)
     #username.delete(0, tk.END)
     #full_name.delete(0, tk.END)
     #email.delete(0, tk.END)
     #password_hash.delete(0, tk.END)
      messagebox.showinfo("Success", "User created successfully")
      choose_enter()
     else:
        accountExists.config(text="Account already exists")



#create choose page 
def choose_enter():  
    # Title of the page
    page = Frame(mainFrame, style="Main.TFrame")
    page.place(width=1000, height=1000)
    enterLabel = Label(page, text="Please choose the feild to enter the data ! ", background=background)
    enterLabel.place(width=500, x=0, y=10)

    # the feild of data 
    AButton = Button(page, text="Insert Authors", command=InsertA)
    AButton.place(width=350, height=50, x=18, y=50)

    #CButton = Button(mainFrame, text="Insert Categories", command=service_L)
    #CButton.place(width=350, height=50, x=18, y=250)
    
    BButton = Button(page, text="Insert New Book", command=AddnewBook)
    BButton.place(width=350, height=50, x=18, y=150) 

    #WButton = Button(mainFrame, text="Barrow Book", command=service_K)
    #WButton.place(width=350, height=50, x=18, y=550) 

    #RButton = Button(mainFrame, text="Return Book", command=service_K)
    #RButton.place(width=350, height=50, x=18, y=450) 

    SButton = Button(page, text="Search for Book", command=search1)
    SButton.place(width=350, height=50, x=18, y=250) 

    LButton = Button(page, text="Search for Loan Book", command=search2)
    LButton.place(width=350, height=50, x=18, y=350) 

    #backbutton
    global storeBackButton
    #pageControlFrame = Frame(page, style="Main.TFrame")
    storeBackButton = Button(page, text="<--", command=store_previous_page1)
    storeBackButton.place(width=50, height=50, x=18, y=550) 



# Create and place the name label and entry field
def InsertA():
 global name_entry
 global bio_text

 fram1 = Frame(mainFrame, style="Main.TFrame")
 fram1.place(width=1000, height=1000)
 Label(fram1, text="Name:", background=background).grid(row=6, column=10)
 name_entry = Entry(fram1)
 name_entry.grid(row=6, column=12)

 # Create and place the bio label and text field
 Label(fram1, text="Bio:", background=background).grid(row=8, column=10, sticky="e")
 bio_text = Text(fram1,height=10, width=50)
 bio_text.grid(row=8, column=12, sticky="e")

 # Create and place the 'Add Author' button
 add_button = Button(fram1, text="Add Author", command=INSERT_authors)
 add_button.grid(row=10, columnspan=12, sticky="e")

 #backbutton
 global storeBackButton
 #global storeNextButton
 pageControlFrame = Frame(mainFrame, style="Main.TFrame")
 storeBackButton = Button(pageControlFrame, text="<--", command=store_previous_page)

 pageControlFrame.place(width=300, height=50, x=0, y=550)
 storeBackButton.place(width=70, height=30, y=10, x=18)

#insert authors
def INSERT_authors():
    Authorsname = name_entry.get() 
    Bio =bio_text.get("1.0", tk.END)
    
    INSERT_INTO_authors(Authorsname,Bio.strip())
    messagebox.showinfo("Success", "Authors insert successfully")


def AddnewBook():
  global title_entry
  global author_entry
  global category_entry
  global isbn_entry
  global publication_year_entry
  global available_copies_entry
  global total_copies_entry


  fram2 = Frame(mainFrame, style="Main.TFrame")
  fram2.place(width=1000, height=1000)

  # Adjusted starting row for "Add Book" section
  Label(fram2, text="Title:", background=background).grid(row=24, column=0)
  title_entry = Entry(fram2)
  title_entry.grid(row=24, column=1)

  Label(fram2, text="Author:", background=background).grid(row=26, column=0)
  author_entry = Entry(fram2)
  author_entry.grid(row=26, column=1)

  Label(fram2, text="Category:", background=background).grid(row=28, column=0)
  category_entry = Entry(fram2)
  category_entry.grid(row=28, column=1)

  isbn_entry = Entry(fram2)
  Label(fram2, text="ISBN:", background=background).grid(row=30, column=0)
  isbn_entry.grid(row=30, column=1)

  publication_year_entry = Entry(fram2)
  Label(fram2, text="Publication Year:", background=background).grid(row=32, column=0)
  publication_year_entry.grid(row=32, column=1)

  available_copies_entry = Entry(fram2)
  Label(fram2, text="Available Copes:", background=background).grid(row=34, column=0)
  available_copies_entry.grid(row=34, column=1)

  total_copies_entry = Entry(fram2)
  Label(fram2, text="Total Copes:", background=background).grid(row=36, column=0)
  total_copies_entry.grid(row=36, column=1)

  # Assuming 'on_add_book' is defined as before, placing the 'Add Book' button correctly
  add_book_button = Button(fram2, text="Add Book", command = on_add_book)
  add_book_button.grid(row=38, column=0, columnspan=2, sticky="e")

  #backbutton
  global storeBackButton
  #global storeNextButton
  #pageControlFrame = Frame(frame2, style="Main.TFrame")
  storeBackButton = Button(fram2, text="<--", command=store_previous_page)

  #pageControlFrame.place(width=300, height=50, x=0, y=550)
  storeBackButton.place(width=70, height=30, y=500, x=18)

def on_add_book():
    # Correctly get values from entry widgets
    Title = title_entry.get()
    Author = author_entry.get()  # Assuming you've defined author_entry correctly
    Category = category_entry.get()  # Assuming you've defined category_entry correctly
    ISBN = isbn_entry.get()
    PublicationYear = publication_year_entry.get()
    AvailableCopies = available_copies_entry.get()
    TotalCopies = total_copies_entry.get()
   
    # Call the function to insert new books into the database
    INSERT_new_books(Title, Author, Category, ISBN, PublicationYear, AvailableCopies, TotalCopies)

    messagebox.showinfo("Success", "book insert successfully")
    # Clear the fields after insertion
    #for entry in [title_entry, author_entry, category_entry, isbn_entry, publication_year_entry, available_copies_entry, total_copies_entry]:
       # entry.delete(0, tk.END)



#create search for book 
def search1 ():
    # Search field and button for find_book
 global results_text
 fram3 = Frame(mainFrame, style="Main.TFrame")
 fram3.place(width=1000, height=1000)
 Label(fram3, text="Author Name:").grid(row=0, column=0, padx=10, pady=10)
 author_name_entry = Entry(fram3)
 author_name_entry.grid(row=0, column=1, padx=10, pady=10)
 Button(fram3, text="Find Book", command=lambda: display_find_book_results(author_name_entry.get())).grid(row=0, column=2, padx=10, pady=10)
 # Results display area
 results_text = Text(fram3, height=15, width=70)
 results_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

 #backbutton
 global storeBackButton
 #global storeNextButton
 pageControlFrame = Frame(mainFrame, style="Main.TFrame")
 storeBackButton = Button(pageControlFrame, text="<--", command=store_previous_page)

 pageControlFrame.place(width=300, height=50, x=0, y=550)
 storeBackButton.place(width=70, height=30, y=10, x=18)

# Event Handlers
def display_find_book_results(author_name):
    results = find_book(author_name)
    results_text.delete(1.0, tk.END)
    for title, year in results:
        results_text.insert(tk.END, f"Title: {title}, Year: {year}\n")


#search in data base for loan of book
def search2 ():
 global results_text
# Search field and button for current_loans
 fram4 = Frame(mainFrame, style="Main.TFrame")
 fram4.place(width=1000, height=1000)
 Label(fram4, text="Username:").grid(row=1, column=0, padx=10, pady=10)
 username_entry = Entry(fram4)
 username_entry.grid(row=1, column=1, padx=10, pady=10)
 Button(fram4, text="Current Loans", command=lambda: display_current_loans_results(username_entry.get())).grid(row=1, column=2, padx=10, pady=10)

  # Results display area
 results_text = Text(fram4, height=15, width=70)
 results_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

 #backbutton
 pageControlFrame = Frame(mainFrame, style="Main.TFrame")
 storeBackButton = Button(pageControlFrame, text="<--", command=store_previous_page)

 pageControlFrame.place(width=300, height=50, x=0, y=550)
 storeBackButton.place(width=70, height=30, y=10, x=18)

def display_current_loans_results(username):
    results = current_loans(username)
    results_text.delete(1.0, tk.END)
    for title, loan_date, due_date in results:
        results_text.insert(tk.END, f"Title: {title}, Loan Date: {loan_date}, Due Date: {due_date}\n")

#INSERT_INTO_categories(name):
def INSERT_categories():
    Categoriesname = name_entry.get()

    INSERT_INTO_categories(Categoriesname)
    messagebox.showinfo("Success", "categories insert successfully")


def store_previous_page():
    #global storeCurrentPage
    choose_enter()

def store_previous_page1():
    #global storeCurrentPage
    signIN()

     

startpage()


"""



#Borrow a book (create a new loan)
def Borrow():
    book_id = book_id_entry.get()
    user_id = user_id_entry.get()
    due_date = due_date_entry.get()
    Borrow_book(book_id, user_id, due_date)
    messagebox.showinfo("Success", "your book barrow successfully")
    
#Return a book (update the loan with a return date)
def Returnbook():
    TitleR = title_entry.get()
    Return_book(TitleR)
    messagebox.showinfo("Success", "your book return successfully")

#create category
tk.Label(root, text="Category Name:").grid(row=20, column=0, sticky="e")
category_name_entry = tk.Entry(root)
category_name_entry.grid(row=20, column=1, sticky="e")

# Create and place the 'Add Category' button
add_button = tk.Button(root, text="Add Category", command=INSERT_categories)
add_button.grid(row=22, columnspan=2, sticky="e")

# Create and place the input fields


#creat enter barrow
book_id_entry = tk.Entry(root)
tk.Label(root, text="Book name:").grid(row=40, column=0)
book_id_entry.grid(row=40, column=1)

user_id_entry = tk.Entry(root)
tk.Label(root, text="User:").grid(row=42, column=0)
user_id_entry.grid(row=42, column=1)

due_date_entry = tk.Entry(root)
tk.Label(root, text="Date:").grid(row=44, column=0)
due_date_entry.grid(row=44, column=1)

# Assuming 'on_add_book' is defined as before, placing the 'Add Book' button correctly
add_book_button = tk.Button(root, text="Barrow", command = Borrow)
add_book_button.grid(row=48, column=0, columnspan=2, sticky="e")

#creat enter return
title_entry = tk.Entry(root)
tk.Label(root, text="Title:").grid(row=50, column=0)
title_entry.grid(row=50, column=1)

# Assuming 'on_add_book' is defined as before, placing the 'Add Book' button correctly
add_book_button = tk.Button(root, text="Return", command = Returnbook)
add_book_button.grid(row=52, column=0, columnspan=2, sticky="e")

search_button = tk.Button(root, text="Search book", command = search1)
search_button.grid(row=2, column=3, columnspan=2, sticky="e")

search_button = tk.Button(root, text="Search laon", command = search2)
search_button.grid(row=3, column=2, columnspan=2, sticky="e")



"""