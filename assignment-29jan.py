collections = []

class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def add_book(self):
        collections.append({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "copies": self.copies
        })

    def remove_book(self, isbn):
        for book in collections:
            if book["isbn"] == isbn:
                collections.remove(book)
                return f"Book with ISBN {isbn} removed."
        return "Book not found."

    def find_book(self, isbn):
        for book in collections:
            if book["isbn"] == isbn:
                return book
        return "Book not found."

    
    def display_books():
        if not collections:
            print("No books available.")
        else:
            for book in collections:
                print(book)


book1 = Book("Harry Potter", "K", "12345", 5)
book1.add_book()

book2 = Book("wings of fire", "B", "67890", 3)
book2.add_book()

print(book1.find_book("12345"))
book1.remove_book("12345")
Book.display_books()


collection=[]
class Employee:
    def __init__(self,name,age,salary,dept):
        self.name=name
        self.age=age
        self.salary=salary 
        self.dept=dept
class Engineer(Employee):
    def __init__(self,name,age,salary,dept,skill,position):
        super(). __init__(name,age,salary,dept)
        self.skill=skill
        self.position=position
class Manager(Employee):
    def __init__(self,name,age,salary,dept,position):
        super(). __init__(name,age,salary,dept)
        self.position=position


