from read_database import tickets_list
from add_ticket import valid_email


def print_data(value):
    """Print object fields."""
    print(f"\nTicket id: {value.ticket_id}")
    print(f"Ticket date: {value.ticket_date}")
    print(f"Customer name: {value.ticket_name}")
    print(f"Customer email: {value.ticket_email}")
    print(f"Ticket heading: {value.ticket_heading}")
    print(f"Ticket query: {value.ticket_query}")
    print("________________________________________________________")


def change_ticket():
    """Change ticket and save to file"""
    # Confirm selection
    print("\nPrint and change ticket has been selected.")
    # Iterate through object list and print all objects and attributes
    for index, value in enumerate(tickets_list):
        # User fefined function to print object fields
        print_data(value)
    # While loop for error check
    while True:
        # Ask user for ticket number to change
        change_id = str(
            input("\nPlease enter the ticket number to change: "))
        if change_id != "":
            # Get out of while loop
            break
        # If error print error
        else:
            print("\nSorry, cannot enter blank input...")
    # Initialise to zero
    ticket_found1 = 0
    # Iterate throught object list
    for index, value in enumerate(tickets_list):
        # Search for change id and print object attributes
        if change_id == str(value.ticket_id):
            # User fefined function to print object fields
            print_data(value)
            # Set id found
            ticket_found1 = 1
        # If id found
        if ticket_found1 == 1:
            while True:
                # Ask user if they want to update name, email, heading
                # or query
                update_option = input(
                    "\nDo you want to update 1 customer name, 2 customer"
                    " email, 3 ticket heading or 4 ticket query: ")
                if update_option != "":
                    if update_option == "1":
                        break
                    elif update_option == "2":
                        break
                    elif update_option == "3":
                        break
                    elif update_option == "4":
                        break
                    else:
                        print("\nSorry, invalid option...")
                else:
                    print("\nSorry, cannot enter blank option...")
            # If update name
            if update_option == "1":
                # While loop for error check
                while True:
                    # Ask user for new name
                    update_name = input(
                        "Please enter new customer name: ")
                    # Check if input blank
                    if update_name != "":
                        # Get out of while loop
                        break
                    # If blank print error
                    else:
                        print("\nSorry, cannot enter blank name...\n")
                # Iterate throught object list
                for index, value in enumerate(tickets_list):
                    # Search for change id
                    if change_id == str(value.ticket_id):
                        # Update name in object
                        value.ticket_name = update_name
            # If update email
            elif update_option == "2":
                # While loop for error check
                while True:
                    # Ask user for new email
                    update_email = input(
                        "Please enter new customer email: ")
                    # Check email format
                    email_valid = valid_email(update_email)
                    # Check if input blank and email valid
                    if update_email != "" and email_valid is True:
                        # Get out of while loop
                        break
                    # If error print error
                    else:
                        print(
                            "\nSorry, cannot enter blank name or"
                            " invalid email address...\n")
                # Iterate through object list
                for index, value in enumerate(tickets_list):
                    # Search for change id
                    if change_id == str(value.ticket_id):
                        # Update email in object
                        value.ticket_email = update_email
            # If update heading
            elif update_option == "3":
                # While loop for error check
                while True:
                    # Ask user for new heading
                    update_heading = input(
                        "Please enter new ticket heading: ")
                    # Check if input blank
                    if update_heading != "":
                        # Get out of while loop
                        break
                    # If error print error
                    else:
                        print(
                            "\nSorry, cannot enter blank heading...\n")
                # Iterate throught object list
                for index, value in enumerate(tickets_list):
                    # Search for change id
                    if change_id == str(value.ticket_id):
                        # Update heading in object
                        value.ticket_heading = update_heading
            # If update query
            elif update_option == "4":
                # While loop for error check
                while True:
                    # Ask user for new query
                    update_query = input(
                        "Please enter new ticket query: ")
                    # Check if input blank
                    if update_query != "":
                        # Get out of while loop
                        break
                    # If error print error
                    else:
                        print("\nSorry, cannot enter blank query...\n")
                # Iterate throught object list
                for index, value in enumerate(tickets_list):
                    # Search for change id
                    if change_id == str(value.ticket_id):
                        # Update query in object
                        value.ticket_query = update_query
            # Open txt file with writing
            with open("database.txt", "w", encoding="utf-8-sig"
                      ) as file:
                # Iterate through object list
                for index, value in enumerate(tickets_list):
                    # Write objects attributes to file
                    file.write(
                        f"{value.ticket_id},{value.ticket_date},")
                    file.write(
                        f"{value.ticket_name},{value.ticket_email},")
                    file.write(
                        f"{value.ticket_heading},")
                    file.write(
                        f"{value.ticket_query}\n")
            # Confirm update
            print("\nTicket updated.")
        # If id not found
    if ticket_found1 == 0:
        # Print error
        print("\nTicket not found.")
