import Member
from Member import members
from Books import books
import random
from datetime import datetime, timedelta

class Admin:
    def __init__(self, adminName, id, password):
        self.adminName = adminName
        self.id = id
        self.password = password

    def addMember(self):
        if members:
            lastID = max(member.id for member in members)
        else:
            lastID = 1020

        newName = input("Name:\n")
        newBirthYear = input("Birth Year:\n")
        newNationalCode = input("National Code:\n")
        newPassword = input("Password:\n")
        
        # Check for duplicate national code
        duplicate = False
        for member in members:
            if member.nationalCode == newNationalCode:
                duplicate = True
                break
                
        if duplicate:
            print("Warning: This national code already exists in the system.")
            confirm = input("Do you still want to register this user? (yes/no): ")
            if confirm.lower() != "yes":
                print("Registration cancelled.")
                return False
        
        # Validate input
        if not newBirthYear.isdigit():
            print("Invalid birth year. Please enter a valid number.")
            return False
            
        newBirthYear = int(newBirthYear)
        
        if 999 < newBirthYear < 10000:
            if newBirthYear < 2008:
                if newNationalCode.isdigit() and len(newNationalCode) == 10:
                    new_member = Member.Member(newName, newBirthYear, lastID + 1, newNationalCode, newPassword)
                    members.append(new_member)
                    print(f"Member: {newName} added with ID: {lastID + 1}, National code: {newNationalCode}")
                    print("=" * 80)
                    return True
                else:
                    print("Invalid National code! It must be 10 digits.")
            else:
                print("Access denied due to member's young age.")
                confirm = input("Add member anyway?\n 1) Yes\n 2) No\n")
                if confirm == "1":
                    new_member = Member.Member(newName, newBirthYear, lastID + 1, newNationalCode, newPassword)
                    members.append(new_member)
                    print(f"Member: {newName} added with ID: {lastID + 1}")
                    return True
        else:
            print("Invalid birth year! It must be a 4-digit number.")
            
        return False

    def removeMember(self, memberID):
        for member in members:
            if str(member.id) == str(memberID):
                members.remove(member)
                print(f"Member {member.name} with ID {member.id} removed successfully.")
                return True
        print("Member not found.")
        return False

    def show_all_members(self):
        if members:
            print("All Members:")
            for member in members:
                print(f"Name: {member.name}, ID: {member.id}, National Code: {member.nationalCode}")
                print(f"Borrowed Books: {sorted(member.borrowed_books_by_ID)}")
                print("=" * 100)
        else:
            print("No members found.")

    def search_members(self):
        print("Search members by:")
        print("1. ID")
        print("2. Name")
        print("3. National Code")
        print("4. Borrowed Books")
        
        search_option = input("Enter your choice: ")
        results = []
        
        if search_option == "1":
            search_id = input("Enter member ID: ")
            for member in members:
                if str(member.id) == search_id:
                    results.append(member)
                    
        elif search_option == "2":
            search_name = input("Enter member name: ")
            for member in members:
                if search_name.lower() in member.name.lower():
                    results.append(member)
                    
        elif search_option == "3":
            search_national_code = input("Enter national code: ")
            for member in members:
                if search_national_code == member.nationalCode:
                    results.append(member)
                    
        elif search_option == "4":
            search_book_id = input("Enter book ID: ")
            for member in members:
                if int(search_book_id) in member.borrowed_books_by_ID:
                    results.append(member)
                    
        else:
            print("Invalid option.")
            return
            
        if results:
            print(f"Found {len(results)} result(s):")
            for member in results:
                print(f"Name: {member.name}, ID: {member.id}, National Code: {member.nationalCode}")
                print(f"Borrowed Books: {sorted(member.borrowed_books_by_ID)}")
                print("=" * 100)
        else:
            print("No members found matching your criteria.")

    def show_all_books(self):
        if books:
            print("All Books:")
            for book in books:
                status = "Available" if book.isInLibrary else "Borrowed"
                print(f"ID: {book.id}, Title: {book.name}, Author: {book.author}, Genre: {book.subject}")
                print(f"Status: {status}")
                if not book.isInLibrary:
                    print(f"Borrowed by: {book.borrowed_by}")
                    print(f"Borrow date: {book.borrow_date}")
                    print(f"Expected return date: {book.return_date}")
                print("=" * 100)
        else:
            print("No books found.")

admins = []

def add_admin():
    admin1 = Admin("Hossein", random.randint(1, 100), "hossein!#*&")
    admin2 = Admin("Ali", random.randint(101, 200), "ali!#^)")
    admins.append(admin1)
    admins.append(admin2)