# read the previews object and load them from the json file
# remove the obejct from this file and save it to the json file
# the json it will be one for book and for the user

import datetime


class BaseClass:
    def __init__(self):
        self.id = id(self)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save_json(self):
        self.updated_at = datetime.datetime.now()


class Book(BaseClass):
    def __init__(self, title, author, genre, year):
        super().__init__()
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.is_borrow = False


class User(BaseClass):
    def __init__(self, name):
        self.name = name

    def borrowing(self, book):
        if not book.is_borrow:
            book.is_borrow = True
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed by someone else.")


book1 = Book("Make Time", "Steve", "deveoplment", 2025)
user1 = User("Alex")

book1.save_json()
# user1.borrowing(book1)
