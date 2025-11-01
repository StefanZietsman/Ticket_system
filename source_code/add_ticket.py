from datetime import date
from ticket_data import TicketData
from read_database import tickets_list
import re


def valid_email(input):
    return bool(
        re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                 input))


def add_ticket():
    """Add ticket and save to file"""
    # Confirm selection
    print("\nAdd a ticket has been selected.")
    # Get length of object list
    length_objects_list = len(tickets_list)
    # Select data of last object
    selected_object = tickets_list[length_objects_list - 1]
    # Set last object ticket_id + 1
    ticket_id = int(selected_object.ticket_id) + 1
    # Get todays date
    ticket_date = date.today()
    # While loop for error check
    while True:
        # Ask user for name
        ticket_name = input("\nPlease enter your name: ")
        # Check if input blank
        if ticket_name != "":
            # Get out of while loop
            break
        # If blank print error
        else:
            print("\nSorry, cannot enter blank name...")
    # While loop for error check
    while True:
        # Ask user for email
        ticket_email = input("Please enter your email address: ")
        # Check email format
        email_valid = valid_email(ticket_email)
        # Check if input blank and email valid
        if ticket_email != "" and email_valid is True:
            # Get out of while loop
            break
        # If error print error
        else:
            print(
                "\nSorry, cannot enter blank name or invalid email address..."
                "\n")
    # While loop for error check
    while True:
        # Ask user for ticket heading
        ticket_heading = input("Please enter query heading: ")
        # Check if input blank
        if ticket_heading != "":
            # Get out of while loop
            break
        # If error print error
        else:
            print("\nSorry, cannot enter blank heading...\n")
    # While loop for error check
    while True:
        # Ask user for ticket query
        ticket_query = input("Please enter you main query: ")
        # Check if input blank
        if ticket_query != "":
            # Get out of while loop
            break
        # If error print error
        else:
            print("\nSorry, cannot enter blank query...\n")
    # Create new object
    tickets_add = [
        TicketData(
            ticket_id,
            ticket_date,
            ticket_name,
            ticket_email,
            ticket_heading,
            ticket_query,
        )
    ]
    # Add object to list
    tickets_list.extend(tickets_add)
    # Open txt file for writing
    with open("database.txt", "w", encoding="utf-8-sig") as file:
        # Iterate throught list
        for index, value in enumerate(tickets_list):
            # Write list object attibutes to file
            file.write(
                f"{value.ticket_id},{value.ticket_date},{value.ticket_name},")
            file.write(
                f"{value.ticket_email},{value.ticket_heading},")
            file.write(f"{value.ticket_query}\n")
    # Confirm addition
    print("\nTicket added.")
