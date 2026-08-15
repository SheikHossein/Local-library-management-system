from Books import books

class Member:
    def __init__(self, name, birthYear, id, nationalCode, password):
        self.name = name
        self.birthYear = birthYear
        self.id = id
        self.nationalCode = nationalCode
        self.password = password
        self.borrowed_books_by_ID = []
        

    def borrow(self, bookID):
        for book in books:
            if str(book.id) == str(bookID):
                if book.isInLibrary:
                    book.isInLibrary = False
                    self.borrowed_books_by_ID.append(book.id)
                    print(f"You have borrowed '{book.name}'.")
                else:
                    print("This book is already borrowed by someone else.")
                return
        print("Book with this ID does not exist.")

    def show_all_books(self):
        if books:
            
            print("All Books:")
            for book in books:
                Availability = None
                if book.isInLibrary:
                    Availability = "Available"
                else:
                    Availability = "Unavailable"
                
                print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}, Availability: {Availability}")
                print("=" * 110)
        else:
            print("No books found.")

    def search_for_books(self):
        search_by_what = input("What method of search you want?\n 1)by ID \n 2)by name \n 3)by genre \n 4)by author\n ")
        
        books_found = 0
        if search_by_what == "1":
            book_id = input("Enter the id that you want to see\n")
            for book in books:
                Availability = None
                if book.isInLibrary:
                    Availability = "Available"
                else:
                    Availability = "Unavailable"
                if str(book.id) == book_id:
                    
                    print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}, Availability: {Availability}")
                    print("=" * 100)
                    books_found += 1
                
                    
            if books_found == 0:
                print("No book found")
                
        elif search_by_what == "2":
            book_name = input("Enter the book name that you want to see \n")
            for book in books:


                Availability = None
                if book.isInLibrary:
                    Availability = "Available"
                else:
                    Availability = "Unavailable"


                if book_name.lower() in book.name.lower():

                    if book.isInLibrary:
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}, Availability: {Availability}")
                        print("=" * 100)
                        books_found += 1
                    
            if books_found == 0:
                print("No book found")
                
        elif search_by_what == "3":
            subjects = set()
            for book in books:
                subjects.add(book.subject)
            
            print("Available genres:")
            for i, subject in enumerate(subjects, 1):
                print(f"{i}. {subject}")
            
            book_genre = input("What genre you want from the list? \nType it here: ")
            for book in books:


                Availability = None
                if book.isInLibrary:
                    Availability = "Available"
                else:
                    Availability = "Unavailable"

                if book_genre.lower() == book.subject.lower():
                    
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}, Availability: {Availability}")
                        print("=" * 100)
                        books_found += 1
                    
            if books_found == 0:
                print("No book found")
                
        elif search_by_what == "4":
            book_author = input("Enter an author name to search for his/her books: ")
            for book in books:
                Availability = None
                if book.isInLibrary:
                    Availability = "Available"
                else:
                    Availability = "Unavailable"

                if book_author.lower() in book.author.lower():
                    
                    print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}, Availability: {Availability}")
                    print("=" * 100)
                    books_found += 1
                    
            if books_found == 0:
                print("No book found")

members = [
