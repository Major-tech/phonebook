def prefix_zero(phone_number: int | None) -> int | None:
    """Prefixes a zero or returns None"""
    if phone_number == None:
        return None
    return f"0{phone_number}"
