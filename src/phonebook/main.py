from phonebook.cli.display import display_menu
from phonebook.cli.input_handlers import collect_search_option
from phonebook.cli.menu import menu_options 
from phonebook.cli.dispatcher import dispatch
from phonebook.domain.exceptions import AppError


def main() -> None:
    """Orchestrates the program"""

    while True:
        try:
            display_menu() 
            user_option = collect_search_option("\nEnter option: ", 0, len(menu_options) + 1) 
            
            result = dispatch(user_option) 
            if result == "exit":
                break 
                
        except AppError as e:
            print(e)
        except ValueError as e:
            print(e) 
        #except Exception as e:
           # print(f"Unexpected error: {e}")

    

if __name__ == "__main__":
    main()
