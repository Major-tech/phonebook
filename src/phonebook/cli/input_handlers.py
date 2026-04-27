from phonebook.domain.exceptions import TooManyInvalidAttemptsError
from phonebook.validators.input_validator import is_valid_int_option
from phonebook.cli.display import display_contacts


# VARIABLES
search_options_prompt = """
SEARCH OPTIONS
1) Search by name
2) Search by phone

Enter option: """

# ----- GET USER OPTION -----

def get_int_option(prompt) -> int:
    """Ensures a user selects an option wnd it's an int"""

    for i in range(3):
        try:
            option = int(input(prompt))
        except ValueError:
            if i < 2:
                print("Please enter a valid number")
            else:
                raise TooManyInvalidAttemptsError()
        else:
            break

    return option


def collect_search_option(prompt: str, start: int, end: int) -> int | None:
    """Collects a user's search option"""

    # User search option
    search_option = get_int_option(prompt)
    # Validate option
    search_option = is_valid_int_option(search_option, start, end)

    return search_option


# ----- GET PHONE NUMBER ----- 

# FOR REGISTRATION / UPDATE 
def prompt_phone_number(position: int = None) -> int | None:
    """Prompts for a contact's phone numbers"""

    # Convert number to a string
    number = str(position)

    for i in range(3):
        try:
            phone = input(f"\nPhone number {position}\n(Press Enter to skip): ")
            # If user skips adding the phone number
            if not phone:
                return None
            # If a value is given ,convert it to an int
            elif phone:
                phone = int(phone)
                return phone

        except ValueError:
            if i < 2:
                print("Please enter a number")
            else:
                # If maximum attempts are reached
                raise TooManyInvalidAttemptsError()


def collect_phone_numbers(count: int = 3) -> dict:
    """Collect phone number"""

    phone_nums = {}

    # Phone numbers
    print("\n[You can store upto 3 different phone numbers per contact]")

    for i in range(1, count + 1):
        # Prompt user for phone numbers
        phone = prompt_phone_number(i)
        phone_nums[f"phone number {i}"] = phone

    return phone_nums


# TO UPDATE, SEARCH OR DELETE 

def collect_phone_num() -> int | None:
    """Prompts a user for a phone number"""

    for i in range(3):
        try:
            phone = input(
                    "\n\nNB: THE FIRST NUMBER SHOULD BE '7' NOT '0'.\nEnter the complete number or any length of numbers belonging to any phone number of the contact  you want.\n (Example: '72345' or '58'): "
                )

            # Number validation
            if not phone:
                print("\nYou did not type anything")
                continue
    
            if phone:
                  phone = int(phone)
                
            break
        
        except ValueError:
            if i < 2:
                printr("\nPlease enter valid numbers")
            else:
                break 

    return phone


# ----- GET CONTACT NAME ----- 

# FOR REGISTRATION 

def collect_contact_name(mode="add", count=3) -> str | None:
    """Return a contact's name"""

    for i in range(count):
        # Contact name

        # In uodate mode, user can skip name
        if mode == "update":
            print("\n[Press Enter to leave name unchanged]")

        name = input("Enter contact name: ")

        # No contact name given
        if not name:
            # ADD
            if mode == "add":
                if i < 3:
                    print("This is required")
                    continue
            # UPDATE
            else:
                return None
                
        return name


# TO UPDATE, SEARCH OR DELETE
def collect_name() -> str | None:
    """Prompts a user for a contact name"""

    for i in range(3):
        name = input(
            "\nEnter the full name or any number of letters matching the contact name you want: "
        )
        # Name validation
        if not name:
            print("\nYou did not type anything")
            continue

        break 

    if not name:
        return None 

    return name


# ----- SELECT CONTACT ----- 

def choose_contact(
    contacts: list[dict[str, list]], search_query: str | int = None
) -> dict[str, list[int | None]]:
    """Contact selection"""

    # Empty list
    if not contacts:
        print(f"\nNo contacts matching {search_query} were found")
        return contacts 

    # Search option -> phone number
    if isinstance(search_query, int):
        print(f"\nContacts matching: {search_query}\n")

    # Search option -> name
    if isinstance(search_query, str):
        print(f"\nContacts matching: '{search_query}'\n")
    
    # List contacts 
    display_contacts(contacts)
    
    # Get user's selection
    user_option = collect_search_option("\nEnter corresponding number of the contact to update:  ",  1, len(contacts) + 1) 
    
    # If user_option is in range
    if user_option:
        contact = contacts[user_option - 1]

        return contact

