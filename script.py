import Library
from Books import books
from Member import members
from Admin import admins
from Admin import add_admin
from data_handler import data_handler
from datetime import datetime, timedelta
print(admins)
print(members)
def user_panel():
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Show All Books")
    print("4. Search for books")
    print("5. Log out")

def admin_Authentication():
    print("Welcome to the Admin Authentication System")
    print("1. Login")
    print("2. Go Back")

def user_Authentication():
    print("Welcome to the User Authentication System")
    print("1. Login")
    print("2. Go Back")
    print("3. *Only admins can register you*")

def first_panel():
    
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    print("What's your choice?")

def admin_panel():
    print("Welcome to the Admin Panel")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Show All Members and Borrowed Books")
    print("4. Search Members")
    print("5. Show All Books")
    print("6. Log out")

thislibrary = Library.Library("My Library", len(members), members, books, admins)

# Load data at startup
data_handler.load_all()
if len(admins) == 0:
    add_admin()
print("Welcome to the Library Management System")
while True:
    
    first_panel()
#first input
    first_selected_option = input("_")
    
    if first_selected_option == "1":
#user authentication    
        user_Authentication()
        user_selected_option = input("_")
        
        if user_selected_option == "1":
            print("User Login")
            userName = input("Username:\n")
            userPassword = input("Password:\n")
            
            user_found = False
            for member in members:
                if member.name == userName and member.password == userPassword:
                    print("Login successful!")
                    print("Welcome to the Library Management System")
                    user_found = True
                    
                    while True:
                        user_panel()
                        user_choose = input("_")
#user.borrow                        
                        if user_choose == "1":
                            print("Borrow Book")
                            book_id = input("Enter Book ID to borrow:\n")
                            book_found = False
                            for book in books:
                                if str(book.id) == book_id:
                                    book_found = True
                                    if book.isInLibrary:
# Ask for borrowing duration
                                        try:
                                            days = int(input("How many days do you want to borrow this book for?\n"))
                                            if days <= 0:
                                                print("Please enter a positive number of days.")
                                                break
                                        except ValueError:
                                            print("Invalid input. Please enter a number.")
                                            break
                                            
                                        book.isInLibrary = False
                                        book.borrowed_by = f"{member.name}, national code: {member.nationalCode}, id: {member.id}"
                                        book.borrow_date = datetime.now().strftime("%Y-%m-%d")
                                        book.return_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
                                        member.borrowed_books_by_ID.append(book.id)
                                        print("Book borrowed successfully!")
                                        print(f"Please return the book by {book.return_date}")
                                        data_handler.save_all()
                                    else:
                                        print("This book is already borrowed by someone else.")
                                        print("You can return for it later.")
                                    break
                            
                            if not book_found:
                                print("Book with this ID does not exist.")
#user.return                                
                        elif user_choose == "2":
                            print("Return Book")
                            book_id = input("Enter Book ID to return:\n")
                            book_found = False
#security for returning the borrowed book
                            for book in books:
                                if str(book.id) == book_id:
                                    book_found = True
                                    if not book.isInLibrary:
                                        if book.borrowed_by == f"{member.name}, national code: {member.nationalCode}, id: {member.id}":
                                            book.isInLibrary = True
                                            book.borrowed_by = None
                                            book.borrow_date = None
                                            book.return_date = None
                                            if int(book_id) in member.borrowed_books_by_ID:
                                                member.borrowed_books_by_ID.remove(int(book_id))
                                            print("Book returned successfully!")
                                            data_handler.save_all()
                                        else:
                                            print("You didn't borrow this book.")
                                    else:
                                        print("This book was not borrowed.")
                                    break
                            
                            if not book_found:
                                print("Book with this ID does not exist.")
#user.show books                                
                        elif user_choose == "3":
                            print("Showing all books")
                            member.show_all_books()
#user.search                            
                        elif user_choose == "4":
                            member.search_for_books()
#user.log out                            
                        elif user_choose == "5":
                            print("Logging out...")
                            break
                            
                        else:
                            print("Invalid choice. Please try again.")
                    
                    break
            
            if not user_found:
                print("Invalid username or password.")
                
        elif user_selected_option == "2":
            print("Going back")
            
        else:
            print("Going Back")
  
    elif first_selected_option == "2":
#Admin select
        admin_Authentication()
        admin_selected_option = input("_")
        
        if admin_selected_option == "1":
            print("Admin Login")
            adminName = input("Admin Name:\n")
            adminPassword = input("Password:\n")
            admin_found = False
#finding admin
            for admin in admins:
                if admin.adminName == adminName and admin.password == adminPassword:
                    print("Login successful!")
                    print(f"Welcome {admin.adminName}! Your ID is {admin.id}")
                    current_admin = admin
                    admin_found = True
                    
                    while True:
#Admin panel
                        admin_panel()
                        admin_choose = input("_")
                        
                        if admin_choose == "1":
                            print("Add member")
                            if current_admin.addMember():
                                data_handler.save_all()
                            
                        elif admin_choose == "2":
                            print("Remove member")
                            member_id = input("Enter Member ID to remove:\n")
                            if current_admin.removeMember(member_id):
                                data_handler.save_all()
                            
                        elif admin_choose == "3":
                            print("Show All Members and Borrowed Books")
                            current_admin.show_all_members()
                            
                        elif admin_choose == "4":
                            print("Search Members")
                            current_admin.search_members()
                            
                        elif admin_choose == "5":
                            print("Show All Books")
                            current_admin.show_all_books()
                            
                        elif admin_choose == "6":
                            print("Logging out...")
                            break
                            
                        else:
                            print("Invalid choice. Please try again.")
                    
                    break
            
            if not admin_found:
                print("Invalid admin name or password.")
                
        elif admin_selected_option == "2":
            print("Going back")
            
        else:
            print("Invalid choice")

    elif first_selected_option == "3":
        print("Exiting the program.")
        data_handler.save_all()
        break
        #break the first while loop

    else:
        print("Invalid choice.")