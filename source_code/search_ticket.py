from read_database import tickets_list


def search_ticket():
    """Search for a ticket"""
    # Confirm selection
    print("\nSearch for a ticket has been selected.")
    # Ask user for id to search
    search_id = str(input("\nPlease enter ticket id to search: "))
    # Initialise to zero
    ticket_found = 0
    # Iterate throught object list
    for index, value in enumerate(tickets_list):
        # Search for ticket id
        if search_id == str(value.ticket_id):
            # Print object attributes
            print(f"\nTicket id: {value.ticket_id}")
            print(f"Ticket date: {value.ticket_date}")
            print(f"Customer name: {value.ticket_name}")
            print(f"Customer email: {value.ticket_email}")
            print(f"Ticket heading: {value.ticket_heading}")
            print(f"Ticket query: {value.ticket_query}")
            print("________________________________________________________")
            # Set id found
            ticket_found = 1
    # If tiket not found
    if ticket_found == 0:
        # Print error
        print("\nTicket not found.")
    return ticket_found
