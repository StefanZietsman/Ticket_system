class TicketData:
    """Ticket object with attributes"""

    def __init__(
        self,
        ticket_id,
        ticket_date,
        ticket_name,
        ticket_email,
        ticket_heading,
        ticket_query,
    ):
        # Initialise ticket attributes
        self.ticket_id = ticket_id
        self.ticket_date = ticket_date
        self.ticket_name = ticket_name
        self.ticket_email = ticket_email
        self.ticket_heading = ticket_heading
        self.ticket_query = ticket_query
