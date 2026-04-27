def is_valid_int_option(option: int | None, start: int, end: int) -> int | None:
    """If the option number is within the specified range, it returns the option, else it returns None"""

    # Invalid option
    if option == None:
        return None

    # Valid option
    if option in range(start, end):
        return option

