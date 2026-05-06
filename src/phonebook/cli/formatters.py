from phonebook.core.constants import DEFAULT_COUNTRY_CODE


def prefix_country_code(phone_number: str) -> str:
    """Prefixes a country code to a phone number"""

    return DEFAULT_COUNTRY_CODE + phone_number[1:] 
