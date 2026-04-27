# DOMAIN ERRORS 

class AppError(Exception):
    """Base class for all domain errors"""

    pass


class TooManyInvalidAttemptsError(AppError):
    """Raised when maximum input attempts are reached"""

    def __str__(self):
        return "Too many invalid attempts.Please try again later"


class ContactNotFoundError(AppError):
    """Raised when a contact doesn't exist"""
    pass

class DuplicatePhoneError(AppError):
    """Raised when an existing phone number is duplicated"""

    pass
