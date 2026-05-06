from phonebook.paths.data import get_data_dir
from pathlib import Path


CONTACTS_FILE_NAME = "contacts.json"


def get_contacts_file() -> Path:
    """
    Get the full path to he contacts JSON file
    """

    return get_data_dir() / CONTACTS_FILE_NAME


