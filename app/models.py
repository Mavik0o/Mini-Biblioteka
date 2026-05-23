class Book:
    def __init__(self, book_id, title, author, year, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.is_available = True


class User:
    def __init__(self, user_id, first_name, last_name, email):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Loan:
    def __init__(self, loan_id, book_id, user_id, borrow_date, return_date=None):
        self.loan_id = loan_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.return_date = return_date