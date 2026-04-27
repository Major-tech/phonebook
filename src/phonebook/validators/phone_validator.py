#from phonebook.services.contact_service import my_phonebook 
from phonebook.core.state import my_phonebook


def is_duplicate(phone_number: int | None) -> None | dict | int:
    """Checks if a phone number belongs to an existing contact"""

    # If phone number == None, stop here
    if phone_number == None:
        return None

    # By default we assume the contact is new
    is_duplicate = False

    # Read phonebook
    phonebook = my_phonebook()

    # Non-empty phonebook
    if phonebook:

        # Cross-check the given number with all saved phone numbers
        # For list of numbers
        for v in phonebook.values():

            # for number in a particular list
            for n in v:

                # If phone number(int) == any number in a list(converted to an int)
                if phone_number == n:
                    # The phone number already exists in the phonebook
                    duplicate_num = phone_number
                    is_duplicate = True
                    # Stop on the first similarity
                    break

    # Existing contact
    if is_duplicate:
        return {"is_duplicate": duplicate_num}
    # New contact
    else:
        return phone_number



