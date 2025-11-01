from read_database import read_database
from add_ticket import add_ticket
from search_ticket import search_ticket
from change_ticket import change_ticket
from delete_ticket import delete_ticket


def start_application():
    """Start the Ticket System Application."""
    # User defined function to read database file or open new file
    read_database()
    # While loop for main menu and print main menu
    while True:
        print("\nWelcome to Service Ticket System Application")
        print("\n1 Add a ticket")
        print("2 Search for a ticket")
        print("3 Print and change ticket")
        print("4 Delete ticket")
        print("5 Exit application")
        # Ask user for menu option
        option = input("\nPlease enter a number to select option: ")
        if option == "1":
            # User defined function to add ticket and save to file
            add_ticket()
        elif option == "2":
            # User defined function to search for ticket id
            search_ticket()
        elif option == "3":
            # User defined function to print and change ticket
            change_ticket()
        elif option == "4":
            # User defined function to delete ticket
            delete_ticket()
        elif option == "5":
            # Confirm exiting application
            print("\nExiting the application. Goodbye!\n")
            # Break out of while loop
            break
        # If other input than menu
        else:
            # Print error
            print("\nSorry, please try again...")
