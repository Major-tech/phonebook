from phonebook.services.contact_service import collect_signup_contact_details, add_contact


# ----- ADD ----- 

def register_contact() -> str | None:
    """Orchestrate saving contacts to phonebook, pass them from input, service upto the DB layer"""

    # Get contact details
    name, phone_numbers = collect_signup_contact_details()

    contact = {name: phone_numbers}

    # Register
    return add_contact(contact)


