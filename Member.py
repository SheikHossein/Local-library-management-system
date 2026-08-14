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
                if book.isInLibrary:
                    print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                    print("=" * 100)
        else:
            print("No books found.")

    def search_for_books(self):
        search_by_what = input("What method of search you want?\n 1)by ID \n 2)by name \n 3)by genre \n 4)by author\n ")
        
        books_found = 0
        if search_by_what == "1":
            book_id = input("Enter the id that you want to see\n")
            for book in books:
                if str(book.id) == book_id:
                    if book.isInLibrary:
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                        print("=" * 100)
                        books_found += 1
                    else:
                        print("This book has been borrowed but here's information:")
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                        print("=" * 100)
                        books_found += 1
            if books_found == 0:
                print("No book found")
                
        elif search_by_what == "2":
            book_name = input("Enter the book name that you want to see \n")
            for book in books:
                if book_name.lower() in book.name.lower():
                    if book.isInLibrary:
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                        print("=" * 100)
                        books_found += 1
                    else:
                        print("This book has been borrowed but here's information:")
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
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
                if book_genre.lower() == book.subject.lower():
                    if book.isInLibrary:
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                        print("=" * 100)
                        books_found += 1
                    else:
                        print("This book has been borrowed but here's information:")
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                        print("=" * 100)
                        books_found += 1
            if books_found == 0:
                print("No book found")
                
        elif search_by_what == "4":
            book_author = input("Enter an author name to search for his/her books: ")
            for book in books:
                if book_author.lower() in book.author.lower():
                    if book.isInLibrary:
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                        print("=" * 100)
                        books_found += 1
                    else:
                        print("This book has been borrowed but here's information:")
                        print(f"{book.id} Title: {book.name} Author: {book.author}, Genre: {book.subject}")
                        print("=" * 100)
                        books_found += 1
            if books_found == 0:
                print("No book found")

members = [
    Member("Alice", 1990, 1001, "1234567890", "alice123"),
    Member("Bob", 1988, 1002, "1234567891", "bob123"),
    Member("Charlie", 1992, 1003, "1234567892", "charlie123"),
    Member("David", 1991, 1004, "1234567893", "david123"),
    Member("Eve", 1993, 1005, "1234567894", "eve123"),
    Member("Frank", 1987, 1006, "1234567895", "frank123"),
    Member("Grace", 1994, 1007, "1234567896", "grace123"),
    Member("Heidi", 1995, 1008, "1234567897", "heidi123"),
    Member("Ivan", 1989, 1009, "1234567898", "ivan123"),
    Member("Judy", 1996, 1010, "1234567899", "judy123"),
    Member("Karl", 1990, 1011, "1234567800", "karl123"),
    Member("Laura", 1992, 1012, "1234567801", "laura123"),
    Member("Mallory", 1993, 1013, "1234567802", "mallory123"),
    Member("Niaj", 1991, 1014, "1234567803", "niaj123"),
    Member("Olivia", 1994, 1015, "1234567804", "olivia123"),
    Member("Peggy", 1995, 1016, "1234567805", "peggy123"),
    Member("Rupert", 1987, 1017, "1234567806", "rupert123"),
    Member("Sybil", 1988, 1018, "1234567807", "sybil123"),
    Member("Trent", 1996, 1019, "1234567808", "trent123"),
    Member("Victor", 1989, 1020, "1234567809", "victor123")
]