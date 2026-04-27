from phonebook.repository.contact_repository import append_contact, save_all_contacts, load_contacts
from phonebook.validators.phone_validator import is_duplicate
from phonebook.cli.input_handlers import search_options_prompt, collect_search_option, collect_contact_name, collect_phone_numbers, collect_name, collect_phone_num, choose_contact

from phonebook.core.state import my_phonebook


# ----- ADD ----- 

def add_contact(contact_name, phone_dict) -> str:
    """Save contact name and numbers to the phonebook"""

    # If name and phone numbers are given
    if contact_name and phone_dict:

        # Save to file
        append_contact(contact_name, phone_dict)
        
        return contact_name


# ----- SEARCH -----

def search_contact() -> str:
    """Lookup an existing contact"""

    # Search option
    search_option = collect_search_option(search_options_prompt, 1, 3)

    # Selected contact
    contact = collect_contact_details(search_option)

    if contact:
        for k, v in contact.items(): 
            return f"{k} | {v[0]} | {v[1]} | {v[2]}"


# ----- UPDATE -----

def update_contact() -> str:
    """Updates an existing contact"""

    # Search option
    search_option = collect_search_option(search_options_prompt, 1, 3)

    # Selected contact 
    contact_to_update = collect_contact_details(search_option) 

     # If a contact is selected 
    if contact_to_update:
        # Get current name, updated name and phone numbers 
        result = update_contact_details(contact_to_update)
    else:
        return 

    if result is None:
        # Exit 
        return 
    else:
        current_name, updated_contact_details = result

    # Read phonebook 
    phonebook = my_phonebook()

    # Non-empty phonebook

    if phonebook:
    
        # Delete old contact details 
        old_name = current_name
        phonebook.pop(current_name)
    
        # Insert updated contact details
        phonebook.update(updated_contact_details)
    
        # Save phonebook to file
        save_all_contacts(phonebook) 

        return old_name 


# ----- DELETE -----

def delete_contact() -> str:
    """Delete an existing contact"""

    # Search option
    search_option = collect_search_option(search_options_prompt, 1, 3)

    # Selected contact
    contact_to_delete = collect_contact_details(search_option)

    # Valid contact
    if contact_to_delete:
        # Read phonebook
        phonebook = my_phonebook()

        # Non-empty phonebook
        if phonebook:
            # Get contact name
            contact_name = [name for name in contact_to_delete][0]
            deleted_contact = contact_name

            # Delete contact
            phonebook.pop(contact_name)

            # Save phonebook to file 
            save_all_contacts(phonebook)

            return deleted_contact


# ----- PHONEBOOK ----- 

def my_phonebooks() -> dict[str, list[int | None]]:
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
 

# ----- GET A SINGLE CONTACT'S DETAILS -----

# FOR CONTACT SIGNUP 

def collect_signup_contact_details() -> tuple(str, dict[int | None]):
    """Collects contact name and phone number(s)"""
    # Input Aggregator

    # Contact name
    name = collect_contact_name()

    # Phone numbers
    phone_nums = collect_phone_numbers()

    return name, phone_nums


# TO UPDATE, SEARCH OR DELETE

def collect_contact_details(search_option: int | None) -> tuple[str, dict[str, list[int | None]]]:
    """Update existing contact details"""

    # search option -> None
    if search_option == None:
        return None

    # search option -> 1 (name)
    if search_option == 1:
        name = collect_name()
        contacts_by_name = get_contacts_by_name(name)
        selected_contact = choose_contact(contacts_by_name, search_query=name)

    # search option -> 2 (phone_number)
    if search_option == 2:

        # Get user input(number)
        phone_num = collect_phone_num()
        # Get list of contact(s) whose first 5 numbers are identical or list of one unique number
        contacts_by_phone_num = get_contacts_by_phone_num(phone_num)
        # User selects one contact to update
        selected_contact = choose_contact(contacts_by_phone_num, search_query=phone_num)

    # Work with selected_contact
    if selected_contact:
        return selected_contact 
    # User option not in range
    else:
        print("No contact was selected.")
        return 


# ----- GET CONTACTS BY NAME ----- 

def get_contacts_by_name(name: str | None) -> list[dict[str, list[int | None]]]:
    """Retrieve multiple contacts with almost identical names"""

    # Read phonebook
    phonebook = my_phonebook()

    # Non-empty phonebook
    if phonebook:
        # Identical names
        matching_names = []

        # For each name and list of phone numbers belonging to a single contact
        for k, v in phonebook.items():
            # Look for a match in every contact name
            if name in k:
                matching_names.append({k: v})

        return matching_names


# ----- GET CONTACTS BY PHONE NUMBER ----- 

def get_contacts_by_phone_num(phone_number: int | None) -> list[dict]:
    """Retrieve multiple contacts by phone number"""

    # Read phonebook
    phonebook = my_phonebook()

    # Non-empty phonebook
    if phonebook:

        # Identical phone nums
        matching_phone_nums = []

        # For each name and list of phone numbers belonging to a single contact
        for k, v in phonebook.items():
            # For num in that list
            for n in v:
                # Convert phone numbers and the search_query to strings when comparing
                if str(phone_number) in str(n):
                    matching_phone_nums.append({k: v})

        return matching_phone_nums


# ----- UPDATE A SINGLE CONTACT'S DETAILS -----

def update_contact_details(
    current_contact_details: dict[str, list[int | None]]
) -> tuple[str, dict[str, list[int | None]]]:
    """Return updated contact name and phone numbers"""

    # Create a copy of the current user details, update tht copy and return it 
    updated_contact_details = current_contact_details.copy()

    # Current name
    current_name = [k for k in updated_contact_details][0]
    # Current phone_nums
    current_phone_nums = [n for v in updated_contact_details.values() for n in v]

    # Collect new contact details
    name = collect_contact_name(mode="update")
    phone_nums = collect_phone_numbers()
 
    
  # Check for duplicate phone nums
    for num_index, num in phone_nums.items():
        num = is_duplicate(num)

        # If a number is a dupicate
        if isinstance(num, dict):
            duplicate_num = num["is_duplicate"]
            
            # if duplicate num is similar to a number belonging to the contact being updated
            if num in current_phone_nums:
                # Allow, don't error out
                break
            # Else
            else:
                # Set it to None
                phone_nums[num_index] = None

                # Alert user
                print(
                    f"\n{num_index}: 0{duplicate_num}, belongs to an existing contact.It won't be added"
            )

    # Update contact details
    if name:
        # Update name
        updated_contact_details[name] = updated_contact_details.pop(current_name, None)

        # Assign new phone numbers to variables
    phone1 = phone_nums["phone number 1"]
    phone2 = phone_nums["phone number 2"]
    phone3 = phone_nums["phone number 3"]

    # If the 1st number is updated
    if phone1:
        for k in updated_contact_details:
            updated_contact_details[k][0] = phone1
    # If the 2nd number is updated
    if phone2:
        for k in updated_contact_details:
            updated_contact_details[k][1] = phone2
    # If the 3rd number is updated
    if phone3:
        for k in updated_contact_details:
            updated_contact_details[k][2] = phone3
    return current_name, updated_contact_details



