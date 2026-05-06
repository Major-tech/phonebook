from phonebook.core.constants import MAX_PHONE_LENGTH
from phonebook.repository.contact_repository import load_contacts


def is_duplicate_number(phone_number: str) -> tuple[str, str] | None:
    """Checks if a phone number belongs to an existing contact"""

    # By default we assume the contact is new
    is_duplicate = False

    # Read phonebook
    phonebook = load_contacts()

    # Non-empty phonebook
    if phonebook:

        # Cross-check the given number with all saved phone numbers
        # For dict of numbers
        for name, phones in phonebook["contacts"].items():
            # for number in each phone type 
            for num in phones.values():
                # If any saved number(str) == the given number (str)
                if num == phone_number:
                    # The phone number already       exists in the phonebook
                    is_duplicate = True 
                    duplicate = (name, phone_number)

    # Existing contact
    # Return the saved contact 
    if is_duplicate:
        return duplicate 
    # New contact
    else:
        return None


def is_valid_phone_format(phone_number: str) -> bool | None:
    """Returns True if a phone number has the correct length"""

    # len == 10, 1st char is 0 and all chars are numeric
    if (
        len(phone_number) == MAX_PHONE_LENGTH
        and phone_number[0] == "0"
        and phone_number.isdigit()
    ):

        # 2nd char == 7
        if phone_number[1] == "7":
            return True

        # 2nd char == 1
        elif phone_number[1] == "1":
            # Second char == 0 or 1
            if phone_number[2] == "0" or phone_number[2] == "1":
                return True

 

