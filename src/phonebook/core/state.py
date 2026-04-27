from phonebook.repository.contact_repository import load_contacts


def my_phonebook() -> dict[str, list[int | None]]:
    """Retrieves all phonebook contacts"""

    phonebook = {}
    
    # Read File
    contacts = load_contacts()

    # Non-empty phonebook
    if contacts:    

        # Clean the data
        # For each contact
        for contact in contacts:
            # Convert it to a string
            contact_string = "".join(contact)
            # Split on "|" and assign name and phone numbers
            name, p1, p2, p3 = contact_string.split("|")

            # Cleaned data
            phonebook[name] = [p1, p2, p3]
            
        # Convert phone numbers to integers
        for k,v in phonebook.items():
            phonebook[k] = [None if 'None' in n else int(n) for n in v]

        return phonebook
 
