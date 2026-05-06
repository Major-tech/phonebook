from phonebook.domain.exceptions import InvalidSelectionError


def is_valid_int_option(option: int | None, start: int, end: int) -> int | None:
    """If the option number is within the specified range, it returns the option, else it returns None"""

    # Invalid option, raise error 
    if option not in range(start, end):
        raise InvalidSelectionError("selection failed — option out of range")
    
    return option 

    

