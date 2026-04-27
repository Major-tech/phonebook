# APPEND NEW CONTACT 

def append_contact(name: str, phone_numbers: dict[str, int]) -> None:
    """Append a new contact""" 
        
    with open("phonebook.txt", "a") as f:
        f.write(
                f"{name}| {phone_numbers['phone number 1']} | {phone_numbers['phone number 2']} | {phone_numbers['phone number 3']}\n"
            )


# ----- UPDATE / DELETE ----- 

def save_all_contacts(contacts: dict[str, list[int]]) -> None:
    """Rewrites the entire file state""" 
    
    with open("phonebook.txt", "w") as f:
        for k,v in contacts.items():
            f.write(f"{k}| {v[0]} | {v[1]} | {v[2]}\n") 


# READ FROM THE REPOSITORY 

def load_contacts() -> list[dict[str, list[int | None]]]: 
    """Load all saved contacts""" 

    try:
        with open("phonebook.txt", "r") as f:
            contacts = f.readlines()
    except FileNotFoundError:
        contacts = [] 
        
    return contacts  


