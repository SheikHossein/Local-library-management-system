import json
import os
from datetime import datetime, timedelta
from Books import books
from Member import members
from Admin import admins

class DataHandler:
    def __init__(self):
        self.data_dir = "data"
        self.books_file = os.path.join(self.data_dir, "books.json")
        self.members_file = os.path.join(self.data_dir, "members.json")
        self.admins_file = os.path.join(self.data_dir, "admins.json")
        
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def save_books(self):
        books_data = []
        for book in books:
            books_data.append({
                'name': book.name,
                'isInLibrary': book.isInLibrary,
                'author': book.author,
                'subject': book.subject,
                'id': book.id,
                'borrowed_by': book.borrowed_by,
                'borrow_date': book.borrow_date,
                'return_date': book.return_date
            })
        
        with open(self.books_file, 'w', encoding='utf-8') as f:
            json.dump(books_data, f, ensure_ascii=False, indent=4)
    
    def load_books(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r', encoding='utf-8') as f:
                books_data = json.load(f)
            
            books.clear()
            for book_data in books_data:
                from Books import Book
                book = Book(
                    book_data['name'],
                    book_data['isInLibrary'],
                    book_data['author'],
                    book_data['subject'],
                    book_data['id'],
                    book_data['borrowed_by']
                )
                book.borrow_date = book_data.get('borrow_date')
                book.return_date = book_data.get('return_date')
                books.append(book)
    
    def save_members(self):
        members_data = []
        for member in members:
            members_data.append({
                'name': member.name,
                'birthYear': member.birthYear,
                'id': member.id,
                'nationalCode': member.nationalCode,
                'password': member.password,
                'borrowed_books_by_ID': member.borrowed_books_by_ID
            })
        
        with open(self.members_file, 'w', encoding='utf-8') as f:
            json.dump(members_data, f, ensure_ascii=False, indent=4)
    
    def load_members(self):
        if os.path.exists(self.members_file):
            with open(self.members_file, 'r', encoding='utf-8') as f:
                members_data = json.load(f)
            
            members.clear()
            for member_data in members_data:
                from Member import Member
                member = Member(
                    member_data['name'],
                    member_data['birthYear'],
                    member_data['id'],
                    member_data['nationalCode'],
                    member_data['password']
                )
                member.borrowed_books_by_ID = member_data['borrowed_books_by_ID']
                members.append(member)
    
    def save_admins(self):
        admins_data = []
        for admin in admins:
            admins_data.append({
                'adminName': admin.adminName,
                'id': admin.id,
                'password': admin.password
            })
        
        with open(self.admins_file, 'w', encoding='utf-8') as f:
            json.dump(admins_data, f, ensure_ascii=False, indent=4)
    
    def load_admins(self):
        if os.path.exists(self.admins_file):
            with open(self.admins_file, 'r', encoding='utf-8') as f:
                admins_data = json.load(f)
            
            admins.clear()
            for admin_data in admins_data:
                from Admin import Admin
                admin = Admin(
                    admin_data['adminName'],
                    admin_data['id'],
                    admin_data['password']
                )
                admins.append(admin)
    
    def save_all(self):
        self.save_books()
        self.save_members()
        self.save_admins()
    
    def load_all(self):
        self.load_books()
        self.load_members()
        self.load_admins()

data_handler = DataHandler()