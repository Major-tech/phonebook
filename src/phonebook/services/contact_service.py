from phonebook.repository.contact_repository import append_contact, save_all_contacts, load_contacts
from phonebook.domain.exceptions import ContactNotFoundError
from phonebook.cli.input_handlers import search_options_prompt, get_int_option, collect_contact_name, collect_phone_numbers, collect_name, collect_phone_num, choose_contact


# ----- ADD ----- 

def add_contact(contact: dict[str | None, dict[str, str]]) -> str | None:
    """Save contact name and numbers to the phonebook"""

    # If name and phone numbers are given
    if contact:

        # Save to file
        new_contact = append_contact(contact)
        
        if new_contact:
            name = [n for n in new_contact][0]

            return name


# ----- SEARCH -----

def search_contact() -> None:
    """Lookup an existing contact"""

    # Search option
    search_option = get_int_option(search_options_prompt, 1, 3)

    # Selected contact
    contact = collect_contact_details(search_option)

    # Display selected contact
    print("\nSELECTED CONTACT")

    for name, numbers in contact.items():
        print(f"Name: {name}")

        for phone_type, number in numbers.items():
            print(f"{phone_type.capitalize()}: {number}")


# ----- UPDATE -----

def update_contact() -> str | None:
    """Updates an existing contact"""

    # Search option
    search_option = get_int_option(search_options_prompt, 1, 3)

    # Selected contact 
    contact_to_update = collect_contact_details(search_option) 
   
    # Update contact details
    result = update_contact_details(contact_to_update)

    if result is None:
        # Exit 
        return 
    else:
        # Get current name, and updated name and phone numbers
        old_name, updated_contact_details = result

    # Read phonebook 
    phonebook = load_contacts()

    # Non-empty phonebook
    if phonebook:
    
        # Delete old contact details 
        #old_name = current_name
        phonebook["contacts"].pop(old_name)
        print(updated_contact_details) 
        # Insert updated contact details
        phonebook["contacts"].update(updated_contact_details)
    
        # Save phonebook to file
        save_all_contacts(phonebook) 

        return old_name 


# ----- DELETE -----

def delete_contact() -> str | None:
    """Delete an existing contact"""

    # Search option
    search_option = get_int_option(search_options_prompt, 1, 3)

    # Selected contact
    contact_to_delete = collect_contact_details(search_option)

    # Read phonebook
    phonebook = load_contacts()

    # Non-empty phonebook
    if phonebook:
        # Get contact name
        contact_name = [name for name in contact_to_delete][0]
        deleted_contact = contact_name

        # Delete contacta
        phonebook["contacts"].pop(contact_name) 

        # Save phonebook to file 
        save_all_contacts(phonebook)

        return deleted_contact


# ----- GET A SINGLE CONTACT'S DETAILS -----

# FOR CONTACT SIGNUP 

def collect_signup_contact_details() -> tuple[str | None, dict[str, str]]:
    """Collects contact name and phone number(s)"""
    # Input Aggregator

    # Contact name
    name = collect_contact_name()

    # Phone numbers
    phone_nums = collect_phone_numbers()

    return name, phone_nums


# TO UPDATE, SEARCH OR DELETE

def collect_contact_details(search_option: int | None) -> dict[str, dict[str, str]]: 
    """Update existing contact details"""

    # search option -> 1 (name)
    if search_option == 1:
        name = collect_name() 
    
        contacts_by_name = get_contacts_by_name(name)
        selected_contact = choose_contact(contacts_by_name, search_query=name)
        

    # search option -> 2 (phone_number)
    elif search_option == 2:

        # Get user input(number)
        phone_num = collect_phone_num()

        # Get list of contact(s) whose numbers are identical
        contacts_by_phone_num = get_contacts_by_phone_num(phone_num)
        # User selects one contact 
        selected_contact = choose_contact(contacts_by_phone_num, search_query=phone_num)

    # Work with selected_contact
    return selected_contact 
         

# ----- GET CONTACTS BY NAME ----- 

def get_contacts_by_name(name_query: str) -> list[dict[str, dict[str, str]]]:
    """Retrieve multiple contacts with almost identical names"""

    # Read phonebook
    phonebook = load_contacts()

    # Identical names
    matching_names = []

    # Non-empty phonebook
    if phonebook:

        # Look for a match in each saved contact's name
        for name, numbers in phonebook["contacts"].items():
            if name_query in name:
                matching_names.append({name: numbers})

    # Raise error if there were no matches found
    if not matching_names:
        raise ContactNotFoundError(name_query)

    return matching_names


# ----- GET CONTACTS BY PHONE NUMBER ----- 

def get_contacts_by_phone_num(phone_number_query: str) -> list[dict[str, dict[str, str]]]:
    """Retrieve multiple contacts by phone number"""

    # Read phonebook
    phonebook = load_contacts()
 
    # Identical phone nums
    matching_phone_nums = []

    # Non-empty phonebook
    if phonebook:

        # Check if the phone number snippet is in any saved phone numbers 
        for name, numbers in phonebook["contacts"].items():
            for number in numbers.values():
                if phone_number_query in number:
                    matching_phone_nums.append({name: numbers})

    # Raise error if there were no matches foun      d
    if not matching_phone_nums:
        raise ContactNotFoundError(phone_number_query)

    return matching_phone_nums


# ----- UPDATE A SINGLE CONTACT'S DETAILS -----

def update_contact_details(
    current_contact_details: dict[str, dict[str, str]]
) -> tuple[str, dict[str, dict[str, str]]]:
    """Return updated contact name and phone numbers"""

    # Create a copy of the current user details, update tht copy and return it 
    updated_contact_details = current_contact_details.copy()

    # Current name
    current_name = [name for name in updated_contact_details][0]

    # Current phone_nums
    current_phone_nums: dict[str, str] = {
    phone_type: num for phone in updated_contact_details.values() for phone_type, num in phone.items()
}

    # Collect new contact details
    updated_name = collect_contact_name(mode="update")
    updated_phone_nums = collect_phone_numbers(mode="update")
    
    # Update contact details
    print(updated_contact_details)

    # Update phone numbers
    for phone_type, num in current_phone_nums.items():
        if phone_type not in updated_phone_nums.keys():
            updated_phone_nums[phone_type] = num
    # Update contact 
    updated_contact_details[current_name] = updated_phone_nums

    # Update name
    if updated_name:
        updated_contact_details.pop(current_name) # remove old name
        updated_contact_details.update({updated_name: updated_phone_nums}) # update name 

    return current_name, updated_contact_details


