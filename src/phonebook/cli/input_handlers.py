from phonebook.domain.exceptions import InvalidSelectionError, MissingContactNameError, MissingPhoneNumberError, PhoneNumberQueryRequiredError, NameQueryRequiredError, InvalidContactSelectionError
from phonebook.validators.input_validator import is_valid_int_option
from phonebook.validators.phone_validator import is_duplicate_number, is_valid_phone_format, is_duplicate_number
from phonebook.cli.display import display_contacts
from phonebook.core.constants import PHONE_NUMBER_TYPES 
from phonebook.cli.formatters import prefix_country_code


# VARIABLES
search_options_prompt = """
SEARCH OPTIONS
1) Search by name
2) Search by phone

Enter option: """
 
# ----- GET USER OPTION -----

def parse_int(number: str) -> int:
    """Returns an integer"""

    try:
        return int(number)
    except ValueError:
        raise InvalidSelectionError("Invalid selection format")


def get_int_option(prompt: str, start: int, end: int) -> int | None:
    """Ensures a user selects an option wnd it's an int"""

    for _ in range(3):
        try:
            option = input(prompt)

            # Convert to integer
            option = parse_int(option)

            #  Check if option is in range
            option = is_valid_int_option(option, start, end)

            return option     

        except InvalidSelectionError as e:
            if _ < 2:
                print(e)
            else:
                raise 


# FOR REGISTRATION / UPDATE 

def get_validated_phone_number(number_type: str, count: int = 3) -> str | None:
    """Prompt for a phone number, validate its format and uniqueness, and return a verified value or raise an error."""

    for _ in range(count):
        phone = input(f"\n(Press Enter to skip)\n{number_type.capitalize()}: ")
        
        # If user skips adding the phone number
        if not phone:
            break

        # Validate phone number format
        if is_valid_phone_format(phone):
            
            # Add country code
            phone = prefix_country_code(phone)

            # Check for duplicates
            duplicate = is_duplicate_number(phone)
            # Duplicate found
            if duplicate:
                name, number = duplicate
                print("DUPLICATE FOUND:")
                print(f"Name: {name}")
                print(f"Phone: {number}")
                continue 
            else:
                return phone 
        else:
            print("Please enter a valid phone number")
            continue
            

def collect_phone_numbers(mode="add") -> dict[str, str]:
    """Collect phone numbers"""

    phone_nums = {} 
    
    # Phone numbers
    print("\n[You can store upto 3 different phone numbers per contact.At least one phone number is needed]")

    # Get and store numbers 
    for phone_type in PHONE_NUMBER_TYPES:
        phone = get_validated_phone_number(phone_type) 
        if phone:
            phone_nums[phone_type] = phone

    # Not a single phone number is given and mode == "add" 
    if not len(phone_nums.values()) and mode == "add":
        raise MissingPhoneNumberError("\nCannot create contact: at least one phone number (e.g., mobile, work, or home) is required.") 

    return phone_nums


# TO SEARCH, UPDATE OR DELETE 

def collect_phone_num(count : int = 3) -> str:
    """Prompts a user for a phone number"""

    for _ in range(count):
    
        phone = input(
                    "\nEnter the complete number or any length of numbers belonging to any phone number of the contact  you want.\n (Example: '72345' or '58'): "
                )

        # Phone number query is given
        if phone:

            # If phone has numerics or "+"
            if phone.isdigit():
                return phone
            elif "+" in phone and len(phone) == 1:
                return phone
            elif phone[0] == "+" and phone[1:].isdigit():
                return phone

            # Reject non-numerical values 
            else:
                print("\nPlease write a valid phone number query")

        # Blank field 
        if not phone:
            print("\nYou did not type anything")
    
    raise PhoneNumberQueryRequiredError("\nSearch failed: a phone number query is required to look up a contact.")
        

# ----- GET CONTACT NAME ----- 

# FOR REGISTRATION 

def collect_contact_name(mode: str ="add", count: int =3) -> str | None:
    """Return a contact's name"""

    for _ in range(count):
        # Contact name

        # In uodate mode, user can skip name
        if mode == "update":
            print("\n[Press Enter to leave name unchanged]")

        name = input("Enter contact name: ")

        # Name is given
        if name:
            return name

        # No contact name given
        if not name:

            # mode == ADD
            if mode == "add":
                if _ < (count - 1):
                    print("This is required")

            # mode == UPDATE
            else:
                return None
                
    # Stop if no name is given during sign up
    raise MissingContactNameError("\nContact name is required but was not provided after retries")


# TO SEARCH, UPDATE OR DELETE

def collect_name() -> str:
    """Prompts a user for a contact name"""

    for _ in range(3):
        name = input(
            "\nEnter the full name or any number of letters matching the contact name you want: "
        ) 

        # Name is given 
        if name:
            return name 

        # Name validation
        if not name:
            print("\nYou did not type anything")

    # Stop if no name is given
    raise NameQueryRequiredError("\nSearch failed: a contact name is required to look up a contact.")


# ----- SELECT CONTACT ----- 

def choose_contact(
        contacts: list[dict[str, dict[str, str]]] , search_query: str) -> dict[str, dict[str,str]]:
    """Contact selection"""

    # Search option -> phone number
    if search_query.isdigit() or "+" in search_query:
        print("\nSEARCH BY PHONE NUMBER\n"      )

    # Search option -> name
    else:
        print("\nSEARCH BY NAME")
    
    # Heading 
    print(f"\nContacts matching: '{search_query}'\n")
    
    # List contacts 
    display_contacts(contacts)
    
    try:
        # Get user's selection and check whether ut is in range
        user_option = get_int_option("\nEnter corresponding number of the contact you want:  ",  1, len(contacts) + 1) 

    except InvalidSelectionError as e:
        raise InvalidContactSelectionError("\nContact selection failed - out of range") from e

    # User option is in range
    if user_option:
        contact = contacts[user_option - 1]

    return contact 
