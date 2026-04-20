class book:
    def __init__(self, title , author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Autthor: {self.author}")
        print(f"Book ID: {self.book_id}")
        print(f"Available: {self.available}")
    def borrow(self):
        if not self.available:
            print('Book is already borrowed.')
            return 
        self.available =False
        print('You have borrowed the book.')
    def return_book(self):
        self.available = True
        print("Book returned successfully.")
class GeneralBook(book):
    pass
class ReferenceBook(book):
    def borrow(self):
        print("Reference books cannot be borrowed.")

book1 = GeneralBook("python programming", "John Doe", 1)
book2 = ReferenceBook("Data Science Handbook", "Jane Smith", 2)

book1.display_info()
book2.display_info()

print()
book1.borrow()
book1.borrow()
book1.display_info()

print()
book2.display_info()
book2.borrow()

print()

book1.return_book()
book1.display_info()

print()
book3 = book("Artificial Intelligence", "Alice Johnson", 3)
book3.display_info()