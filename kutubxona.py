import os

class Kutubxona:


    def __init__(self, filename="Kutubxona.txt"):

        self.filename = filename
        self.books = self._load_books()

    def _load_books(self):

        books = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                books = file.readlines()
            books = [book.strip() for book in books]
        return books

    def _save_books(self):
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(f"{book}\n")

    def add_book(self, title):

        if title in self.books:
            raise ValueError(f"Book '{title}' Kutubxonada mavjud.")
        self.books.append(title)
        self._save_books()
        print(f"Book '{title}' kutubxonaga qo'shildi.")

    def remove_book(self, title):

        if title not in self.books:
            raise ValueError(f"Book '{title}' kutubxonada topilmadi.")
        self.books.remove(title)
        self._save_books()
        print(f"Book '{title}' kutubxonadan olib tashlandi.")

    def display_books(self):
        if not self.books:
            print("Kutubxonada kitob yo'q.")
        else:
            print("Mavjud kitoblar:")
            for book in self.books:
                print(f"- {book}")

my_library = Kutubxona()

my_library.add_book("Ikki eshik orasi")
my_library.add_book("Shum bola")
my_library.add_book("Kecha va Kunduz")

my_library.display_books()

my_library.remove_book("Shum bola")


my_library.display_books()
