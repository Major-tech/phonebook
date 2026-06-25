from phonebook.paths.contacts import get_contacts_file

import json


# CORE VARIABLES
contacts_file = get_contacts_file()

# APPEND NEW CONTACT 

def append_contact(contact: dict[str | None, dict[str, str]]) -> dict[str | None, dict[str, str]]: 
    """Append a new contact""" 

    # Read file 
    try:
        with open(contacts_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"contacts": {}} 

    # Append data 
    data["contacts"].update(contact)

    # Save appended data
    with open(contacts_file, "w") as file:
        json.dump(data, file) 

    return contact 


# ----- UPDATE / DELETE ----- 

def save_all_contacts(contacts: dict[str, dict[str, dict[str, str]]]) -> None:
    """Rewrites the entire file state""" 
    
    with open(contacts_file, "w") as file:
        json.dump(contacts, file)


# READ FROM THE REPOSITORY 

def load_contacts() -> dict[str, dict[str, dict[str,str]]]:
    """Retrieves all the saved contacts"""

    try:
        with open(contacts_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"contacts": {}}

    return data 
