class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class UserNotFoundError(LibraryError):
    pass

class BookNotAvailableError(LibraryError):
    pass

class LoanNotFoundError(LibraryError):
    pass

class InvalidEmailError(LibraryError):
    pass
