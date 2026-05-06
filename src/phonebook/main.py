from phonebook.cli.display import display_menu
from phonebook.cli.input_handlers import get_int_option 
from phonebook.cli.menu import menu_options 
from phonebook.cli.dispatcher import dispatch
from phonebook.domain.exceptions import AppError, InvalidSelectionError, InvalidMenuSelectionError


def run_cli() -> None:
    """Orchestrates the program"""

    while True:
        try:
            display_menu()

            # Validate user menu selection 
            try:
                user_option = get_int_option("\nEnter option: ", 0, len(menu_options) + 1) 
            except InvalidSelectionError:
                raise InvalidMenuSelectionError("menu selection failed - out of range") 

            # If option is in range, dispatch cmd
            if user_option == 0 or user_option:
                result = dispatch(user_option) 
                if result == "exit":
                    break 
                
        except AppError as e:
            print(e)
        except ValueError as e:
            print(e) 
        except Exception as e:
            print(f"Unexpected error: {e}")


def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()

