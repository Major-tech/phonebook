# DOMAIN ERRORS 

# GENERAL DOMAIN ERRORS

class AppError(Exception):
    """Base class for all domain errors"""

    pass


class TooManyInvalidAttemptsError(AppError):
    """Raised when maximum input attempts are reached"""

    def __str__(self):
        return "Too many invalid attempts.Please try again later"


class InvalidSelectionError(AppError):
    """Raised when a numeric selection is outside the allowed range."""

    pass


class ContactNotFoundError(AppError):
    """Raised when a contact name is not found in the phonebook."""

    def __init__(self, search_pattern) -> None:
        self.search_pattern = search_pattern 
        
    def __str__(self) -> str:
        return f"\nNo contacts matching {self.search_pattern} were found" 


class DuplicatePhoneError(AppError):
    """Raised when an existing phone number is duplicated"""

    pass


# ----- INVALID SELECTIONS -----

class SelectionError(AppError):
    """Base class for invalid selection operations."""

    pass


class InvalidMenuSelectionError(SelectionError):
    """Raised when a user selects an invalid menu option outside the available range."""

    pass


class InvalidContactSelectionError(SelectionError):
    """Raised when a user selects a contact index that does not exist in the current result set."""

    pass 


# ----- VALUE ERROR ----- 

class MissingContactNameError(AppError, ValueError):
    """Raised when a contact name is not provided after allowed retries.""" 
    
    pass


class MissingPhoneNumberError(AppError, ValueError):
    """Raised when a contact has no phone numbers but at least one is required."""

    pass


class PhoneNumberQueryRequiredError(AppError, ValueError):
    """Raised when a phone number is required for a search but not provided."""

    pass 


class NameQueryRequiredError(AppError, ValueError):
    """Raised when a contact name is required to perform a search but none is provided."""

    pass 
