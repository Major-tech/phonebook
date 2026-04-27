from phonebook.cli.menu import menu_options
from phonebook.services.formatters import prefix_zero


def display_menu() -> None:
    """Homepage"""

    print("\nMY PHONEBOOK\n")

    print("Enter 0 to exit\n")

    # List options
    for k, v in menu_options.items():
        print(f"{k}) {v.title()}")


def display_contacts(list_of_contacts) -> None:
    """Displays a list of contacts"""
    
    for i, contact in enumerate(list_of_contacts, start=1):
        for k, v in contact.items():
            print(
                f"\n({i})| Name: {k} | Phone number 1: {prefix_zero(v[0])} | Phone number 2: {prefix_zero(v[1])} | Phone number 3: {prefix_zero(v[2])}"
            )

