from phonebook.services.contact_service import collect_signup_contact_details, add_contact
from phonebook.validators.phone_validator import is_duplicate


# ----- ADD ----- 

def register_contact() -> str:
    """Orchestrate saving contacts to phonebook, pass them from input, service upto the DB layer"""

    # Get contact details
    name, phone = collect_signup_contact_details()

    # Check for duplicates
    for k, v in phone.items():
        v = is_duplicate(v)

        # If a number is a dupicate
        if isinstance(v, dict):
            duplicate = v["is_duplicate"]

            # Set it to None
            phone[k] = None

            # Alert user
            print(
                f"\n{k}: 0{duplicate}, belongs to an existing contact.It won't be added"
            )
    # Check if any of the numbers are similar

    # Register
    return add_contact(name, phone)


