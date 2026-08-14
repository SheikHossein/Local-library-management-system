class Book:
    def __init__(self, name, isInLibrary, author, subject, id, borrowed_by):
        self.name = name
        self.isInLibrary = isInLibrary
        self.author = author
        self.subject = subject
        self.id = id
        self.borrowed_by = borrowed_by
        self.borrow_date = None
        self.return_date = None

books = [
    Book("The Great Gatsby", True, "F. Scott Fitzgerald", "Novel", 1, None),
    Book("To Kill a Mockingbird", True, "Harper Lee", "Novel", 2, None),
    Book("1984", True, "George Orwell", "Dystopian", 3, None),
    Book("Pride and Prejudice", True, "Jane Austen", "Romance", 4, None),
    Book("The Catcher in the Rye", True, "J.D. Salinger", "Novel", 5, None),
    Book("Moby Dick", True, "Herman Melville", "Adventure", 6, None),
    Book("War and Peace", True, "Leo Tolstoy", "Historical", 7, None),
    Book("The Odyssey", True, "Homer", "Epic", 8, None),
    Book("Crime and Punishment", True, "Fyodor Dostoevsky", "Psychological", 9, None),
    Book("The Brothers Karamazov", True, "Fyodor Dostoevsky", "Philosophical", 10, None),
    Book("Brave New World", True, "Aldous Huxley", "Dystopian", 11, None),
    Book("Jane Eyre", True, "Charlotte Bronte", "Novel", 12, None),
    Book("Wuthering Heights", True, "Emily Bronte", "Novel", 13, None),
    Book("The Hobbit", True, "J.R.R. Tolkien", "Fantasy", 14, None),
    Book("Fahrenheit 451", True, "Ray Bradbury", "Dystopian", 15, None),
    Book("The Lord of the Rings", True, "J.R.R. Tolkien", "Fantasy", 16, None),
    Book("Animal Farm", True, "George Orwell", "Satire", 17, None),
    Book("Great Expectations", True, "Charles Dickens", "Novel", 18, None),
    Book("Little Women", True, "Louisa May Alcott", "Novel", 19, None),
    Book("Dracula", True, "Bram Stoker", "Horror", 20, None)
]