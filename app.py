# read the previews object and load them from the json file
# remove the obejct from this file and save it to the json file
# the json it will be one for book and for the user

import datetime
import json
import os


class BaseClass:
    def __init__(self):
        self.id = str(id(self))
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save_json(self):
        self.updated_at = datetime.datetime.now()
        file = f"{self.__class__.__name__.lower()}s.json"

        if os.path.exists(file):
            with open(file, "r") as f:
                try:
                    saved_data = json.load(f)
                except json.JSONDecodeError:
                    saved_data = {}
        else:
            saved_data = {}
        saved_data[self.id] = self.__dict__

        with open(file, "w") as f:
            json.dump(saved_data, f, indent=4, default=str)

        print(f"{self.__class__.__name__} saved to {file}")

    def remove_json(self):
        file = f"{self.__class__.__name__.lower()}s.json"
        if os.path.exists(file):
            with open(file, "r") as f:
                saved_data = json.load(f)
            if self.id in saved_data:
                del saved_data[self.id]
                with open(file, "w") as f:
                    json.dump(saved_data, f, indent=4, default=str)
                print(f"{self.__class__.__name__} removed from {file}")
            else:
                print(f"{self.__class__.__name__} not found in {file}")
        else:
            print(f"{file} does not exist.")

    @classmethod
    def getting_json(class_name):
        file = f"{class_name.__name__.lower()}s.json"
        get_object = []
        if os.path.exists(file):
            with open(file, "r") as f:
                saved_data = json.load(f)
            for object_id, data in saved_data.items():
                obj = class_name.__new__(class_name)
                obj.__dict__.update(data)
                get_object.append(obj)
            return get_object
        else:
            print(f"{file} does not exist.")


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
        super().__init__()
        self.name = name

    def borrowing(self, book):
        if not book.is_borrow:
            book.is_borrow = True
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed by someone else.")


book1 = Book("Make Time", "Steve", "deveoplment", 2025)
user1 = User("Alex")
book2 = Book("The Power of Habit", "Charles Duhigg", "self-help", 2012)


book1.save_json()
user1.save_json()
