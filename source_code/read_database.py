from ticket_data import TicketData
tickets_list = []


def read_database():
    """Open database.txt file and read. If file not found,
       create file."""
    # Cater for file not found error
    try:
        # Open txt file for reading
        with open("database.txt", "r", encoding="utf-8-sig") as file:
            # Iterate through lines in file
            for line in file:
                # Remove \n
                data = line.strip("\n")
                # Split string into list
                data1 = data.split(",")
                # Create object from list
                tickets = [
                    TicketData(data1[0], data1[1], data1[2], data1[3],
                               data1[4], data1[5])]
                # Add object to list
                tickets_list.extend(tickets)
    # If file not found
    except FileNotFoundError:
        # Print message
        print("\nDatabase file does not exist. New database file created.")
        # Add sample data to object
        tickets = [
            TicketData(1, "2025-01-01", "John", "John@gmail.com", "Faulty",
                       "Decoder faulty")]
        # Add object to list
        tickets_list.extend(tickets)
        # Open new txt file for writing
        with open("database.txt", "w", encoding="utf-8-sig") as file:
            # Iterate throught list
            for index, value in enumerate(tickets_list):
                # Write list object attibutes to file
                file.write(
                    f"{value.ticket_id},{value.ticket_date},")
                file.write(
                    f"{value.ticket_name},{value.ticket_email},")
                file.write(
                    f"{value.ticket_heading},{value.ticket_query}\n")
