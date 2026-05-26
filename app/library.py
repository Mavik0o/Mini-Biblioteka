from datetime import date

from app.models import Book, User, Loan
from app.exceptions import (
    BookNotFoundError,
    UserNotFoundError,
    BookNotAvailableError,
    LoanNotFoundError
)


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, year, category):
        pass

    def add_user(self, first_name, last_name, email):
        pass

    def find_book_by_id(self, book_id):
        pass

    def find_user_by_id(self, user_id):
        pass

    def borrow_book(self, book_id, user_id):
        pass

    def return_book(self, book_id):
        pass

    def get_available_books(self):
        pass

    def get_borrowed_books(self):
        pass
