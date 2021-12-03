"""This module provides Ticket Viewer CLI"""

import sys
import re
from typing import List, Dict, Optional

from ticket_viewer import STATUS_CODE_MESSAGE
from ticket_viewer.util import *

class CLIApp():
  """
  A class for receiving user's inputs and
  displaying results fetched from Zendesk API
  """
  
  def __init__(self) -> None:
    self.ticket_viewer = get_ticket_viewer() # To connect to Zendesk API
    self.prev_link = "" # To access prev page of tickets if >25 tickets are returned
    self.next_link = "" # To access next page of tickets if >25 tickets are returned
    self.is_page_through = False # If the user is paging through tickets
    self.page_through_options = ["", ""] # Where there might be more tickets to see

  def print_main_menu(self) -> None:
    """
    Show the main menu containing main functionalities of the app
    """

    print(
        re.sub(" {2}", "",
        """
        Select view options:
        * Type '1' to view all tickets
        * Type '2' to view a specific ticket
        * Type 'quit' to exit
        """)
    )
      
  def print_table(self, tickets: List[Dict[str, str]]) -> None:
    """
    Print a table containing tickets the account has
    """

    column_names = ["ID", "Updated at (SGT)", "Type", \
      "Priority", "Status", "Subject"] # Table headers
    keys = ["id", "updated_at", "type", "priority", "status", "subject"]
    
    # Find the width of each column in the table
    col_width = find_column_width(tickets, keys, column_names)

    # Print table headers
    headers_list = [""] * len(column_names)

    for idx, col in enumerate(column_names):
      header_value = generate_cell(
        col,
        col_width[idx],
        is_first_col=idx == 0
      )
      headers_list[idx] = header_value

    headers = "".join(headers_list)
    print(f"\n{headers}")
    print("-" * len(headers))

    # Print table content (tickets) row by row
    for ticket in tickets:
      row = generate_row(ticket, keys, col_width)
      print(row)

  def print_page_through_results(
    self, 
    tickets: List[Dict[str, str]],
    error_message_idx: Optional[int] = None
  ) -> None:
    """
    Print results for when user is paging through tickets
    """

    # If table contains tickets, print table
    if len(tickets):
      self.print_table(tickets)

    error_message = {
      1: "\nIt seems that you have reached the end of the table." \
        " You may choose to go in the opposite direction.",
      2: "\nIt seems that there are no other tickets to see." \
        " You may go back to the main menu and try again.",
      3: "\nInvalid input. Please try again."
    }

    if error_message_idx is not None:
      print(error_message[error_message_idx])
    
    page_through_option = {
      0: "",
      1: "\n* Type 'next' to see other tickets",
      2: "\n* Type 'prev' to see other tickets",
      3: "\n* Type 'next' or 'prev' to see other tickets"
    }

    page_through_option_idx = -1

    # No available options/no more tickets to see
    if not len(self.page_through_options) :
      page_through_option_idx = 0
    
    # One of the options might contain more tickets
    elif len(self.page_through_options) == 1:
      page_through_option_idx = 1 if "next" in self.page_through_options else 2
    
    # Both options might contain more tickets
    else:
      page_through_option_idx = 3

    # Print options
    print(
      re.sub(" {2}", "",
      f"""
      Select view options:{page_through_option[page_through_option_idx]}
      * Type 'menu' to go back to the main menu
      * Type 'quit' to exit
      """)
    )

  def page_through(self, input: str) -> None:
    """
    Logic for when user is paging through tickets
    """


    is_valid_input = False # To check if user provides a valid input

    # Valid input ('prev' or 'next')
    if input in self.page_through_options:
      is_valid_input = True
  
    # Return to main menu
    elif "menu" == input:
      self.is_page_through = False
      self.print_main_menu()
    
    # Invalid input (not from the options provided)
    else:
      self.print_page_through_results(
        [], 
        1 if len(self.page_through_options) and input in ["prev", "next"] else 3
      )

    if is_valid_input:
      get_tickets_response = self.ticket_viewer.get_tickets(
        link=self.next_link if input == "next" else self.prev_link
      )
      tickets = get_tickets_response.tickets

      # If API is unavailable, go back to main menu
      if get_tickets_response.status_code != 200:
        self.is_page_through = False
        print(STATUS_CODE_MESSAGE[get_tickets_response.status_code])
        self.print_main_menu()

      # If tickets are returned, print table
      elif len(tickets):
        self.prev_link = get_tickets_response.prev_link
        self.next_link = get_tickets_response.next_link

        all_options = ["next", "prev"]

        # Should not keep going in the same direction
        # since there are no more tickets to see
        if len(tickets) < 25:
          all_options.remove(input)
        
        self.page_through_options = all_options 
        
        self.print_page_through_results(
          tickets,
          1 if len(self.page_through_options) == 1 else None
        )
      
      # If no tickets are returned despite valid input,
      # send a message to user depending on 
      # whether there are still unexplored page_through_options
      else:
        self.page_through_options.remove(input)

        # Ask the user to return to the main menu and try again later
        # if there are no more options
        self.print_page_through_results(
          [], 
          1 if len(self.page_through_options) == 1 else 2
        )

  def process_get_all_tickets_request(self) -> None:
    """
    Logic for when user requests to see all tickets
    """

    status_code, count = self.ticket_viewer.count_tickets()

    # Inform user if API is unavailable
    if status_code != 200:
      print(STATUS_CODE_MESSAGE[status_code])
      self.print_main_menu()
    
    # If there is 0 ticket
    elif not count:
      print("\nThere are no tickets to see.")
      self.print_main_menu()
    
    else:
      # Since count is bigger than 0, try to get user's tickets
      # sorted by their 'updated_at' with the most recently updated one first
      get_tickets_response = self.ticket_viewer.get_tickets()

      # If we fail to connect to API, remain at main menu
      if get_tickets_response.status_code != 200:
        print(STATUS_CODE_MESSAGE[get_tickets_response.status_code])
        self.print_main_menu()
      
      # If there are <=25 tickets, print table and remain at main menu
      elif count <= 25:
        self.print_table(get_tickets_response.tickets)
        self.print_main_menu()

      # If there are > 25 tickets, enter page_through mode
      else:
        self.is_page_through = True
        self.prev_link = get_tickets_response.prev_link
        self.next_link = get_tickets_response.next_link
        self.page_through_options = ["next", "prev"]

        self.print_page_through_results(get_tickets_response.tickets)

  def process_get_indiv_ticket_request(self, ticket_number: str) -> None:
    """
    Logic for when user requests for a specific ticket
    """

    response = self.ticket_viewer.get_individual_ticket(ticket_number)
    
    if response.status_code == 200:
      self.print_table(response.tickets)
      self.print_main_menu()

    else:
      print(STATUS_CODE_MESSAGE[response.status_code])
      self.print_main_menu()

  def run(self) -> None:
    """
    Start the CLI app
    """

    print("\nWelcome to the Ticket Viewer.")
    self.print_main_menu()

    for line in sys.stdin:
      if "quit" == line.strip():
          print("\nThank you for using Ticket Viewer. Bye. :D\n")
          sys.exit()
      
      # Check if user is in page through mode
      if self.is_page_through:
          self.page_through(line.strip())

      else:
        # Get all tickets
        if "1" == line.strip():
          self.process_get_all_tickets_request()

        # Get a specific ticket
        elif "2" == line.strip():
          ticket_number = input("\nEnter ticket ID:\n").strip()

          # Input has to be integer
          if not ticket_number.isdigit():
            print("\nTicket number has to be an integer. Please try again.")
            self.print_main_menu()

          else:
            self.process_get_indiv_ticket_request(ticket_number)

        else:
            print("\nInvalid input. Please try again.")
            self.print_main_menu()
    
    return