from phonebook.services.auth_service import register_contact
from phonebook.services.contact_service import search_contact, update_contact, delete_contact

    
def dispatch(option: int):
    """Dispatch commands"""

    # EXIT
    if option == 0:
        return "exit"
    
    # ADD
    elif option == 1:
        added = register_contact()
        # Saved contact
        if added:
            print(f"\n{added} saved successfully!")
                
    # SEARCH
    elif option == 2:
        contact = search_contact()
        if contact:
            print(f"\nSELECTED CONTACT: {contact}")
    

    # UPDATE 
    elif option == 3:
        updated = update_contact() 
        if updated:
            print(f"\n{updated} was updated successfully!")
                       
    # DELETE 
    elif option == 4:
        deleted = delete_contact()
        if deleted:
            print(f"\n{deleted} was deleted successfully!")
                           
    # Invalid option
    else:
        print("Invalid option")
      
