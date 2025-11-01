from read_database import tickets_list


def delete_ticket():
    """Delete ticket and save to file"""
    # Confirm selection
    print("\nDelete ticket has been selected.")
    while True:
        try:
            # Ask user for ticket id to delete
            delete_id = str(input("\nPlease enter ticket id to delete: "))
            if delete_id != "":
                # Check if input interger
                if 1 <= int(delete_id) <= 1000:
                    # Initialise to zero
                    ticket_found2 = 0
                    # Iterate throught object list
                    for index, value in enumerate(tickets_list):
                        # Search for delete id and print attributes
                        if delete_id == str(value.ticket_id):
                            print(f"\nTicket id: {value.ticket_id}")
                            print(f"Ticket date: {value.ticket_date}")
                            print(f"Customer name: {value.ticket_name}")
                            print(f"Customer email: {value.ticket_email}")
                            print(f"Ticket heading: {value.ticket_heading}")
                            print(f"Ticket query: {value.ticket_query}")
                            print(
                                "_____________________________________"
                                "___________________")
                            # Set id found
                            ticket_found2 = 1
                    # It id found
                    if ticket_found2 == 1:
                        # ASk user for delete confirmation
                        confirm_delete = input(
                            "\nAre you sure you want to delete ticket"
                            " (y or n): ")
                        # If lowercase y
                        if confirm_delete.lower() == "y":
                            # Iterate throught object list
                            for index, value in enumerate(tickets_list):
                                # Search for deleted id
                                if delete_id == str(value.ticket_id):
                                    # Remove object index from object
                                    # list
                                    tickets_list.remove(tickets_list[index])
                            # Open txt file for writing
                            with open("database.txt", "w", encoding="utf-8-sig"
                                      ) as file:
                                # Iterate throught object list
                                for index, value in enumerate(tickets_list):
                                    # Write objects attributes to file
                                    file.write(
                                        f"{value.ticket_id},")
                                    file.write(
                                        f"{value.ticket_date},")
                                    file.write(
                                        f"{value.ticket_name},")
                                    file.write(
                                        f"{value.ticket_email},")
                                    file.write(
                                        f"{value.ticket_heading},")
                                    file.write(
                                        f"{value.ticket_query}\n")
                            # Confirm deletion
                            print("\nTicket deleted.")
                            break
                    # If id not found
                    if ticket_found2 == 0:
                        # Print error
                        print("\nTicket not found.")
            else:
                print("\nSorry, cannot enter blank input...")
        except ValueError:
            print("\nSorry, please enter only numbers...")
