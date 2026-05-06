from phonebook.cli.menu import menu_options


def display_menu() -> None:
    """Homepage"""

    print("\nMY PHONEBOOK\n")

    # List options
    for k, v in menu_options.items():
        print(f"{k}) {v.title()}")


def display_contacts(list_of_contacts: list[dict[str, dict[str, str]]]) -> None:
    """Displays a list of contacts"""

    for i, contact in enumerate(list_of_contacts, start=1):
        for name, phone_type in contact.items():
            mobile = phone_type.get("mobile", "")
            work = phone_type.get("work", "")
            home = phone_type.get("home", "")

            print(
                f"{i} | Name: {name} | Mobile: {mobile} | Work: {work} | Home: {home}"
            )

