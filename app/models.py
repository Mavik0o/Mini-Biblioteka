class Book:
    def __init__(self, book_id, title, author, year, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.is_available = True

    def mark_as_borrowed(self):
        self.is_available = False

    def mark_as_available(self):
        self.is_available = True

    def __str__(self):
        status = "dostępna" if self.is_available else "wypożyczona"
        return f"{self.book_id}. {self.title} - {self.author} ({self.year}), kategoria: {self.category}, status: {status}"


class User:
    def __init__(self, user_id, first_name, last_name, email):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f"{self.user_id}. {self.first_name} {self.last_name}, email: {self.email}"


class Loan:
    def __init__(self, loan_id, book_id, user_id, borrow_date, return_date=None):
        self.loan_id = loan_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def close_loan(self, return_date):
        self.return_date = return_date

    def is_active(self):
        return self.return_date is None

    def __str__(self):
        status = "aktywne" if self.is_active() else f"zwrócono: {self.return_date}"
        return f"Wypożyczenie {self.loan_id}: książka ID {self.book_id}, użytkownik ID {self.user_id}, data: {self.borrow_date}, status: {status}"