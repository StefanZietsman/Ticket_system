from read_database import read_database
from add_ticket import add_ticket
from search_ticket import search_ticket
from change_ticket import change_ticket
from delete_ticket import delete_ticket
from datetime import date
from unittest import mock
import unittest
import os


class Test_ticket_system(unittest.TestCase):
    """Testing ticket system modular functions"""

    # Supply inputs for user inputs
    @mock.patch("builtins.input", side_effect=["Ben", "ben@gmail.com",
                                               "Laptop", "Need new laptop"])
    def test_add_ticket(self, mock_input):
        """Test add ticket to object list and file"""
        try:
            # Delete 'database.txt' for testing program only
            os.remove("database.txt")
        except FileNotFoundError:
            pass
        # User defined module function
        read_database()
        # User defined module function
        add_ticket()
        # Get data from file
        file_list1 = read_data_file()
        # Read data in index 1
        check_id = file_list1[1][0]
        check_date = file_list1[1][1]
        check_name = file_list1[1][2]
        check_email = file_list1[1][3]
        check_heading = file_list1[1][4]
        check_query = file_list1[1][5]
        # Test add_ticket input against output
        self.assertEqual(check_id, "2", "Id wrong")
        self.assertEqual(check_date, str(date.today()), "Date wrong")
        self.assertEqual(check_name, "Ben", "Name wrong")
        self.assertEqual(check_email, "ben@gmail.com", "Email wrong")
        self.assertEqual(check_heading, "Laptop", "Heading wrong")
        self.assertEqual(check_query, "Need new laptop", "Query wrong")

    # Supply inputs for user inputs
    @mock.patch("builtins.input", side_effect=["1"])
    def test_search_ticket(self, mock_input):
        """Test search for ticket"""
        # Get ticket found conrifmation from user defined module
        # function
        confirm_ticket_found = search_ticket()
        # Test search_ticket input against output
        self.assertEqual(confirm_ticket_found, 1, "Ticket error")

    # Supply inputs for user inputs
    @mock.patch("builtins.input", side_effect=["2", "1", "Sue"])
    def test_change_ticket(self, mock_input):
        """Test change ticket name in object list and save to file"""
        # User defined module function
        change_ticket()
        # Get data from file user defined function
        file_list2 = read_data_file()
        # Get name from index 1
        check_name = file_list2[1][2]
        # Test change_ticket input against output
        self.assertEqual(check_name, "Sue", "Name wrong")

    # Supply inputs for user inputs
    @mock.patch("builtins.input", side_effect=["2", "y"])
    def test_delete_ticket(self, mock_input):
        """Test delete ticket name in object list and save to file"""
        # User defined module function
        delete_ticket()
        # Get data from file user defined function
        file_list3 = read_data_file()
        # Get length of list
        list_length = len(file_list3)
        # Test delete_ticket input aganst output
        self.assertEqual(list_length, 1, "Length wrong")


def read_data_file():
    """Read data from file"""
    # Initialise empty list
    file_list = []
    # Open txt file for reading
    with open("database.txt", "r", encoding="utf-8-sig") as file:
        # Iterate through lines in file
        for line in file:
            # Remove \n
            data = line.strip("\n")
            # Split string into list
            data1 = data.split(",")
            # Add to list
            file_list.append(data1)
    # Return list
    return file_list


if __name__ == '__main__':
    unittest.main()
